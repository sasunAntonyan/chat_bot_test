# Generated by Django 2.2.5 on 2019-09-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threads',
            name='thread_id',
        ),
        migrations.AlterField(
            model_name='threads',
            name='id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]