from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import GroceriesForm, ListsForm
from .models import Lists, Groceries


def main_logout(request):
    logout(request)
    return redirect("index")


def index(request):
    if request.user.is_authenticated():
        return redirect("main")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return redirect("index")

    else:
        return render(request, "index.html", locals())


@login_required(login_url="index")
def main(request):
    return render(request, "main.html", locals())


def todo(request):
    return render(request, "todo.html", locals())


def tvseries(request):
    return render(request, "tvseries.html", locals())


def groceries(request, list_name):
    print(list_name)
    list_obj = Lists.objects.get(name=list_name)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        groceries_form = GroceriesForm(request.POST)
        # check whether it's valid:
        if groceries_form.is_valid():
            # process the data in form.cleaned_data as required
            grocery_name = groceries_form.cleaned_data['name']
            grocery_quantity = groceries_form.cleaned_data['quantity']
            grocery_measurement = groceries_form.cleaned_data['measurement']
            grocery_is_bought = groceries_form.cleaned_data['is_bought']
            grocery = Groceries(
                name=grocery_name,
                list_name=list_obj,
                quantity=grocery_quantity,
                measurement=grocery_measurement,
                is_bought=False
            )
            grocery.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/list/{}/'.format(list_obj.name))

    # if a GET (or any other method) we'll create a blank form
    else:
        groceries_form = GroceriesForm()
        groceries_for_list = Groceries.objects.filter(list_name=list_obj.id)
    return render(request, "groceries.html", locals())


def show_lists(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        list_form = ListsForm(request.POST)
        # check whether it's valid:
        if list_form.is_valid():
            # process the data in form.cleaned_data as required

            list_name = list_form.cleaned_data['name']
            new_list = Lists(name=list_name)
            new_list.save()

            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        list_form = ListsForm()
        all_lists = Lists.objects.all()
    return render(request, "lists.html", locals())    


def _validate_register(username, email, password):
    if username is None or username.strip() == "":
        return False

    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "":
        return False

    return True


def register(request):
    if request.user.is_authenticated():
        return redirect("main")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not _validate_register(username, email, password):
            return HttpResponseBadRequest("Something is missing")

        user = User.objects.create_user(username, email, password)
        return redirect("index")

    else:
        return render(request, "register.html", locals())