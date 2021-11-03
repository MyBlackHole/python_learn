from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    '''图书模型管理器类'''

    # 1.改变原有查询的结果集
    def all(self):
        # 1.调用父类的all方法，获取所有数据
        books = super().all()  # QuerySet
        # 2.对books中的数据进行过滤
        books = books.filter(isDelete=False)
        # 返回books
        return books

    # 2.封装方法，操作模型类对应的数据表（增删改查)
    def create_book(self, btitle, bpub_date):
        '''添加一本图书'''
        # 1.创建一个图书对象
        # 获取self所在的模型类
        model_class = self.model
        book = model_class()
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.添加进数据库
        book.save()
        # 3.返回book
        return book


# 一类
# booktest2_bookinfo
class BookInfo(models.Model):
    '''图书模型类'''
    # 图书名称
    btitle = models.CharField(max_length=20, db_column='title')
    # 图书名字唯一
    # btitle = models.CharField(max_length=20, unique=True, db_index=True)
    # 价格,最大位数为10,小数为2
    # bprice = models.DecimalField(max_digits=10, decimal_places=2)
    # 出版日期
    bpub_date = models.DateField()
    # bpub_date = models.DateField(auto_now_add=True) # 创建时间
    # bpub_date = models.DateField(auto_now=True) # 更新时间
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    # book = models.Manager() # 自定一个Manager类对象，管理器对象
    objects = BookInfoManager()  # 自定义一个BookInfoManager类的对象

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     '''添加一本图书'''
    #     # 创建一个cls类的对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 添加进数据库
    #     obj.save()
    #     # 返回obj
    #     return obj

    class Meta:
        db_table = 'bookinfo'  # 指定模型类对应表名


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200, null=True, blank=False)
    # 　关系属性
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # 删除标记
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    '''地区模型类'''
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'areas'
