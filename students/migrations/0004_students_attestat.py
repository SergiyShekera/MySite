# Generated by Django 2.0.3 on 2018-04-20 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20180420_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='attestat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Attestat'),
        ),
    ]
