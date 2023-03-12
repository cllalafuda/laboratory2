from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.shortcuts import render


def home(request):
    return render(request, "static_handler.html")
