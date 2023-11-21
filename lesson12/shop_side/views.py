from django.shortcuts import render, redirect, HttpResponse
from shop_side.models import Product, Category, Shop


def product_create_view(request):
    context = {'category_list': Category.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
       

        if not price.isnumeric():
            return HttpResponse('Некорректное значение цены')
        
        if not quantity.isnumeric():
            return HttpResponse('Некоректное значение количества')
        
        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )
        product.save()


        
        return redirect('product_list')
    else:
        return render(request,'shop_side/product_create.html',context)
    

   
                 







    

   











