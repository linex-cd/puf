# -*- coding: utf-8 -*- 
import requests
import config



def get(url, headers, cookies):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	result = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxies, timeout = config.timeout.http);
	
	return result;
#enddef


def post(url, headers, cookies, body):
	
	proxies = None;
	if config.proxy.enable == True:
		proxies = config.proxy.proxies;
	#endif
	
	result = requests.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = proxies, timeout = config.timeout.http);
	
	return result;
#enddef

	
if __name__ == '__main__':
	pass;
#end