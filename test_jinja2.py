# coding: utf-8

import jinja2

env = jinja2.Environment()

cmd = "a|int//20+1"

source = u"{{{{ {} }}}}".format(cmd)
template = env.from_string(source)

print template.render({'a': 2})


