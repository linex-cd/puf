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
	* (major, minor) = puf_version

* io
	* null = print(text)
    * null = println(text)
	* string = scanln()
	* null = print(text)
	* null = status(text)

* time
	* string = get_time_str(timestamp = None)
	* string = get_date_str(timestamp = None)
	* string = get_timestamp(timestr = None)
	* string = get_time_tick(seconds)
	
* str
	* string = shape(src_str, prefix_str, suffix_str)
	* string = md5(src_str)

* file
	* string = read(filename, charset = "UTF-8", binary = False)
	* bool = write(text, filename, overwrite, charset = "UTF-8", binary = False)
	* bool = exist(filename)
	* bool = delete(filename)
* dir
	* list = travel(path, ext)
	* list = list(path)
	* bool = exist(path)
	* bool = make(path)
	
* ex
	* result = ternary(condition, result_true, result_false)
	* result = switch(case_input, case_name, case_function, case_function_args = ())

* log
	* null = msg(text, echo = True, tofile = None)
	* null = info(text)
	* null = debug(text)
	* null = warn(text)

#### lib

* network
	* http
		* response = get(url, headers, cookies)
		* response = post(url, headers, cookies, body)
		* response = head(url, headers, cookies, allow_redirects = False)
		* bool = download(url, headers, cookies, file_name)
		* cookies = string2cookies(string)

* db
	* mysql
		* C style
			* conn = connect()
			* null = close(conn)
			* id = insert(conn, sql)
			* id = lastrowid(conn)
			* bool = update(conn, sql)
			* list = fetch(conn, sql)
		
		* Class style (class name: CMysql)
			* id = .insert(sql)
			* id = .lastrowid()
			* bool = .update(sql)
			* list = .fetch(sql)
	
	* redis
		* C style
			* conn = connect()
			* int = dbsize(conn)
			* bool = set(conn, key, value)
			* bool = setnx(conn, key, value)
			* bool = setex(conn, key, time, value)
			* int = setrange(conn, key, start, value)
			* int = getrange(conn, key, start, end)
			* string = get(conn, key)
			* list = keys(conn, pattern)
			* (cursor, list) = scan(conn, cursor, pattern, count)
			* bool = delete(conn, key)
			* int = incr(conn, key, default = 1)
			* int = decr(conn, key, default = 1)
			* string = hget(conn, hash_name, hash_key)
			* bool = hset(conn, hash_name, hash_key, hash_value)
			* list = hgetall(conn, hash_name)
			* bool = hdel(conn, name, key = None)
			* bool = clear(conn)
			* bool = lpush(conn, key, value)
			* string = lpop(conn, key)
			
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
			* bool = .hdel(name, key = None)
			* bool = .clear()
			* bool = .lpush(key, value)
			* string = .lpop(key)
			

- config
    * project
    * log
    * proxy
    * mysql
    * redis
    * timeout




