from django.shortcuts import render
from .models import category,subcategory
# Create your views here.


def categoryview(request):
 
    return render(request,'index.html')


def subcategorypage(request,slug):
    
    subcat=subcategory.objects.get(slug=slug)
    return render(request,'subcatpage.html',{'subcatdata':subcat})