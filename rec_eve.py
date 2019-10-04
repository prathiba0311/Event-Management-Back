import MySQLdb
class RECIEPT_EVENT:
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
        
    def delete(self,id):
        self.db_connect()
        
        self.cur.execute("delete from reciept_event where e_id = {0}".format(id))
        self.conn.commit()
        
    def insert(rid,eid):
        self.db_connect()
        
        self.cur.execute("insert into reciept_event(rid,eid) values({0},{1})".format(rid,eid))
        self.conn.commit()
       
    
   
