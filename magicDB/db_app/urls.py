from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^register/$", views.register, name="register"),
    url(r"^main/", views.main, name="main"),
    url(r"^todo/", views.todo, name="todo"),
    url(r"^tvseries/", views.tvseries, name="tvseries"),
    url(r"^list/$", views.show_lists, name="show_lists"),
    url(r"^list/(?P<list_name>\w+)/$", views.groceries, name="groceries"),
    # url(r"^groceries/", views.groceries, name="groceries"),
    url(r"^logout/$", views.main_logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
