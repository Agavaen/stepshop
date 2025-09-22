from django.shortcuts import render
from django.template.defaultfilters import title


def index(request):
    title = 'Главная - StepShop'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты - StepShop'

    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)

def product(request):
    title = 'Товар - StepShop'

    context = {
        'title': title,
    }
    return render(request, 'Product.html', context)

def products(request):
    title = 'Товары - StepShop'

    context = {
        'title': title,
    }
    return render(request, 'Products.html', context)

def about(request):
    title = 'О нас - StepShop'

    context = {
        'title': title,
    }
    return render(request, 'about.html', context)