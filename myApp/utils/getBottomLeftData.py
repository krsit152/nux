import json
import time
from .getPublicData import *
import re

def getSquareData():
    cars=getAllCars()
    carsVolume={}
    for i in cars:
        if carsVolume.get(i.carname,-1) == -1:
            carsVolume[i.carname] = int(i.saleVolume)
        else:
            carsVolume[i.carname] += int(i.saleVolume)
    carsVolume = sorted(carsVolume.items(),key=lambda x:x[1],reverse=True)[:15]
    brandlist=[]
    volumelist=[]
    pricelist=[]
    for i in carsVolume:
        brandlist.append(i[0])
        volumelist.append(i[1])
    for i in cars[:15]:
        i.price=re.findall('\d+\.\d+',i.price)
        i.price=i.price[0]
        pricelist.append(float(i.price))
    return brandlist,volumelist,pricelist