from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search)  |
            Q(kategori__isim__icontains =search)
        )
    if request.method == 'POST':
      if request.user.is_authenticated:
        urunId = request.POST['urunId']
        adet = request.POST['adet']
        urunum = Urun.objects.get(id = urunId)
        if Sepet.objects.filter(user = request.user, urun = urunum).exists():
            sepetim = Sepet.objects.get(user = request.user, urun = urunum)
            sepetim.adet += int(adet)
            sepetim.toplam = urunum.no * int(sepetim.adet)
            sepetim.save()
            return redirect('index')
        else:
            sepetim = Sepet.objects.create(
                urun = urunum,
                user = request.user,
                adet = adet,
                toplam = urunum.no * int(adet)
            )
            sepetim.save()
            return redirect('index')
      else:
          messages.info(request, 'Ürün alabilmek için giriş yapmanız gerekmektedir')
          return redirect('login')
    sepetAdet = Sepet.objects.filter(user = request.user).count()
    context = {
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler,
        'sepetAdet':sepetAdet
    }
    return render(request, 'index.html', context)

def hakkimda(request):
    return render(request, 'hakkimda.html')

def urun(request, urunId):
    product = Urun.objects.filter(id = urunId)
    context = {
        'urun':product
    }
    return render(request, 'urun.html', context)

def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            # oluşturan bilgisini doldurmak için
            user = form.save(commit = False)
            user.olusturan = request.user #girişli olan kullanıcı
            user.save()
            messages.success(request, 'Ürün oluşturuldu')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

def urunlerim(request):
    urunler = Urun.objects.filter(olusturan = request.user)
    if request.method =='POST':
        sil = request.POST['sil']
        
        urun = Urun.objects.get(id =sil)
        urun.delete()
        messages.success(request, 'ürün silindi')
        return redirect('urunlerim')
    context = {
        'urunler':urunler
    }
    return render(request, 'urunlerim.html', context)

def sepet(request):
    urunler = Sepet.objects.filter(user = request.user)
    toplam = 0
    for i in urunler:
        print(i.toplam)
        toplam += i.toplam
        print("t = ", toplam)
    if request.method =='POST':
        sil = request.POST['sil']
        
        urun = Sepet.objects.get(id =sil)
        urun.delete()
        messages.success(request, 'ürün sepetten kaldırıldı')
        return redirect('sepet')
    context = {
        'urunler':urunler,
        'toplam':toplam
    }
    return render(request, 'sepet.html', context)