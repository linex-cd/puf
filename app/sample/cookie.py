import app;
import config;
import std.io;
import std.ex;
import std.log;
import std.env;

import std.cookie;


if __name__ == '__main__':
	pass;
#end

def test1():
	#remove expired cookies
	std.cookie.clean();
	pass;
#enddef

def test2():
	#remove all cookies
	std.cookie.flush();
	pass;
#enddef

def main():
	keys = std.cookie.keys();
	print(keys)
	std.io.echo("Input a key:");
	key = std.io.scanln();
	
	std.io.echo("Input a value:");
	value = std.io.scanln();
	
	std.cookie.put(key, value, 30);
	
	[v, e] = std.cookie.get(key);
	std.io.println("value=%s, expire=%s" % (v, e));
	

	std.io.println("Bye!");
	pass;
#enddef




