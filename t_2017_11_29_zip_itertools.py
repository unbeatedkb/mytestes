# coding: utf-8

import itertools

def expand_result(fields, values):
    """将结果转换
    :param fields: dict {
        "gp1" : ["f1","f2",..]
    }
    :param values dict: 格式 {
        "gp1": [[1,2],[3,4]]
        "gp2": [["a"],["b"]]
    }
    :return ["f1","f2",...] , [(1,3,"a","b"),..]
    """
    thevalues = values.values()
    for index, v in enumerate(thevalues):
        for _index, _v in enumerate(v):
            if len(_v) > 1:
                _v = [','.join([i for i in _v])]
            v[_index] = _v
        thevalues[index] = v
    for index, key in enumerate(values.keys()):
        values[key] = thevalues[index]

    _tmp_values = []
    field_names = list(itertools.chain(*fields.values()))

    # 同group值合并成tuple
    _tmp_values = [zip(*vs) for vs in values.values()]
    # _tmp_values = [zip(vs) for vs in values.values()]

    field_values = [list(itertools.chain(*x)) for x in itertools.product(*_tmp_values)]
    return field_names, field_values

def t1():
    fields = {'1': ['name', 'age', 'hobby'], '2': ['weight', 'from']}

    values = {'1': [['kb', 'bk'], ['22'], ['sleep']], '2': [['144'], ['holololo']]}

    print expand_result(fields, values)

def t_zip():
    a = [2, 4]
    b = [1, 2, 9]
    c = [(1, 7), (3, 4)]
    print zip(a, b)
    print zip(*c)    


t_zip()


















