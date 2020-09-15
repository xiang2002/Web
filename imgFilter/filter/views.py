import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
import os
# from django.contrib.auth.decorators import login_required
# from filter.util import init_queue
from django.contrib.auth.models import User
from filter.models import Queue
from filter.util import delete_img, move_img


def logout(request):
    if request.session is not None:
        request.session.flush()
        return redirect(reverse('filter:index'))


def index(request):
    if request.method == "POST":
        usernmae = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=usernmae, password=password)
        if user is not None:
            login(request, user)
            # print(request.session.get('_auth_user_id'))
            return redirect(reverse('filter:index'))
        else:
            pass
    if request.user.is_authenticated:
        user_id = request.session.get('_auth_user_id')
        name = ""
        if Queue.objects.filter(state=user_id):
            img = Queue.objects.filter(state=user_id).first()
            name = img.name
        elif Queue.objects.filter(state=0):
            img = Queue.objects.filter(state=0).first()
            img.state = user_id
            name = img.name
            img.save()
        else:
            return HttpResponse("任务完成!")
        h, w, c = plt.imread("filter/static/data/"+name).shape
    return render(request, 'index.html', locals())


def delete(request):
    if request.method == "GET":
        img = request.GET.get("img")
        print(img)
        qs = Queue.objects.get(name=img)
        qs.state = 'ok'
        qs.save()
        delete_img(img)
        return redirect(reverse('filter:index'))


def move(request):
    if request.method == "GET":
        print(os.getcwd())
        img = request.GET.get("img")
        qs = Queue.objects.get(name=img)
        qs.state = 'ok'
        qs.save()
        move_img(img)
        return redirect(reverse('filter:index'))


def save(request):
    print(os.getcwd())
    user_id = request.session.get('_auth_user_id')
    img = Queue.objects.filter(state=user_id).first()
    img.state = 'ok'
    img.save()
    return redirect(reverse('filter:index'))


