from django.shortcuts import render, redirect

from app1.forms import todoform
from app1.models import todo


# Create your views here.
def kidkinder(request):
    return render(request,'index.html')

def add_todo(request):
    form = todoform()
    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_todo')
    return render(request,'new.html',{'form':form})

def view_todo(request):
    data=todo.objects.all()
    return render(request,'view.html',{'data':data})

def update_todo(request,id):
    data = todo.objects.get(id=id)
    form = todoform(instance=data)
    if request.method == 'POST':
        form = todoform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_todo')
    return render(request,'update.html',{'form':form})

def delete_todo(request,id):
    todo.objects.get(id=id).delete()
    return redirect('view_todo')
