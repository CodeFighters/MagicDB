from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^register/$", views.register, name="register"),
    url(r"^main/", views.main, name="main"),
    url(r"^logout/$", views.main_logout, name="logout"),
]
