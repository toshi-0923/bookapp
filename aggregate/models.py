from django.db import models
import re

class Index(models.Model):
    date = models.CharField("年月一覧",max_length=100)
    def __str__(self):
        return self.date
    
class Aggregate(models.Model):
    date = models.DateField("日付")#日付
    pay_type = models.CharField("方法",max_length=100)#カード/現金/振込/引き出し/収入
    column_type = models.CharField("カテゴリ",max_length=100)#大項目
    column = models.CharField("カテゴリの内訳",max_length=100)#詳細項目
    pay_trans = models.CharField("入金先",max_length=100)#
    value = models.IntegerField("合計",)#金額
    category = models.ForeignKey(Index, on_delete=models.PROTECT,null=True)

    def __str__(self):
        return "<{}>".format(self.date)
    