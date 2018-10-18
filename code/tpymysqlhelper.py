from PymysqlHelper import PymysqlHelper

sql = "select * from student"
sql1 = "update student set sname = '老6' where id = 1"
pyhelp = PymysqlHelper("10.211.55.3","root","mysql",3306,"school")
pyhelp.cud(sql1)
resul=pyhelp.selectall(sql)
for i in resul:
    print(i)
