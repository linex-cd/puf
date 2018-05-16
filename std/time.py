# -*- coding: utf-8 -*- 
from __future__ import absolute_import
import time as sys_time;


def get_time_str(timestamp = None):
	
	time_t = sys_time.localtime(int(sys_time.time()));
	if timestamp != None:
		time_t = sys_time.localtime(timestamp);
	#endif

	timestr = sys_time.strftime("%Y-%m-%d %H:%M:%S", time_t);
	
	return timestr;
#enddef

def get_date_str(timestamp = None):

	time_t = sys_time.localtime(int(sys_time.time()));
	if timestamp != None:
		time_t = sys_time.localtime(timestamp);
	#endif
	
	datestr = sys_time.strftime("%Y-%m-%d", time_t);
	
	return datestr;
#enddef

def get_timestamp(time_str = None):

	timestamp = sys_time.time();
	if time_str != None:
		timestamp = sys_time.mktime(sys_time.strptime(time_str,'%Y-%m-%d %H:%M:%S'));
	#endif
	
	timestamp = int(timestamp);
	
	return timestamp;
#enddef

def get_time_tick(seconds):
	
	start_flag = False;
	
	str_year = "";
	year = (seconds) // (60 * 60 * 24 * 365);
	str_s = "";
	if year > 1:
		str_s = "s";
	#endif
	if year > 0:
		str_year = "%d year%s, " % (year, str_s);
		start_flag = True;
	#endif
	
	str_month = "";
	seconds = seconds - year * 60 * 60 * 24 * 365;
	month = (seconds) // (60 * 60 * 24 * 30);
	str_s = "";
	if month > 1:
		str_s = "s";
	#endif
	if start_flag or month > 0:
		str_month = "%d month%s, " % (month, str_s);
		start_flag = True;
	#endif
	
	str_day = "";
	seconds = seconds - month * 60 * 60 * 24 * 30;
	day = (seconds ) // (60 * 60 * 24);
	str_s = "";
	if day > 1:
		str_s = "s";
	#endif
	if start_flag or day > 0:
		str_day = "%d day%s, " % (day, str_s);
		start_flag = True;
	#endif
	
	str_hour = "";
	seconds = seconds - day *  60 * 60 * 24;
	hour = (seconds) // (60 * 60);
	str_s = "";
	if hour > 1:
		str_s = "s";
	#endif
	if start_flag or hour > 0:
		str_hour = "%d hour%s, " % (hour, str_s);
		start_flag = True;
	#endif
	
	str_minute = "";
	seconds = seconds - hour * 60 * 60;
	minute = (seconds) // (60); 
	str_s = "";
	if minute > 1:
		str_s = "s";
	#endif
	if start_flag or minute > 0:
		str_minute = "%d minute%s, " % (minute, str_s);
		start_flag = True;
	#endif
	
	str_second = "";
	seconds = seconds - minute * 60;
	second = (seconds) // (1);  
	str_s = "";
	if start_flag or second > 1:
		str_s = "s";
	#endif
	str_second = "%d second%s." % (second, str_s);

	
	timetickstr = str_year + str_month + str_day + str_hour + str_minute + str_second;
	
	return timetickstr;
#enddef

if __name__ == '__main__':
	pass;
#end