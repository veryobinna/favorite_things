# Generated by Django 2.2.4 on 2019-08-11 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("favorite_things_app", "0002_auto_20190811_1628")]

    operations = [
        migrations.AlterField(
            model_name="favoritething",
            name="ranking",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        )
    ]