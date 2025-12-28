from django.urls import path
from . import views

urlpatterns = [
    # Ana sayfa (boþ býrakýrsak direkt siteye girince açýlýr)
    path('', views.dashboard, name='dashboard'),
]