import app;
import config;
import std.io;
import std.ex;
import std.log;
import std.env;

import std.time;

import time;

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
	
	std.io.echo("Input a string(a, b or other):");
	x = std.io.scanln();
	
	std.ex.switch(x, "a", fun_a, ("args for a"));
	std.ex.switch(x, "b", fun_b, ("args 1 for b", "args 2 for b"));
	
	std.log.info("INPUT: " + x);
	
	t1 = std.time.get_timestamp();
	total=300;
	for i in range(0,total): 
		percent=float(i)*100/float(total)
		std.io.status("%.2f%%"%percent);
		time.sleep(0.03);
	#endfor
	
	t2 = std.time.get_timestamp();
	elapses = std.time.get_time_tick(t2-t1+7200);
	std.io.println("\n%s" % elapses);
	
	std.log.info("Bye!");
#enddef




