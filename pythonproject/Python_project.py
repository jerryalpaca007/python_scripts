#Car accident report database

import mysql.connector

sql=mysql.connector.connect(host='localhost',username='root',password='helloworld',database='schoolproject')
cur=sql.cursor()
a=cur.execute('show tables')
print(a)