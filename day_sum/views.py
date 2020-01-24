from django.shortcuts import render, redirect
from .models import Day_sum
from .forms import CreateForm

def main(request):
    #全てのデータ
    all_data = Day_sum.objects.all()
    #最後に追加したデータ
    data = all_data.filter().order_by("pk").last().value
    
    
    params = {
            "title":"hello",
            "goal": 25000,
            "count":2,
            "data":all_data,
            "value":data,
            }
    return render(request, "day_sum/main.html", params)



#データ登録
def create(request):
    if (request.method == "POST"):
        obj = Day_sum()
        form = CreateForm(request.POST, instance=obj)
        form.save()
        return redirect(to="/day_sum")
    params = {
            "title":"create",
            "form": CreateForm(),
            }
    return render(request, "day_sum/create.html", params)