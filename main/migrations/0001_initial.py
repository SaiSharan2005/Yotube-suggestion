# Generated by Django 4.2 on 2023-08-26 09:39

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('durations_days', models.IntegerField(default=0)),
                ('duration_hour', models.IntegerField(default=0)),
                ('duration_minute', models.IntegerField(default=0)),
                ('duration_seconds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('tutorial_Video', embed_video.fields.EmbedVideoField()),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
