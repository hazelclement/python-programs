import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='cnd131')

if con.is_connected:
    print("yes")
else:
    print("no")