#!/usr/bin/python
# -*-config: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect(
    host='47.94.138.118',
    port=3306 ,
    user ='nous' ,
    passwd ='gotmoney',
    db='python_test' );
cursor = db.cursor();

sql = """ INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
 VALUES ('fs' ,'dsds',20 , 'M' , 3000 );
"""

try:
    cursor.execute(sql);
    db.commit();
except:
    db.rollback();
finally:
    db.close();