from django.shortcuts import render, redirect
from . import csv_make as CSV
from .models import Aggregate,Index
from .forms import UploadForm
from django.db.models import Q, Count, Sum, Avg
from django.core.paginator import Paginator


def index_page(request, item):
    item = Index.objects.get(date = item)
    data = Aggregate.objects.filter(category=item)
    
    #現金合計
    pay_money = data.filter(column_type="【現金】")
    pay_money = pay_money.aggregate(Sum("value"))
    print(pay_money)
    #カード合計
    pay_credit = data.filter(~Q(column_type="【現金】") & ~Q(column_type="-") & ~Q(pay_type="income"))
    pay_credit = pay_credit.aggregate(Sum("value"))
    print(pay_credit)
    #収入合計
    pay_income = data.filter(pay_type="income")
    pay_income = pay_income.aggregate(Sum("value"))
    print(pay_income)
    #食費合計
    food_value = data.filter(column="食費")
    food_value = food_value.aggregate(Sum("value"))
    print(food_value)
    #日用品合計
    goods_value = data.filter(column="日用品")
    goods_value = goods_value.aggregate(Sum("value"))
    print(goods_value)
    #交際費合計
    ent_value = data.filter(column="交際費")
    ent_value = ent_value.aggregate(Sum("value"))
    print(ent_value)
    #交通費合計
    trans_value = data.filter(column="交通費")
    trans_value = trans_value.aggregate(Sum("value"))
    print(type(trans_value))
    #固定料金
    life_value = data.filter\
    (Q(column="家賃") | Q(column="電気") | Q(column="ガス") | Q(column="水道") | Q(column="モバイル") | Q(column="税金") | Q(column="遅刻"))
    life_value = life_value.aggregate(Sum("value"))
    print(life_value)
    
    value_data = {"pay_money":pay_money,"pay_credit":pay_credit,"pay_income":pay_income,"food_value":food_value,\
                  "goods_value":goods_value,"ent_value":ent_value,"trans_value":trans_value,"life_value":life_value}
    
    
    params = {
            "title":"title",
            "data": data,
            "value_data":value_data,
            }
    
    
    return render(request, "aggregate/index.html", params)
    
def req(request, data):
#    item = Index.objects.get(date = item)
    data2 = Aggregate.objects.filter(category=data)
    
    life_value = data2.filter\
    (Q(column="家賃") | Q(column="電気") | Q(column="ガス") | Q(column="水道") | Q(column="モバイル") | \
     Q(column="税金") | Q(column="遅刻"))
    return render(request,"aggregate/req.html",{"life":life_value})


def csv_import(request):
    if (request.method=="POST"):
        form = UploadForm(request.POST, request.FILES)
        file_obj = request.FILES["file"]
        file_name = str(file_obj.name)
        print(file_obj)
        data = CSV.main("\\aggregate\\" + file_name)
        file_name = file_name.replace(".csv","")
        
        index = Index()
        index.date = file_name
        index.save()
#        
        for i in range(0,len(data)):
            value = data.loc[i]
            obj = Aggregate()
            obj.date = value[0]
            obj.pay_type = value[1]
            obj.column_type = value[2]
            obj.column = value[3]
            obj.pay_trans = value[4]
            obj.value = value[5]
            obj.category = index
            obj.save()
        return redirect(to="csv_import")
        
    else:
        form = UploadForm()
        params = {"form":form,}

        return redirect(to="/aggregate")
    return render(request, "aggregate/upload.html", params)
    
#    
def aggre_main(request, num=1):
    index_list = Index.objects.order_by("date")
    data = Aggregate.objects.all()
    page = Paginator(data, 5)

    
    params = {
            "title":"hello",
#            "data":data,
            "page":page.get_page(num),
            "index":index_list,
            #numに月の数字を入れて検索対象にできる？
            }
    return render(request, "aggregate/main.html", params)