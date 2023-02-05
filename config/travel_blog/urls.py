from django.urls import path

from . import views

app_name = 'travel_blog'

urlpatterns = [
    path('',views.product_all,name='product_all'),
    path('about/', views.about, name='about'),
    path('best-places/', views.discover, name='discover'),
    
]
