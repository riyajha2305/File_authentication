# Generated by Django 3.1.6 on 2021-07-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phoneno',
            field=models.IntegerField(default=1234567890),
            preserve_default=False,
        ),
    ]