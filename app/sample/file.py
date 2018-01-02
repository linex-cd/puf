import app;
import std.file;

if __name__ == '__main__':
	pass;
#end

def main():
	
	content = std.file.read("testfile1.txt");
	
	std.file.write(content, "testfile2.txt", False);
	
	pass;
#enddef




