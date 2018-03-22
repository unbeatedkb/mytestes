# coding: utf-8

'''python2 frequent used codes
'''


def use_mysql():
    import MySQLdb
    # 打开数据库连接
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    print "Database version : %s " % data
    # 关闭数据库连接
    db.close()

def use_mysql2():
    import datetime
    import mysql.connector

    cnx = mysql.connector.connect(user='scott', database='employees')
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name, hire_date FROM employees "
             "WHERE hire_date BETWEEN %s AND %s")

    hire_start = datetime.date(1999, 1, 1)
    hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query, (hire_start, hire_end))

    for (first_name, last_name, hire_date) in cursor:
      print("{}, {} was hired on {:%d %b %Y}".format(
        last_name, first_name, hire_date))

    cursor.close()
    cnx.close()