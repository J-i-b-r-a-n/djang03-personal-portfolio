# Generated by Django 3.2.5 on 2021-08-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
