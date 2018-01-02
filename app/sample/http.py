import std.io;
import std.log;
import lib.network.http;



def http_request():
		
	url = "http://127.0.0.1/test.php";
	body = "hello=world";
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'Keep-Alive',
		'User-Agent': 'Apache-HttpClient/UNAVAILABLE',
	};

	result = lib.network.http.post(url, headers, None, body);
	
	text = "";
	if result.status_code == 200:
		text = result.text;
	#endif
	
	std.log.info("text fetched!");
	return text;
#enddef	

if __name__ == '__main__':
	pass;
#end

def main():
	text = http_request();
	std.log.info(text);
#enddef




