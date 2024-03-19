from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .utils import  getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from .utils import getCenterRightData
from .utils import getCenterRightChange
from .utils import getBottomRightData
# Create your views here.
def center(request):
    if request.method =='GET':
        sumCar,highVolume,topCar,mostmodel,mostBrand,averangePrice=getCenterData.getBaseData()
        lastSortlist = getCenterData.getRollData()
        oilRare,eleRare,mixRare=getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar':sumCar,
            'highVolume':highVolume,
            'topCar':topCar,
            'mostmodel':mostmodel,
            'mostBrand':mostBrand,
            'averangePrice':averangePrice,
            'lastSortlist':lastSortlist,
            'oilRare':oilRare,
            'eleRare':eleRare,
            'mixRare':mixRare,
        })

def centerLeft(request):
    if request.method == 'GET':
        getCenterLeftData.getPieBrandData()
        lastPieList=getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList':lastPieList,
        })

def bottomLeft(request):
    if request.method == 'GET':
        brandlist,volumelist,pricelist=getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandlist':brandlist,
            'volumelist':volumelist,
            'pricelist':pricelist,
        })

def centerRight(request):
    if request.method == 'GET':
        realData=getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData':realData
        })

def centerRightChange(request,energyType):
    if request.method == 'GET':
        oilData,electricData=getCenterRightChange.getCircleData()
        realData=[]
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse({
            'realData':realData,
        })

def bottomLeftRight(request):
    if request.method == 'GET':
        carData=getBottomRightData.getRankData()
        return JsonResponse({
            'carData':carData
        })