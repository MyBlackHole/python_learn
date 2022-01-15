#环境配置
- mysql安装
    ```bash
    sudo apt install mysql-server
    ```
- mysql配置(root用户下进行操作)
     ```sql
      # 创建用户
      create user heidong identified by '1358244533';
      # 创建数据库
      create database Dong charset=utf8;
      # 授权heidong用户对于Dong数据库所有操作权限，并且授予本地登陆的权限
      grant all privileges on Dong.* to heidong@'localhost' identified by '1358244533'
     ```
- redis安装
    ```bash
    sudo apt install redis-server
    ```
- nginx安装
    ```bash
    sudo apt install nginx
    ```
    - 配置
        - nginx conf配置
        ```
        location / {
            #将所有的参数转到uwsgi下
            include uwsgi_params;
            #uwsgi的ip与端口
            uwsgi_pass 127.0.0.1:8000;
        }

        location /static {
            alias /var/www/tt_test1/static/
        }
        ```
        ```bash
        sudo mkdir -p /var/www/tt_test1/static
        sudo chmod -R 777 /var/www/tt_test1/static
        ``` 
        - settings.py配置
        ```
        STATIC_ROOT = '/var/www/tt_test1/static'
        ```
        ```bash
        python3 manage.py collectstatic
        ```
- fdfs分布式存储系统安装
    ```bash
    unzip fastdfs-master.zip
    cd fastdfs-master
    ./make.sh
    sudo ./make install
    ```
#pip包
- pip install 
    ```bash
    # 富文本编辑器
    pip3 install django-tinymce
    # 全文搜索
    pip3 install django-haystack #（全文检索框架）
    pip3 install whoosh #（搜索引擎）
    pip3 install jieba #（结巴分词）
    # fdfs分布式储存
    pip3 install fdfs_client
    # 登陆信息加密
    pip3 install itsdangerous
    # session cache
    pip3 install django-redis
    # celery分布式任务队列
    pip3 install celery
    pip3 install django_celery_results
    # 支付宝接入
    pip3 install python-alipay-sdk
    ```
# 启动worker
- 启动
    ```bash
    celery -A test6 worker -l debug
    celery -A test6 worker -l info
    ```

# 开发阶段启动django
- 启动
    ```bash
    python3 manage.py runserver
    ```

# 本项目启动（在安装、配置完全下）
```bash
# 在项目根目录执行以下命令即可
./run
```

# 自动化测试
python3 WEB.py