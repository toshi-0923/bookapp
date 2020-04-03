from django.db import models
from stdimage.models import StdImageField

#class Index(models.Model):
#    date = models.CharField("年月一覧",max_length=100)
#    def __str__(self):
#        return self.date
    
class Actress(models.Model):
    image = StdImageField(upload_to="media", blank=True, variations={
            "large": (600, 400),
            "thumbnail":(100,100,True),
            "medium":(300,200),
            })
#    image = models.ImageField(upload_to='images/', blank=True,null=True)
    no = models.IntegerField("ID",blank=True,null=True)
    name = models.CharField("名前",max_length=100,blank=True)#
    age = models.CharField("年齢",max_length=100,blank=True)#
    visit = models.CharField("住み",max_length=100,blank=True)#
    work = models.CharField("仕事",max_length=100,blank=True)#
    judgment = models.CharField("性格判定", max_length=100, null=True,blank=True )#
    hobby = models.CharField("趣味",max_length=100,blank=True)#
    birth = models.DateField("誕生日",null=True,blank=True)#
    co_date = models.DateField("記念日",null=True,blank=True)#
    my_date = models.CharField("伝えた誕生日", max_length=100, null=True, blank=True)
    career = models.TextField("経歴", null=True, blank=True)
    family = models.TextField("家族メモ", null=True, blank=True)
    date = models.DateField("LINE開始日",null=True,blank=True)#
    memo = models.TextField("メモ",blank=True)
    scenario = models.CharField("シナリオ",max_length=100,blank=True)
    car = models.BooleanField("車", null=True,blank=True)

    def __str__(self):
        return "{}".format(self.no)
    
    