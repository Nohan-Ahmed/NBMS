# Generated by Django 5.0.3 on 2024-07-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='book', to='categories.category'),
        ),
    ]