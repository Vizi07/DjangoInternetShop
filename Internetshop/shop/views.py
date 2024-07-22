from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Review


# Create your views here.

def home(request):  #Начальная страница
    products = Product.objects.all()
    return render(request, "index.html",
                  {'products': products

                   })


def view_product(request, id): #cтраница продукта
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review(author=author, rating=int(rating), text=text, product=product)
        review.save()

    reviews = product.review_set.all()
    return render(request, 'product.html', {
        'product': product,
        'id': id,
        'reviews': reviews,
    })


def payment(request,id): #страница оплаты
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        print(name, address, phone)

    return render(request,'payment.html',{
        'product': product,
        'id':id,

                   })

def payment_success(request):
    return render(request, 'success.html')