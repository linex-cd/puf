# -*- coding: utf-8 -*- 
import hashlib;

def md5(src_str):
	m2 = hashlib.md5();
	m2.update(src_str);
	dest = m2.hexdigest();
	return dest;
#enddef


def yeast_decode(string):

	alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_';
	length = 64;
	map = {alphabet[i]: i for i in range(length)};

	temp = 0;
	for x in string:
	  temp = temp*64 + map[x];
	#endfor
	
	number = temp;
	return number;
#enddef

def yeast_encode(number):
	
	alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_';
	length = 64;
	map = {alphabet[i]: i for i in range(length)};

	temp = "";
	while True:
		temp = alphabet[number % length] + temp;
		number = int(number / length);
		if number == 0:
			break;
		#endif
	#endwhile

	string = temp;
	return string;
#enddef

if __name__ == '__main__':
	pass;
#end