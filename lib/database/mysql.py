# -*- coding: utf-8 -*- 
import std.env;

if std.env.python_version < (3, 0):
	from lib.db.mysql2 import *;
else:
	from lib.db.mysql3 import *;
#endif

 
class CMysql:
	
	conn = None;
	
	def __init__(self):
		self.conn = connect();
	#enddef
	
	def __del__(self):
		if self.conn != None:
			close(self.conn);
		#endif
	#enddef
	
	def insert(self, sql):
		return insert(self.conn, sql);
	#enddef
	
	def lastrowid(self):
		return lastrowid(self.conn, sql);
	#enddef
	
	def update(self, sql):
		return update(self.conn, sql);
	#enddef
	
	def fetch(self, sql):
		return fetch(self.conn, sql);
	#enddef

#endclass	

if __name__ == '__main__':
	pass;
#end

