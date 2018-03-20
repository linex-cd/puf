# -*- coding: utf-8 -*- 
import requests
import config

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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