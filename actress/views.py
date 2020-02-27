from django.shortcuts import render, redirect
from .models import Actress
from .forms import CreateForm

def index(request):
    createform = CreateForm()
    data = Actress.objects.all()
    
    params = {
            "title":"index",
            "createform":createform,
            "data":data,
            }
    return render(request, "actress/index.html", params)

def create_actress(request):
    if(request.method == "POST"):
        createform = CreateForm(request.POST,request.FILES)
        createform.save()
        return redirect(to="/actress")
    
def cast_page(request, item):
    cast = Actress.objects.all().filter(no=item)
    params = {
            "title":"Cast",
            "data":cast,
            }
    return render(request, "actress/cast.html", params)

def cast_edit(request, item):
    cast = Actress.objects.all().filter(no=item).first()
    if (request.method=="POST"):
        form = CreateForm(request.POST, request.FILES, instance=cast)
        form.save()
        return redirect(to="/actress/cast_edit{}".format(item))
    
    params = {
            "title":"Cast",
            "data":cast,
            "form":CreateForm(instance=cast),
            }
    return render(request, "actress/edit.html", params)
