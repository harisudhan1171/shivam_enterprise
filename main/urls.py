from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('shop/', views.shop_view, name='shop'),
    path('search/', views.product_search, name='search'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('product/<slug:slug>/', views.product_view, name='product-view'),
    path('about/', views.about_view, name='about'),
    path('terms&conditions/', views.terms_conditions, name = 'terms&conditions'),
]