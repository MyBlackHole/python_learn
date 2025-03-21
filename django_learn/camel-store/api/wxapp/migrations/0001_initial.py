# Generated by Django 2.0 on 2017-12-13 03:52

from django.db import migrations, models
import django.db.models.deletion
import wxapp.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unionid', models.CharField(blank=True, default='', max_length=128, verbose_name='unionID')),
                ('web_openid', models.CharField(blank=True, default='', max_length=128, verbose_name='web_openid')),
                ('app_openid', models.CharField(blank=True, default='', max_length=128, verbose_name='app_openid')),
                ('web_access_token',
                 models.CharField(blank=True, default='', max_length=256, verbose_name='web_access_token')),
                ('web_refresh_token',
                 models.CharField(blank=True, default='', max_length=256, verbose_name='web_refresh_token')),
                ('web_access_token_deadline', models.DateTimeField(default=wxapp.models.default_access_token_deadline,
                                                                   verbose_name='web access_token失效时间')),
                ('web_refresh_token_deadline', models.DateTimeField(default=wxapp.models.default_refresh_token_deadline,
                                                                    verbose_name='web refresh_token失效时间')),
                ('app_access_token',
                 models.CharField(blank=True, default='', max_length=256, verbose_name='app_access_token')),
                ('app_refresh_token',
                 models.CharField(blank=True, default='', max_length=256, verbose_name='app_refresh_token')),
                ('app_access_token_deadline', models.DateTimeField(default=wxapp.models.default_access_token_deadline,
                                                                   verbose_name='app access_token失效时间')),
                ('app_refresh_token_deadline', models.DateTimeField(default=wxapp.models.default_refresh_token_deadline,
                                                                    verbose_name='app refresh_token失效时间')),
            ],
            options={
                'db_table': 'wx_access_token',
            },
        ),
        migrations.CreateModel(
            name='WxAppCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='渠道')),
                ('scene',
                 models.CharField(default=wxapp.models.generate_scene, max_length=32, unique=True, verbose_name='场景值')),
                ('url', models.CharField(blank=True, default='', max_length=128, verbose_name='url地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '渠道',
                'verbose_name_plural': '渠道管理',
            },
        ),
        migrations.CreateModel(
            name='WxSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=128, unique=True, verbose_name='Session')),
                ('session_key', models.CharField(blank=True, default='', max_length=128, verbose_name='Session Key')),
                ('wxapp_openid', models.CharField(blank=True, default='', max_length=128, verbose_name='WxApp OpenId')),
                ('expires_in', models.IntegerField(default=7200, verbose_name='有效时间(秒)')),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Session',
            },
        ),
        migrations.CreateModel(
            name='WxUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union_id', models.CharField(blank=True, default='', max_length=128, verbose_name='unionID')),
                ('web_openid', models.CharField(blank=True, default='', max_length=128, verbose_name='Web openID')),
                ('app_openid', models.CharField(blank=True, default='', max_length=128, verbose_name='App openID')),
                (
                    'wx_app_openid',
                    models.CharField(blank=True, default='', max_length=128, verbose_name='WxApp openID')),
                ('nickname', models.CharField(blank=True, default='', max_length=128, verbose_name='用户昵称')),
                ('avatar_url', models.CharField(blank=True, default='', max_length=512, verbose_name='头像URL')),
                ('language', models.CharField(blank=True, default='', max_length=32, verbose_name='语言')),
                (
                    'gender',
                    models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='用户性别')),
                ('province', models.CharField(blank=True, default='', max_length=64, verbose_name='省份')),
                ('city', models.CharField(blank=True, default='', max_length=64, verbose_name='城市')),
                ('country', models.CharField(blank=True, default='', max_length=64, verbose_name='国家')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
            ],
            options={
                'verbose_name': '微信用户',
                'verbose_name_plural': '微信用户',
            },
        ),
        migrations.AddField(
            model_name='wxsession',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='session', to='wxapp.WxUser', verbose_name='微信用户'),
        ),
    ]
