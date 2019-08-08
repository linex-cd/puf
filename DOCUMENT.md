## PUF Document
### Run
python puf.py $app_name $module_name [$action_name|main]
You can find samples under folder app/sample

```
python puf.py sample hello

python puf.py sample login get_token

```

### API LOOKUP

#### std

* env
	* (major, minor) = python_version
		- return the python version
		- 返回Python版本号
	* (major, minor) = puf_version
		- return the PUF version
		- 返回PUF框架版本号

* io
	* string = scanln()
		- keyboard input, end with enter
		- 键盘输入，回车结束
	* null = println(text)
		- screen output, end with new line
		- 屏幕输出行，带换行
	* null = echo(text)
		- screen output, end without new line
		- 屏幕输出文本，不带换行
	* null = status(text)
		- screen output, without updating editor cursor
		- 屏幕输出文本，不更新编辑器光标位置

* time
	* string = get_time_str(timestamp = None)
		- get time string with second timestamp, current time is default
		- 根据秒时间戳获取时间字符串，默认当前时间
	* string = get_date_str(timestamp = None)
		- get date string with second timestamp, current time is default
		- 根据秒时间戳获取日期字符串，默认当前时间
	* int = get_timestamp(timestr = None)
		- get second timestamp with time string, current time is default
		- 根据时间字符串获取秒时间戳，默认当前时间
	* string = get_time_tick(seconds)
		- format the seconds goes by to time string
		- 格式化秒为时间字符串
	
* str
	* string = shape(src_str, prefix_str, suffix_str)
		- get a string between prefix and suffix from a source string
		- 从源字符串获取前缀和后缀之间的子字符串
	
* codec
	* string = md5(src_str)
		- get a md5 hash of a string
		- 获取一个字符串的md5哈希值

	* int = yeast_decode(string)
		- get a integer number from a string encoded by yeast
		- 把使用yeast算法得到的字符串转换为整数
	* string = yeast_encode(int)
		- get a string from an integer number encoded by yeast
		- 使用yeast算法把数字转换为字符串
	* string = url_encode(string)
		- encode a string by urlencode
		- 使用urlencode编码字符串
	* string = url_decode(string)
		- decode a string by urldecode
		- 使用urldecode解码字符串

* file
	* string = read(filename, charset = "UTF-8", binary = False)
		- read a file content, UTF-8 charset is default, text mode is default (Please check the accessibility of the file by api exist, this interface does not deal with file access excetion.)
		- 读取文件内容，默认UTF-8编码，默认文本模式 (请使用exist检查文件是否存在和可访问,本接口不处理文件访问异常。)
	* bool = write(text, filename, overwrite, charset = "UTF-8", binary = False)
		- white content to a file , UTF-8 charset is default, text mode is default, if overwrite is False, content will append to the file (Please check the accessibility of the file by api exist, this interface does not deal with file access exception.)
		- 写文件内容，默认UTF-8编码，默认文本模式，如果overwrite为False，内容将追加到文件 (请使用exist检查文件是否存在和可访问,本接口不处理文件访问异常。)
	* bool = exist(filename)
		- check the accessibility of a file
		- 检查文件的可访问性
	* bool = delete(filename)
		- delete a file (Please check the accessibility of the file by api exist, this interface does not deal with file access exception.)
		- 删除一个文件 (请使用exist检查文件是否存在和可访问,本接口不处理文件访问异常。)

* dir
	* list = files(path, ext = None)
		- enumerate all files in a directory, including sub directory, if ext is not None, files without this extension will be filtered (Please check the accessibility of the directory by api exist, this interface does not deal with directory access exception.)
		- 枚举一个目录下的所有文件，不包含子目录，如果ext参数不为空，文件不带ext后缀的文件将被过滤 (请使用exist检查目录是否存在和可访问，本接口不处理目录访问异常。)
	* list = ls(path)
		- get sub directories and files in a directory, excluding sub directory (Please check the accessibility of the directory by api exist, this interface does not deal with directory access exception.)
		- 枚举一个目录下的子目录和文件，不包含子目录 (请使用exist检查目录是否存在和可访问，本接口不处理目录访问异常。)
	* bool = exist(path)
		- check the accessibility of a directory
		- 检查目录的可访问性
	* bool = make(path)
		- create a directory, if the parent directory does not exist, also create it
		- 创建一个目录，如果父目录不存在，则自动创建父目录
	
