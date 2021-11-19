# Generated by Django 2.2.24 on 2021-11-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=256)),
                ('model', models.CharField(blank=True, max_length=256, null=True)),
                ('count_tires', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]