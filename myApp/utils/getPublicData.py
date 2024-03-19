from myApp.models import *

def getAllCars():
    return carinformation.objects.all()
