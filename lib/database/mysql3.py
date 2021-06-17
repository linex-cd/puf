# -*- coding: utf-8 -*- 
import std.log;
import config;

import pymysql;

from dbutils.persistent_db import PersistentDB;
from dbutils.steady_db import SteadyDBConnection;

PersistentPool = None

def connect(Persistent = False):
	global PersistentPool;
	RETRY_TIMES = 3;
	conn = None;
	for i in range(RETRY_TIMES):
		try:
		
			if Persistent and PersistentPool is None:
				
				PersistentPool = PersistentDB(
					creator = pymysql, 
					maxusage = None,
					setsession = [],
					ping = 2,
					closeable = False,
					threadlocal = None,
					host = host,
					port = port,
					user = user,
					password = password,
					database = db,
					charset = charset
				);
				conn = PersistentPool.connection();
			else:
				conn = pymysql.connect(
				host = host,
				user = user,
				password = password,
				db = db, 
				port = port, 
				charset = charset, 
				connect_timeout = mysql_timeout
				);
			#endif
			
			break;
		except Exception as e:
			#log("Mysql Connect Error: %s" % e);
			log("data connection error");
		finally:  
			pass;
		#endtry
		
	#endfor
	
	return conn;
#enddef

def close(conn):
	try:
		conn.close()
	except Exception as e:
		std.log.warn("Mysql Close Error: %s" % e);
	#endtry
	pass;
#endif


def insert(conn, sql):
	id = 0;
	try:
		cur = conn.cursor();
		cur.execute(sql);
		
		if type(conn) is SteadyDBConnection:
			id = 1;
		else:
			id = int(conn.insert_id());
		#endif
		
		conn.commit();
	except Exception as e:
		std.log.warn("Mysql Insert Error: %s" % e);
		conn.rollback();
		id = -1;
	#endtry
	
	return id;
#enddef

def lastrowid(conn):
	id = 0;
	try:
		cur = conn.cursor();
		id = int(cur.lastrowid);
		
	except Exception as e:
		std.log.warn("Mysql LastRowID Error: %s" % e);
		id = -1;
	#endtry
	
	return id;
#enddef

def update(conn, sql):
	result = True;

	try:
		cur = conn.cursor(pymysql.cursors.DictCursor);
		cur.execute(sql);

		conn.commit();
	except Exception as e:
		std.log.warn("Mysql Update Error: %s" % e);
		conn.rollback();
		result = False;
	#endtry
	
	return result;
#enddeef

def fetch(conn, sql):
	list = [];
	try:
		cur = conn.cursor(pymysql.cursors.DictCursor);
		rs = cur.execute(sql);
		list = cur.fetchmany(rs);

		conn.commit();
	except Exception as e:
		std.log.warn("Mysql Fetch Error: %s" % e);
		conn.rollback();
		list = None;
	#endtry
	
	return list;
#enddeef


if __name__ == '__main__':
	pass;
#end

