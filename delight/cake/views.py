from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .forms import ContactForm
from .models import  Product
# Create your views here.
@login_required(login_url='sign_in')


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def order(request):
    return render(request,'order.html')

def menu(request):
    return render(request,'menu.html')


def product_list(request, category):
    products = Product.objects.filter(category__iexact=category)
    return render(request, 'product.html', {
        'products': products,
        'category': category.capitalize()
    })

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form}) 

def live_search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query)
        )
    else:
        products = Product.objects.none()

    data = []
    for product in products:
        data.append({
            'name': product.name,
            'price': str(product.price),
            'image': product.image.url,
        })

    return JsonResponse({'products': data})

def sign_up(request):
    if request.method=="POST":
        register_form=UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('sign_in')
    else:   
        register_form=UserCreationForm()
    return render(request,'register.html',{'register_form':register_form}) 

def sign_in(request):
    if request.method=="POST":
        login_form=AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            return redirect('index')
    else:  
        login_form=AuthenticationForm()
    return render(request,'login.html',{'login_form':login_form}) 
    
def sign_out(request):
    logout(request)
    return redirect('sign_in')

