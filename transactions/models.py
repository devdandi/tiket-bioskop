from django.db import models
import uuid
from products.models import Films
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
    sheet = models.ForeignKey(Sheets, on_delete=models.CASCADE)
    product = models.ForeignKey(Films, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
