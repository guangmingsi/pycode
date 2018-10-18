import pymysql

class PymysqlHelper(object):
    """封装连接数据库"""
    def __init__(self,host,user,passwd,db,port=3306,charset="utf8"):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.datebase=db
        self.port=port
        self.charset=charset

    def open(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,db=self.datebase,port=self.port,charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def cud(self,sql,param=[]):
        try:
            self.open()
            self.cur.execute(sql,param)
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            self.close()

    def selectall(self,sql,param=[]):
        self.open()
        self.cur.execute(sql,param)
        result = self.cur.fetchall()
        self.close()
        return result