from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
from flipkartapp.models import cat,prod


def flipkart(request,cslug=None):
    cpage=None
    productslist=None
    if cslug!=None:
        cpage=get_object_or_404(cat,slug=cslug)
        productslist=prod.objects.all().filter(category=cpage,availability=True)
    else:
        productslist = prod.objects.all().filter(availability=True)
    paginator=Paginator(productslist,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except  (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,"category.html",{'category':cpage,'prod':products})
def Pdetails(request,cslug,pslug):
    try:
        product=prod.objects.get(category__slug=cslug,slug=pslug)
    except Exception as e:
        raise e
    return render(request,'product.html',{ 'p':product })