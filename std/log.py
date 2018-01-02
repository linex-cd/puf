# -*- coding: utf-8 -*- 
import config;
import std.io;
import std.file;
import std.time;

import sys;

def msg(text, echo = True, tofile = None):
	parent_function_file = sys._getframe().f_back.f_back.f_code.co_filename; 
	parent_function_name = sys._getframe().f_back.f_back.f_code.co_name;
	parent_line_number = sys._getframe().f_back.f_back.f_lineno;

	if echo:
		echostr = "["+std.time.get_time_str() + "]" + text;
		std.io.println(echostr);
	#endif
	
	if tofile:
		logstr = "["+std.time.get_time_str() + "]" + parent_function_file + ":" + parent_function_name + ":" + str(parent_line_number) + "\n" + text;
		std.file.write(logstr + "\n", tofile, False);
	#endif
	pass;
#enddef

def info(text):

	logstr = "[INFO]" + text;
	
	logfile = None;
	if config.log.info_file == True:
		logfile = config.log.path + "_" + std.time.get_date_str() +"_info.log";
	#endif
	msg(logstr, config.log.info_echo, logfile);
	pass;
#enddef

def debug(text):
	logstr = "[DEBUG]" + text;
	logfile = None;
	if config.log.debug_file == True:
		logfile = config.log.path + "_" + std.time.get_date_str() +"_debug.log";
	#endif
	msg(logstr, config.log.debug_echo, logfile);
	pass;
#enddef

def warn(text):
	logstr = "[WARNING]" + text;
	logfile = None;
	if config.log.warn_file == True:
		logfile = config.log.path + "_" + std.time.get_date_str() +"_warning.log";
	#endif
	msg(logstr, config.log.warn_echo, logfile);
	pass;
#enddef

if __name__ == '__main__':
	pass;
#end