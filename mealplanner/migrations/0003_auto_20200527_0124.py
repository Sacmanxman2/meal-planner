# Generated by Django 3.0.6 on 2020-05-27 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0002_auto_20200527_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Recipe'),
            preserve_default=False,
        ),
    ]
