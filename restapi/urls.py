from django.urls import path

from . import views


urlpatterns = [
    path('products_detail_all',views.products_detail_all.as_view() ,name='products_detail_all'),
    path('products_detail/<int:id>/', views.products_detail,name='products_detail'),
]