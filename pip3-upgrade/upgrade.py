from pip._internal.utils.misc import get_installed_distributions
from subprocess import call

for dist in get_installed_distributions():
    # 此处使用python3所以是pip3,如果使用python2版本,去掉3
    # Linux下如果不适用sudo会造成权限不够导致安装出错
    # Windows下去掉sudo
    call("sudo -H pip install --upgrade " + dist.project_name, shell=True)

# 终端运行
# python3 upgrade.py
