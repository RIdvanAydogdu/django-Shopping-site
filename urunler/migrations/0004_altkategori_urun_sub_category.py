# Generated by Django 4.1.7 on 2023-11-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_kategori_alter_urun_aciklama_alter_urun_isim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='urun',
            name='sub_category',
            field=models.ManyToManyField(to='urunler.altkategori'),
        ),
    ]
