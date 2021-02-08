# Generated by Django 3.1.2 on 2021-02-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('attributes', models.JSONField()),
            ],
        ),
    ]
