# Generated by Django 2.0.5 on 2018-05-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20180506_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccontent',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='video_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]