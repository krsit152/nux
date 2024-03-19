import json
import time
from .getPublicData import *
def getBaseData():
    cars=list(getAllCars())
    sumCar = len(cars)
    highVolume = cars[0].saleVolume
    topCar=cars[0].carname
    carModels = {}
    maxmodel=0
    mostmodel=''
    for i in cars:
        if carModels.get(i.carModel,-1) == -1:
            carModels[str(i.carModel)] = 1
        else:
            carModels[str(i.carModel)] += 1
    carModels=sorted(carModels.items(),key=lambda x:x[1],reverse=True)
    mostmodel=carModels[0][0]
    carBrands = {}
    maxBrand = 0
    mostBrand = 0
    for i in cars:
        if carBrands.get(i.brand,-1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    for k,v in carBrands.items():
        if v>maxBrand:
            maxBrand=v
            mostBrand=k

    averangePrice = 0
    carPrices={}
    sumPrice=0
    for i in  cars:
        x=json.loads(i.price)[0] + json.loads(i.price)[0]
        sumPrice +=x
    averangePrice=sumPrice/(sumCar*2)
    averangePrice=round(averangePrice,2)
    return sumCar,highVolume,topCar,mostmodel,mostBrand,averangePrice

def getRollData():
    cars = list(getAllCars())
    carBrands = {}
    for i in cars:
        if carBrands.get(i.brand,-1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] +=1
    brandlist=[(value,key) for key,value in carBrands.items()]
    brandlist=sorted(brandlist,reverse=True)[:10]
    sortDict={i[1]:i[0] for i in  brandlist}
    lastSortlist=[]
    for k,v in sortDict.items():
        lastSortlist.append({
            'name':k,
            'value':v
        })
    return lastSortlist
def getTypeRate():
    cars=getAllCars()
    carTypes={}
    for i  in cars:
        if carTypes.get(i.energyType,-1) == -1:
            carTypes[str(i.energyType)] = 1
        else:
            carTypes[str(i.energyType)] +=1
    oilRare =round(carTypes['汽油']/563*100,2)
    eleRare = round(carTypes['纯电动']/563*100,2)
    mixRare = round(((563-carTypes['汽油']-carTypes['纯电动'])/563*100),2)
    return oilRare,eleRare,mixRare