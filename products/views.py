from django.shortcuts import render,redirect, get_object_or_404,HttpResponse

from . models import Product
from . forms import ProductsForm

def products(request):
    p1_id = request.POST.get('p_id')
    print("**$$4*****")
    print(p1_id)
    quatation = ['1','2','3']

    if p1_id not in quatation:
        quatation.append(p1_id)
    else:
        print("error")
    print('Updated  list: ', quatation)
    prod = Product.objects.filter(status=1).all()
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
        prod_get = Product.objects.get(id = prod_id)
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
        prod_data = Product.objects.get(id = prod_id)
    except Product.DoesNotExist:
        return redirect('products')
    prod_data.status = '0'
    prod_data.save()
    return redirect('products')


def search_jwel(request):
    if request.method == 'POST':
        query = request.POST['design_number']
        results = Product.objects.filter(design_number=query)
        if query:
            context = {
                'results':results,
            }
        else:
            prod = Product.objects.filter(status=1).all()
            context = {
                'prod':prod,
                'query':query,
            }
            
    return render(request, "products/add_quatation.html", context)



def add_quatation(request):
    p1_id = request.POST.get('p_id')
    p11_id = request.POST.get('p11_id')
    print("**$$4*****")
    print(p11_id)
    if request.session.get("quatation", None) is None:
        quatation = []
        request.session["quatation"] = quatation
    else:
        quatation = request.session["quatation"]
        if p1_id not in quatation or p11_id in quatation:
            quatation.append(p1_id)
            quatation.remove(p11_id)
            request.session["quatation"] = quatation
            print('Updated  list: ', quatation)
        else:
            print("Item already available")
    
    print("helo")
    print(quatation)
    print("heloo")
    List1 = []
    res = [i for i in quatation if i]

    print(res)
    prod = Product.objects.filter(status=1).all()

    for ab in res:
        ab_ = {'quat': Product.objects.filter(id=ab), 'ab': ab}
        List1.append(ab_)    

    context = {
        'prod':prod,
        'List1':List1,
    }
    return render(request, 'products/add_quatation.html', context)
    

def quatation(request):
    return render(request, 'products/view_quatation.html')

