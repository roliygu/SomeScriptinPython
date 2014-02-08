urllib
	t = urllib.urlopen(url[,data,proxies])
	t 是一个网页文件类对象包含的方法有:
		read(),readline(),readlines(),close()等文件的方法
		info() 返回远程服务器返回的头信息,不过这些信息是啥意思还不知道
		getcode() 返回状态码,200是请求成功,404表示网址未找到
		geturl() 返回url
	实际上urllib模块只是用来编码的
		value = {'userName':'roliy','password':'xxxx'}
		data = urllib.urlencode(value)
		编码之后的data利用urllib2模块中的方法传给服务器
urllib2
	req = urllib2.Request(url,data)
	urllib2.HTTPCookieProcessor()
	urllib2.build_opener()
	urllib2.install_opener()
cookielib
	cookielib.LWPCookieJar()
re
random