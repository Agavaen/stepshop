from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

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