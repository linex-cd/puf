# -*- coding: utf-8 -*- 
from sys import version_info;

from os import W_OK as os_W_OK;
from os import access as os_access;
from os import remove as os_remove;
from os.path import join as os_path_exists;
from os.path import isfile as os_path_isfile;

from config import *;
import time;
import random;

#######################################

(major, minor, micro, releaselevel, serial) = version_info;
python_version = (major, minor);

#######################################

if python_version < (3, 0):
	def_printline_src='''
def printline(string):
	print string
#enddef
'''
else:
	def_printline_src='''
def printline(string):
	print(string);
#enddef
'''
#endif

exec(def_printline_src);

######################################

def shape(src_str, prefix_str, suffix_str):
	
	prefix_pos = src_str.find(prefix_str) + len(prefix_str);
	if prefix_pos == -1:
		return None;
	#endif
	temp_str = src_str[prefix_pos:];
	
	suffix_pos = temp_str.find(suffix_str);
	if suffix_pos == -1:
		return None;
	#endif
	dest_str = temp_str[:suffix_pos];
	
	return dest_str;
#enddef


def log(text):

	now = time.strftime("%Y-%m-%d %H:%M:%S");
	text = "["+now+"] "+text;

	printline(text);
	pass;
#enddef


def readfile(filename):
	
	f = open(filename, "r");
	if f == False:
		return None;
	#endif
	
	text = "";
	
	for line in f.readlines():
		text = text + line;
	#endfor

	f.close();
	
	return text;
#enddef


def writefile(filename, text, mode = "w"):
	
	f = None;
	encoding = "UTF-8";
	if mode.find("b") >=0:
		encoding = None;
	#endif
	
	if python_version < (3, 0):
		from codecs import open as open2;
		f = open2(filename, mode, encoding);
	else:
		f = open(filename, mode, encoding);
	#endif
	
	f.write(text);
	f.close();
	pass;
#enddef

def existfile(filename):
	if os_path_exists(filename) and os_path_isfile(filename) and os_access(filename, os_W_OK):
		return True;
	#endif
	return False;
#enddef


######################################
import hashlib   

def md5(src):
	m2 = hashlib.md5();
	m2.update(src);
	dest = m2.hexdigest();
	return dest;
#enddef

######################################

def yeast_decode(string):

	alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_';
	length = 64;
	map = {alphabet[i]: i for i in range(length)};

	temp = 0;
	for x in string:
		temp = temp*64 + map[x];
	#endfor
	
	number = temp;
	return number;
#enddef

def yeast_encode(number):
	
	alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_';
	length = 64;
	map = {alphabet[i]: i for i in range(length)};

	temp = "";
	while True:
		temp = alphabet[number % length] + temp;
		number = int(number / length);
		if number == 0:
			break;
		#endif
	#endwhile

	string = temp;
	return string;

#enddef


def url_encode(string):
	if python_version < (3, 0):
		from urllib import quote as urlencode;
	else:
		from urllib.parse import quote_plus as urlencode;
	#endif
	return urlencode(string);
#enddef

def url_decode(string):
	if python_version < (3, 0):
		from urllib import quote as urldecode;
	else:
		from urllib.parse import unquote_plus as urldecode;
	#endif
	return urldecode(string);
#enddef


######################################

proxy_list = [];
proxy_filename = "proxy.txt";
if existfile(proxy_filename) == True:
	f = open(proxy_filename);
	for line in f:
		line = line.strip();
		if len(line) < 3:
			continue;
		#endif
		proxy_list.append(line);
	#endfor
	
	f.close();
	
#endif
'''
import win_inet_pton;
import socket;
import socks;

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, socksip, socksport);
socket.socket = socks.socksocket;
'''
import requests;

from requests.packages.urllib3.exceptions import InsecureRequestWarning;
requests.packages.urllib3.disable_warnings(InsecureRequestWarning);

def create_session():

	return requests.session();
#enddef

def get(url, headers, cookies, session = None):
	if proxy_proxies["http"] != None and len(proxy_list) > 0: 
		proxy = random.choice(proxy_list);

		proxy_proxies["http"] = proxy;
		proxy_proxies["https"] = proxy;
		#print("proxy:"+proxy);
	#endif

	if session != None:
		response = session.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout);
	else:
		response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout);
	#endif
	return response;
#enddef


def post(url, headers, cookies, body, files = None, session = None):
	if len(proxy_list) > 0: 
		proxy = random.choice(proxy_list);

		proxy_proxies["http"] = proxy;
		proxy_proxies["https"] = proxy;
		#print("proxy:"+proxy);
	#endif
	if session != None:
		response = session.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout, files = files);
	else:	
		response = requests.post(url = url, data = body, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout, files = files);
	#endif
	return response;
#enddef


def download(url, headers, cookies, file_name, session = None):
	if len(proxy_list) > 0: 
		proxy = random.choice(proxy_list);

		proxy_proxies["http"] = proxy;
		proxy_proxies["https"] = proxy;
		#print("proxy:"+proxy);
	#endif	
	if session != None:
		response = session.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout);
	else:
		response = requests.get(url = url, headers = headers, cookies = cookies, verify = False, proxies = proxy_proxies, timeout = http_timeout);
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

