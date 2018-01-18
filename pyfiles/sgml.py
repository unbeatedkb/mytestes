# coding: utf8
"""
Customized sgml link extractor extended from scrapy.contrib.linkextractors.sgml
record the changes below:
1) SgmlLinkExtractor renamed to SgmlLinkProcesser:
the class will not only do the extraction work
2) the class will do the bad/good filter base on regex per host
3) the class will do the dup filter base on HBase url seen 
4) url_is_from_any_domain to _url_is_from_any_host:
judge the expansion internal/external basing on host but domain
"""

import re
from urlparse import urlparse

from scrapy.selector import HtmlXPathSelector
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.python import FixedSGMLParser, unique as unique_list, str_to_unicode
from scrapy.utils.url import safe_url_string, urljoin_rfc
from scrapy.utils.response import get_base_url
from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
from scrapy import log


# from claw.utils.http import get_from_attribute_extend

from claw.utils.url import canonicalize_url
from claw.utils.url import get_domain

_re_type = type(re.compile("", 0))

_matches = lambda url, regexs: any((r.search(url) for r in regexs))
_is_valid_url = lambda url: url.split('://', 1)[0] in set(['http', 'https', 'file'])

_re_js_link = re.compile('(?P<quote>[\'"])(.*?)(?P=quote)')



interesting = re.compile('[&<]')
incomplete = re.compile('&([a-zA-Z][a-zA-Z0-9]*|#[0-9]*)?|'
                            '<([a-zA-Z][^<>]*|'
                            '/([a-zA-Z][^<>]*)?|'
                            '![^<>]*)?')
 
