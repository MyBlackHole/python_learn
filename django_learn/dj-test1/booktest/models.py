from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=128)

    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, )

    def __str__(self):
        return self.hname

# python3 manage.py sqlmigrate booktest 0001 查看sql
# 这个migrate命令选中所以没有迁移并应用在数据库上
