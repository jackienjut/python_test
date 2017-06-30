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
sql = "SELECT * FROM EMPLOYEE WHERE INCOME>'%d'" % (1000);
try:
    cursor.execute(sql);
    res = cursor.fetchall();
    for row in res:
        fname = row[0];
        lname = row[1];
        age = row[2];
        sex = row[3];
        income = row[4];
        print "fname=%s , lname=%s , age=%s , sex=%s , income=%s" % (fname, lname, age, sex, income);
except:
    print "Error : unable to featch the data"
finally:
    db.close();
