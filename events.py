import MySQLdb
class EVENTS:
	def __init__(self):
		self.host = '0.0.0.0'                
		self.user = 'root'
		self.pswd = 'pr@th1b@'
		self.db = 'DB1'
		self.conn =	None
		self.cur = None
	def db_connect(self):
		self.conn = MySQLdb.connect(user=self.user, password=self.pswd,host=self.host,database=self.db)
		self.cur = self.conn.cursor()
	def insert(self,data):
		self.db_connect()
	
		self.cur.execute("INSERT into events(name,time,det,venue,uid,cat) VALUES('{0}' , '{1}' , '{2}' , '{3}' , '{4}','{5}' )".format(data['name'],data['time'],data['det'],data['venue'],data['uid'],data['cat']))
		self.conn.commit()
