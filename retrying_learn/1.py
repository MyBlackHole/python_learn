import requests
import time
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}


@retry(stop_max_attempt_number=3, stop_max_delay=1000)  # 表示重试以下代码三次
def _parse_url(url):
    print("-" * 30)
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except Exception as e:
        print(e)
        html_str = None
    return html_str


if __name__ == "__main__":
    url = 'www.baidu.com'
    print(parse_url(url))
