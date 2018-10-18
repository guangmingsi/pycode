import pymysql
try:
    db =pymysql.connect("10.211.55.3","root","mysql","school")
    cursor = db.cursor()
    sql = "select * from student"
    sql1 = "insert into student values (0,'红星','天津','1990-01-01',1)"
    cursor.execute(sql1)
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    cursor.close()
    db.commit()

except:
    db.rollback()
finally:
    db.close()

