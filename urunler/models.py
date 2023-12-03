from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim

class AltKategori(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim

class Tek(models.Model):
    isim = models.CharField(max_length=100)
    def __str__(self):
        return self.isim   
    
class Urun(models.Model):
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    sub_category = models.ManyToManyField(AltKategori)
    tekBilgi = models.OneToOneField(Tek, on_delete=models.CASCADE, null=True, blank=True)
    isim = models.CharField(max_length=100, verbose_name="ürün ismi")
    aciklama = RichTextField(max_length=500, verbose_name="ürün açıklaması")
    no = models.IntegerField(verbose_name="ürün fiyatı")
    resim = models.FileField(upload_to='urunler/', null=True, blank=True, verbose_name="ürün resmi")
    def __str__(self):
        return self.isim
    
class Sepet(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adet = models.IntegerField()
    toplam = models.IntegerField()
    
    def __str__(self):
        return self.user.username