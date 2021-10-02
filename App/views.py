from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo

# Create your views here.

def list_todo_items(request):
  return render(request, 'todoApp/todoList.html')

def insert_list_item(request:HttpResponse):
  # return render(request, 'todoApp/todoList.html')
  todo = ToDo(content = request.POST['content'])
  
  todo.save()
  return redirect('/App/list/')

def App_home(request):
  return HttpResponse('From App_Home')