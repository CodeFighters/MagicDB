from django.conf.urls import include, url
from django.contrib import admin
import tvseries.views
import dbapp.views
import todo.views

urlpatterns = [
    url(r"^$", dbapp.views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^logout/$", dbapp.views.main_logout, name="logout"),

    url(r"^register/", dbapp.views.register, name="register"),
    url(r"^main/", dbapp.views.main, name="main"),

    url(r'^tvseries/$', tvseries.views.index, name="tvseries"),
    url(r"^todo/", todo.views.post_list, name="todo"),

    url(r"^groceries/", todo.views.post_list, name="groceries"),
    url(r'^post/new/$', todo.views.post_new, name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/$',  todo.views.post_detail),
    url(r'^post/(?P<pk>[0-9]+)/edit/blog.views.post_list$', todo.views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', todo.views.post_edit, name='post_edit'),

    url(r'^post/new/blog.views.post_list$', todo.views.post_list),
]
