# Generated by Django 4.1.7 on 2023-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=14)),
                ('content', models.TextField()),
            ],
        ),
    ]
