# Generated by Django 3.1.2 on 2021-04-26 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userno', models.AutoField(primary_key=True, serialize=False)),
                ('uaccount', models.CharField(max_length=64)),
                ('upassword', models.CharField(max_length=64)),
            ],
        ),
    ]
