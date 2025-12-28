from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Dashboard View
def dashboard(request):
    return render(request, 'academic/dashboard.html')