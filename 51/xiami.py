# -*- coding: cp936 -*-
'''
Created on 2012-11-15

@author: liushuai
'''
import urllib, urllib2, cookielib, sys

class LoginXiami:
    login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}
    signin_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4', 'X-Requested-With':'XMLHttpRequest', 'Content-Length':0, 'Origin':'http://www.xiami.com', 'Referer':'http://www.xiami.com/'}
    email = ''
    password = ''
    cookie = None
    cookieFile = './cookie.dat'

    def __init__(self, email, pwd):
        self.email = email
        self.password = pwd
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)
        
    def login(self):
        postdata = {'email':self.email, 'password':self.password, 'done':'http://www.xiami.com', 'submit':'%E7%99%BB+%E5%BD%95'}
        postdata = urllib.urlencode(postdata)
        print 'Logining...'
        req = urllib2.Request(url='http://www.xiami.com/member/login', data=postdata, headers=self.login_header)
        result = urllib2.urlopen(req).read()
        self.cookie.save(self.cookieFile)
        result = str(result).decode('utf-8').encode('gbk')
        if 'Email 或者密码错误' in result:
            print 'Login failed due to Email or Password error...'
            sys.exit()
        else :
            print 'Login successfully!'
      
    def signIn(self):
        postdata = {}
        postdata = urllib.urlencode(postdata)
        print 'signing...'
        req = urllib2.Request(url='http://www.xiami.com/task/signin', data=postdata, headers=self.signin_header)
        result = urllib2.urlopen(req).read()
        result = str(result).decode('utf-8').encode('gbk')
        self.cookie.save(self.cookieFile)
        try:
            result = int(result)
        except ValueError:
            print 'signing failed...'
            sys.exit()
        except:
            print 'signing failed due to unknown reasons ...'
            sys.exit()
        print 'signing successfully!'
        print self.email,'have signed', result, 'days continuously...'
            

if __name__ == '__main__':
    user = LoginXiami('你的登录邮箱', '你的密码')
    user.login()
    user.signIn()