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
	
	timestr = time.strftime("%Y-%m-%d", time_t);
	
	return timestr;
#enddef


if __name__ == '__main__':
	pass;
#end