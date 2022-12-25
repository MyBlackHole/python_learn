# -*- coding: utf-8 -*-

import rsa
import json
import requests
import logging 

logger = logging.getLogger()

# 代理IP获取接口
ZDY_API_URL = 'http://122.224.105.174:38152/GetAgency'
# ZDY_API_URL = 'http://192.168.100.146:38152/GetAgency'

# 代理IP用户名/产品的API_ID
ZDY_USERNAME = '202005152050125047'

# 代理IP密码
ZDY_PASSWORD = '43014570'

# 代理接口解密私钥
KEY = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqgIBAAKCAQEAjP5CE2jeoCRLgBn8Ju/nm5RVtuk6Vw+Ynr4GOfzE00pwHcJ7\n+3TywFtlofeP7Yw8UGN8O7ZtxeFabBx4PuexX1vfwgchF8w6iq9SBjRieFVnhYEF\n+Rm9GN6Cfp0AhUNdrAbR+g/XXKcEbAhcZBT28V5IkrRAOGDUj2Ky1c7aTGSpCyjr\n8pu8TfhFaRT+MKrO+IMBD/PAhCDYmaqelOD60llNT38u91EmfXG5h5e6sYbFjlFc\nyDQOfLiyxNNJVqKiBYrtahF1QO7sAc//q7q+3IgGtTGocSP+4pm9xQ1t1uDHQNmF\n/CUTYVO6ya9qdldcY4vCuqVH8X7lYegowEH3IwIDAQABAoIBAE2rl6znnZSsyebU\n6cJtcLKVQa7Uxq3FSrdQSU/Sfn9DR4YtaG163Gu5LcDPBzu+gE9srriaY9iZr11V\nRaypqF222AokMUfR2wIhWNdQLlrJ+ZBjJm42jqRPl6W2Sd4f4U9uJmhSJ7rDyzzU\nUklT/0GyRdqDb8lfFfzF9A1w7O8gqvHk9sF51+BjPyDLBTEk0lSxedJ46E/nIKAc\nYmUrYdfXkmVveNLTZwdJArPWhbAregK3je38d0Mr/GPOfr7wu++iQkIxy8K1ZRZb\n+qRUKUMZYhJZXIQV92iykT8u9Q49euU0ulItO3OhKZtnIhrNMhJlVrI7IGRWdVka\n69f/bzkCgYkAqK+e/gUuEat50mJfvqvAUCWOZRh0eC4NMijYV3WKMQ2DBfl9iAHY\n/H5hfo6D0CxiWQNxiMnuO2fqdaq/60ZlIp7TgO6uy471qkyDN2ALs57CukuonvGI\nBHY6/kosmMEdEB1d8nMCV57mNZMQE3zSBYuM1J+/xFZmoMStYrF45V4bxi7iuk3o\nvQJ5ANX5GDyf/BOz+PCCXPzkK+yJYXtSAixSogENzWyLHUzJrrVqnSIgSMJltqMw\nvQCvN/ieiNhPtfHO8V6NHCpC8/y19ooOI9GBnWqvY3akMFoCC5hygG0bnEiLIkQw\nEmzkwNt3ApBgNOmTSyGce8iXxzhzq60ZVJMNXwKBiQCd6rN0aRME1bwZGaE6lf1W\nyqHwwKEgdTRDVfuafN4fJ+AWMsezEM+7KPFKkk6SD0sOu+uIvEn7cUAMYgqDToaV\nj4y/cjNPO4l+oVxh9ddek20HDJdSHRlR3AFEV9pCMt9rW6K8u7BgqNApLYDqTXss\nV8VCtD7Jpn0zWoxbDXv5dk2YDgKRmSgdAnkAycdPLcyIwGPVe6jT27+oFDUxckPR\nvM5n66qCb7t4c/M1B+t0JrxfIMMeSiIp+b1CgPevgJ0arN9ECq/zQX9F6qgFyAax\njF44fmTK3RTUa+zF1osTxNBmvppGRBs5JOtLWyqNhmzTOPknvph8ups2yWt7F49t\njAbtAoGIGK0/YDxpfWhZb6sjvkKOpN93vz/stNXYRppyZoLb3zrkQiPLiD4TkgiC\n+vpnLOUY1z1I/ZvtMbVMQ82sJ6dmVoaxhhk7HnacNWxPEHKcl9YrmVMWaZA6Rhbl\n/fyUQuyiAhdRjMXobpDDauHgadFU3P4rx2EAvOGpBXLyL7NHzDAotTkptarldg==\n-----END RSA PRIVATE KEY-----\n'


# 获取站大爷代理
def get_zdy_proxy():
    proxies = {}
    try:
        headers = {
            'Connection': 'close',
        }
        resp = requests.get(url=ZDY_API_URL, headers=headers, timeout=10)
        res = resp.content
        priv = rsa.PrivateKey.load_pkcs1(KEY)
        # rsa私钥解密
        res = rsa.decrypt(res, priv).decode('utf-8')
        res = json.loads(res)
        # print(res, type(res))
        ip = res.get('IP')
        port = res.get('Port')
        if ip and port:
            proxy = 'http://{}:{}@{}:{}'.format(ZDY_USERNAME, ZDY_PASSWORD, ip, port)
            proxies = {
                "http": proxy,
                "https": proxy,
            }
            logger.error('ZDY：获取代理成功...{}'.format(proxies))
    except Exception as e:
        print('ZDY：获取代理失败...{}'.format(e))
        logger.exception('ZDY：获取代理失败...{}'.format(e))
    return proxies


if __name__ == '__main__':
    res = get_zdy_proxy()
    print(res)
