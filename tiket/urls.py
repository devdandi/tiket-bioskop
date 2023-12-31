"""
URL configuration for tiket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from welcomes import views as welcome_views
from products import views as product_views
from transactions import views as transaction_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_views.index, name='home'),
    path('products/', product_views.index, name='products'),
    path('products/<str:product_id>', product_views.detail, name='products.detail'),
    path('carts/', transaction_views.carts, name='carts'),
    path('carts/add/<str:product_id>', transaction_views.add_to_carts, name='carts.add'),
    path('carts/remove/<str:cart_id>', transaction_views.remove_carts, name='carts.remove'),

    path('checkout/', transaction_views.checkout, name='checkout'),
    path('payments/<uuid:transaction_id>/<str:snap_token>', transaction_views.payments, name='payments'),
    path('transactions/histories', transaction_views.histories, name='histories'),





    path('users/logout/', welcome_views.logout_user, name='user.logout'),
    path('users/signin/', welcome_views.login_user, name='user.signin'),
    path('users/register/', welcome_views.register_user, name='user.register'),


    path('api/v1/payments/handling', transaction_views.handling_payments, name='api.v1.payments.handling'),
    path('api/v1/payments/recurring/handling', transaction_views.handling_recurring, name='api.v1.recurring.handling'),
    path('api/v1/payments/pay-accounts/handling', transaction_views.handling_pay_accounts, name='api.v1.pay_accounts.handling'),
    path('api/v1/payments/finish/handling', transaction_views.handling_finish_redirect, name='api.v1.finish.handling'),
    path('api/v1/payments/unfinish/handling', transaction_views.handling_unfinish_redirect, name='api.v1.unfinish.handling'),
    path('api/v1/payments/error/handling', transaction_views.handling_error_redirect, name='api.v1.error.handling'),








] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
