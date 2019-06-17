# coding: utf-8

with open('t4', 'r') as f:
	content = f.read()

# print content
content = content.replace('\\r',  '\r')
content = content.replace('\\n',  '\n')
content = content.replace('\\"',  '"')
content = content.replace('\\t',  '\t')
content = content.replace('\/',  '/')
with open('t5', 'w') as f:
	f.write(content)
	