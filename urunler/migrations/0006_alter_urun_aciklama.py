# Generated by Django 4.1.7 on 2023-11-11 19:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_tek_urun_tekbilgi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='aciklama',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='ürün açıklaması'),
        ),
    ]
