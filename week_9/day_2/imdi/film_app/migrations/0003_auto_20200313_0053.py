# Generated by Django 3.0.3 on 2020-03-12 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0002_auto_20200312_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
