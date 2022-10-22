# Generated by Django 2.2.11 on 2022-10-16 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet_id', models.SlugField()),
                ('type_of_meet', models.CharField(choices=[('do', 'DSA AND OPERATING SYSTEM'), ('dd', 'DSA AND DATABASE'), ('dn', 'DSA AND NETWORKING'), ('od', 'OPERATING SYSTEM AND DATABASE'), ('mo', 'MOCK INTERVIEW')], max_length=10)),
                ('additon_time', models.DateTimeField(auto_now_add=True)),
                ('meet_time', models.DateTimeField()),
                ('attendee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
