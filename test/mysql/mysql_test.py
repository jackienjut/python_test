#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

#connect to mysql

db = MySQLdb.connect(
    host='47.94.138.118',
    port=3306 ,
    user ='nous' ,
    passwd ='gotmoney',
    db='python_test' );
cursor = db.cursor();
cursor.execute("drop table IF EXISTS EMPLOYEE");

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
print " Data version :%s" % 'success' ;

db.close();
