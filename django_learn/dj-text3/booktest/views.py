from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    '''首页'''
    return render(request, 'booktest/index.html')


def login(request):
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    '''登陆校验'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    if username == 'black' and password == '1358244533':
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7 * 24 * 3600)

        request.session['islogin'] = True

        return response
    else:
        return redirect('/login')


def ajax_test(request):
    '''ajax'''
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    return JsonResponse({'res': 1})


def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'black' and password == '1358244533':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')


# /set_cookie
def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息,名字为num, 值为1
    response.set_cookie('num', 1, max_age=14 * 24 * 3600)
    # response.set_cookie('num2', 2)
    # response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=14))
    # 返回response
    return response


# /get_cookie
def get_cookie(request):
    '''获取cookie的信息'''
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)


# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'smart'
    request.session['age'] = 18
    # request.session.set_expiry(5)
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + str(age))


# 　/clear_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()
    request.session.flush()
    return HttpResponse('清除成功')
