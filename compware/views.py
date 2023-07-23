from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Item
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
        mydata = list(Item.objects.all().order_by('item_name'))
        template = loader.get_template('compware/index.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))
    
@login_required
def hardware(request):
        mydata = list(Item.objects.filter(item_category=1).order_by('item_name'))
        template = loader.get_template('compware/hardware.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))
    
@login_required
def software(request):
        mydata = list(Item.objects.filter(item_category=2).order_by('item_name'))
        template = loader.get_template('compware/software.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))

@login_required
def computingcomponents(request):
        mydata = list(Item.objects.filter(item_subcat=1).order_by('item_name'))
        template = loader.get_template('compware/computingcomponents.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))

@login_required
def networkingcomponents(request):
        mydata = list(Item.objects.filter(item_subcat=2).order_by('item_name'))
        template = loader.get_template('compware/networkingcomponents.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))

@login_required
def peripherals(request):
        mydata = list(Item.objects.filter(item_subcat=3).order_by('item_name'))
        template = loader.get_template('compware/peripherals.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))


@login_required
def utilitysoftware(request):
        mydata = list(Item.objects.filter(item_subcat=6).order_by('item_name'))
        template = loader.get_template('compware/utilitysoftware.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))


@login_required
def operatingsystem(request):
        mydata = list(Item.objects.filter(item_subcat=5).order_by('item_name'))
        template = loader.get_template('compware/operatingsystem.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))

@login_required
def antivirus(request):
        mydata = list(Item.objects.filter(item_subcat=4).order_by('item_name'))
        template = loader.get_template('compware/antivirus.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))

def search(request):
    query = request.GET.get('q')
    results = ''
    context = { 'query' : results}
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    
    if query:
        results = Item.objects.filter(item_name__icontains=query) or Item.objects.filter(item_price__icontains=query)
        
    context.update({'results': results})
    return render(request, 'compware/results.html', context)

                
def about(request):
    return render(request, 'compware/about.html')

