from django.db import models
import uuid

# Create your models here.
class Sheets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField()


    def __str__(self) -> str:
        return f"Seat num {self.number}"