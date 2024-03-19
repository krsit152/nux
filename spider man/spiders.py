import requests
from lxml import etree
import csv
import os
import time
import json
import pandas as pd
import re
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','数据可视化.settings')
django.setup()
from myApp.models import carinformation
class spider (object):
    def __init__(self):
        self.spiderUrl="https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E6%B7%B1%E5%9C%B3&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0"
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv','a',newline="",encoding='utf-8') as wf:      #创建csv文件
                write=csv.writer(wf)        #读取文件并赋值给write
                write.writerow(['brand_name','carname','carImg','saleVolume',' price','manufacturer',
                                'rank','carModel',' energyType','marketTime','insure'])         #写入关键字
    def get_page(self):     #获取值
        with open('./spiderPage.txt','r') as r_f:
            return ( r_f.readlines()[-1].strip())       #读取文件的最后一行并去除空格

    def set_page(self,newpage):     #改变值
        with open('./spiderPage.txt','a') as a_f:
            a_f.write('\n'+str(newpage))


    def main(self):
        count =self.get_page()
        print(count)
        params={
            'offset':int(count)
        }
        print('数据从{}开始爬取'.format(int(count)+1))
        pageJson=requests.get(self.spiderUrl,headers=self.headers,params=params).json()  #获取数据并转为python可读取的
        pageJson=pageJson['data']['list']                                                #获取data下的list数据
        time.sleep(1)
        print(pageJson)
        print("####")
        for index,car in enumerate(pageJson):                           #将列表中的字典赋值给car，索引赋值给index
            carData=[]                                                  #创建一个空列表
            print('正在爬取第%d'%(index+1)+'数据')
            carData.append(car['brand_name'])                           #将品牌名存入列表中
            carData.append(car['series_name'])                          #将车名存入列表中
            carData.append(car['image'])                                #图片地址
            carData.append(car['count'])                                #销量
            price=[]
            #爬取价格
            price.append(car['min_price'])
            price.append(car['max_price'])
            carData.append(price)
            carData.append(car['sub_brand_name'])                          #厂商
            carData.append(car['rank'])                                    #销量排名
            #爬取车型和能源类型f、上市时间、保修期限
            carnumber=car['series_id']
            infoHTML=requests.get('https://www.dongchedi.com/auto/params-carIds-x-%s'%carnumber,headers=self.headers) #访问汽车参数页面

            infoHTMLpath=etree.HTML(infoHTML.text)
            try:
                carModel=infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
            except IndexError:
                carModel='null'
            else:
                carModel = infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
            carData.append(carModel)
            try:
                energytype=infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
            except IndexError:
                energytype='null'
            else:
                energytype = infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
            carData.append((energytype))
            # print(carModel)
            # print(energytype)
            try:
                marketTime=infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
            except IndexError:
                marketTime='null'
            else:
                marketTime = infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
            carData.append(marketTime)

            try:
                insure=infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
            except IndexError:
                insure='null'
            else:
                insure = infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
            carData.append(insure)
            print(carData)
            self.save_to_csv(carData)
        print(pageJson)
        self.set_page(int(count)+10)
        self.main()

    def save_to_csv(self,Ddta):
        with open('./temp.csv','a',newline='',encoding='utf-8') as f:
            writer=csv.writer(f)
            writer.writerow(Ddta)

    def clear_csv(self):            #数据清洗
        df=pd.read_csv('temp.csv')
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        print('总数量为%d'%df.shape[0])
        return df.values

    def save_to_sql(self):
        data=self.clear_csv()
        for car in data:
            carinformation.objects.create(
                brand = car[0],
                carname = car[1],
                carImg = car[2],
                saleVolume = car[3],
                price = car[4],
                manufacturer = car[5],
                rank = car[6],
                carModel = car[7],
                energyType = car[8],
                marketTime=car[9],
                insure=car[10]



            )

if __name__=='__main__':
    spiderObj=spider()
    #spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_sql()


