# Generated by Django 2.2.6 on 2019-10-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(default='none', max_length=15),
            preserve_default=False,
        ),
    ]
