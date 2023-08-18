from django.shortcuts import render, redirect
from .models import ToDoS
import json

# Create your views here.
def redirect_view(request):
    return redirect('/home')

def home(request):
    doList = ToDoS.objects.all()
    return render(request, 'todolist.html', {'doList': doList})

def add_content(request):
    body_arg = json.loads(request.body)
    new_item = ToDoS(name = body_arg['name'])
    new_item.save()
    return redirect('/home')

def delete_content(request):
    body_arg = json.loads(request.body)
    for items in body_arg:
        delete_object = ToDoS.objects.filter(name=items).first()
        if delete_object:
            delete_object.delete()
        
    return redirect('/home')