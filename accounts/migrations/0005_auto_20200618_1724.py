# Generated by Django 2.2.11 on 2020-06-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200507_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='accounts/default_profile.jpg', upload_to=''),
        ),
    ]
