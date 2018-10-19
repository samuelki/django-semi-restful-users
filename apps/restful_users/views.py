from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'restful_users/index.html', {'users': User.objects.all()})

def new(request):
    return render(request, 'restful_users/new.html')

def create(request):
    errors = User.objects.validator(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/users/new')
    else:
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/users/'+str(user.id))

def show(request, id):
    return render(request, 'restful_users/show.html', {'user': User.objects.get(id=id)})

def destroy(request, id):
    User.objects.get(id=id).delete()

    return redirect('/users')

def edit(request, id):
    return render(request, 'restful_users/edit.html', {'user': User.objects.get(id=id)})

def update(request):
    user = User.objects.get(id=request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()

    return redirect('/users/{}'.format(user.id))