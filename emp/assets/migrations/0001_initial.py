# Generated by Django 5.0.6 on 2024-07-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_role', models.CharField(max_length=200)),
                ('asset', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
