# Generated by Django 4.1.4 on 2022-12-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='sa', upload_to='Gallery'),
            preserve_default=False,
        ),
    ]
