import app;
import config;
import std.io;
import std.ex;
import std.log;
import std.env;

if __name__ == '__main__':
	pass;
#end

def fun_a(args):
	(msg) = args
	std.io.println(msg);

#enddef

def fun_b(args):
	(msg1, msg2) = args
	std.io.println(msg1);
	std.io.println(msg2);

#enddef

def main():
	std.io.println("Hello world");
	std.io.println("Project Name: " + config.project.name);
	std.io.println("Project version: " + config.project.version);
	
	std.io.print("Input a string(a, b or other):");
	x = std.io.scanln();
	
	std.ex.switch(x, "a", fun_a, ("args for a"));
	std.ex.switch(x, "b", fun_b, ("args 1 for b", "args 2 for b"));
	
	std.log.info("INPUT: " + x);
	total=100000  
	for i in range(0,total): 
		percent=float(i)*100/float(total)
		std.io.status("%.4f"%percent);
	#endfor
	
	std.log.info("Bye!");
#enddef




