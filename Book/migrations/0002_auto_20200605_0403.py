# Generated by Django 3.0.7 on 2020-06-05 02:03

import Book.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=Book.fields.IntegerRangeField(),
        ),
    ]