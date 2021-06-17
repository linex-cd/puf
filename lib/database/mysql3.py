# -*- coding: utf-8 -*- 
import std.log;
import config;

import pymysql;
import dbutils;

def connect():

	conn = None;
	try:
		conn = pymysql.connect(host = config.mysql.host, user = config.mysql.user, password = config.mysql.pwd, db = config.mysql.db, port = config.mysql.port, charset = config.mysql.charset, connect_timeout = config.timeout.mysql);
		
	except Exception as e:
		std.log.warn("Mysql Connect Error: %s" % e);
	#endtry
	
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
		
		if type(conn) is dbutils.steady_db.SteadyDBConnection:
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

