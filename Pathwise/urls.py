from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Gelen boþ istekleri academic uygulamasýndaki urls.py dosyasýna gönder
    path('', include('academic.urls')),
]