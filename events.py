import MySQLdb
class EVENTS:
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
    
    def getevents(self,e):
        self.db_connect()
        events = []
        for eid in e:
            self.cur.execute("select * from event where e_id = {0} ".format(eid));
            events.append(self.cur.fetchall()[0])
        event_objects=[]
        for e_id,e_date,e_time,e_type,e_venue in events:
            event_objects.append({'e_id':e_id, 'e_date':e_date, 'e_time':e_time, 'e_type':e_type,'e_venue':e_venue})
        return event_objects
    
    def delete(self,id):
        self.db_connect()
        
        self.cur.execute("delete from event where e_id = {0}".format(id))
        self.conn.commit()
       
    def size(self):
        self.db_connect()
        
        entries=self.cur.execute("select * from event");
        return entries
    
    def check_date(self,date):
        self.db_connect()
        
        entries=self.cur.execute("select * from event where e_date = '{0}' ".format(date))
        if(entries==1):
            return True
        else:
            return False
    def insert(self,data,eid):
        self.db_connect()
        
        self.cur.execute("INSERT into event(e_id,e_date,e_time,e_type,e_venue) VALUES('{0}' , '{1}' , '{2}' , '{3}' , '{4}')".format(data['e_id'],data['e_data'],data['e_time'],data['e_type'],data['e_venue'],data['cat']))
        self.conn.commit()    
    
