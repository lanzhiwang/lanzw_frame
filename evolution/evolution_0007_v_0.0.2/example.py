#!/usr/bin/env python
# -*- coding: utf-8 -*-


from evolution_0007 import route, run, request, response, send_file, abort, validate

# Lets start with "Hello World!"
# Point your Browser to 'http://localhost:8080/' and greet the world :D
@route('/')
def hello_world():
    return 'Hello World!'

# Receiving GET parameter (/hello?name=Tim) is as easy as using a dict.
@route('/hello')
def hello_get():
    name = request.GET['name']
    return 'Hello %s!' % name

# This example handles POST requests to '/hello_post'
@route('/hello_post', method='POST')
def hello_post():
    name = request.POST['name']
    return 'Hello %s!' % name

# Cookies :D
@route('/counter')
def counter():
    print '开始处理 Request 中的 cookie 信息'
    old = request.COOKIES.get('counter',0)
    new = int(old) + 1
    print '获取 Response 中的 cookie 信息'
    cookie = response.COOKIES
    print '设置 Response 中的 cookie 信息'
    cookie['counter'] = new  # 或者使用 response.set_cookie('counter', new)，两种设置 cookie 的方法都行
    return "You viewed this page %d times!" % new

"""
store Cookie
curl --cookie-jar cookie.txt http://localhost:8080/counter

send Cookie
curl --cookie cookie.txt http://localhost:8080/counter


第一次请求客户端没有携带 cookie，请求之后将服务器端发送的 cookie 存储到文件
curl --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 1 times!

ll cookie.txt 
-rw-r--r-- 1 root root 171 Aug  3 17:33 cookie.txt

cat cookie.txt 
# Netscape HTTP Cookie File
# http://curl.haxx.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

localhost	FALSE	/	FALSE	0	counter	1

第二次请求客户端携带 cookie，服务端会接收客户端的 cookie，然后服务端会发生新的 cookie，但此时客户端没有存储新的 cookie
curl --cookie cookie.txt http://localhost:8080/counter
You viewed this page 2 times!

cat cookie.txt 
# Netscape HTTP Cookie File
# http://curl.haxx.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

localhost	FALSE	/	FALSE	0	counter	1

第三次请求携带的是旧的 cookie 值，所以返回结果不变
curl --cookie cookie.txt http://localhost:8080/counter
You viewed this page 2 times!

cat cookie.txt 
# Netscape HTTP Cookie File
# http://curl.haxx.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

localhost	FALSE	/	FALSE	0	counter	1

服务端输出:
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: 
Request raw_dict.values(): []
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=1
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:18:28] "GET /counter HTTP/1.1" 200 29
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: Set-Cookie: counter=1
Request raw_dict.values(): [<Morsel: counter='1'>]
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=2
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:18:31] "GET /counter HTTP/1.1" 200 29
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: Set-Cookie: counter=1
Request raw_dict.values(): [<Morsel: counter='1'>]
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=2
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:18:33] "GET /counter HTTP/1.1" 200 29

###############################################

curl --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 1 times!

curl --cookie cookie.txt --cookie-jar cookie1.txt http://localhost:8080/counter
You viewed this page 2 times!

curl --cookie cookie1.txt --cookie-jar cookie2.txt http://localhost:8080/counter
You viewed this page 3 times!

服务端输出:
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: 
Request raw_dict.values(): []
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=1
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:21:34] "GET /counter HTTP/1.1" 200 29
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: Set-Cookie: counter=1
Request raw_dict.values(): [<Morsel: counter='1'>]
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=2
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:22:36] "GET /counter HTTP/1.1" 200 29
开始处理 Request 中的 cookie 信息
Request cookie raw_dict: Set-Cookie: counter=2
Request raw_dict.values(): [<Morsel: counter='2'>]
Request type(raw_dict.values()): <type 'list'>
获取 Response 中的 cookie 信息
Response COOKIES not exits
Response COOKIES: 
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
设置 Response 中的 cookie 信息
Response COOKIES: Set-Cookie: counter=3
Response type(self._COOKIES): <class 'Cookie.SimpleCookie'>
响应头信息设置 cookies
127.0.0.1 - - [03/Aug/2019 18:22:54] "GET /counter HTTP/1.1" 200 29

###############################################

curl --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 1 times!

curl --cookie cookie.txt --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 2 times!

curl --cookie cookie.txt --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 3 times!

curl --cookie cookie.txt --cookie-jar cookie.txt http://localhost:8080/counter
You viewed this page 4 times!

"""


# URL-parameter are a useful tool and generate nice looking URLs
# This handles requests such as '/hello/Tim' or '/hello/Jane'
@route('/hello/:name')
def hello_url(name):
    return 'Hello %s!' % name

# By default, an URL parameter matches everything up to the next slash.
# You can change that behaviour by adding a regular expression between two '#'
# in this example, :num will only match one or more digits.
# Requests to '/number/Tim' won't work (and result in a 404)
@route('/number/:num#[0-9]+#')
def hello_number(num):
    return "Your number is %d" % int(num)

# How to send a static file to the Browser? Just name it.
# Bottle does the content-type guessing and save path checking for you.
@route('/static/:filename#.*#')
def static_file(filename):
    send_file(filename, root='/path/to/static/files/')

# You can manually add header and set the content-type of the response.
@route('/json')
def json():
    response.header['Cache-Control'] = 'no-cache, must-revalidate'
    response.content_type = 'application/json'
    return "{counter:%d}" % int(request.COOKIES.get('counter',0))

# Throwing an error using abort()
@route('/private')
def private():
    if request.GET.get('password','') != 'secret':
        abort(401, 'Go away!')
    return "Welcome!"

"""
# Validating URL Parameter
@route('/validate/:i/:f/:csv')
@validate(i=int, f=float, csv=lambda x: map(int, x.strip().split(',')))
def validate_test(i, f, csv):
    return "Int: %d, Float:%f, List:%s" % (i, f, repr(csv))
"""


def validate_test(i, f, csv):
    return "Int: %d, Float:%f, List:%s" % (i, f, repr(csv))


decorator = validate(i=int, f=float, csv=lambda x: map(int, x.strip().split(',')))
wrapper = decorator(validate_test)
route('/validate/:i/:f/:csv')(wrapper)
"""
curl http://localhost:8080/validate/2/2.5/csv
vkargs: {'i': <type 'int'>, 'csv': <function <lambda> at 0x20ae668>, 'f': <type 'float'>}
kargs: {'i': '2', 'csv': 'csv', 'f': '2.1'}
"""

run(host='localhost', port=8080)