* ex
	* result = ternary(condition, result_true, result_false)
		- ternary operation
		- 三目运算
	* result = switch(case_input, case_name, case_function, case_function_args = ())
		- switch operation
		- 开关操作

* log
	* null = msg(text, echo = True, tofile = None)
		- output message to log. echo is print to screen, tofile is write to file
		- 输出消息到日志，echo表示输出到屏幕，tofile表示写入到文件
	* null = info(text)
		- infomation log, calls msg, set echo and tofile in configuration file
		- 提示日志，调用msg，echo和tofile在配置文件中设置
	* null = debug(text)
		- debug log, calls msg, set echo and tofile in configuration file
		- 调试日志，调用msg，echo和tofile在配置文件中设置
	* null = warn(text)
		- warning log, calls msg, set echo and tofile in configuration file
		- 警告日志，调用msg，echo和tofile在配置文件中设置
* cookie
	* [value, expire] = get(key)
		- get value and expiration time with a key
		- 通过键名获取值和有效期
	* bool = put(key, value, expire = 0)
		- set value and expiration time with a key
		- 通过键名设置值和有效期
	* bool = delete(key)
		- delete a key
		- 删除一个键
	* list = keys()
		- get all keys
		- 获取所有键列表
	* null = clean()
		- delete expired keys
		- 清除过期的键
	* null = flush()
		- delete all keys
		- 清除所有键
	
#### lib

* network
	* http
		* session = create_session()
			- create a session with keep-live connection
			- 创建长连接会话
		* response = get(url, headers, cookies, session = None)
			- GET method of HTTP
			- HTTP的GET方法
		* response = post(url, headers, cookies, body, files = None, session = None)
			- POST method of HTTP, body and files both are dictory objects.
			- HTTP的GET方法, body和files都是字典对象
		* response = head(url, headers, cookies, allow_redirects = False, session = None)
			- HEAD method of HTTP, allow_redirects is whether allow redirection
			- HTTP的HEAD方法，allow_redirects是否允许重定向跳转
		* bool = download(url, headers, cookies, file_name, session = None)
			- download a file to file_name path
			- 下载文件到file_name的位置
		* dict = getcookies(response)
			- get cookies from a HTTP response object
			- 从HTTP响应对象中获取cookie
		* cookies = string2cookies(string)
			- convert string to cookies object
			- 把字符串转为cookies对象
		* string = cookies2string(cookies)
			- convert cookies object to string
			- 把cookies对象转为字符串
		* string = cookie_from_ios_cookies_binary_hex_string(ios_cookies_binary_hex_string)
			- sort url parameters, ascent is default
			- 把iOS的Cookies.binarycookies文件转成cookies字符串
		* string = sorturl(string, asc = True)
			- sort url parameters, ascent is default
			- url参数排序，默认升序

