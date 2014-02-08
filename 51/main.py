import urllib,urllib2,cookielib,re,random

class Login:
    _login_url = 'http://home.51cto.com/index.php?s=/Index/doLogin'
    _method = 'post'
    _headers = [
                ('host','home.51cto.com'),\
                ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'),\
                ('Referer','http://home.51cto.com/index.php?s=/Index/index/reback/http%253A%252F%252Fwww.51cto.com%252F/')\
        ]
    _data = {
             'cookie_file_path':'./51cto_cookies.dat'
        }
    _re = r'src="(.+?)"'
    _version = '0.1'
    _connect_info = {}
    def __init__(self,email,pwd):
        self._login_data ={
        'email':email,'passwd':pwd
        }
        self._connect_info['cookie'] = cookielib.LWPCookieJar()
        try:
            self._connect_info['cookie'].revert(self._data['cookie_file_path'])
        except Exception,e:             
            print e
        self._connect_info['cookie_processor'] = urllib2.HTTPCookieProcessor(self._connect_info['cookie'])
        self._connect_info['post_data'] = urllib.urlencode(self._login_data)
    def open(self):
        opener = urllib2.build_opener(self._connect_info['cookie_processor'])
        opener.addheaders = self._headers
        urllib2.install_opener(opener)

        
        #opener.open(request)
        request = urllib2.Request(self._login_url,self._connect_info['post_data'])
        conn = opener.open(request)
        if(conn.geturl() == self._login_url):
            self._connect_info['cookie'].save(self._data['cookie_file_path'])
        else:
            pass
        partner = re.compile(self._re)
        match = partner.findall(conn.read())
        
        for item in match:
            opener.open(item)
              
        
        url = 'http://down.51cto.com/download.php'
        data = {'do':'getfreecredits','t':random.random()}
        opener.open(url, urllib.urlencode(data))
        #html = opener.open('http://down.51cto.com/')
        
        url = 'http://home.51cto.com/index.php?s=/Home/toSign'
        data = {'s':''}
        opener.open(url, urllib.urlencode(data))
        print "done it"

if __name__ == '__main__':
    login_51cto = Login('roliygu@gmail.com','66626110')
    login_51cto.open()
    login_51cto = Login('279581355@qq.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu@163.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu1@163.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu2@163.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu3@163.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu4@163.com','66626110')
    login_51cto.open()
    login_51cto = Login('roliygu5@163.com','66626110')
    login_51cto.open()
        
        