# Generated by Django 2.0.3 on 2018-04-22 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20180422_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attestat',
            old_name='stundent',
            new_name='student',
        ),
    ]
