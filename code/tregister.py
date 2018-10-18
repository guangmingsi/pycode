#coding=utf-8
import PymysqlHelper
import hashlib
register_name = input("输入注册姓名：")
register_passwd =input("输入注册密码 ")
pysql = PymysqlHelper.PymysqlHelper("10.211.55.3","root","mysql","python3")
sqlword = "select * from users where name=%s"
param = [register_name,register_passwd]
alluser = pysql.selectall(sqlword,[register_name])
if len(alluser)==0:
    print("用户名可用")
    sha1 = hashlib.sha1()
    sha1.update(register_passwd.encode("utf-8"))
    sha1_pwd = sha1.hexdigest()
    sqlword2 = "insert into users (name,passwd) values(%s,%s)"
    pysql.cud(sqlword2, [register_name, sha1_pwd])
    print("注册成功")
else:
    print("用户名重复")

