# 模拟一个RequestContext类，其中包含用户请求和session
class RequestContext(object):
    def __init__(self):
        self.request = "my request"
        self.session = "my session"


if __name__ == "__main__":
    # 创建保存上下文实例的栈（支持数据隔离）
    _request_ctx_stack = LocalStack()
    # 当用户请求到达时，request和session被封装到RequestContext中
    # 将封装好的RequestContext对象保存到栈中
    _request_ctx_stack.push(RequestContext())

    # 根据参数，取栈中上下文里的request或session
    def _lookup_req_object(arg):
        ctx = _request_ctx_stack.top
        return getattr(ctx, arg)

    import functools

    # 通过functools.partial将其封装成两个偏函数，方便使用（源码中的request和session还包了一层LocalProxy类，可以看后面LocalProxy的章节）
    request = functools.partial(_lookup_req_object, "request")
    session = functools.partial(_lookup_req_object, "session")

    # 通过request和sesison获取上下文中的数据
    print(request())
    print(session())
