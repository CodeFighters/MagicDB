from django.shortcuts import render
from tvseries import models
from django.contrib.auth.models import User


def add_to_db(movie, episode, season, user, watched=False):
    q = models.Series(
        movie=movie, episode=episode, user=user, season=season, watched=watched)
    q.save()


def delete_e(target):
    del_me = models.Series.objects.filter(id=target)
    del_me.delete()


def update_me(select, is_watched):
    to_upd = models.Series.objects.select_for_update().filter(
        id=select).update(watched=is_watched)


# Create your views here.


def index(request):
    user = request.user
    tv = models.Series.objects.filter(user=user).all().order_by("id")

    if request.method == "POST":
        movie = request.POST.get("movie")
        season = request.POST.get("season")
        episode = request.POST.get("episode")
        watched = 0
        add_to_db(movie, episode, season, user, int(watched))

    if request.method == "GET":
        target = request.GET.get("target")
        change = request.GET.get("change")
        status = request.GET.get("status")

        print(status)
        if status is not None:
            watched = 1
            update_me(int(status), int(watched))
        else:
            print("here")
            watched = 0

        delete_e(target)

    return render(request, "tv.html", locals())
