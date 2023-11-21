from django.shortcuts import render
from shop_side.models import Product, Shop


def product_list_view(request):

    shops = Shop.objects.all()
    selected_shop = request.POST.get('shop')

    if selected_shop:
        products = Product.objects.filter(shops__title=selected_shop)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'shops': shops,
        'selected_shop': selected_shop,
    }
   
    return render(request,
                  'client_side/product_list.html',
                  context)


def product_detail_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request,
                  'client_side/product_detail.html',
                  context)




