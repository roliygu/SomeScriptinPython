#! /usr/bin/python 
# -*- coding: utf-8 -*- 
# python 3.2 
import urllib.request 
import http.cookiejar 
import http.cookies 
import platform 
import datetime 
import hashlib 
import json  
import time  
import sys 
import os 
 
class kuaipan: 
    _folder = "/tmp/" 
    _logFile = 'eddie.log' 
    _cookieFile = 'cookie.dat' 
    _login_url = 'https://www.kuaipan.cn/index.php?ac=account&op=login' 
    _sign_url = 'http://www.kuaipan.cn/index.php?ac=common&op=usersign' 
    _logout_url = 'http://www.kuaipan.cn/index.php?ac=account&op=logout' 
 
    _login_data = { 
        'username':'帳號', 
        'userpwd': '密碼' 
    } 
 
    _headers = [ 
        ('host','www.kuaipan.cn'), 
        ('User-Agent','Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.8pre) Gecko/20071015 Firefox/2.0.0.7 Navigator/9.0'), 
        ('Referer','http://www.kuaipan.cn/account_login.htm') 
    ] 
 
    _data = { 
        'cookie_file_path':'', 
        'log_file_path':'' 
    } 
     
    _connect_info = {} 
 
    def __init__(self): 
        if platform.system().lower() == 'windows': 
            self._folder = 'C:/' 
 
        self._data['cookie_file_path'] = '{0}{1}'.format(self._folder,self._cookieFile) 
        self._data['log_file_path'] = '{0}{1}'.format(self._folder,self._logFile) 
         
        if not os.path.exists(self._data['log_file_path']): 
            try: 
                with open(self._data['log_file_path'], mode='a', encoding='utf-8') as a_file:                                    
                    a_file.close() 
                self.Log('{0} 檔案不存在已重建'.format(self._data['log_file_path'])) 
            except IOError as ioerr: 
                print(ioerr) 
                sys.exit(1) 
 
        if not os.path.exists(self._data['cookie_file_path']): 
            try: 
                with open(self._data['cookie_file_path'], mode='a', encoding='utf-8') as a_file:                                     
                    a_file.close() 
                self.Log('{0} 檔案不存在已重建'.format(self._data['cookie_file_path'])) 
            except IOError as ioerr: 
                self.Log(ioerr) 
                print(ioerr) 
                sys.exit(1) 
 
        self._connect_info['cookie'] = http.cookiejar.LWPCookieJar() 
 
        try: 
            self._connect_info['cookie'].revert(self._data['cookie_file_path']) 
        except Exception as e:              
            open(self._data['cookie_file_path'], "a") 
        self._connect_info['cookie_processor'] = urllib.request.HTTPCookieProcessor(self._connect_info['cookie']) 
        self._connect_info['post_data'] = urllib.parse.urlencode(self._login_data) 
 
 
    def makeCookie(self, name, value): 
        return http.cookiejar.Cookie( 
            version=0,  
            name = name,  
            value = value, 
            port = None,  
            port_specified=False, 
            domain = self._headers[0][1],  
            domain_specified=True,  
            domain_initial_dot=False, 
            path = "/",  
            path_specified=True, 
            secure=False, 
            expires=None, 
            discard=False, 
            comment=None, 
            comment_url=None, 
            rest={} 
        ) 
 
    def Log(self,msg): 
        try: 
            with open(self._data['log_file_path'], mode='a', encoding='utf-8') as a_file: 
                a_file.write('{0} {1}\n'.format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f') , msg))                
                a_file.close() 
        except IOError: 
            pass 
 
    def sign(self): 
        conn = urllib.request.build_opener(self._connect_info['cookie_processor']) 
        conn.addheaders = self._headers 
        urllib.request.install_opener(conn) 
        response = conn.open(urllib.request.Request(self._login_url,self._connect_info['post_data'].encode('utf-8'))) 
         
        if response.url != "http://www.kuaipan.cn/home.htm": 
            msgb = '帳號登入錯誤程式終止' 
            self.Log(msg) 
            print(msg)   
            response.close() 
            return False 
 
        response.close() 
        msg = 'kuai %s 登陸成功，準備簽到' % self._login_data['username'] 
        print(msg) 
        self.Log(msg)        
 
        response = conn.open(self._sign_url) 
        sign_js = json.loads(response.read().decode("utf-8")) 
        response.close() 
 
        if sign_js['state'] == -102: 
            msg = 'kuai %s 今天已簽到了' % self._login_data['username'] 
            print(msg) 
            self.Log(msg)  
        elif sign_js['state'] == 1: 
            msg = "簽到成功! 獲得積分：%d，總積分：%d；獲得空間：%dM\n" % (sign_js['increase'], sign_js['status']['points'], sign_js['rewardsize']) 
            print(msg) 
            self.Log(msg) 
        else: 
            msg = 'kuai %s 簽到失敗' % self._login_data['username'] 
            print(msg) 
            self.Log(msg)  
             
        conn.open(self._logout_url)  
        conn.close() 
if __name__ == '__main__': 
    kuaipan().sign() 