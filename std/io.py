# -*- coding: utf-8 -*- 
import config;
import std.file;

import std.env;


def scanln():
	if std.env.python_version < (3, 0):
		from std.scan2 import scanline;
	else:
		from std.scan3 import scanline;
	#endif
	return scanline();
#enddef

def println(str):
	if std.env.python_version < (3, 0):
		from std.print2 import printline;
	else:
		from std.print3 import printline;
	#endif
	printline(str);
	pass;
#enddef

def print(str):
	if std.env.python_version < (3, 0):
		from std.print2 import printstr;
	else:
		from std.print3 import printstr;
	#endif
	printstr(str);
	pass;
#enddef

if __name__ == '__main__':
	pass;
#end