from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Thing, Thingy

# from .models import Question


def index(request):
    all_the_things = Thing.objects.all()
    context = {"things": all_the_things}

    return render(request, "thing/index.html", context)


def detail_thingy(request, thingy_id):
    thingy = Thingy.objects.get(id=thingy_id)
    context = {"thingy": thingy}

    return render(request, "thing/detail_thingy.html", context)


def add_thing(request):
    # TODO: validate form and add to database
    print(request.POST["thing_name"])

    return HttpResponseRedirect(reverse("thing:index"))
