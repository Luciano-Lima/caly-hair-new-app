# Generated by Django 4.0.3 on 2022-03-08 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Colour',
        ),
        migrations.DeleteModel(
            name='Cutting',
        ),
        migrations.DeleteModel(
            name='Highlights',
        ),
        migrations.DeleteModel(
            name='Styling',
        ),
        migrations.DeleteModel(
            name='Toners',
        ),
        migrations.DeleteModel(
            name='Treatment',
        ),
    ]
