from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        phones = list(Phone.objects.all().order_by('name'))
    elif sort == 'min_price':
        phones = list(Phone.objects.all().order_by('price'))
    else:
        phones = list(Phone.objects.all().order_by('price').reverse())

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
