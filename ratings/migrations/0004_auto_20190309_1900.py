# Generated by Django 2.1.7 on 2019-03-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_teacher_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='cover',
            field=models.ImageField(default='all_covers/user.png', upload_to='all_covers/'),
        ),
    ]
