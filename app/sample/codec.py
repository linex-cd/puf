import app;
import config;
import std.io;
import std.codec;
import std.log;
import std.env;

import std.time;

import time;

if __name__ == '__main__':
	pass;
#end


def main():
	std.io.println("Hello world");
	std.io.println("Project Name: " + config.project.name);
	std.io.println("Project version: " + config.project.version);
	
	
	std.log.info("CODEC DEMO");
	
	a = "你好";
	b = std.codec.url_encode(a);
	c = std.codec.url_decode(b);
	std.log.info(a);
	std.log.info(b);
	std.log.info(a);
	
	std.log.info("Bye!");
#enddef




