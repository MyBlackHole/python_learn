# Generated by Django 2.1.7 on 2019-03-07 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('trade', '0040_auto_20190306_0942'),
        ('feedback', '0003_feedbackoperationlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='feedback', to='trade.Orders', verbose_name='订单'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='feedback', to='goods.Goods', verbose_name='商品'),
        ),
    ]