from urlparse import urlparse, urlunparse
from string import lower
import re


class InvalidUrl(Exception):
    pass

_server_authority = re.compile('^(?:([^\@]+)\@)?([^\:\[\]]+|\[[a-fA-F0-9\:\.]+\])(?:\:(.*?))?$')
_default_port = {'http': '80',
                 'itms': '80',
                 'ws': '80',
                 'https': '443',
                 'wss': '443',
                 'gopher': '70',
                 'news': '119',
                 'snews': '563',
                 'nntp': '119',
                 'snntp': '563',
                 'ftp': '21',
                 'telnet': '23',
                 'prospero': '191',
                 }
_relative_schemes = set(['http',
                         'https',
                         'ws',
                         'wss',
                         'itms',
                         'news',
                         'snews',
                         'nntp',
                         'snntp',
                         'ftp',
                         'file',
                         ''
                         ])

params_unsafe_list = set('?=+%#;')
qs_unsafe_list = set('?&=+%#')
fragment_unsafe_list = set('+%#')
path_unsafe_list = set('/?;%+#')
_hextochr = dict(('%02x' % i, chr(i)) for i in range(256))
_hextochr.update(('%02X' % i, chr(i)) for i in range(256))


def unquote_path(s):
    return unquote_safe(s, path_unsafe_list)


def unquote_params(s):
    return unquote_safe(s, params_unsafe_list)


def unquote_qs(s):
    return unquote_safe(s, qs_unsafe_list)


def unquote_fragment(s):
    return unquote_safe(s, fragment_unsafe_list)


def unquote_safe(s, unsafe_list):
    """unquote percent escaped string except for percent escape sequences that are in unsafe_list"""
    # note: this build utf8 raw strings ,then does a .decode('utf8') at the end.
    # as a result it's doing .encode('utf8') on each block of the string as it's processed.
    res = _utf8(s).split('%')
    for i in xrange(1, len(res)):
        item = res[i]
        try:
            raw_chr = _hextochr[item[:2]]
            if raw_chr in unsafe_list or ord(raw_chr) < 20:
                # leave it unescaped (but uppercase the percent escape)
                res[i] = '%' + item[:2].upper() + item[2:]
            else:
                res[i] = raw_chr + item[2:]
        except KeyError:
            res[i] = '%' + item
        except UnicodeDecodeError:
            # note: i'm not sure what this does
            res[i] = unichr(int(item[:2], 16)) + item[2:]
    o = "".join(res)
    return _unicode(o)


def norm(url):
    """given a string URL, return its normalized/unicode form"""
    url = _unicode(url)  # operate on unicode strings
    url_tuple = urlparse(url)
    normalized_tuple = norm_tuple(*url_tuple)
    return urlunparse(normalized_tuple)

def norm_tuple(scheme, authority, path, parameters, query, fragment):
    """given individual url components, return its normalized form"""
    scheme = lower(scheme)
    if not scheme:
        raise InvalidUrl('missing URL scheme')
    authority = norm_netloc(scheme, authority)
    if not authority:
        raise InvalidUrl('missing netloc')
    path = norm_path(scheme, path)
    # TODO: put query in sorted order; or at least group parameters together
    # Note that some websites use positional parameters or the name part of a query so this would break the internet
    # query = urlencode(parse_qs(query, keep_blank_values=1), doseq=1)
    parameters = unquote_params(parameters)
    query = unquote_qs(query)
    fragment = unquote_fragment(fragment)
    return (scheme, authority, path, parameters, query, fragment)


def norm_path(scheme, path):
    if scheme in _relative_schemes:
        # resolve `/../` and `/./` and `//` components in path as appropriate
        i = 0
        parts = []
        start = 0
        while i < len(path):
            if path[i] == "/" or i == len(path) - 1:
                chunk = path[start:i+1]
                start = i + 1
                if chunk in ["", "/", ".", "./"]:
                    # do nothing
                    pass
                elif chunk in ["..", "../"]:
                    if len(parts):
                        parts = parts[:len(parts)-1]
                    else:
                        parts.append(chunk)
                else:
                    parts.append(chunk)
            i+=1
        path = "/"+ ("".join(parts))
    path = unquote_path(path)
    if not path:
        return '/'
    return path

MAX_IP = 0xffffffffL


def int2ip(ipnum):
    assert isinstance(ipnum, int)
    if MAX_IP < ipnum or ipnum < 0:
        raise TypeError("expected int between 0 and %d inclusive" % MAX_IP)
    ip1 = ipnum >> 24
    ip2 = ipnum >> 16 & 0xFF
    ip3 = ipnum >> 8 & 0xFF
    ip4 = ipnum & 0xFF
    return "%d.%d.%d.%d" % (ip1, ip2, ip3, ip4)


def norm_netloc(scheme, netloc):
    if not netloc:
        return netloc
    match = _server_authority.match(netloc)
    if not match:
        raise InvalidUrl('no host in netloc %r' % netloc)

    userinfo, host, port = match.groups()
    # catch a few common errors:
    if host.isdigit():
        try:
            host = int2ip(int(host))
        except TypeError:
            raise InvalidUrl('host %r does not escape to a valid ip' % host)
    if host[-1] == '.':
        host = host[:-1]

    # bracket check is for ipv6 hosts
    if '.' not in host and not (host[0] == '[' and host[-1] == ']'):
        raise InvalidUrl('host %r is not valid' % host)

    authority = lower(host)
    if 'xn--' in authority:
        subdomains = [_idn(subdomain) for subdomain in authority.split('.')]
        authority = '.'.join(subdomains)

    if userinfo:
        authority = "%s@%s" % (userinfo, authority)
    if port and port != _default_port.get(scheme, None):
        authority = "%s:%s" % (authority, port)
    return authority


def _idn(subdomain):
    if subdomain.startswith('xn--'):
        try:
            subdomain = subdomain.decode('idna')
        except UnicodeError:
            raise InvalidUrl('Error converting subdomain %r to IDN' % subdomain)
    return subdomain


def _utf8(value):
    if isinstance(value, unicode):
        return value.encode("utf-8")
    assert isinstance(value, str)
    return value


def _unicode(value):
    if isinstance(value, str):
        return value.decode("utf-8")
    assert isinstance(value, unicode)
    return value