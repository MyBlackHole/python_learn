# Generated by Django 2.1.7 on 2019-05-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号码')),
                ('model_code', models.CharField(max_length=20, verbose_name='模板CODE')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '短信发送记录',
                'verbose_name_plural': '短信发送记录',
                'ordering': ('-add_time',),
            },
        ),
        migrations.CreateModel(
            name='SmsSwitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='短信类型')),
                ('sms_type', models.CharField(max_length=100, verbose_name='code')),
                ('switch', models.BooleanField(default=True, verbose_name='开关')),
            ],
            options={
                'verbose_name': '短信服务开关',
                'verbose_name_plural': '短信服务开关',
            },
        ),
    ]