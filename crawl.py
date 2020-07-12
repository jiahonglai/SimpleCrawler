#encoding='gbk'
import requests
import bs4
import re
import json
def judge_chinese(ch):
    if ('\u4e00' <= ch <= '\u9fff'):
        return True
    return False
def crawl(url):
    url="https://xueqiu.com/1689987310/"+url
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    r.encoding='utf-8'
    b=bs4.BeautifulSoup(r.text,'html.parser')
    k=0
    s=x=''
    for i in b.find_all('p'):
        m=str(i)
        if (re.search(r'正面新闻',m)!=None):
            k=1
            continue
        if (re.search(r'负面新闻',m)!=None):
            k=2
            continue
        for j in m:
            if (judge_chinese(j)):
                if (k==1):s+=j
                if (k==2):x+=j
        if (k==1):s+='\n'
        if (k==2):x+='\n'
    zm.write(s)
    fm.write(x)
def geturl(page):
    session=requests.Session()
    cookie=''
    session.headers = {'User-Agent':'Mozilla/5.0',
                        'Cookie':cookie}
    session.get('https://xueqiu.com/')
    url='https://xueqiu.com/v4/statuses/user_timeline.json?page='+page+'&user_id=1689987310'
    t=session.get(url)
    t=json.loads(t.text)
    t=t['statuses']
    for i in t:
        s=re.search('正负面新闻',i['title'])
        if (s!=None):crawl(str(i['id']))
def main():
    global zm,fm
    zm=open('zmxw.txt','w')
    fm=open('fmxw.txt','w')
    for page in range(1,100):
        geturl(str(page))
    zm.close()
    fm.close()
main()