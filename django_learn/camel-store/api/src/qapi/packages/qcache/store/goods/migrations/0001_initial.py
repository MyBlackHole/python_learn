# Generated by Django 2.2.7 on 2019-12-02 09:53

from django.db import migrations, models
import qcache.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('tag', models.ManyToManyField(blank=True, null=True, to='goods.Tag')),
            ],
            bases=(qcache.models.VersionedMixin, models.Model),
        ),
    ]
