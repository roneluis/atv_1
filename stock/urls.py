from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('list', views.product_list),
  path('nameorder/', views.name_order),
  path('lowestprice/', views.lowest_price),
  path('biggerprice/', views.bigger_price)
]