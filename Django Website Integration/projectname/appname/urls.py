from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.galleryview, name='gallery'),
    path('heritage/', views.heritageview, name='heritage'),
    path('hotelbooking/', views.hotelbookingview, name='hotelbooking'),
    path('contact/', views.contactview, name='contact'),
]