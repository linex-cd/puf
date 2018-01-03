# -*- coding: utf-8 -*- 

import time;


def get_time_str(timestamp = None):
	
	time_t = time.localtime(int(time.time()));
	if timestamp != None:
		time_t = time.localtime(timestamp);
	#endif

	timestr = time.strftime("%Y-%m-%d %H:%M:%S", time_t);
	
	return timestr;
#enddef

def get_date_str(timestamp = None):

	time_t = time.localtime(int(time.time()));
	if timestamp != None:
		time_t = time.localtime(timestamp);
	#endif
	
	datestr = time.strftime("%Y-%m-%d", time_t);
	
	return datestr;
#enddef

def get_time_tick(seconds):

	year = (seconds) // (60 * 60 * 24 * 365);
	
	seconds = seconds - year * 60 * 60 * 24 * 365;
	month = (seconds) // (60 * 60 * 24 * 30);
	
	seconds = seconds - month * 60 * 60 * 24 * 30;
	day = (seconds ) // (60 * 60 * 24);
	
	seconds = seconds - day *  60 * 60 * 24;
	hour = (seconds) // (60 * 60);
	
	seconds = seconds - hour * 60 * 60;
	minute = (seconds) // (60); 
	
	seconds = seconds - minute * 60;
	second = (seconds) // (1);  
	
	timetickstr = "%d year(s), %d month(s), %d day(s), %d hour(s), %d minute(s), %d second(s)" % (year, month, day, hour, minute, second);
	
	return timetickstr;
#enddef

if __name__ == '__main__':
	pass;
#end