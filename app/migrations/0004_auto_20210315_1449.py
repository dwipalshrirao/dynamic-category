# Generated by Django 3.1.1 on 2021-03-15 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_subcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='data',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=40),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcname',
            field=models.CharField(max_length=100),
        ),
    ]