import MySQLdb
class EVENT_USER:
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
        
    def getevents(self,uid):
        self.db_connect()
        
        self.cur.execute("select * from event_user where uid = {0}".format(uid))
        events = self.cur.fetchall()
        e =[]
        for e_id, uid in events:
            e.append(e_id)
        return e
        
    def delete(self,eid):
        self.db_connect()
        
        self.cur.execute("delete from event_user where e_id = {0}".format(eid))
        self.conn.commit()
        
    def insert(self,eid,uid):
        self.db_connect()
        
        self.cur.execute("insert into event_user(e_id,uid) values({0},{1})".format(eid,uid))
        self.conn.commit()
       
    
   
