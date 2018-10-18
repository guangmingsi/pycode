import pymysql

name = input("请输入学生姓名")
hometown = input("输入学生的家乡")
db = pymysql.connect(host="10.211.55.3",user="root",passwd="mysql",db="school")
try:
    cur = db.cursor()
    sql ="insert into student (sname,hometown) values(%s,%s)"
    cur.execute(sql,(name,hometown))
    db.commit()
    cur.execute("select * from student")
    file = cur.fetchall()
    print(file)
    cur.close()

except:
    db.rollback()
db.close()
print("添加完毕")

