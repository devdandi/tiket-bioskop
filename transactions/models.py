from django.db import models
import uuid
from products.models import Films, FilmSchedules
from django.contrib.auth.models import User
from sheets.models import Sheets

# Create your models here.
class Carts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Films, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheets, null=True, blank=True, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.UUIDField(editable=False, null=True, blank=True)
    sheet = models.ForeignKey(Sheets, on_delete=models.CASCADE)
    product_schedule = models.ForeignKey(FilmSchedules, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    transaction_status = models.CharField(null=True, blank=True, default='unpayments')
    fraud_status = models.CharField(null=True, blank=True, default='unpayments')
    transaction_time = models.DateTimeField(blank=True, null=True)
    payment_type = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
