# Generated by Django 3.1 on 2020-08-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_refmaterial_medium'),
    ]

    operations = [
        migrations.AddField(
            model_name='refmaterial',
            name='m_type',
            field=models.CharField(choices=[('image', 'image'), ('video', 'video'), ('website', 'website')], default='image', max_length=20),
        ),
    ]
