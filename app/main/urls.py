from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("info/", views.contact_info, name="contact_info"),
    path("delivery_and_payment/", views.delivery_and_payment, name="delivery_and_payment")
]