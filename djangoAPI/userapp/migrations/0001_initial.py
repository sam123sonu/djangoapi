# Generated by Django 4.0.1 on 2022-01-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('zip', models.IntegerField()),
                ('email', models.CharField(max_length=500)),
                ('web', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
