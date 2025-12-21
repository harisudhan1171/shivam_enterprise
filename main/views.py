from django.shortcuts import HttpResponse, render,get_object_or_404
from django.template import loader
from store.models import *
from django.db.models import Q


def home_view(request):
    All_category = category.objects.all()
    context = {
        'all_category': All_category,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def gallery(request):
    gallerymodel = GalleryAlbum.objects.all()
    context = {'gallerymodel' : gallerymodel}
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render(context))

def category_view(request,slug):
    get_id = get_object_or_404(category,slug=slug)
    get_product_by_category = products.objects.filter(category_id__exact = get_id)
    context = {
        'pro_by_cat' : get_product_by_category,
    }
    template = loader.get_template('shop.html')
    return HttpResponse(template.render(context))
 

def product_search(request):
    
    if request.method =='GET':
        user_request = request.GET.get('search_input')
        text = user_request.replace(" ","")
        searched_product = products.objects.filter(Q(Model_No__iexact= text) | Q(Material__iexact = text) |Q(slug__iexact = text))
        products_list = products.objects.all()
        template = loader.get_template('shop.html')
        context = {
            'searched_product': searched_product,
            'products': products_list,
            'user_request': user_request,
            
        }
        if not searched_product :
            context = {
                'message': f'No records found for "{ user_request}" !',
                'searched_product': searched_product,
                'products': products_list,
                
            }
            return render(request,'shop.html',context)
    return HttpResponse(template.render(context))

def product_view(request,slug):
    specific_product = get_object_or_404(products,slug=slug)
    related_product = products.objects.filter(Material__icontains=specific_product.Material)

   
    context = {
        'specific_product' : specific_product,
        'related_products' : related_product
    }
    template = loader.get_template('product_view.html')
    return HttpResponse(template.render(context))     
        
    
def shop_view(request):
    products_list = products.objects.all()
    context = {
        'products': products_list,
    }
    template = loader.get_template('shop.html')
    return HttpResponse(template.render(context))

def about_view(request):

    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def terms_conditions(request):
    template = loader.get_template('terms&conditions.html')
    return HttpResponse(template.render())
