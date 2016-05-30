#-8- coding utf-8 -*--
import requests,time,pymongo,lxml,random
from bs4 import BeautifulSoup

start_url='http://bj.ganji.com/wu/'
host='http://bj.ganji.com'
def get_class_links(start_url):
    wb_data=requests.get(start_url)
    #if wb_data.status_code()==200:
    soup=BeautifulSoup(wb_data.text,'lxml')
    channels=soup.select('dl.fenlei > dt > a')
    print(channels)
    channels_url=[]
    for url in channels:
        channel_url=host+url.get('href')
        channels_url.append(channel_url)
    print(channels_url)

get_class_links(start_url)

# channels_url=['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/', 'http://bj.ganji.com/shouji/', 'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/', 'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/', 'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/', 'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/', 'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/', 'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/', 'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/', 'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/']
