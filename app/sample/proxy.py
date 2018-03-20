import app;
import config;
import std.io;

import lib.db.mysql;
import lib.network.http;


import time;

if __name__ == '__main__':
	pass;
#end

def main():
	std.io.println("Hello world");
	std.io.println("Project Name: " + config.project.name);
	std.io.println("Project version: " + config.project.version);
	
	
	config.proxy.enable = True;

	config.mysql.host = "10.10.0.1";
	config.mysql.user = "test";
	config.mysql.pwd = "test";
	config.mysql.db = "callproxy";

	mysql = lib.db.mysql.CMysql();
	if mysql.conn == None:
		return None;
	#endif
	
	sql = "select * from proxy;";
	list = mysql.fetch(sql);
	
	token = None;
	if len(list) == 0:
		std.io.println("No Available Proxy!");
		return None;
	i = 0;
	for item in list:
		proxy = item["ip"];
		config.proxy.proxies = {
			'http': proxy,
			'https': proxy,
		};
		
		i = i + 1;
		std.io.print(str(i)+"#"+proxy+"\t\t");
		
		t1 = time.time();
		
		url = "https://www.so.com/";

		try:
			result = lib.network.http.get(url, None, None);
			if result.status_code == 200:
				std.io.print("OKAY\t");
			else:
				std.io.print("ERROR\t");
			#endif
		except:
			std.io.print("FAILED\t");
		#endtry
		
		
		
		t2 = time.time();
		c = t2 - t1;
		std.io.print(str(int(c*1000)) + "ms\n");
		
		
	#endfor
	

	std.log.info("Bye!");
#enddef




