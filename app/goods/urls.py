from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path("search/", views.catalog, name="search"), # если оставить это url ниже, он попадет в slug url index;
    path("<slug:category_slug>/", views.catalog, name="index"),
    #path("<slug:category_slug>/<int:page>/", views.catalog, name="index") no needed anymore. 
    path("product/<slug:product_slug>/", views.product, name="product"),


]