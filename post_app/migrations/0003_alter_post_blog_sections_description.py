# Generated by Django 3.2.5 on 2021-07-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_auto_20210724_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_blog_sections',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
    ]