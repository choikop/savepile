import urllib2
from bs4 import BeautifulSoup
import json

url = ""
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }



for i in range(1,500):

	url = "http://map.naver.com/search2/local.nhn?query=%EB%84%A4%EC%9D%BC%EC%95%84%ED%8A%B8&page="
	seed = url + str(i)
	r = urllib2.Request(url, headers=headers)
	urllib2.urlopen(r,timeout = 10).read()
	htmltext = urllib2.urlopen(r,timeout=10).read()

	data = json.loads(htmltext)

	for d in data['result']['site']['list']:
		print d['name'].encode('utf-8')
