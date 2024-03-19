import json
import time
from .getPublicData import *

def getPriceSortData():
    cars = list(getAllCars())
    priceSortlist={'0-5w':0,'5-10w':0,'10-20w':0,'20-30w':0,'30w以上':0,}
    for i in cars:
        s=[json.loads(i.price)[0]][0]
        if s<5:
            priceSortlist['0-5w'] +=1
        elif s>=5 and s<=10:
            priceSortlist['5-10w'] += 1
        elif s >= 10 and s <= 20:
            priceSortlist['10-20w'] += 1
        elif s >= 20 and s <= 30:
            priceSortlist['20-30w'] += 1
        else:
            priceSortlist['30w以上'] += 1
    realData=[]
    for k,v in priceSortlist.items():
        realData.append({
            'name':k,
            'value':v
        })
    return realData