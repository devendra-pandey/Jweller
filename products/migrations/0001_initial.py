# Generated by Django 3.1.7 on 2021-03-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='static/Uploads/product/')),
                ('gold_weight', models.CharField(max_length=30)),
                ('diamond_carat', models.CharField(max_length=30)),
                ('design_number', models.CharField(default=0, max_length=30, unique=True)),
                ('status', models.BooleanField(default='1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'get_latest_by': 'created',
            },
        ),
    ]
