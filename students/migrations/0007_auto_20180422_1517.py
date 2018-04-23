# Generated by Django 2.0.3 on 2018-04-22 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180421_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='attestat',
        ),
        migrations.AddField(
            model_name='attestat',
            name='stundent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Students', unique=True),
        ),
    ]
