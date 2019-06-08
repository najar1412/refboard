from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Thing, Thingy, RefMaterial
from .forms import NewThingForm, NewThingyForm


def index(request):
    all_the_things = Thing.objects.all().order_by("-init_date")
    new_thing_form = NewThingForm()
    new_thingy_form = NewThingyForm()

    context = {
        "things": all_the_things,
        "new_thing_form": new_thing_form,
        "new_thingy_form": new_thingy_form,
    }

    return render(request, "thing/index.html", context)


def detail_thing(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    new_thingy_form = NewThingyForm()
    all_refs = RefMaterial.objects.all()
    context = {
        "thing": thing,
        "ref_materials": all_refs,
        "new_thingy_form": new_thingy_form,
    }

    return render(request, "search/index.html", context)


def detail_thingy(request, thingy_id):
    thingy = Thingy.objects.get(id=thingy_id)
    context = {"thingy": thingy}

    return render(request, "thing/detail_thingy.html", context)


def add_thing(request):
    # TODO: add user validation
    if request.method == "POST":
        form = NewThingForm(request.POST)
        if form.is_valid():
            new_thing = Thing(name=form.cleaned_data["thing_name"])
            new_thing.save()

            return HttpResponseRedirect(reverse("thing:index"))

    return redirect("thing:index")


def add_thingy(request, thing_id):
    # TODO: add user validation
    if request.method == "POST":
        form = NewThingyForm(request.POST)
        if form.is_valid():
            new_thingy = Thingy(name=form.cleaned_data["thingy_name"])
            new_thingy.thing = Thing.objects.get(id=thing_id)
            new_thingy.save()

            return HttpResponseRedirect(reverse("thing:index"))

    return redirect("thing:index")


def delete_thing(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    thing.delete()

    return redirect("thing:index")


def delete_thingy(request, thingy_id):
    thingy = Thingy.objects.get(id=thingy_id)
    thingy.delete()

    return redirect("thing:index")

