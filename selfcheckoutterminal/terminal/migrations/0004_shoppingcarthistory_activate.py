# Generated by Django 3.2 on 2021-04-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0003_auto_20210419_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcarthistory',
            name='activate',
            field=models.BooleanField(default=True, verbose_name='Activating'),
            preserve_default=False,
        ),
    ]
