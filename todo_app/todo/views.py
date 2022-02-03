from django.shortcuts import render,redirect
from .forms import Todoform
from .models import Todomodel
# Create your views here.

db = Todomodel.objects.all()

def home(request):

    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        new = Todomodel(todo_item=form.data['todo_field'])
        new.save()
        db = Todomodel.objects.all()
        return render(request,"todo/index.html",{
        "form":form,
        "db":db,
        })

    elif request.method == 'GET':
        db = Todomodel.objects.all()
        return render(request,"todo/index.html",{
        "form":form,
        "db":db,
        })

    return render(request,"todo/index.html")

def delete(request, pk):
    print(Todomodel.objects.filter(id=pk))
    Todomodel.objects.filter(id=pk).delete()
    return redirect('/')