* database
	* mysql
		* C style
			* conn = connect()
				- connect to MySQL server, return the connection object, set host, port, .etc in configuration file
				- 连接到MySQL服务器，返回连接对象。在配置文件中设置连接属性
			* null = close(conn)
				- close connection object
				- 关闭连接对象
			* id = insert(conn, sql)
				- execute insert sql, and get the latest inserted row id
				- 执行插入数据的SQL，并获取插入的最后一条ID
			* id = lastrowid(conn)
				- get latest row id
				- 获取最后一条记录ID
			* bool = update(conn, sql)
				- execute update sql, and return whether update success or not
				- 执行插入数据的SQL，并获取是否成功的结果
			* list = fetch(conn, sql)
				- execute query sql, and return row list (column name is the row key, not array index)
				- 执行查询数据的SQL，并获取条目列表 （列名是记录的键名，而不是数组下标）
			* string = make_insert_sql(table_name, data_dictionary, update_columns)
				- make an insert sql with the table name, data dictionary and update columns, and return the sql string
				- 根据数据字典生成插入表的SQL语句，并根据数组生成当主键存在时的更新语句
		
		* Class style (class name: CMysql)
			* id = .insert(sql)
			* id = .lastrowid()
			* bool = .update(sql)
			* list = .fetch(sql)
			* string = .make_insert_sql(table_name, data_dictionary, update_columns)
	
	* redis
		* C style
			* conn = connect()
				- connect to Redis server, return the connection object, set host, port, .etc in configuration file
				- 连接Redis服务器，返回连接对象。在配置文件中设置连接属性
			* int = dbsize(conn)
				- get databbase keys count
				- 获取数据库键数目
			* bool = set(conn, key, value)
				- set key-value
				- 设置键值对
			* bool = setnx(conn, key, value)
				- set key-value if key not exists
				- 设置键值对如果键不存在
			* bool = setex(conn, key, time, value)
				- set key-value and expire time, if key exists, update it
				- 设置键值对和有效期，如果键存在则更新
			* int = setrange(conn, key, start, value)
				- overwrite value of key, start at the start
				- 用value覆盖key原有的值，覆盖的位置start开始
			* int = getrange(conn, key, start, end)
				- get value of key in the range of start to end
				- 获取键名为key的从start到end的值
			* string = get(conn, key)
				- get value by key
				- 根据键名获取值
			* list = keys(conn, pattern)
				- get keys list with pattern
				- 使用pattern通配符获取键名列表
			* (cursor, list) = scan(conn, cursor, pattern, count)
				- get a number keys list of count with pattern from cursor
				- 使用pattern通配符获取从sursor开始的count个键名列表
			* bool = delete(conn, key)
				- delete a key-value
				- 删除键值对
			* int = incr(conn, key, default = 1)
				- increase a counter key by default
				- 计数器key递增default
			* int = decr(conn, key, default = 1)
				- decrease a counter key by default
				- 计数器key递减default
			* string = hget(conn, hash_name, hash_key)
				- return value of the hash_key in the hash_name
				- 返回哈希表hash_name中指定字段hash_key的值
			* bool = hset(conn, hash_name, hash_key, hash_value)
				- set hash_value of the hash_key in the hash_name
				- 设置哈希表hash_name中指定字段hash_key的值hash_value
			* list = hgetall(conn, hash_name)
				- return hash key-value list of the hash_name
				- 返回哈希表hash_name中key-value的列表
			* bool = hdel(conn, hash_name, hash_key)
				- delete hash_key of the hash_name
				- 删除哈希表hash_name中的hash_key
			* list = hvals(conn, hash_name)
				- retutn the hash values list of hash_name
				- 返回哈希表hash_name所有键的值列表
			* bool = flushdb(conn)
				- delete all data in the database
				- 清空数据库
			* bool = lpush(conn, key, value)
				- push a value to the left side of a list of the key
				- 列表key的左端加入一个value
			* string = lpop(conn, key)
				- remove a value from the left side of a list of the key
				- 列表key的左端移除一个value
			* bool = rpush(conn, key, value)
				- push a value to the right side of a list of the key
				- 列表key的右端加入一个value
			* string = rpop(conn, key)
				- remove a value from the right side of a list of the key
				- 列表key的右端移除一个value
			
		* Class style (class name: CRedis)
			* int = .dbsize()
			* bool = .set(key, value)
			* bool = .setnx(key, value)
			* bool = .setex(key, time, value)
			* int = .setrange(key, num, value)
			* int = .getrange(key, start, end)
			* string = .get(key)
			* list = .keys(pattern)
			* (cursor, list) = .scan(cursor, pattern, count)
			* bool = .delete(key)
			* int = .incr(key, default = 1)
			* int = .decr(key, default = 1)
			* string = .hget(hash_name, hash_key)
			* bool = .hset(hash_name, hash_key, hash_value)
			* list = .hgetall(hash_name)
			* bool = .hdel(name)
			* bool = .flushdb()
			* bool = .lpush(key, value)
			* string = .lpop(key)
			* bool = .rpush(key, value)
			* string = .rpop(key)
			

- config
    * project
		- set project infomation like name, version, description, .etc.
		- 设置项目名称，版本，描述等信息
    * log
		- set log configuration
		- 配置日志
    * proxy
		- set http proxy configuration
		- 配置HTTP代理
    * mysql
		- set MySQL configuration
		- 配置MySQL
    * redis
		- set Redis configuration
		- 配置Redis
    * timeout
		- set MySQL, Redis, HTTP, socket timeout
		- 配置 MySQL, Redis, HTTP, socket 超时时间




