# Generated by Django 2.2.5 on 2019-12-11 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litsearch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='literatureitem',
            old_name='detail',
            new_name='details_link',
        ),
    ]
