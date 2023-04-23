# from django.contrib.auth.decorators import login_required

# 登陆验证与页面跳转
from flask import request, session, url_for
from werkzeug.utils import redirect


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, name):
        print("name", name)
        print(cls)
        view = super(LoginRequiredMixin, cls).as_view(name)

        # print(view)

        def login_required(page=None, id=None):
            try:
                name = session["username"]
            except KeyError:
                return redirect(url_for("login"))
            print(name)
            print(page, id)
            print(view)
            print(dir(view))
            print(request)
            print(session)
            print("view")
            if page is not None and id is not None:
                return view(page, id)
            elif id is not None:
                return view(id)
            elif page is not None:
                return view(page)

        return login_required
        # except KeyError:
        #     print('login')