####################################################
#*******************************************************************************#
# cookie_from_ios63data: Written By Linex                                       #
#                                                                               #
#                                                                               #
# Safari browser and iOS applications store the persistent cookies in a binary  #
# file names Cookies.binarycookies.BinaryCookieReader is used to dump all the   #
# cookies from the binary Cookies.binarycookies file.                           #
#                                                                               #
#*******************************************************************************#

import struct
import io
import time;
import binascii;


def cookie_from_ios_cookies_binary_hex_string(ios_cookies_binary_hex_string):

	raw = binascii.unhexlify(ios_cookies_binary_hex_string);
	binary_file = io.BytesIO(raw);
	
	
	file_header = binary_file.read(4);                             #File Magic String:cook 

	if file_header.decode() != 'cook':
		return None;
	#endif
		
	num_pages = struct.unpack('>i',binary_file.read(4))[0];              #Number of pages in the binary file: 4 bytes

	page_sizes = []
	for np in range(num_pages):
		page_sizes.append(struct.unpack('>i',binary_file.read(4))[0]);  #Each page size: 4 bytes*number of pages
	#endfor
	
	pages = []
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



####################################################
import pymysql;

def connect():
	
	RETRY_TIMES = 3;
	conn = None;
	for i in range(RETRY_TIMES):
		try:
			conn = pymysql.connect(host = host, user = user, password = password, db = db, port = port, charset = charset, connect_timeout = mysql_timeout);
			break;
		except Exception as e:
			#log("Mysql Connect Error: %s" % e);
			log("data connection error");
		finally:  
			pass;
		#endtry
		
	#endfor
	
	return conn;
#enddef


def close(conn):
	
	try:
		conn.close()
	except Exception as e:
		#log("Mysql Close Error: %s" % e);
		log("data shutdown error");
	finally:  
		pass;
	#endtry
	
	return True;
#enddef


def insert(conn, sql):
	
	id = 0;
	try:
		cur = conn.cursor();
		cur.execute(sql);
		
		id = int(conn.insert_id()); #conn.insert_id() must be used before conn.commit(), or it will be zero  
		
		conn.commit();
	except Exception as e:
		log("Mysql Insert Error: %s, %s" % (e, sql));
		log("data insert error");
		conn.rollback();
		id = -1;
	finally:  
		cur.close();
	#endtry
	
	return id;
#enddef

def lastrowid(conn):
	
	id = 0;
	try:
		cur = conn.cursor();
		id = int(cur.lastrowid);
		
	except Exception as e:
		#log("Mysql LastRowID Error: %s" % e);
		log("data last_id error");
		id = -1;
	finally:  
		cur.close();
	#endtry
	
	return id;
#enddef

def update(conn, sql):
	
	result = True;

	try:
		cur = conn.cursor(pymysql.cursors.DictCursor);
		cur.execute(sql);

		conn.commit();
	except Exception as e:
		log("Mysql Update Error: %s" % e);
		writefile("mysql-err.txt", sql, mode = "a");
		log("data update error");
		conn.rollback();
		result = False;
	finally:  
		cur.close();
	#endtry
	
	return result;
#enddef

def fetch(conn, sql):
	
	list = [];
	try:
		cur = conn.cursor(pymysql.cursors.DictCursor);
		rs = cur.execute(sql);
		list = cur.fetchmany(rs);
		conn.commit();
	except Exception as e:
		log("Mysql Fetch Error: %s" % e);
		log("data fetch error");
		conn.rollback();
		list = None;
	finally:  
		cur.close();
	#endtry
	
	return list;
#enddef	


def make_insert_sql(table_name, data_dictionary, update_columns):
		
	columnssql = "";
	valuessql = "";
	updatessql = "";
	if len(update_columns) > 0:
		updatessql = " on duplicate key update ";
	#endif
	for key in data_dictionary.keys():
		data_dictionary[key] = str(data_dictionary[key]);
		data_dictionary[key] = data_dictionary[key].replace("'", "\'");
		data_dictionary[key] = data_dictionary[key].replace("`", "\`");
		data_dictionary[key] = data_dictionary[key].replace("\\", "\\\\");
		columnssql = columnssql + "`"+key+"`,\n";
		valuessql = valuessql + "'"+data_dictionary[key]+"',\n";
		
		if key in update_columns:
			updatessql = updatessql + "`"+key+"` = '"+str(data_dictionary[key])+"',\n";
		#endif
	#endfor
	
	sql = "insert into `#tablename#`( #columns# ) values( #values# ) #updates# ;\n";
	
	columnssql = columnssql[:-2];
	valuessql = valuessql[:-2];

	if len(updatessql) > len(" on duplicate key update "):
		updatessql = updatessql[:-2];
	else:
		updatessql = "";
	#endif
	
	sql = sql.replace("#tablename#", table_name);
	sql = sql.replace("#columns#", columnssql);
	sql = sql.replace("#values#", valuessql);
	sql = sql.replace("#updates#", updatessql);
	
	return sql;
#enddef

	
if __name__ == '__main__':
	pass;
#end

