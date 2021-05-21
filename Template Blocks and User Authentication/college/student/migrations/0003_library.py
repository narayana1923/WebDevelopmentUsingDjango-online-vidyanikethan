# Generated by Django 2.2.2 on 2021-05-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210517_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=30)),
                ('publication_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
