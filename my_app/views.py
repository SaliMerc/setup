from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import Book


# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', context={'books': books})