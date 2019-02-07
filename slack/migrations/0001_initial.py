# Generated by Django 2.1.5 on 2019-02-06 13:12

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackChannel',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('watching', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlackMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ts', models.CharField(max_length=20)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slack.SlackChannel')),
            ],
        ),
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='slackmessage',
            name='slackuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slack.SlackUser'),
        ),
    ]
