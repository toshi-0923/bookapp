from django.db import models
import re

class Day_sum(models.Model):
    date = models.DateField()
    value = models.CharField(max_length=100)

    def __str__(self):
        #掛け算に対応してない→対応させるならif分岐
        sums = re.split("[+*]",self.value)
        return "<{0}> {1}円  {2}".format(self.date, sum([int(i) for i in sums]), self.id)
