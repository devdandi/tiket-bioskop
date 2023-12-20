from django.shortcuts import render
from .models import Films
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    film_list = Films.objects.all()

    q = request.GET.get('q')
    
    if q:
        film_list = film_list.filter(name__icontains=q)
    
    paginator = Paginator(film_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj' : page_obj})

def detail(request, product_id):
    film = Films.objects.get(pk=product_id)
    


    return render(request, 'detail-products.html')