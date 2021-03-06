# Generated by Django 2.2 on 2019-05-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('category', models.CharField(db_index=True, max_length=150)),
                ('description', models.CharField(db_index=True, max_length=150)),
                ('price', models.IntegerField(db_index=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
