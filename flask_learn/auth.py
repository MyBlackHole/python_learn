from flask import Flask, request
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app,
    version="1.0",
    title="TodoMVC API",
    description="A simple TodoMVC API",
)

ns = api.namespace("todos", description="TODO operations")

todo = api.model(
    "Todo",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "task": fields.String(required=True, description="The task details"),
    },
)


class TodoDAO(object):
    """
    实体
    """

    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo["id"] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo["id"] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


# 创建填充对象
DAO = TodoDAO()
DAO.create({"task": "Build an API"})
DAO.create({"task": "?????"})
DAO.create({"task": "profit!"})

save_task_args = reqparse.RequestParser()
save_task_args.add_argument(
    "a", type=str, required=True, default="", help="只支持+号，空格默认为+号"
)

parser = reqparse.RequestParser()
parser.add_argument("file", type=FileStorage, location="files")


@ns.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @ns.doc("list_todos")
    @ns.expect(save_task_args)
    def get(self):
        """list get 方法"""
        args = save_task_args.parse_args(request)
        print(type(args))
        args["ok"] = 1
        print(args["ok"])
        return "ok"

    @ns.doc("create_todo")
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        """创建task方法"""
        return DAO.create(api.payload), 201


@ns.route("/Upload")
class Todo(Resource):
    @ns.expect(parser)
    def post(self):
        args = parser.parse_args()
        file = args["file"]
        file.save("1.png")
        return file.name, 201


@ns.route("/<int:id>/<string:str>")
@ns.response(404, "Todo not found")
@ns.param("id", "The task identifier")
@ns.param("str", "string")
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @ns.doc("get_todo")
    @ns.marshal_with(todo)
    def get(self, _id):
        """get id 返回"""
        return DAO.get(_id)

    @ns.doc("delete_todo")
    @ns.response(204, "Todo deleted")
    def delete(self, _id):
        """delete id null"""
        DAO.delete(_id)
        return "", 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, _id):
        """put id 返回"""
        return DAO.update(_id, api.payload)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000,
        ssl_context=(
            r"./secret.pem",
            r"./secret.key",
        ),
    )
