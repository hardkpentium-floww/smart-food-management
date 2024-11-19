# Generated by Django 2.2.2 on 2024-11-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='type',
            new_name='meal_type',
        ),
        migrations.RemoveField(
            model_name='usermeal',
            name='type',
        ),
        migrations.AddField(
            model_name='usermeal',
            name='meal_preference',
            field=models.CharField(choices=[('FULL', 'FULL'), ('HALF', 'HALF'), ('CUSTOM', 'CUSTOM')], default='FULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='usermeal',
            name='meal_status',
            field=models.CharField(choices=[('ATE', 'ATE'), ('SKIPPED', 'SKIPPED'), ('NULL', 'NULL')], default='ATE', max_length=250),
        ),
        migrations.AlterField(
            model_name='usermeal',
            name='meal_type',
            field=models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER')], default='LUNCH', max_length=250),
        ),
    ]
