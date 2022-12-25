#!/usr/bin/env bash

# 生成app
python3 manage.py startapp name

# 生成迁移文件
python3 manage.py makemigrations

# 数据库迁移
python3 manage.py migrate