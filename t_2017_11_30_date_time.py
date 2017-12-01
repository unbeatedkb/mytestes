# coding: utf-8


import datetime, time

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# days、seconds、minutes、hours、weeks
print (datetime.datetime.now()-datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")

updatetime = '2017-10-17 10:42:58'
updatetime = datetime.datetime.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
print type(updatetime)
print updatetime

thetime = '2016-3-21 16:24'
print int(time.mktime(time.strptime(thetime,'%Y-%m-%d %H:%M')))

