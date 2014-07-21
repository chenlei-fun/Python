import pymssql
import _mssql
import socket
import decimal
import uuid

class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "Not Setted")
        self.conn = pymssql.connect(host = self.host, user = self.user, password= self.pwd, database=self.db, charset="utf8" )
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "Connect Error!")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
    ms = MSSQL(host="localhost", user="sa", pwd="prolog.123", db="SyncfloEPM_2.9.0")
    resList = ms.ExecQuery("select top 10 ProductID from Products")
    for ProductID in resList:
        print str(ProductID)

if __name__ == "__main__":
    main()





