# coding: utf-8
import sys
from bs4 import BeautifulSoup
import urllib, urllib2

def translate(sl, tl, word):
    # from sl to tl
    # data = {'sl':'ko', 'tl':'en', 'text':'word'}
    data = {'text':'word'}

    languate_code = {'한':'ko', '영':'en'}

    # data['sl']=languate_code[sl]
    # data['tl']=languate_code[tl]
    data['text']=word

    querystring = urllib.urlencode(data)
    print "querystring:", querystring
    # 안녕하세요를 치면 text=%EC%95%88%EB%85%95%ED%95%AB%EC%97%90%E3%85%9B&tl=en&sl=ko

    # request = urllib2.Request('http://translate.google.com'+'?'+querystring) # 옛날 버전
    # request = urllib.Request('https://translate.google.com/#ko/en/%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94')
    # request = urllib2.Request('https://translate.google.com/#ko/en/'+querystring)
    request = urllib2.Request('https://translate.google.com/#ko/en/'+querystring)

    request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
    opener = urllib2.build_opener()
    feeddata = opener.open(request).read()
    f2 = open('test.txt','w')
    f2.write (str(feeddata))
    f2.close()
    soup = BeautifulSoup(feeddata, 'html.parser')
    f2 = open('test.txt','a')
    f2.write (str(soup))
    f2.close()
    # return soup.find('sapn', id="result_box").get_text()
    return soup.find('sapn', id="result_box").find_all()

sl_to_tl = raw_input("어떤? : ")
sl = sl_to_tl[0:3]
tl = sl_to_tl[3:6]

word = raw_input("번역할:" )

print translate(sl,tl,word)