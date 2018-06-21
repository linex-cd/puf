# -*- coding: utf-8 -*- 
import requests;
import config;

from requests.packages.urllib3.exceptions import InsecureRequestWarning;
requests.packages.urllib3.disable_warnings(InsecureRequestWarning);

def create_session():

	return requests.session();
#enddef

def get(url, headers, cookies, session = None):
	
	if session != None:
		response = session.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http);
	else:	
		response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http);
	#endif
	
	return response;
#enddef


def post(url, headers, cookies, body, files = None, session = None):
	
	if session != None:
		response = session.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http, files = files);
	else:
		response = requests.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http, files = files);
	#endif
	
	return response;
#enddef

def head(url, headers, cookies, allow_redirects = False, session = None):
		
	if session != None:
		response = session.head(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, allow_redirects = allow_redirects, timeout = config.timeout.http);
	else:
		response = requests.head(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, allow_redirects = allow_redirects, timeout = config.timeout.http);
	#endif
	
	return response;
#enddef

def download(url, headers, cookies, file_name, session = None):
		
	if session != None:
		response = session.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http);
	else:
		response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = config.proxy.proxies, timeout = config.timeout.http);
	#endif
	
	
	if response.status_code != 200:
		return False;
	#endif
	
	chunk_size = 1024;
	with open(file_name, "wb") as file:
		for data in response.iter_content(chunk_size = chunk_size):
			file.write(data);
		#endfor
	#endwhile

	return True;
#enddef


def getcookies(reponse):
	cookies = None;
	if reponse.status_code == 200:
		cookies = requests.utils.dict_from_cookiejar(reponse.cookies);
	#endif
	
	return cookies;
#enddef

def string2cookies(string):
	cookies={};
	if string.find("=") == -1:
		return cookies;
	#endif
	
	for cookie in string.split(';'):
		name,value=cookie.strip().split('=',1);
		cookies[name]=value;
	#endfor
	
	return cookies;

#enddef

def cookies2string(cookies):
	string = "";
	for key in cookies.keys():
		string = string + key + "=" + cookies[key] + "; "
	#endfor
	
	if string != "":
		string = string[:-2];
	#endif
	
	return string;
#enddef
	
if __name__ == '__main__':
	pass;
#end