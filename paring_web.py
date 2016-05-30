#-8- coding utf-8 -*--
import requests,time,pymongo,lxml,random
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',

}
client=pymongo.MongoClient('localhost',27017)
items=client['itmes']
items_link=items['items_link']
# items_info=items['items_info']
items_info9=items['items_info9']

#proxies=[]
#proxy_ip=random.choice(proxies)

# spider1 抓取首页类目链接
# spider2 抓取类目链接下的商品链接
# spider3 抓取商品链接的商品信息


#spider1
start_url='http://bj.ganji.com/wu/'
host='http://bj.ganji.com'
def get_class_links(start_url):
    wb_data=requests.get(start_url,headers=headers)
    #if wb_data.status_code()==200:
    soup=BeautifulSoup(wb_data.text,'lxml')
    channels=soup.select('dt > a')
    channels_url=[]
    for url in channels:
        channel_url=host+url.get('href')
        channels_url.append(channel_url)
    #print(channels_url)

#get_class_links(start_url)


#spider2 抓取类目链接下的商品链接
# channels_url='http://bj.ganji.com/shouji/'
def get_items_from(channels_url):
    for page in range(1,100):
        channel_url="{}pn{}/".format(channels_url,page)
        wb_data=requests.get(channel_url,headers=headers)
        if wb_data.status_code ==200:               #判断页面是否存在者ip是否被封ip
            soup=BeautifulSoup(wb_data.text,'lxml')
            for item in soup.select(' dd.feature > div > ul > li > a'):
                item_link=item.get('href')
                item_data={
                    'item':item_link
                }
                get_items_info(item_link)
                items_link.insert_one(item_data)
                #print(item_data)

# get_items_from(channels_url)

#spider3 抓取商品链接的商品信息
#item_link='http://bj.ganji.com/shouji/2079187773x.htm'
def get_items_info(item_link):
    wb_data=requests.get(item_link,headers=headers)
    if wb_data.status_code ==200: #判断页面是否存在者ip是否被封ip
        soup=BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('.title-name')
        times = soup.select('.pr-5')
        types = soup.select('ul.det-infor > li:nth-of-type(1) > span > a')
        prices = soup.select('i.f22')
        adrs = soup.select('ul.det-infor > li:nth-of-type(3)')
        cates=soup.select('div.h-crumbs')
        qualities = soup.select(' div.leftBox > div:nth-of-type(4) > div.det-summary > div > div ')
        for title, time, type, price, adr, cate, quality in zip(titles, times, types, prices, adrs, qualities,cates):
            items_data = {
                'title': title.get_text(),
                'times': time.get_text().split(),
                'type': type.get_text(),
                'price': price.get_text(),
                'adr': list(adr.stripped_strings),
                'qualities': list(quality.stripped_strings),
                'cate':cate.get_text()
            }
            items_info9.insert_one(items_data)
            print(items_data)
