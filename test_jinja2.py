# coding: utf-8

import jinja2
import datetime

env = jinja2.Environment()

# cmd = "a|int//20+1"
cmd  = "a.strftime('%Y-%m-%d %H:%M:%S')"

source = u"{{{{ {} }}}}".format(cmd)
template = env.from_string(source)

print template.render({'a': datetime.datetime.now()})


