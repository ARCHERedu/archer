# Generated by Django 5.0.4 on 2024-04-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_user_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=100000)),
                ('password', models.CharField(max_length=100000)),
                ('role', models.CharField(max_length=1000)),
                ('grade', models.CharField(max_length=1000)),
                ('school', models.CharField(max_length=100000)),
                ('state', models.CharField(max_length=100000)),
                ('city', models.CharField(max_length=100000)),
                ('country', models.CharField(max_length=100000)),
            ],
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
