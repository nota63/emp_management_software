# Generated by Django 5.0.6 on 2024-07-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('joined', models.CharField(max_length=300)),
            ],
        ),
    ]
