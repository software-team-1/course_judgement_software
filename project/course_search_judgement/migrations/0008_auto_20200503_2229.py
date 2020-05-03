# Generated by Django 3.0.3 on 2020-05-03 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_search_judgement', '0007_auto_20200503_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgement_system',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 22, 29, 35, 462857)),
        ),
        migrations.AlterField(
            model_name='judgement_system',
            name='hard_core_mark',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='judgement_system',
            name='mark_of_interest',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='judgement_system',
            name='recommend_mark',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
    ]
