# Generated by Django 4.2 on 2023-10-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_userselected_sub_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_course',
            name='extra_details',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
