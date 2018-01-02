import std.io;
import std.log;
import std.time;
import lib.db.mysql;
import config.mysql;

import json;
import time;
import datetime;


def save_token(token_str):
	
	token_str = token_str.replace("'", "\"");
	token = None;
	try:
		token = json.loads(token_str);
	except Exception as e:
		std.log.warn("JSON Parse Error: %s" % e);
		return None;
	finally:
		pass;
	#endtry
	
	
	conn = lib.db.mysql.connect();
	if conn == None:
		return None;
	#endif
	
	ltime = time.localtime(int(time.time()) + token["expires_in"]);
	expire_time = std.time.get_str(ltime);
	
	sql = "insert into token(`token`, `type`, `expire`, `expiretime`) values('"+ token["access_token"] +"', '"+ token["token_type"] +"', '"+ str(token["expires_in"]) +"', '"+ expire_time +"');";
	lib.db.mysql.insert(conn, sql);
	lib.db.mysql.close(conn);
	
	std.log.info("Token Saved!");
	pass;
#enddef


def get_token():
	
	mysql = lib.db.mysql.CMysql();
	if mysql.conn == None:
		return None;
	#endif
	
	nowtime = std.io.get_time_str();
	sql = "select * from token where expiretime > '" + nowtime +"' order by expiretime desc;";
	list = mysql.fetch( sql);
	

	token = None;
	if len(list) == 0:
		std.log.warn("No Available Token!");
		return None;
	row = list[0];

	return row;
#enddef


if __name__ == '__main__':
	pass;
#end

def main():
	
	token = get_token();
	if token != None:
		save_token(token);
	#endif
#enddef




