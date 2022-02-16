import time
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response, Request
from werkzeug.routing import Map, Rule
from werkzeug import run_simple
 
class MyMiddleWare(object):
    """
    wsgi中间件
    """
    def __init__(self, application):
        self.application = application
        print("创建middleware")

    def __call__(self, environ, start_response):
        b = time.time()
        result = self.application(environ, start_response)
        duration = (time.time() - b)/1000
        print("duration: %f" % duration)
        return result

class MyApp(object):
    def __init__(self):
        self.url_map = None
        print("创建app")
    def url_adapter(self):
        pass

    # handler方法需要返回Response对象（werkzeug封装的实现wsgi application）
    def new_url_handler(self, request):
        return Response('{"code": 0}', status=404)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        print(adapter, request.environ, "ok")
        try:
            # 根据请求路由找出匹配的endpoint,value是一个字典，代表的是路由的位置参数
            endpoint, values = adapter.match()
            print(endpoint, values, "oo")
            # 通过 endpoint + _handler 找到对应的函数
            return getattr(self, endpoint + '_handler')(request, **values)
        except HTTPException as e:
            print(repr(e))
            return Response("hello world")

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app():
    app = MyApp()
    # 加入中间件
    app.wsgi_app = MyMiddleWare(app.wsgi_app)
    # 添加路由,endpoint指向的是一个函数，通过路由地址绑定到该endpoint上
    app.url_map = Map(
        [Rule('/', endpoint="new_url")]
    )
    return app
    
if __name__ == '__main__':
    app = create_app()
    run_simple('127.0.0.1', 5000, app)
