from django.contrib import admin
from .models import Stock, StockSnapshot

admin.site.register(Stock)
admin.site.register(StockSnapshot)