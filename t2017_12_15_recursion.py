# coding: utf-8

def set_values(templ, key, value):
    if isinstance(templ, dict):
        for k, v in templ.items():
            if k == key:
                templ[k] == value
                continue
            set_values(v, key, value)

    return templ


templ = {
    'test': 'test',
    'keyword': '', 
    'sec': {
        'tes': 'tes',
        'te': 'te',
        'refresh_rage': '',
    },
    'k': {
        'v': {
            'priority': '',
        }
    }
}

keyword = 'keyword'
refresh_rage = 'refresh_rage'
priority = 'priority'

templ = set_values(templ, 'keyword', keyword)
templ = set_values(templ, 'refresh_rage', refresh_rage)
templ = set_values(templ, 'priority', priority)


import pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(templ)


