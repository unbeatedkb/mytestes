# coding: utf-8


import urllib
import uritools

def _merge_uri(uri, default_uri):
    """合并默认的配置
    """
    QUERY_PRIVATE_PREFIX = "_DC_" # _DC_开头的query为系统内部保留变量
    input_URI = uritools.urisplit(uri)
    default_URI = uritools.urisplit(default_uri)
    parts=[]
    private_query = {}
    sorted_querylist = []
    for key in ["scheme", "authority", "path", "query", "fragment"]:
        if key == "query":
            # query需要合并
            _query = default_URI.getquerydict()
            _query.update(input_URI.getquerydict())

            # 过滤内部变量
            for k in list(_query.keys()):
                if k.startswith(QUERY_PRIVATE_PREFIX):
                    private_query[k[len(QUERY_PRIVATE_PREFIX):]] = _query.pop(k)

            value= urllib.urlencode(_query, True)

            # 按照输入query顺序输出querylist
            sorted_querylist = input_URI.getquerylist()
            _input_querykeys = [k for k,_ in sorted_querylist]
            sorted_querylist.extend([(k,v) for k,v in default_URI.getquerylist()
                                            if k not in _input_querykeys])
            # 过滤内部变量
            sorted_querylist = [(k,v) for k,v in sorted_querylist if k in _query]
        else:
            value = getattr(input_URI,key) or getattr(default_URI,key)
        parts.append(value)
    return uritools.urisplit(uritools.uriunsplit(parts)), private_query, sorted_querylist


uri = u'mongodb://?table=recurits&opt=upsert'
default_uri = 'mongodb://kb:kb@192.168.40.190:27017/test_all?table=seeds'

final_URI, private_query, sorted_querylist = _merge_uri(uri, default_uri)
print final_URI.__dict__








