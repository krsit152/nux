import requests
from lxml import etree
import csv
import os
import time
import json
import pandas as pd
import re
import django
qwe=[]
headers='User-Agent''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
infoHTML=requests.get('https://www.dongchedi.com/auto/params-carIds-x-6298') #访问汽车参数页面
print(infoHTML)
infoHTMLpath=etree.HTML(infoHTML.text)
carModel=infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
print(carModel)
insure=infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
print(insure)
energytype=infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
print(energytype)