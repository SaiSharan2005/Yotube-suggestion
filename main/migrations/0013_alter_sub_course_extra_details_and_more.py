# Generated by Django 4.2 on 2023-10-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_sub_topic_extra_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_course',
            name='extra_details',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sub_topic',
            name='extra_details',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]