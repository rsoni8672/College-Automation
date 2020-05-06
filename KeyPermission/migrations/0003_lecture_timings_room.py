# Generated by Django 2.2.4 on 2020-03-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KeyPermission', '0002_auto_20200321_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('room_type', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'ROOM',
            },
        ),
        migrations.CreateModel(
            name='LECTURE_TIMINGS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room_number', models.ForeignKey(on_delete='models.CASCADE', to='KeyPermission.ROOM')),
            ],
            options={
                'db_table': 'LECTURE_TIMINGS',
            },
        ),
    ]