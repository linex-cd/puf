import std.io;
import lib.db.redis;


if __name__ == '__main__':
	pass;
#end

def main():
	
	r = lib.db.redis.connect();
	r.set("abc", "123");
	r.set("abd", "456");
	v = r.get("abc");
	std.io.println(v);
	l = r.keys("ab*");
	std.io.println(l);
	
#enddef




