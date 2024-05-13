from django.shortcuts import render
from product.models import Products
from product.forms import productform
def home(request):
   m=Products.objects.all()
   return render(request, 'home.html', {'m': m})


def detail(request,n):
   m =Products.objects.get(id=n)
   return render(request, 'detail.html', {'m': m})
def add(request):
    if(request.method=="POST"):
         form=productform(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            return home(request)

    form=productform()
    return render(request, 'add.html', {'form': form})
def update(request,n):
    m = Products.objects.get(id=n)
    if (request.method == "POST"):
        form = productform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)

    form = productform(instance=m)
    return render(request, 'add.html', {'form': form})
def delete(request,n):
    m = Products.objects.get(id=n)
    m.delete()
    return home(request)
