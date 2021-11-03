import hashlib

from requests_html import HTMLSession

name = 1
session = HTMLSession()


class DFS():
    def __init__(self):
        self.uncrawl_url = []  # 存放url
        self.crawled = []  # 存放已采集的url
        self.list_url = []  # 存放图片的标识

    def save_uncrawl(self, url):
        if url not in self.crawled:
            self.uncrawl_url.append(url)

    def get_uncrawl(self):
        return self.uncrawl_url.pop()

    def save_crawled(self, url):
        return self.crawled.append(url)

    def isempty(self):
        if not self.uncrawl_url:
            return True
        else:
            return False


flag = 0


class Crawler():

    # 调度器
    def __init__(self):
        self.dfs = DFS()

    # 爬取含有高清图片页面的url
    def crawl(self):
        global flag
        self.dfs.save_uncrawl('http://www.win4000.com/meinv131804_10.html')
        while not self.dfs.isempty():
            try:
                r = session.get(self.dfs.get_uncrawl())
                # 拿到了页面所有url
                items_img = r.html.links
                for i in items_img:
                    if flag > 5:
                        flag = 0
                        break
                    if 'win4000.com/meinv' in i:
                        print(i)
                        self.dfs.save_uncrawl(i)
                        self.get_img(i)
                        # 把访问过的页面添加已采集列表
                        self.dfs.save_crawled(i)
            except:
                pass

    # 获取图片下载路径
    def get_img(self, a):
        global flag
        r = session.get(a)
        img_url = r.html.find('img.pic-large')
        if img_url:
            for j in img_url:
                url = j.attrs['url']
                self.save_img(url)

    # 保存图片
    def save_img(self, url):
        global name
        img = session.get(url).content
        img_unqiue = self.md5_img(img)
        if img_unqiue:
            with open('img/%s.jpg' % name, 'wb') as w:
                w.write(img)
            print(str(name) + '张')
            name += 1

    # 生成图片唯一标识
    def md5_img(self, img):
        global flag
        m = hashlib.md5()
        m.update(img)
        unique = m.hexdigest()
        if unique not in self.dfs.list_url:
            print(self.dfs.list_url)
            self.dfs.list_url.append(unique)
            return True
        else:
            print('该图片已存在')
            flag += 1
            return False


if __name__ == '__main__':
    Crawler().crawl()
