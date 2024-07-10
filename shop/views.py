from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index (request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    
    if item_name!='' and item_name is not None:
      products = Product.objects.filter(title__icontains= item_name)
      
    paginator = Paginator(products, 4) 
    page = request.GET.get('page')  
    products = paginator.get_page(page)
    return render(request,'shop/index.html', {'products': products})
  
def detail(request, myid):
  products = Product.objects.get(id=myid)
  
  return render(request,'shop/detail.html', {'product': products})