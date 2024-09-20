from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'index'),
    path('contact/',views.contact,name = 'contact'),
    path('page/<int:pk>/',views.page,name = 'page'),
    path('about_us/',views.about_us,name = 'about_us'),
]
