from django.contrib.auth.decorators import login_required 
from django.shortcuts import render , get_object_or_404 
  
from item.models import Item 

def index(request):
    item = Item.objects.filters(created_by = request.user)

    return render(request, 'dashboard/index.html',{
        'items': items, 
    })
