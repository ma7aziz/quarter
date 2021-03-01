# Generated by Django 3.1.7 on 2021-02-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('short_description', models.TextField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='services/')),
            ],
            options={
                'verbose_name_plural': 'الخدمات',
            },
        ),
    ]