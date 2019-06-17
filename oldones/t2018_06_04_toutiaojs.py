# coding: utf-8

import execjs
import codecs
import json
 
node = execjs.get()
print node
thefile = 'pyfiles/toutiao.js'
content = codecs.open(thefile, 'r', 'utf-8').read()
ctx = node.compile(content)


js = 'getHoney()'
result = ctx.eval(js)
print result
res = json.dumps(result)
with open('files/t1', 'w') as f:
    f.write(res)

# user_id = 1
# max_behot_time = 0
# res1 = ctx.eval('return TAC.sign(' + str(user_id) + str(max_behot_time) + ')')
# print res1

#{'as': 'A1552A7A02C3DF3', 'cp': '5AA2036D0FE39E1'}