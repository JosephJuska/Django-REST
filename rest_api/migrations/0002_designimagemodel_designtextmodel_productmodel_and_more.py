# Generated by Django 5.0.4 on 2024-04-26 16:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='design_images/', verbose_name='Design Image')),
                ('x_coor', models.FloatField(default=1.0, verbose_name='Design Image X Coordinate')),
                ('y_coor', models.FloatField(default=1.0, verbose_name='Design Image Y Coordinate')),
            ],
            options={
                'verbose_name': 'Design Image',
                'verbose_name_plural': 'Design Images',
            },
        ),
        migrations.CreateModel(
            name='DesignTextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(default='BRANDNAME', max_length=256, verbose_name='Design Context')),
                ('x_coor', models.FloatField(default=1.0, verbose_name='Design X Coordinate')),
                ('y_coor', models.FloatField(default=1.0, verbose_name='Design Y Coordinate')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Product Title')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Product Image')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Design Title')),
                ('identifier', models.CharField(max_length=256, verbose_name='Design Identifier')),
            ],
            options={
                'verbose_name': 'Text Design',
                'verbose_name_plural': 'Text Designs',
            },
        ),
        migrations.CreateModel(
            name='DesignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('images', models.ManyToManyField(to='rest_api.designimagemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('texts', models.ManyToManyField(to='rest_api.designtextmodel')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_api.productmodel')),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designs',
            },
        ),
        migrations.AddField(
            model_name='designtextmodel',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.textmodel'),
        ),
    ]
