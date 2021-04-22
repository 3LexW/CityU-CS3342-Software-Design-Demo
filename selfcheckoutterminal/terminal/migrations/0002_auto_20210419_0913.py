# Generated by Django 3.2 on 2021-04-19 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='shoppingCartHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(verbose_name='Name')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.product', verbose_name='user')),
                ('shoppingCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.shoppingcart', verbose_name='user')),
            ],
        ),
    ]