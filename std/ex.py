# -*- coding: utf-8 -*- 
def switch(case_input, case_name, case_function, case_function_args = ()):
	if case_input == case_name:
		return case_function(case_function_args);
	#endif
	return None;
#enddef


def ternary(condition, result_true, result_false):
	if condition:
		return result_true;
	else:
		return result_false;
	#endif
	
	pass;
#enddef

if __name__ == '__main__':
	pass;
#end