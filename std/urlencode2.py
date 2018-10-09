# -*- coding: utf-8 -*- 
from urllib import quote as urllib_quote;
def urlencode(string):
	return urllib_quote(string);
#enddef