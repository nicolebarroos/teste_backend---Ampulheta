# Generated by Django 4.0 on 2022-06-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]