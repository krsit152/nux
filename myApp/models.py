from django.db import models

# Create your models here.
class carinformation(models.Model):
    id=models.AutoField('id',primary_key=True)
    brand=models.CharField('品牌',max_length=255,default='')
    carname = models.CharField('车名', max_length=255, default='')
    carImg = models.CharField('汽车图片', max_length=255, default='')
    saleVolume = models.CharField('销量', max_length=255, default='')
    price = models.CharField('价格', max_length=255, default='')
    manufacturer = models.CharField('厂商', max_length=255, default='')
    rank = models.CharField('销量排名', max_length=255, default='')
    carModel = models.CharField('车型', max_length=255, default='')
    energyType = models.CharField('能源类型', max_length=255, default='')
    marketTime = models.CharField('上市时间', max_length=255, default='')
    insure = models.CharField('保修期限', max_length=255, default='')
    cretetime=models.DateField('创建时间',auto_now_add=True)
    class Meta:
        db_table='carinformation'

#用户
class User(models.Model):
    id = models.AutoField('id', primary_key=True)
    username=models.CharField('用户名',max_length=255,default='')
    password = models.CharField('密码', max_length=255,default='')
    creteTime = models.DateField('创建时间', auto_now_add=True)
    class Meta:
        db_table='user'


