from pathlib import Path

LOCALHOST = {
    'host': "127.0.0.1",
    'user': "BlackHole",
    'password': "1358244533",
    'database': "test",
    'port': 3306
}

# 项目根目录
ROOT_PATH = Path(__file__).parent.parent

# 文档存放路径
DOCS_PATH = ROOT_PATH / 'docs'
