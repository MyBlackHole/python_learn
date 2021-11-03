import re

import requests
from m3u8.Video_AES import prpcrypt


# url检测
def url_checking(url):
    if 'http' not in url:
        return True


# url拼接
def url_intercept(url, position):
    url_part = url.split('/')
    assert len(url_part) > 0
    assert len(url_part) > position
    url_head = ""
    for i, part in enumerate(url_part):
        url_head += part + "/"
        if position - 1 == i:
            break
    return url_head


def test_url_intercept():
    print(url_intercept('https://www.duboku.tv/vodplay/1207-2-1.html', 4))


# 链接提取
def draw_url_urls(url, rule, position=3):
    rp = requests.get(url=url)
    text = rp.text
    urls = re.findall(rule, text)
    if len(urls):
        if url_checking(urls[0]):
            url_head = url_intercept(url, position)[:-1]
            for i, url in enumerate(urls):
                urls[i] = url_head + url
    return urls, text


# 链接提取
def draw_text_urls(text, rule, position=3):
    urls = re.findall(rule, text)
    return urls


# 视频链接提取
def test_video_urls():
    urls, text = draw_url_urls('https://www.duboku.tv/voddetail-1207.html', r"/vodplay/1207-2-\d+\.html", 3)
    print("text", text)
    print("urls", urls)


# 解析提取m3u8链接
def test_m3u8_urls():
    urls, text = draw_url_urls('https://www.duboku.tv/vodplay/1207-2-2.html', r'https[:\\/.\w]*\.m3u8')
    url = re.sub(r'\\|"', "", urls[0])
    print("text", text)
    print("url", url)


def test_key_ts_url():
    urls, text = draw_url_urls("https://tv2.xboku.com/20200221/pFLAeKvX/index.m3u8", r"https[:/.\w]*\.key")
    if not len(urls):
        url = draw_text_urls(text, r'[/.\w]*\.m3u8')
        url_head = url_intercept("https://tv2.xboku.com/20200221/pFLAeKvX/index.m3u8", 3)[:-1]
        url = url_head + url[0]
        url_key, text = draw_url_urls(url, r"https[:/.\w]*\.key")
        urls_ts = draw_text_urls(text, r"https://.*\.ts")
    print("text", text)
    print("url_m3u8", url_key)
    print("url_ts", urls_ts)


# 视频解密
def aes_decrype(key_urls, urls_video, path='./', name='1.mp4'):
    rp = requests.get(url=key_urls)
    key = rp.text
    print("key", key)
    for url in urls_video:
        with open(path + name, 'wb') as f:
            ts = requests.get(url=url)
            pc = prpcrypt(key)  # 初始化密钥
            d = pc.decrypt(ts.content)
            print(url + '下载成功')
            f.write(d)
    return key


def test_video_aes():
    print(aes_decrype('https://v.duboku.tv/20200221/pFLAeKvX/hls/key.key',
                      ['https://v.fanstui.com/20200221/pFLAeKvX/hls/Dat4ghgO.ts']))


def dow_load():
    urls, text = draw_url_urls('https://www.duboku.tv/voddetail-1207.html', r"/vodplay/1207-2-\d+\.html", 3)


if __name__ == "__main__":
    test_video_aes()
    # test_key_ts_url()
    # test_video_urls()
    # test_url_intercept()
