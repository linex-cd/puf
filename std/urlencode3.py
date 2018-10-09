# -*- coding: utf-8 -*- 
from urllib.parse import quote_plus as urllib_parse_urlencode;
def urlencode(string):
	return urllib_parse_urlencode(string);
#enddef