import MySQLdb
from datetime import date
class PAYMENT:
    def __init__(self):
        self.host = '0.0.0.0'                
        self.user = 'root'
        self.pswd = 'pr@th1b@'
        self.db = 'DB1'
        self.conn = None
        self.cur = None
    def db_connect(self):
        self.conn = MySQLdb.connect(user=self.user, password=self.pswd,host=self.host,database=self.db)
        self.cur = self.conn.cursor()
    
    def delete(self,rid):
        self.db_connect()
        
        self.cur.execute("delete from pay_table where rid = {0}".format(rid))
        self.conn.commit()
        
    def size(self):
        self.db_connect()
        
        entries=self.cur.execute("select * from pay_table")
        return entries

    def insert(self,rid, amt):
        self.db_connect()
        
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        self.cur.execute("insert into pay_table(rid,amount,payment_date) values({0},{1},'{2}')".format(rid,amt,d1))
        self.conn.commit()
        
        
        
