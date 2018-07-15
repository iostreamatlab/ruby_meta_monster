import urllib2

from bs4 import BeautifulSoup
 
page=2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #pattern = re.compile(r'<div class="content">(.*?)</div>')
    #print re.findall(pattern,content)
    try:
        soup = BeautifulSoup(content)
        found = soup.findAll("div",attrs={"class":"content"})
        
        for items in found:
            print items.text
        

    except UnicodeEncodeError:
        pass
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason