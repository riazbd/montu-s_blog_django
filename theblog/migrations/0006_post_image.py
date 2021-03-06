# Generated by Django 4.0.2 on 2022-02-07 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
