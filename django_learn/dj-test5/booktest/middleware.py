from django.http import HttpResponse


class BlockedIPSMiddleware(object):
    '''中间件类'''

    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        print('----init1----')
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    EXCLUDE_IPS = ['172.16.179.152']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


class TestMiddleware(object):
    '''中间件类'''

    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        print('----init1----')
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        '''产生request对象之后，url匹配之前调用'''
        print('----process_request----')
        # return HttpResponse('process_request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''url匹配之后，视图函数调用之前调用'''
        print('----process_view----')
        return HttpResponse('process_view')

    def process_response(self, request, response):
        '''视图函数调用之后，内容返回浏览器之前'''
        print('----process_response----')
        return response


class ExceptionTest1Middleware(object):

    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        print('----init1----')
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        print('----process_exception1----')
        print(exception)


class ExceptionTest2Middleware(object):

    def __init__(self, get_response):
        '''服务器重启之后，接收第一个请求时调用'''
        print('----init2----')
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        print('----process_exception2----')
