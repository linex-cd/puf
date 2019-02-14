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
	
		
	def make_insert_sql(self, tablename, data, updates):
		return make_insert_sql(tablename, data, updates):
	#enddef

#endclass	

def make_insert_sql(table_name, data_dictionary, update_columns):
		
	columnssql = "";
	valuessql = "";
	updatessql = "";
	for key in data.keys():
		value = str(data[key]);
		value = value.replace("'", "\'");
		value = value.replace("`", "\`");
		columnssql = columnssql + "`"+key+"`,\n";
		valuessql = valuessql + "'"+value+"',\n";
		
		if key in updates:
			updatessql = updatessql + "`"+key+"` = '"+str(data[key])+"',\n";
		#endif
	#endfor
	
	sql = "insert into `#tablename#`( #columns# ) values( #values# ) on duplicate key update #updates# ;\n";
	
	columnssql = columnssql[:-2];
	valuessql = valuessql[:-2];
	if len(updatessql) > 2:
		updatessql = updatessql[:-2];
	#endif
	
	sql = sql.replace("#tablename#", tablename);
	sql = sql.replace("#columns#", columnssql);
	sql = sql.replace("#values#", valuessql);
	sql = sql.replace("#updates#", updatessql);
	
	return sql;
#enddef

if __name__ == '__main__':
	pass;
#end

