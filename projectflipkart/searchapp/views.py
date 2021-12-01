from django.db.models import Q
from django.shortcuts import render
from flipkartapp . models import prod
# Create your views here.
def search(request,):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=prod.objects.all().filter(Q(name__contains=query)|Q(descr__contains=query))
        return render(request,'search.html',{'q':query,'p':products})
