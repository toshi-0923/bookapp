from django.shortcuts import render, redirect
from .models import Book
from .forms import CreateForm, FindForm
from .Dokurepo import main
def index(request):
    data = Book.objects
    params = {
            "title":"まゆちんすきすきチュッチュ丸ヽ(*´∀｀)ノ",
            "data":data.all(),
            "count":data.all().count(),
            }
        
    return render(request, "book/index.html", params)

def create(request):
    if (request.method == "POST"):
        obj = Book()
        book = CreateForm(request.POST, instance=obj)
        book.save()
        return redirect(to="/book")

    params = {
            "title":"Create",
            "form":CreateForm(),
            }
    return render(request, "book/create.html", params)

def edit(request, num):
    obj = Book.objects.get(id=num)
    if (request.method == "POST"):
        book = CreateForm(request.POST, instance=obj)
        book.save()
        return redirect(to="/book")
    params = {
            "title":"edit",
            "id":num,
            "form":CreateForm(instance=obj),
            }
    return render(request, "book/edit.html", params)

def delete(request, num):
    book = Book.objects.get(id=num)
    if (request.method == "POST"):
        book.delete()
        return redirect(to="/book")
    params = {
            "title":"delete",
            "id":num,
            "data":book,
            }
    return render(request, "book/delete.html", params)


def find(request):
    if (request.method=="POST"):
        msg = "検索します"
        form = FindForm(request.POST)
        str = request.POST["find"]
        data = Book.objects.filter(writer__contains=str)
        count = data.count()
    else:
        msg = "検索待機"
        form = FindForm()
        data = Book.objects.all()
        count = data.count()
    params = {
            "title":"Find",
            "message":msg,
            "form":form,
            "data":data,
            "count":count
            }
    return render(request, "book/find.html", params)


def csv(request):
    book_data = main()
    for item in book_data:
        if item[2] == "none"or"?":
            item[2] = item[2].replace("none","2000-01-01").replace("?","2000-01-01")
            obj = Book()
            obj.writer = item[0]
            obj.title = item[1]
            obj.date = item[2]
            obj.save()
        else:
            obj = Book()
            obj.writer = item[0]
            obj.title = item[1]
            obj.date = item[2]
            obj.save()
    return redirect(to="/book")

def csv_check(request):
    params = {
            "title":"インポートします。よろしいですか？？",
            "data":main(),
            }
    return render(request, "book/csv.html", params)



