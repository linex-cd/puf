# -*- coding: utf-8 -*- 
import config;
import std.file;

import std.env;

import sys;

if std.env.python_version < (3, 0):
	def_scanline_src='''
def scanline():
	return raw_input();
#enddef
'''

	def_printline_src='''
def printline(string):
	print string
#enddef
'''

	def_printstr_src='''
def printstr(string):
	print string,
#enddef
'''

else:
	def_scanline_src='''
def scanline():
	return input();
#enddef
'''

	def_printline_src='''
def printline(string):
	print(string);
#enddef
'''

	def_printstr_src='''
def printstr(string):
	print(string, end = "");
#enddef
'''

#endif
exec(def_scanline_src);

exec(def_printline_src);

exec(def_printstr_src);


def scanln():
	return scanline();
#enddef

def println(text):
	printline(text);
	pass;
#enddef

def echo(text):
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