# Generated by Django 4.0.3 on 2022-03-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_general'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
    ]