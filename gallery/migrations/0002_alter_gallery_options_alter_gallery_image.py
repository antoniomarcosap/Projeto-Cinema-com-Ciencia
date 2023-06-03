# Generated by Django 4.2 on 2023-06-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('created',), 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='gallery/%Y/%m/%d'),
        ),
    ]
