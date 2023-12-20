from django.contrib import admin
from .models import Films, Categories, FilmSchedules
# Register your models here.


admin.site.register(Films)
admin.site.register(Categories)
admin.site.register(FilmSchedules)