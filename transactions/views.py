from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from products.models import Films, FilmSchedules
from transactions.models import Carts, Transactions
from sheets.models import Sheets
import uuid
import requests
import base64
import json
from django.views.decorators.csrf import csrf_exempt




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
    
    total = subtotal
    return render(request, 'carts.html', {'carts' : cart_list, 'subtotal' : subtotal, 'total' : total, 'sheets' : sheet_list})

def checkout(request):

    transaction_id = f"{uuid.uuid4()}"

    midtrans_object = {
        "transaction_details" : {
            "order_id" : None,
            "gross_amount" : 0
        },
        "item_details" : [],
        "customer_details" : {
            "first_name" : request.user.first_name,
            "last_name" : request.user.last_name,
            "username" : request.user.username
        }
    }


    for cart in request.POST:
        if cart.startswith('sheet_'):
            split_sheet = cart.split('_')
            _sheet, sheet_id, _cart, cart_id = split_sheet
            

            subtotal = request.POST.get('subtotal')
            total = request.POST.get('total')

            schedule_id = request.POST.get(f"schedule_cart_{cart_id}")

            sheet_instance = Sheets.objects.get(pk=sheet_id)
            cart_instance = Carts.objects.get(pk=cart_id)
            schedule_instance = FilmSchedules.objects.get(pk=schedule_id)

            Transactions.objects.create(
                sheet=sheet_instance,
                product_schedule=schedule_instance,
                subtotal=subtotal,
                total=total,
                user = request.user,
                transaction_id=transaction_id
            )

            midtrans_object['item_details'].append({
                "id" : str(cart_instance.product.id),
                "name" : cart_instance.product.name,
                "quantity" : cart_instance.total_items,
                "category_id" : str(cart_instance.product.categoryId.id),
                "category_name" : cart_instance.product.categoryId.name,
                "price" : cart_instance.product.price
            })

    
            
            cart_instance.delete()

    midtrans_object['transaction_details']['order_id'] = transaction_id
    midtrans_object['transaction_details']['gross_amount'] = request.POST.get('total')

    server_key = "SB-Mid-server-7KSCrt--TiX4YiAKKxDrftHi"
    server_key_bytes = server_key.encode("ascii")

    b64_server_key = base64.b64encode(server_key_bytes)
    b64_server_key_string = b64_server_key.decode('ascii')


    responses = requests.post("https://app.sandbox.midtrans.com/snap/v1/transactions", headers={"Authorization" : f"Basic {b64_server_key_string}", "Content-Type" : "application/json"}, json=midtrans_object)
    data = responses.json()
    snapToken = data['token']

    return redirect(reverse('payments', kwargs={"transaction_id" : transaction_id, 'snap_token' : snapToken}) + f"?transaction_id={transaction_id}&snapToken={snapToken}")


def payments(request, transaction_id, snap_token):
    
    return render(request, 'payment.html', {'snap_token' : snap_token})


def histories(request):
    transaction_list = Transactions.objects.filter(user=request.user).order_by('transaction_time')
    return render(request, 'history.html', {'transactions' : transaction_list})


@csrf_exempt
def handling_payments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        transaction_id = data['order_id']
        transaction_instance = Transactions.objects.filter(transaction_id=transaction_id)
        for transaction_status in transaction_instance:
            transaction_status.transaction_status = data['transaction_status']
            transaction_status.fraud_status = data['fraud_status']
            transaction_status.transaction_time = data['transaction_time']
            transaction_status.payment_type = data['payment_type']
            transaction_status.save()
    
    return redirect('products')



@csrf_exempt
def handling_recurring(request):
    if request.method == 'POST':
        pass

@csrf_exempt
def handling_pay_accounts(request):
    if request.method == 'POST':
        pass

@csrf_exempt
def handling_finish_redirect(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

    transaction_id = request.GET.get('transaction_id')

    if not transaction_id:
        return HttpResponse("Failed to parse transaction")

    transaction = Transactions.objects.filter(transaction_id=transaction_id)

    transactions_summarize = Transactions.objects.filter(transaction_id=transaction_id).values('transaction_id', 'total', 'subtotal', 'payment_type', 'transaction_status').distinct().first()


    return render(request, 'payment_finish.html', {'transactions' : transaction, 'transactions_summarize' : transactions_summarize, 'transaction_id' : transaction_id})

@csrf_exempt
def handling_unfinish_redirect(request):
    if request.method == 'POST':
        pass

    return HttpResponse("Payment unfinish")

@csrf_exempt
def handling_error_redirect(request):
    if request.method == 'POST':
        pass

    return HttpResponse("Payment failed")
