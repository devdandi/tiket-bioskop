from django.shortcuts import render
from .models import Films
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    film_list = Films.objects.all()
    paginator = Paginator(film_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj' : page_obj})

def detail(request, product_id):
    film = Films.objects.get(pk=product_id)
    


    return render(request, 'detail-products.html')