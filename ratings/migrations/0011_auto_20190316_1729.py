# Generated by Django 2.1.7 on 2019-03-16 11:59

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0010_auto_20190316_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ratings',
            field=jsonfield.fields.JSONField(default={1: 0, 2: 0, 3: 0, 4: 0, 5: 0}),
        ),
    ]