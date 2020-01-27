from django.shortcuts import render, redirect
from .models import Day_sum
from .forms import CreateForm
from django.db.models import QuerySet
import re

def main(request):
    #金額部分を合計値に変換する関数→main.htmlに渡して表示
    def sums(sums_value):
        values = []
        for i in sums_value:
            ss = i.get("value")
            ss = re.split("[+*]", ss)
            values.append(sum([int(item) for item in ss]))
        return values

    #データのクリエイト部分
    if (request.method == "POST"):
        obj = Day_sum()
        form = CreateForm(request.POST, instance=obj)
        form.save()
        return redirect(to="/day_sum")
    #全てのデータ
    all_data = Day_sum.objects.all()
    #クエリデータの中の金額部分だけのデータ
    sums_value = all_data.values("value")
    #目標金額
    GOAL = 25000
    #期間
    DAYS = 30
    #一日あたり参考
    TODAY_GOAL = int(GOAL / DAYS)
    #データ個数
    COUNT = all_data.count()
    #合計
    sum_value = sum(sums(sums_value))
    #平均
    ave_value = int(sum_value / COUNT)
    #推移だよ
    tra_value = int(sum_value * DAYS)
    #一日あたりに使ってもいい金額
#    goal_value = int(TODAY_GOAL + ((TODAY_GOAL - ave_value) * COUNT))
    goal_value = int((GOAL - sum_value) / (DAYS - COUNT))
    #最新入力データ
    last_value = sums(sums_value)[-1]
    #残金
    bal_value = GOAL - sum_value
    
    
    
    
    #変数リスト
    result_list = {"sum_value":sum_value, "ave_value":ave_value, "tra_value":tra_value, \
                   "GOAL":GOAL, "TODAY_GOAL":TODAY_GOAL, "COUNT":COUNT, \
                   "last_value":last_value, "goal_value":goal_value, "bal_value":bal_value}


    
    params = {
            "title":"Todayマネー(ﾟ∀ﾟ　)",
            "data":all_data,
            "sums":sums(sums_value),
            "form":CreateForm(),
            "result_list":result_list,
            }
    return render(request, "day_sum/main.html", params)

def day_edit(request, num):
    obj = Day_sum.objects.get(id=num)
    if (request.method=="POST"):
        form = CreateForm(request.POST,instance=obj)
        form.save()
        return redirect(to="/day_sum")
    params = {
            "title":"Edit",
            "id":num,
            "form":CreateForm(instance=obj),
            }
    
    return render(request, "day_sum/day_edit.html", params)
