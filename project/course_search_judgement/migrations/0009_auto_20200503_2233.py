# Generated by Django 3.0.3 on 2020-05-03 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_search_judgement', '0008_auto_20200503_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(default='社会科学', max_length=20),
        ),
        migrations.AlterField(
            model_name='judgement_system',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 22, 33, 43, 565947)),
        ),
    ]
