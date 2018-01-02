# -*- coding: utf-8 -*- 
import std.log;
import config;

import MySQLdb;

def connect():
	conn = None;
	try:
		conn = MySQLdb.connect(host = config.mysql.host, user = config.mysql.user, passwd = config.mysql.pwd, db = config.mysql.db, port = config.mysql.port);
		cur = conn.cursor()
		cur.execute("set names " + config.mysql.charset +";");
		cur.close();
	except MySQLdb.Error as e:
		std.log.warn("Mysql Connect Error %d: %s" % (e.args[0], e.args[1]));
	#endtry
	
	return conn;	
#enddef


def close(conn):
	try:
		conn.close()
	except MySQLdb.Error as e:
		std.log.warn("Mysql Close Error %d: %s" % (e.args[0], e.args[1]));
	pass;
#endif


def insert(conn, sql):
	id = 0;
	try:
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor);
		cur.execute(sql);
		
		id = int(conn.insert_id()); #conn.insert_id() must be used before conn.commit(), or it will be zero  
		cur.close();

		conn.commit();
	except MySQLdb.Error as e:
		std.log.warn("Mysql Insert Error %d: %s" % (e.args[0], e.args[1]));
		id = -1;
	#endtry
	
	return id;
#enddef

def lastrowid(conn):
	id = 0;
	try:
		cur = conn.cursor();
		id = int(cur.lastrowid);
		cur.close();
		
	except MySQLdb.Error as e:
		std.log.warn("Mysql LastRowID Error %d: %s" % (e.args[0], e.args[1]));
		id = -1;
	#endtry
	
	return id;
#enddef

def update(conn, sql):
	result = True;
	try:
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor);
		cur.execute(sql);
		cur.close();
		
		conn.commit();
	except MySQLdb.Error as e:
		std.log.warn("Mysql Update Error %d: %s" % (e.args[0], e.args[1]));
		result = False;
	#endtry
	
	return result;

#enddeef


def fetch(conn, sql):
	list = [];
	try:
		cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor);
		rs = cur.execute(sql);
		list = cur.fetchmany(rs);
		cur.close();

		conn.commit();
	except MySQLdb.Error as e:
		std.log.warn("Mysql Fetch Error %d: %s" % (e.args[0], e.args[1]));
		list = None;
	#endtry
	
	return list;

#enddeef

if __name__ == '__main__':
	pass;
#end

