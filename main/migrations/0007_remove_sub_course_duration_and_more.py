# Generated by Django 4.2 on 2023-10-04 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_sub_course_extra_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_course',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='sub_course',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='sub_course',
            name='tutorial_Video',
        ),
        migrations.AlterField(
            model_name='sub_course',
            name='extra_details',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='UserSelected_Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sub_course')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('extra_details', models.CharField(default='', max_length=30)),
                ('tutorial_Video', embed_video.fields.EmbedVideoField()),
                ('duration', models.DurationField(null=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sub_course')),
            ],
        ),
        migrations.CreateModel(
            name='DefaultTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_details', models.CharField(default='', max_length=100)),
                ('topic_name', models.CharField(max_length=100)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Default_Subtopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('extra_details', models.CharField(default='', max_length=30)),
                ('tutorial_Video', embed_video.fields.EmbedVideoField()),
                ('duration', models.DurationField(null=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sub_course')),
            ],
        ),
    ]