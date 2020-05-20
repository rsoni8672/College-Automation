# Generated by Django 2.2.4 on 2020-02-21 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AlumniTracking', '0002_alumni_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('joindate', models.DateField()),
                ('workingpresently', models.IntegerField()),
                ('alumniid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlumniTracking.alumni')),
            ],
            options={
                'db_table': 'experience',
            },
        ),
    ]
