#!/usr/bin/python
import urllib
import urllib2
import cookielib

url='http://10.11.77.18:1234/login'
values={'username':'zhangshan','password':'ok'}
data = urllib.urlencode(values)
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
req = urllib2.Request(url, data,headers)
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
response =opener.open(req)
the_page =response.read().decode("utf-8").encode("gbk")
print the_page
