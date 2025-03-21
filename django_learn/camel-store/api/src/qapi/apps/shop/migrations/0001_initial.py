# Generated by Django 2.1.2 on 2018-12-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='店铺名')),
                ('province', models.CharField(max_length=128, verbose_name='省/直辖市')),
                ('city', models.CharField(max_length=128, verbose_name='市')),
                ('district', models.CharField(max_length=128, verbose_name='区')),
                ('detail', models.CharField(max_length=128, verbose_name='详细信息')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='纬度')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='经度')),
                ('delivery_range', models.TextField(blank=True, null=True, verbose_name='配送范围列表')),
            ],
            options={
                'verbose_name': '点铺',
                'verbose_name_plural': '点铺',
            },
        ),
    ]
