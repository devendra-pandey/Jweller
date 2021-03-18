from django.shortcuts import render,redirect, get_object_or_404,HttpResponse

from . models import Products
from . forms import ProductsForm

def products(request):

    prod = Products.objects.filter(status=1).all()

    context = {
        'prod':prod,
    }

    
    return render(request, 'products/products.html',context)


def products_create(request):
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('products')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'products'}}">reload</a>""")
    else:
        return render(request, 'products/add_product.html', {'upload_form':form}) 



def update_products(request, id):
    prod_id = int(id)
    try:
        prod_get = Products.objects.get(id = prod_id)
    except Products.DoesNotExist:
        return redirect('products')
    form = ProductsForm(request.POST or None, instance = prod_get)
    if form.is_valid():
       form.save()
       return redirect('products')
    return render(request, 'products/add_product.html', {'upload_form':form })



def delete_products(request, id):
    prod_id = int(id)
    try:
        prod_data = Products.objects.get(id = prod_id)
    except Products.DoesNotExist:
        return redirect('products')
    prod_data.status = '0'
    prod_data.save()
    return redirect('products')


def search_jwel(request):

    context_dict = {}
    if request.method == 'POST':
        query = request.POST['design_number']
        results = Products.objects.filter(design_number=query)
        if query:
            context_dict['results'] = results
        else:
            context_dict['no_results'] = query
            
    return render(request, "products/add_quatation.html", context_dict)


def add_quatation(request):
    prod = Products.objects.filter(status=1).all()
    context = {
        'prod':prod,
        
    }
    return render(request, 'products/add_quatation.html', context)


def quatation(request):
    return render(request, 'products/view_quatation.html')

