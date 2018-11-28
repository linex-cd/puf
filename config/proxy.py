# -*- coding: utf-8 -*- 

system_proxies = None;

disable_proxies = {'http': None, 'https': None};

proxies_protocol = "http";
proxies_protocol = "socks5";

defined_proxies = {
			'http': proxies_protocol+'://127.0.0.1:8888',
			'https': proxies_protocol+'://127.0.0.1:8888',
		};

proxies = system_proxies;


if __name__ == '__main__':
	pass;
#end