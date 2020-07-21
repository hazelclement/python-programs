import mysql.connector as sql
c=sql.connect(host='localhost',user='root',passwd='cnd131')
cur=c.cursor()
cur.execute('use class12')
for i 

diplay='''select name from student order by asc '''
