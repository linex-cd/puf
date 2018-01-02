# -*- coding: utf-8 -*- 
import std.env;
import config.redis;
 
import redis;

class CRedis:
	
	conn = None;
	
	def __init__(self):
		self.conn = connect();
	#enddef
	
	def __del__(self):
		self.conn = None;

	#enddef
	
	def set(self, key, value):
		return set(self.conn, key, value);
	#enddef

	def setnx(self, key, value):
		return setnx(self.conn, key, value);
	#enddef
	
	def setex(self, key, time, value):
		return setex(self.conn, key, time, value);
	#enddef

	def setrange(self, key, start, value):
		return setrange(self.conn, key, start, value);
	#enddef
	
	def getrange(self, key, start, end):
		return getrange(self.conn, key, start, end);
	#enddef

	def get(self, key):
		return get(self.conn, key);
	#enddef
	
	def keys(self, pattern):
		return keys(self.conn, pattern);
	#enddef

	def delete(self, key):
		return delete(self.conn,key);
	#enddef

	def incr(self, key, default = 1):
		return incr(self.conn, key, default);
	#enddef

	def decr(self, key, default = 1):
		return decr(self.conn, key, default);
	#enddef
	
	def hget(self, hash_name, hash_key):
		return hget(self.conn, hash_name, hash_key);
	#enddef
	
	def hset(self, hash_name, hash_key, hash_value):
		return hset(self.conn, hash_name, hash_key, hash_value);
	#enddef

	def hgetall(self, hash_name):
		return hgetall(self.conn, hash_name);
	#enddef
	
	def hdel(self, name, key = None):
		return hdel(self.conn, name, key = None);
	#enddef

	def clear(self):
		return flushdb(self.conn);
	#enddef

	def lpush(self, key, value):
		return lpush(self.conn, key, value);
	#enddef

	def lpop(self, key):
		return plush(self.conn, key);
	#enddef

#endclass		

# C style function
def connect():
	return redis.Redis(host = config.redis.host, port = config.redis.port, db = config.redis.db);
#enddef

#string
def set(conn, key, value):
	return conn.set(key, value);
#enddef

def setnx(conn, key, value):
	return conn.setnx(key, value);
#enddef

def setex(conn, key, time, value):
	return conn.setex(key, time, value);
#enddef

def setrange(conn, key, start, value):
	return conn.setrange(key, start, value);
#enddef

def getrange(conn, key, start, end):
	return conn.getrange(key, start, end);
#enddef

def get(conn, key):
	if isinstance(key, list):
		return conn.mget(key);
	else:
		return conn.get(key);
	#endif
	pass;
#enddef

def keys(conn, pattern):
	return conn.keys(pattern);
#enddef

def delete(conn, key):
	return conn.delete(key);
#enddef

def incr(conn, key, default = 1):
	if (1 == default):
		return conn.incr(key);
	else:
		return conn.incr(key, default);
	#endif
	pass;
#enddef

def decr(conn, key, default = 1):
	if (1 == default):
		return conn.decr(key);
	else:
		return conn.decr(key, default);
	#endif
	pass;
#enddef

#hash
def hget(conn, hash_name, hash_key):
	return conn.hget(hash_name, hash_key);
#enddef

def hset(conn, hash_name, hash_key, hash_value):
	return conn.hset(hash_name, hash_key, hash_value);
#enddef

def hgetall(conn, hash_name):
	return conn.hgetall(hash_name);
#enddef

def hdel(conn, name, key = None):
	if(key):
		return conn.hdel(name, key);
	#endif
	return conn.hdel(name);
#enddef

def clear(conn):
	return conn.flushdb();
#enddef

#lists
def lpush(conn, key, value):
	return conn.lpush(key, value);
#enddef

def lpop(conn, key):
	return conn.plush(key);
#enddef

		
if __name__ == '__main__':
	pass;
#end