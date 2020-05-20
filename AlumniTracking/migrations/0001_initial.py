# Generated by Django 2.2.4 on 2020-02-21 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnumber', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=50)),
                ('passoutyear', models.IntegerField()),
                ('authorized', models.IntegerField(default=0)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumni',
            },
        ),
    ]
