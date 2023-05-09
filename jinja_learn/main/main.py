# pip install Jinja2

# 导入相关模块
from jinja2 import Environment, FileSystemLoader, Template

# 首先告诉Jinja2模块，jinja模板文件路径在哪？(如当前目录)
j2_loader = FileSystemLoader("./")

# 然后定义一个环境，告诉jinja2，从哪里调用模板
env = Environment(loader=j2_loader)

# 之后通过 get_template 获取并载入模板
j2_tmpl = env.get_template("./jinja2.j2")

# 最后传入参数，渲染模板
result = j2_tmpl.render(name="xdai")

print(result)
