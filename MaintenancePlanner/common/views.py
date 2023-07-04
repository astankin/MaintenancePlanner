from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home-page.html')
    return render(request, 'index.html')
