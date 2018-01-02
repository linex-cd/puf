# -*- coding: utf-8 -*- 
from os import walk as os_walk;
from os import listdir as os_listdir;
from os import W_OK as os_W_OK;
from os import access as os_access;
from os import makedirs as os_makedirs;
from os.path import join as os_path_join;
from os.path import join as os_path_exists;
from os.path import isdir as os_path_isdir;

def travel(path, ext):
	
	file_list = [];
	ls = os_walk(path);
	for dirName, subdirList, fileList in ls:
		
		if ext == "" or ext == None:
			for file in fileList:
				
				filepath = os_path_join(dirName,file);
				filepath = filepath.replace("\\", "/");
				file_list.append(filepath);
						
			#endfor
		else:
			for file in fileList:
				extlen = len(ext);
				if file[-1-extlen:] == "." + ext:
					filepath = os_path_join(dirName,file);
					filepath = filepath.replace("\\", "/");
					file_list.append(filepath);
				#endif
							
			#endfor
		
		#endif
		
		
	#endfor
	
	return file_list;
#enddef


def list(path):
	
	dir_list = os_listdir(path);
	dir_list.sort(key = str.lower);
	
	return dir_list;
#enddef

def exist(path):
	if os_path_exists(path) and os_path_isdir(path) and os_access(path, os_W_OK):
		return True;
	#endif
	return False;
#enddef

def make(path):
	ret = True;
	try:
		os_makedirs(path);
	except:
		ret = False;
	#endtry
	return ret;
#enddef

if __name__ == '__main__':
	pass;
#end