entityref = re.compile('&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile('&#([0-9]+)[^0-9]')

starttagopen = re.compile('<[>a-zA-Z]')
shorttagopen = re.compile('<[a-zA-Z][-.a-zA-Z0-9]*/')
shorttag = re.compile('<([a-zA-Z][-.a-zA-Z0-9]*)/([^/]*)/')
piclose = re.compile('>')
endbracket = re.compile('[<>]')
tagfind = re.compile('[a-zA-Z][-_.a-zA-Z0-9]*')
attrfind = re.compile(
                      r'\s*([a-zA-Z_][-:.a-zA-Z_0-9]*)(\s*=\s*'
                      r'(\'[^\']*\'|"[^"]*"|[][\-a-zA-Z0-9./,:;+*%?!&$\(\)_#=~\'"@]*))?')


class TransformUrl(object):

    def __init__(self):
        self._link_callbacks = []

    def register(self, func, condfunc):
        pass


    def need_trans(self, url, resp):
        for x in xrange(1,10):
            pass




class SgmlLinkProcesser(BaseSgmlLinkExtractor):

    def __init__(self, allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(), 
                 tags=('a', 'area'), attrs=('href'), canonicalize=True, unique=True, process_value=None):
        self.allow_res = [x if isinstance(x, _re_type) else re.compile(x) for x in arg_to_iter(allow)]
        self.deny_res = [x if isinstance(x, _re_type) else re.compile(x) for x in arg_to_iter(deny)]
        self.allow_domains = set(arg_to_iter(allow_domains))
        self.deny_domains = set(arg_to_iter(deny_domains))
        self.restrict_xpaths = tuple(arg_to_iter(restrict_xpaths))
        self.canonicalize = canonicalize
        tag_func = lambda x: x in tags
        attr_func = lambda x: x in attrs
        BaseSgmlLinkExtractor.__init__(self, tag=tag_func, attr=attr_func, 
            unique=unique, process_value=process_value)
    
    def _extract_links(self, response_text, response_url, response_encoding, base_url=None, jsurl=None):
        """ Do the real extraction work """
        self.reset()
        self.feed(response_text)
        self.close()

        ret = []
        if base_url is None:
            base_url = urljoin_rfc(response_url, self.base_url) if self.base_url else response_url
        for link in self.links:
            link.url = link.url.strip()

            if jsurl:
                lu = link.url
                if lu.startswith('javascript:'):
                    g = _re_js_link.search(lu)
                    if g:
                        gs = g.groups()
                        link.url = gs[1]                

            link.url = urljoin_rfc(base_url, link.url, response_encoding)
            link.url = safe_url_string(link.url, response_encoding)
            try:
                link.text = str_to_unicode(link.text, response_encoding)
            except:
                link.text = None
                log.msg("link text codec error: [%s]" % link.url, level=log.INFO)
            ret.append(link)
            
        return ret

    def extract_links(self, response):
        base_url = None
        if self.restrict_xpaths:
            hxs = HtmlXPathSelector(response)
            html = ''.join(''.join(html_fragm for html_fragm in hxs.select(xpath_expr).extract()) \
                for xpath_expr in self.restrict_xpaths)
        else:
            html = response.body
            
        base_url = get_base_url(response)
        
        try:
            meta = response.meta
            attr = meta.get('attribute')
            extend = attr.get('extend')
            jsurl = extend.get('jsurl')
        except:
            jsurl = None

        # jsurl = get_from_attribute_extend(response, 'jsurl')

        links = self._extract_links(html, response.url, response.encoding, base_url, jsurl)

        ###href="javascript:..."

        links = self._process_links(links)

        #links = self._dup_eliminate_links(links)
        #links = self._regex_filter_links(urlparse_cached(response).hostname, links)
        return links

    def _process_links(self, links):
        links = [link for link in links if _is_valid_url(link.url)]

        if self.allow_res:
            links = [link for link in links if _matches(link.url, self.allow_res)]
        if self.deny_res:
            links = [link for link in links if not _matches(link.url, self.deny_res)]
        if self.allow_domains:
            #links = [link for link in links if self._url_is_from_any_host(link.url, self.allow_domains)]
            links = [link for link in links if self._url_is_from_any_domain(link.url, self.allow_domains)]
        if self.deny_domains:
            #links = [link for link in links if not self._url_is_from_any_host(link.url, self.deny_domains)]
            links = [link for link in links if not self._url_is_from_any_domain(link.url, self.deny_domains)]

        if self.canonicalize:
            for link in links:
                #log.msg("extract link before normalize: [%s]" % link.url, level=log.INFO)
                link.url = canonicalize_url(link.url)

        links = BaseSgmlLinkExtractor._process_links(self, links)
        return links

    
    def _dup_eliminate_links(self, links):
        """
            link DE goes here
        """
        return links

    def _regex_filter_links(self, hostname, links):
        """
            expansion link filter chain goes here
            return None to ignore the link
        """
        return links

    def matches(self, url):
        if self.allow_domains and not self._url_is_from_any_host(url, self.allow_domains):
            return False
        if self.deny_domains and self._url_is_from_any_host(url, self.deny_domains):
            return False

        allowed = [regex.search(url) for regex in self.allow_res] if self.allow_res else [True]
        denied = [regex.search(url) for regex in self.deny_res] if self.deny_res else []
        return any(allowed) and not any(denied)
    
    def _url_is_from_any_host(self, url, hosts):
        """Return True if the url belongs to any of the given hosts"""
        host = urlparse(url).hostname
    
        if host:
            return any((host == d) for d in hosts)
        else:
            return False
        
    def _url_is_from_any_domain(self, url, domains):
        """Return True if the url belongs to any of the given hosts"""
        domain = get_domain(url)
    
        if domain:
            return any((domain == d) for d in domains)
        else:
            return False

    def handle_data(self, data):
        '''
        In order to avoid some codec error, override the method.
        '''
        """
        http://www.zjkqxq.gov.cn
        File "scrapy/contrib/linkextractors/sgml.py", line 77, in handle_data
            self.current_link.text = self.current_link.text + data.strip()
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xd6 in position 0: ordinal not in range(128)
        """
        if self.current_link:
            try:
                self.current_link.text = self.current_link.text + data.strip()
            except:
                self.current_link.text = self.current_link.text


    # Internal -- handle data as far as reasonable.  May leave state
    # and data to be processed by a subsequent call.  If 'end' is
    # true, force handling all data as if followed by EOF marker.
    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            if self.nomoretags:
                self.handle_data(rawdata[i:n])
                i = n
                break
            match = interesting.search(rawdata, i)
            if match: j = match.start()
            else: j = n
            if i < j:
                self.handle_data(rawdata[i:j])
            i = j
            if i == n: break
            if rawdata[i] == '<':
                if starttagopen.match(rawdata, i):
                    if self.literal:
                        self.handle_data(rawdata[i])
                        i = i+1
                        continue
                    k = self.parse_starttag(i)
                    if k < 0: break
                    i = k
                    continue
                if rawdata.startswith("</", i):
                    k = self.parse_endtag(i)
                    if k < 0: break
                    i = k
                    self.literal = 0
                    continue
                if self.literal:
                    if n > (i + 1):
                        self.handle_data("<")
                        i = i+1
                    else:
                        # incomplete
                        break
                    continue
                if rawdata.startswith("<!--", i):
                        # Strictly speaking, a comment is --.*--
                        # within a declaration tag <!...>.
                        # This should be removed,
                        # and comments handled only in parse_declaration.
                    k = self.parse_comment(i)
                    if k < 0: break
                    i = k
                    continue
                if rawdata.startswith("<?", i):
                    k = self.parse_pi(i)
                    if k < 0: break
                    i = i+k
                    continue
                if rawdata.startswith("<!DOCTYPE", i):
                    # This is some sort of declaration; in "HTML as
                    # deployed," this should only be the document type
                    # declaration ("<!DOCTYPE html...>").
                    try:
                        k = self.parse_declaration(i)
                        if k < 0: break
                        i = k
                    except Exception, exception:
                        log.msg("catch except when parse declaration, %s" % (exception, ), level=log.INFO)
                        i = rawdata.find("<", i+1)
                        continue
                    continue
            elif rawdata[i] == '&':
                if self.literal:
                    self.handle_data(rawdata[i])
                    i = i+1
                    continue
                match = charref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_charref(name)
                    i = match.end(0)
                    if rawdata[i-1] != ';': i = i-1
                    continue
                match = entityref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_entityref(name)
                    i = match.end(0)
                    if rawdata[i-1] != ';': i = i-1
                    continue
            else:
                self.error('neither < nor & ??')
            # We get here only if incomplete matches but
            # nothing else
            match = incomplete.match(rawdata, i)
            if not match:
                self.handle_data(rawdata[i])
                i = i+1
                continue
            j = match.end(0)
            if j == n:
                break # Really incomplete
            self.handle_data(rawdata[i:j])
            i = j
        # end while
        if end and i < n:
            self.handle_data(rawdata[i:n])
            i = n
        self.rawdata = rawdata[i:]
