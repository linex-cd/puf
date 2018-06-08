# -*- coding: utf-8 -*- 

def shape(src_str, prefix_str, suffix_str):
	
	prefix_pos = src_str.find(prefix_str) + len(prefix_str);
	if prefix_pos == -1:
		return None;
	#endif
	temp_str = src_str[prefix_pos:];
	
	suffix_pos = temp_str.find(suffix_str);
	if suffix_pos == -1:
		return None;
	#endif
	dest_str = temp_str[:suffix_pos];
	
	return dest_str;
#enddef

if __name__ == '__main__':
	pass;
#end