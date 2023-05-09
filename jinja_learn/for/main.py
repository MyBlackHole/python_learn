from jinja2 import Environment, FileSystemLoader, Template

j2_loader = FileSystemLoader("./")
env = Environment(loader=j2_loader)
j2_tmpl = env.get_template("./jinja2_for_with_dict.j2")
# 传入一个列表，列表里面的人进行自我介绍
people = [
    {"name": "Zhang San", "age": 18},
    {"name": "Li Si", "age": 20},
    {"name": "Wang Wu", "age": 22},
]
result = j2_tmpl.render(people=people)
print(result)
