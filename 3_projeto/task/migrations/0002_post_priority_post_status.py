# Generated by Django 4.2 on 2023-05-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=25),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('concluded', 'Concluded'), ('pending', 'Pending'), ('postponed', 'Postponed')], default='pending', max_length=25),
        ),
    ]