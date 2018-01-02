# -*- coding: utf-8 -*- 
from __future__ import absolute_import;

from os import W_OK as os_W_OK;
from os import access as os_access;
from os.path import join as os_path_exists;
from os.path import isfile as os_path_isfile;

import std.env;

def read(filename, charset = "UTF-8", binary = False):
	f = False;
	mode = "r";
	if binary:
		mode = mode+"b";
	#endif
	
	if std.env.python_version < (3, 0):
		from codecs import open as open2;
		f = open2(filename, mode, encoding = charset);
	else:
		f = open(filename, mode, encoding = charset);
	#endif
	
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

def write(text, filename, overwrite, charset = "UTF-8", binary = False):
	mode = "a";
	if overwrite == True:
		mode = "w";
	#endif
	
	f = False;
	if binary:
		mode = mode+"b";
	#endif
	
	if std.env.python_version < (3, 0):
		from codecs import open as open2;
		f = open2(filename, mode, encoding = charset);
	else:
		f = open(filename, mode, encoding = charset);
	#endif

	if f == False:
		return False;
	#endif
	

	f.write(text);
	f.close();
	return True;
#enddef

def exist(filename):
	if os_path_exists(filename) and os_path_isfile(filename) and os_access(filename, os_W_OK):
		return True;
	#endif
	return False;
#enddef

if __name__ == '__main__':
	pass;
#end