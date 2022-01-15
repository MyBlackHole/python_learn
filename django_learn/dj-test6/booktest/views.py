import time

from booktest import tasks
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')


def editor(request):
    return render(request, 'booktest/editor.html')


from booktest.models import GoodsInfo


def show(request):
    goods = GoodsInfo.objects.get(pk=2)

    context = {'g': goods}

    return render(request, 'booktest/show.html', context)


def query(request):
    return render(request, 'booktest/query.html')


def send(request):
    tasks.sendopen.delay()
    return HttpResponse('ok')


def sayhello(request):
    print('hello……')
    time.sleep(2)
    print('world……')
    tasks.sayhello.delay()
    return HttpResponse("hello world")


def set_session(request):
    ''' 设置session '''
    request.session['username'] = 'smart'
    request.session['age'] = 18

    return HttpResponse('设置session')


def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username + ':' + str(age))
