#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# connect to mysql
db = MySQLdb.connect(
    host='47.94.138.118',
    port=3306,
    user='nous',
    passwd='gotmoney',
    db='python_test');
cursor = db.cursor();

# SQL select language
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql);
    db.commit();
except:
    print "Error : unable to featch the data"
    db.rollback();
finally:
    db.close();
