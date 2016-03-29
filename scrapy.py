#coding:utf-8
import urllib
import urllib2
import re
import time
import json
import requests

email = "xxxxxxxx@xxx.com"
password = "xxxxxxx"

s = requests.session()

headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip,deflate",
"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
"Connection": "keep-alive",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
"Referer": "http://www.zhihu.com/"
}

xsrf_url = "https://www.zhihu.com/#signin"
request = urllib2.Request(xsrf_url)
handle = urllib2.urlopen(request)
content = handle.read()

#print (content)
pattern = re.compile('<input type="hidden" name="_xsrf" value=".{32}"\/>',re.I|re.S)

pattern = pattern.findall(content)
#print (pattern[1])

_xsrf = pattern[1][41:(len(pattern[1])-3)]
print (_xsrf)

postdata = urllib.urlencode({
				'_xsrf':_xsrf,
                'email':email,
                'password':password,
                'remember_me':True
            })


res = s.post("http://www.zhihu.com/login/email", headers = headers, data = postdata)
print res.status_code
#print res.headers
#print res.content
#print res.cookies
m_cookies = res.cookies

#for item in cookie:
#    print 'Name = '+item.name
#    print 'Value = '+item.value

test_url = 'http://www.zhihu.com/'
res = s.get(test_url, headers = headers, cookies = m_cookies,verify = False)

#print res.content
my_patt = re.compile('<span class="name">.*<\/span>')
result = my_patt.findall(res.content)
if result:
	my_str = result[0]+" successfully login!"
	print my_str
else:
	print "login failure!"

my_patt = re.compile('href="\/question\/\d*#answer-\d*">.*<\/a><\/h2>')
result = my_patt.findall(res.content)
#print type(result)
for i in range(len(result)):
	print (result[i])

