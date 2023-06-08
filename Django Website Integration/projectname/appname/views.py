from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contactview(request):
    return render(request, 'contact.html')

def galleryview(request):
    return render(request, 'gallery.html')

def heritageview(request):
    return render(request, 'heritage.html')

def hotelbookingview(request):
    return render(request, 'hotelbooking.html')