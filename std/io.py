# -*- coding: utf-8 -*- 
import config;
import std.file;

import std.env;

import sys;


def scanln():
	if std.env.python_version < (3, 0):
		from std.scan2 import scanline;
	else:
		from std.scan3 import scanline;
	#endif
	return scanline();
#enddef

def println(text):
	if std.env.python_version < (3, 0):
		from std.print2 import printline;
	else:
		from std.print3 import printline;
	#endif
	printline(text);
	pass;
#enddef

def print(text):
	if std.env.python_version < (3, 0):
		from std.print2 import printstr;
	else:
		from std.print3 import printstr;
	#endif
	printstr(text);
	pass;
#enddef

def status(text):
	sys.stdout.write(text);
	sys.stdout.write("\r");
	sys.stdout.flush();
	pass;
#enddef

if __name__ == '__main__':
	pass;
#end