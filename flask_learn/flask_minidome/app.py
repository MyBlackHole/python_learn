import hashlib
import os
import random
import string

from __init__ import app, db
from captcha.image import ImageCaptcha
from flask import (Response, jsonify, make_response, redirect, render_template,
                   request, session, url_for)
from flask.views import MethodView
from mixin import LoginRequiredMixin
from models import EmpInfo, User


class Query(MethodView):
    def get(self):
        text = request.args.get("text")
        text = "%" + text + "%"
        # emplist = EmpInfo.query.filter(User.name.like(text)).paginate(page=2, per_page=4)
        emplist = EmpInfo.query.filter(EmpInfo.name.like(text))

        user_dict = {}
        id = 0
        for i in emplist:
            user_dict[id] = {
                "id": i.id,
                "name": i.name,
                "age": i.age,
                "salary": i.salary,
                "image": i.operation,
            }
            id = id + 1

        # return user_dict
        # def fu(users):
        #     user_dict = {
        #         'has_next': users.has_next,
        #         'has_prev': users.has_prev,
        #         'next_num': users.next_num,
        #         'prev_num': users.prev_num,
        #     }
        #     id = 0
        #     for i in users.items:
        #         items = {
        #             'id': i.id,
        #             'name': i.name,
        #             'age': i.age,
        #             'salary': i.salary,
        #             'image': i.operation
        #         }
        #         id = id + 1
        #     user_dict['items'] = items
        #     print(user_dict)
        #     return 1

        # return json.dumps([emplist], default=fu)
        return make_response(jsonify(user_dict))


class Pwd(MethodView):
    def get(self):
        pwd = request.args.get("pwd")
        pwds = request.args.get("pwds")
        print(pwd, pwds)
        if pwd == pwds:
            return Response({"1"})
        return Response({"2"})


class Name(MethodView):
    def get(self):
        name = request.args.get("name")
        print(name)
        users = User.query.filter(User.username == name)
        print(users)
        for i in users:
            if i.username:
                return Response({"1"})
        return Response({"2"})


class Emplist(LoginRequiredMixin, MethodView):
    def get(self, page):
        # print(request)
        # print(page)
        pag = db.session.query(EmpInfo).paginate(page=page, per_page=4)
        # print(pag)
        return render_template("emplist.html", pag=pag, page=page)


class Login(MethodView):
    def get(self):
        return render_template("login.html")

    def post(self):
        username = request.form["username"]
        password = request.form["password"]
        users = User.query.filter(User.username == username, User.pwd == password).all()
        for i in users:
            if i.username:
                session["username"] = request.form["username"]
                session.permanent = True
                print(session["username"])
                return redirect(url_for("emplist", page=1))
        return self.get()


class Regist(MethodView):
    def get(self):
        return render_template("regist.html")

    def post(self):
        username = request.form["username"]
        name = request.form["name"]
        pwd = request.form["pwd"]
        result = request.form["code"]
        code = session["code"]
        sex = request.form["sex"]
        if sex == "m":
            sex = True
        else:
            sex = False
        empinfo = User(name=name, username=username, pwd=pwd)
        db.session.add(empinfo)
        db.session.commit()
        return Response({"1"})


class UpdateEmp(LoginRequiredMixin, MethodView):
    def get(self, id, page):
        emp = EmpInfo.query.get(id)
        return render_template("updateEmp.html", emp=emp, page=page)


class AddEmp(LoginRequiredMixin, MethodView):
    def get(self, page):
        return render_template("addEmp.html")

    def post(self, page):
        name = request.form["name"]
        salsry = request.form["salary"]
        age = request.form["age"]
        filename = hashlib.md5()
        image = request.files["image"]
        filename.update(image.filename.encode("utf-8"))
        empinfo = EmpInfo(
            name=name, salary=salsry, age=age, operation=filename.hexdigest()
        )
        db.session.add(empinfo)
        db.session.commit()
        pag = db.session.query(EmpInfo).paginate(page=page, per_page=4)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename.hexdigest()))
        return redirect(url_for("emplist", id=1, page=pag.pages))


class Create(MethodView):
    def get(self):
        # 创建 验证码图片对象
        image = ImageCaptcha()
        print(image)
        # 验证码 随机 验证码库？大小写英文字符 数字
        code_list = random.sample(string.ascii_letters + string.digits, 5)
        print(code_list)
        # 把列表转成 str_learn
        random_str = "".join(code_list)
        # 保存在session中 以为之后 验证使用
        session["code"] = random_str
        print(random_str)
        # 生成验证码图片
        data = image.generate(random_str)
        return Response(data)


class Delect(LoginRequiredMixin, MethodView):
    def get(self, id, page):
        emp = EmpInfo.query.get(id)
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for("emplist", id=1, page=page))


if __name__ == "__main__":
    app.run()
