# Generated by Django 2.1.4 on 2018-12-15 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0003_shop_status'),
        ('count', '0002_auto_20181212_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Shop',
                                    verbose_name='所属店铺'),
        ),
    ]