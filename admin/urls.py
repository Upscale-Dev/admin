from django.contrib import admin
from django.urls import path

admin.site.site_header = "Bizboost Admin"

urlpatterns = [
    path('', admin.site.urls),
]
