# Generated by Django 3.1.2 on 2021-02-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_entity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_desc_type',
            field=models.CharField(default='defaultvalue', max_length=120),
            preserve_default=False,
        ),
    ]