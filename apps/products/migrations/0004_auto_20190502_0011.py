# Generated by Django 2.1.5 on 2019-05-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190502_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='ativo?'),
        ),
    ]
