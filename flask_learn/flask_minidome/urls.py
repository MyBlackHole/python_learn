from app import (AddEmp, Create, Delect, Emplist, Login, Name, Pwd, Query,
                 Regist, UpdateEmp, app)

update_view = UpdateEmp.as_view("updateemp")
app.add_url_rule(
    "/update",
    endpoint="updateemp",
    defaults={"id": 1, "page": 1},
    view_func=update_view,
    methods=[
        "GET",
    ],
)
app.add_url_rule(
    "/update/<int:id>/<int:page>",
    endpoint="updateemp",
    view_func=update_view,
    methods=[
        "GET",
    ],
)

addemp_view = AddEmp.as_view("addemp")
app.add_url_rule(
    "/addemp",
    endpoint="addemp",
    defaults={"page": 1},
    view_func=addemp_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/addemp/<int:page>",
    endpoint="addemp",
    view_func=addemp_view,
    methods=["GET", "POST"],
)

create_view = Create.as_view("create")
app.add_url_rule(
    "/create",
    endpoint="create",
    view_func=create_view,
    methods=[
        "GET",
    ],
)

name_view = Name.as_view("name")
app.add_url_rule(
    "/name",
    endpoint="name",
    view_func=name_view,
    methods=[
        "GET",
    ],
)

pwd_view = Pwd.as_view("pwd")
app.add_url_rule(
    "/pwd",
    endpoint="pwd",
    view_func=pwd_view,
    methods=[
        "GET",
    ],
)

query_view = Query.as_view("query")
app.add_url_rule(
    "/query",
    endpoint="query",
    view_func=query_view,
    methods=[
        "GET",
    ],
)

emplist_view = Emplist.as_view("emplist")
app.add_url_rule(
    "/",
    endpoint="emplist",
    defaults={"page": 1},
    view_func=emplist_view,
    methods=[
        "GET",
    ],
)
app.add_url_rule(
    "/<int:page>",
    endpoint="emplist",
    view_func=emplist_view,
    methods=[
        "GET",
    ],
)

delect_view = Delect.as_view("delete")
app.add_url_rule(
    "/delect",
    endpoint="delete",
    defaults={"id": 1, "page": 1},
    view_func=delect_view,
    methods=[
        "GET",
    ],
)
app.add_url_rule(
    "/delect/<int:id>/<int:page>",
    endpoint="delete",
    view_func=delect_view,
    methods=[
        "GET",
    ],
)

login_view = Login.as_view("login")
app.add_url_rule(
    "/login", endpoint="login", view_func=login_view, methods=["GET", "POST"]
)

regist_view = Regist.as_view("regist")
app.add_url_rule(
    "/regist", endpoint="regist", view_func=regist_view, methods=["GET", "POST"]
)
