from django.shortcuts import render, redirect
from products.models import Films
from transactions.models import Carts, Transactions
from sheets.models import Sheets



def add_to_carts(request, product_id):
    if not request.user.is_authenticated:
        return redirect('user.signin')
    product = Films.objects.get(pk=product_id)

    Carts.objects.create(
        product=product,
        user=request.user
    )

    return redirect('carts')

def remove_carts(request, cart_id):
    if not request.user.is_authenticated:
        return redirect('user.signin')
    cart = Carts.objects.get(pk=cart_id)
    cart.delete()

    return redirect('carts')
    
# Create your views here.
def carts(request):
    cart_list = Carts.objects.filter(user=request.user)
    sheet_list = Sheets.objects.all().order_by('number')
    subtotal = 0
    total = 0
    for cart in cart_list:
        subtotal += cart.product.price
    
    total = subtotal + 300
    return render(request, 'carts.html', {'carts' : cart_list, 'subtotal' : subtotal, 'total' : total, 'sheets' : sheet_list})

def checkout(request):

    for cart in request.POST:
        if cart.startswith('sheet_'):
            split_sheet = cart.split('_')
            _sheet, sheet_id, _cart, cart_id = split_sheet

            subtotal = request.POST.get('subtotal')
            total = request.POST.get('total')

            

            sheet_instance = Sheets.objects.get(pk=sheet_id)
            cart_instance = Carts.objects.get(pk=cart_id)

            Transactions.objects.create(
                sheet=sheet_instance,
                product=cart_instance.product,
                subtotal=subtotal,
                total=total,
                user = request.user
            )
            
            cart_instance.delete()

    return redirect('payments')


def payments(request):
    return render(request, 'payment.html')


def histories(request):
    transaction_list = Transactions.objects.filter(user=request.user)
    return render(request, 'history.html', {'transactions' : transaction_list})