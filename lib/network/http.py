# -*- coding: utf-8 -*- 
import requests;
import config;

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get(url, headers, cookies):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxies, timeout = config.timeout.http);
	
	return response;
#enddef


def post(url, headers, cookies, body):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	response = requests.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = proxies, timeout = config.timeout.http);
	
	return response;
#enddef

def head(url, headers, cookies, allow_redirects = False):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	response = requests.head(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxies, allow_redirects = allow_redirects, timeout = config.timeout.http);
	
	return response;
#enddef

def download(url, headers, cookies, file_name):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxies, timeout = config.timeout.http);
	
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

def string2cookies(string):
	cookies={};
	for cookie in string.split(';'):
		name,value=cookie.strip().split('=',1);
		cookies[name]=value;
	#endfor
	
	return cookies

#enddef
	
if __name__ == '__main__':
	pass;
#end