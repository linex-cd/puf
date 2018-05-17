# -*- coding: utf-8 -*- 
import std.io;
import std.file;
import std.dir;
import std.time;
import std.session;

import config.cookie;

def get(key):
	value = None;
	expire = None;
	
	cookie_path = config.cookie.path + key + "@" + std.session.module + ".cookie";
	if std.file.exist(cookie_path):
		cookie = std.file.read(cookie_path);
		pos = cookie.find("\n");
		expire = cookie[:pos];
		value = cookie[pos+1:];

	#endif
	
	return [value, expire];
#enddef

def put(key, value, expire = 0):
	if isinstance(expire, int) == False:
		return False;
	#endif
	
	if expire > 0:
		expire = std.time.get_timestamp() + expire;
	#endif
	
	cookie_path = config.cookie.path + key + "@" + std.session.module + ".cookie";
	
	cookie = str(expire) + "\n" + value;
	std.file.write(cookie, cookie_path, True);
		
	return True;
#enddef

def delete(key):
	cookie_path = config.cookie.path + key + "@" + std.session.module + ".cookie";
	
	if std.file.exist(cookie_path):
		std.file.delete(cookie_path);
	else:
		return False;
	#endif
	
	return True;
#enddef


def keys():
	keys = [];
	cookies = std.dir.travel(config.cookie.path, "cookie");
	for cookie in cookies:
		p1 = cookie.rfind("/");
		p2 = cookie.rfind("@");
		key = cookie[p1+1:p2];
		keys.append(key);
	#endfor
	
	return keys;
#enddef

#remove expired cookies
def clean():
	cookies = std.dir.travel(config.cookie.path, "cookie");
	for cookie in cookies:
		p1 = cookie.rfind("/");
		p2 = cookie.rfind("@");
		key = cookie[p1+1:p2];
		
		[v, e] = get(key);

		expire = int(e);
		if std.time.get_timestamp() - expire > 0:
			delete(key);
		#endif
		
	#endfor
	pass;
#enddef

#remove all cookies
def flush():
	cookies = std.dir.travel(config.cookie.path, "cookie");
	for cookie in cookies:
		std.file.delete(cookie);
	#endfor
	pass;
#enddef



if __name__ == '__main__':
	pass;
#end