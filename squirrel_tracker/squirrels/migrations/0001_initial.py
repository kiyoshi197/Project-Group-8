# Generated by Django 3.0.5 on 2020-05-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('unique_squirrel_id', models.CharField(max_length=256, unique=True, verbose_name='Unique Squirrel ID')),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=16, verbose_name='Shift')),
                ('date', models.DateField(verbose_name='Date')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('junvenile', 'Juvenile')], max_length=64, verbose_name='Age')),
            ],
        ),
    ]
