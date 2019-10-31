from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('list/', views.product_list),
  path('<int:id>/comprar/', views.sum),
  path('show/', views.product_show),
  path('cart/', views.cart)
]