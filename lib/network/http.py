# -*- coding: utf-8 -*- 
import requests;
import config;

from requests.packages.urllib3.exceptions import InsecureRequestWarning;
requests.packages.urllib3.disable_warnings(InsecureRequestWarning);


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