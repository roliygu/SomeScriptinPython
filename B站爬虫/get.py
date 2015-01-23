import urllib2
import BeautifulSoup
import StringIO,gzip
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''

response = urllib2.urlopen("http://www.bilibili.com/video/part-twoelement-1.html")
request.add_header('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0')
request.add_header('Host','www.bilibili.com')
request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
request.add_header('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
request.add_header('Referer','http://www.bilibili.com/')
request.add_header('Cookie','CNZZDATA2724999=cnzz_eid%3D1839222402-1421725204-http%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1421830922; pgv_pvi=5409110016; pgv_si=s3456984064; sid=jnkivof2; __track_isp_speed=1')
request.add_header('Connection','keep-alive')
'''

def getURLList():
	def getURLfromnum(num):
		url = 'http://www.bilibili.com/video/part-twoelement-1.html'
		newurl = url[:-6]+str(num)+url[-5:]
		return newurl
	return [getURLfromnum(i) for i in range(1,302)]

def gzdecode(data):
	temp = StringIO.StringIO(data) 
	gziper = gzip.GzipFile(fileobj=temp)
	return gziper.read()

def dealOnePage(url):
	def getNameViewer(tag):
		def getnum(string):
			if(string[0]=='-'):
				return 0;
			else:
				return int(string)

		lable = tag.next()
		name = lable[2].contents[0]
		gk = getnum(lable[4].contents[0])
		sc = getnum(lable[5].contents[0])
		dm = getnum(lable[6].contents[0])
		return (name,gk,sc,dm)
	response = urllib2.urlopen(url)
	html = gzdecode(response.read())
	soup = BeautifulSoup.BeautifulSoup(html)
	liList = soup.findAll('li')
	List = []
	for i in liList:
		if i.has_key('class') and i['class'] == 'l1':
			List.append(getNameViewer(i))
	return List

def show(List):
	for i in List:
		print '('+i[0]+','+str(i[1])+','+str(i[2])+','+str(i[3])+')'


def getAllPage(urlList):
	AList = []
	for i in urlList:
		onepagelist = dealOnePage(i)
		for j in onepagelist:
			AList.append(j)
	return AList

def sortandwrite(T):
	opener = open('/home/roliy/newsort.txt','w')
	sor = sorted(T, key=lambda t: t[1])
	for i in sor[::-1]:
		opener.write(i[0])
		opener.write(",    ")
		opener.write(str(i[1]))
		opener.write(",    ")
		opener.write(str(i[2]))
		opener.write(",    ")
		opener.write(str(i[3]))
		opener.write('\n')

url = getURLList()
Al = getAllPage(url)
sortandwrite(Al)