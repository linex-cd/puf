# -------------------------------------
# system proxy
proxy_proxies = None;


# -------------------------------------
# no proxy
proxy_proxies = {
	"https": None,
	"http": None,
};
'''
# -------------------------------------
# local proxy
proxy_proxies = {
	"https": "127.0.0.1:8888",
	"http": "127.0.0.1:8888",
};

# -------------------------------------
# vpn proxy
proxy_proxies = {
	"https": "10.10.0.50:8888",
	"http": "10.10.0.50:8888",
};

# -------------------------------------
# http proxy
proxyHost = "http-dyn.xxx.com"
proxyPort = "9020"
proxyProtocol = "http";


# -------------------------------------
# socks proxy
proxyHost = "socks-cla.xxx.com"
proxyPort = "8030"
proxyProtocol = "socks5";

proxyUser = "-"
proxyPass = "-"


proxyMeta = "%(protocol)s://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "protocol" : proxyProtocol,
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}

proxy_proxies = {
	"https": proxyMeta,
	"http": proxyMeta,
};


'''

http_timeout = 20;

'''
host = "localhost";
user = "root";
password = "";
'''

host = "127.0.0.1";
user = "root";
password = "";


db = "puf";
port = 3306;
charset = "utf8mb4";
mysql_timeout = 1800;

	
if __name__ == '__main__':
	pass;
#end

