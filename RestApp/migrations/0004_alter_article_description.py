# Generated by Django 4.0.3 on 2022-03-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0003_rename_desctiption_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=191),
        ),
    ]