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


def getcookies(response):
	cookies = None;
	if response.status_code == 200:
		cookies = requests.utils.dict_from_cookiejar(response.cookies);
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


import struct
import io
import binascii;
import time;


def cookie_from_ios_cookies_binary_hex_string(ios_cookies_binary_hex_string):

	raw = binascii.unhexlify(ios_cookies_binary_hex_string);
	binary_file = io.BytesIO(raw);
	
	
	file_header = binary_file.read(4);                             #File Magic String:cook 

	if file_header.decode() != 'cook':
		return None;
	#endif
		
	num_pages = struct.unpack('>i',binary_file.read(4))[0];              #Number of pages in the binary file: 4 bytes

	page_sizes = [];
	for np in range(num_pages):
		page_sizes.append(struct.unpack('>i',binary_file.read(4))[0]);  #Each page size: 4 bytes*number of pages
	#endfor
	
	pages = [];
	for ps in page_sizes:
		pages.append(binary_file.read(ps));                     				#Grab individual pages and each page will contain >= one cookie
	
	#endfor
	
	cookie_str = "";
	for page in pages:
		page = io.BytesIO(page);                                     			#Converts the string to a file. So that we can use read/write operations easily.
		page.read(4);                                            				#page header: 4 bytes: Always 00000100
		num_cookies=struct.unpack('<i',page.read(4))[0];                		#Number of cookies in each page, first 4 bytes after the page header in every page.
		
		cookie_offsets=[];
		for nc in range(num_cookies):
			cookie_offsets.append(struct.unpack('<i',page.read(4))[0]); 		#Every page contains >= one cookie. Fetch cookie starting point from page starting byte

		page.read(4);                                            				#end of page header: Always 00000000

		cookie = '';
		for offset in cookie_offsets:
			page.seek(offset);                                   				#Move the page pointer to the cookie starting point
			cookiesize = struct.unpack('<i',page.read(4))[0];             			#fetch cookie size
			cookie = io.BytesIO(page.read(cookiesize));             					#read the complete cookie 
			
			cookie.read(4);                                      				#unknown
			
			flags = struct.unpack('<i',cookie.read(4))[0];                			#Cookie flags:  1=secure, 4=httponly, 5=secure+httponly
			cookie_flags = '';
			if flags == 0:
				cookie_flags = '';
			elif flags == 1:
				cookie_flags = 'Secure';
			elif flags == 4:
				cookie_flags = 'HttpOnly';
			elif flags == 5:
				cookie_flags = 'Secure; HttpOnly';
			else:
				cookie_flags = 'Unknown';
			
			#endif			
			
			cookie.read(4);                                      					#unknown
			
			urloffset = struct.unpack('<i',cookie.read(4))[0];            			#cookie domain offset from cookie starting point
			nameoffset = struct.unpack('<i',cookie.read(4))[0];           			#cookie name offset from cookie starting point
			pathoffset = struct.unpack('<i',cookie.read(4))[0];           			#cookie path offset from cookie starting point
			valueoffset = struct.unpack('<i',cookie.read(4))[0];          			#cookie value offset from cookie starting point
			
			endofcookie = cookie.read(8);                         					#end of cookie
									
			expiry_date_epoch = struct.unpack('<d',cookie.read(8))[0]+978307200;          			#Expiry date is in Mac epoch format: Starts from 1/Jan/2001
			expiry_date = time.strftime("%a, %d %b %Y ",time.gmtime(expiry_date_epoch))[:-1]; 		#978307200 is unix epoch of  1/Jan/2001 //[:-1] strips the last space
					
			create_date_epoch = struct.unpack('<d',cookie.read(8))[0]+978307200;           			#Cookies creation time
			create_date = time.strftime("%a, %d %b %Y ",time.gmtime(create_date_epoch))[:-1];
			#print create_date
			
			cookie.seek(urloffset-4);                            #fetch domaain value from url offset
			url = '';
			u = cookie.read(1);
			while struct.unpack('<b',u)[0] != 0:
				url = url + u.decode();
				u = cookie.read(1);
			#endwhile
			
			cookie.seek(nameoffset-4);                           #fetch cookie name from name offset
			name = '';
			n = cookie.read(1);
			while struct.unpack('<b',n)[0] != 0:
				name = name + n.decode();
				n = cookie.read(1);
			#endwhile
			
			cookie.seek(pathoffset-4);                          #fetch cookie path from path offset
			path = '';
			pa = cookie.read(1)
			while struct.unpack('<b',pa)[0] != 0:
				path = path + pa.decode();
				pa = cookie.read(1);
			#endwhile
			
			cookie.seek(valueoffset-4);                         #fetch cookie value from value offset
			value = '';
			va = cookie.read(1);
			while struct.unpack('<b',va)[0] != 0:
				value = value + va.decode();
				va = cookie.read(1);
			#endwhile
			
			cookie_item = name+'='+value+'; domain='+url+'; path='+path+'; '+'expires='+expiry_date+'; '+cookie_flags;
			cookie_str = cookie_str + cookie_item;
					
		#endfor
	#endfor
	
	return cookie_str;

#enddef


def sorturl(url, asc = True):

	p1 = url.find("?");
	if p1 == -1:
		return url;
	#endif
	
	p2 = url.find("#");
	if p2 == -1:
		p2 = len(url);
	#endif
	
	query = url[p1+1: p2];
	arr = query.split("&");
	dict = [];
	for item in arr:
		temp = item.split("=");
		
		dict.append((temp[0],temp[1]));
	#endfor

	reverse = not asc;
	dict = sorted(dict, key=lambda k:k[0], reverse = reverse);
	
	query = "";
	for item in dict:
		(k, v) = item;
		query = query + k + "=" + v + "&";
	#endfor
	
	query = query[:-1];
	url = url[: p1+1] + query;
	
	return url;
#endif

	
if __name__ == '__main__':
	pass;
#end