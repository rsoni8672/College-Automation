# Generated by Django 2.2.4 on 2020-02-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumniTracking', '0005_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='batchyear',
            field=models.CharField(default='2020', max_length=100),
        ),
    ]
