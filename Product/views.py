from django.shortcuts import render
from .form import ProductForm
from .models import Product
from django.shortcuts import redirect,render,get_object_or_404



# Create your views here.
def upload_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = ProductForm()
    return render(request,"Product/product_upload.html",{"form":form})

def product_list(request):
    products=Product.objects.all()
    return render(request,'Product/product_list.html',{"products": products})
def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"Product/product_detail.html",{"product":product})
def edit_product_view(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return redirect("product_detail_view",id=product.id)
    else:
        form=ProductForm(instance=product)
        return render(request,"Product/edit_product.html",{"form":form})
 