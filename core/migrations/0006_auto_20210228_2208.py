# Generated by Django 3.1.7 on 2021-02-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('message', models.TextField(blank=True, max_length=250)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='service_type',
            field=models.CharField(choices=[('private', 'الفيلات الخاصة '), ('educational', 'الجامعات والمدارس'), ('companies', 'الشركات'), ('malls', 'المولات و المحلات')], max_length=50),
        ),
    ]