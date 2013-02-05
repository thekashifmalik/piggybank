from django.contrib import admin
from .models import Fetch, FetchType, FetchResult

admin.site.register(Fetch)
admin.site.register(FetchType)
admin.site.register(FetchResult)