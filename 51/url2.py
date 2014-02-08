import urllib2
import urllib

response = urllib2.urlopen('http://www.baidu.com')
data = {'q':'find'}
en_data = urllib.urlencode(data)
print en_data