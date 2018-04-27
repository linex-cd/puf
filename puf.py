# -*- coding: utf-8 -*- 
import sys;
import os;

import std.file;
import std.io;
import std.env;
import config;

APP_ROOT_DIR = "app";

def main():
	#Say hello
	std.io.println("Python. Universal. Framework. (%d.%d)" % (std.env.puf_version));
	std.io.println("Python Version: %d.%d" % (std.env.python_version));
	
	std.io.println("Project: %s (%s)" % (config.project.name, config.project.version));

	
	
	if len(sys.argv) < 3:
		std.io.println("Missing parameters.");
		return -1;
	#endif
	
	#specialize param
	app_name = sys.argv[1];
	app_module = sys.argv[2];
	app_action = "main";
	
	if len(sys.argv) > 3:
		app_action = sys.argv[3];
	#endif
	
	#load package
	init_str = "";
	std.file.write(init_str, APP_ROOT_DIR + "/__init__.py", True);
	exe_str = "import "+APP_ROOT_DIR+";";
	exec(exe_str,globals());
	
	app_path = APP_ROOT_DIR + "/" + app_name;
	if not os.path.exists(app_path):
		std.io.println("App not exist.");
		return -2;
	#endif
	
	#load app package
	exe_str = "from " + APP_ROOT_DIR + " import " + app_name + ";";
	exec(exe_str,globals());
	
	#run constructor
	ctor_path = APP_ROOT_DIR + "/" + app_name + "/__ctor__.py";
	if os.path.exists(app_path):
		exe_str = std.file.read(ctor_path);
		exec(exe_str,globals());
	#endif
	
	
	
	#load module
	module_path = app_path + "/" + app_module + ".py";
	if not os.path.exists(module_path):
		std.io.println("Module not exist.");
		return -3;
	#endif
	
	#Set log path
	temp = "/";
	if config.log.path[-1:] == "/" or config.log.path[-1:] == "\\":
		temp = "";
	#endif
	
	if std.dir.exist(config.log.path + temp + app_name) == False:
		r = std.dir.make(config.log.path + temp + app_name);
		if r == False:
			std.io.println("Make sure you have permission to access the log path.");
			return -3;
		#endif
	#endif
	
	config.log.path = config.log.path + temp +app_name + "/" + app_module;
	
	init_str = "";
	ls = os.walk(app_path);
	for dirName, subdirList, fileList in ls:
		
		for file_name in fileList:
			if file_name == "__init__.py":
				continue;			
			#endif
			
			if file_name == "__ctor__.py":
				continue;			
			#endif
			
			if file_name[-3:] != ".py":
				continue;			
			#endif
			
			module_name = file_name[0:-3];
			
			init_str += "from . import "+module_name+";\n";
						
			exe_str = "from "+APP_ROOT_DIR+"."+app_name+" import "+module_name+";";	
			exec(exe_str,globals());
			
		#endfor
		
		std.file.write(init_str, APP_ROOT_DIR + "/"+app_name+"/__init__.py", True);
		
	#endfor
	
	
	
	#run command
	exe_str = "app."+app_name+"."+app_module+"."+app_action+"();";
	exec(exe_str,globals());
		
	
	return 0;
	
#enddef
	

if __name__ == '__main__':
	main();
#end
