from ast import literal_eval

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


def _helper_parse_dropped_ref(data):
    ref_objs = []
    for raw_ref_id in data:
        try:
            cleaned = int(raw_ref_id.split("_")[-1])
            ref = RefMaterial.objects.get(id=cleaned)
            ref_objs.append(ref)
        except:
            pass

    return ref_objs


def append_to_thing(request, thingy_id):
    if request.method == "POST":
        for k, v in request.POST.items():
            ref_ids = _helper_parse_dropped_ref(literal_eval(k))
            thingy = Thingy.objects.get(id=thingy_id)
            thingy.ref_materials.add(*ref_ids)

        return HttpResponseRedirect(reverse("thing:index"))

    return redirect("thing:index")


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


def view_thing(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    thingys = Thingy.objects.filter(thing=thing.id)
    print(thingys)
    context = {
        "thing": thing,
        'thingys': thingys
        }

    return render(request, "thing/view_thing.html", context)


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

            # return HttpResponseRedirect(reverse("thing:index"))
            return HttpResponseRedirect(f"/thing/{thing_id}/search/")

    return HttpResponseRedirect(reverse("thing:index"))


def delete_thing(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    thing.delete()

    return redirect("thing:index")


def delete_thingy(request, thingy_id):
    thingy = Thingy.objects.get(id=thingy_id)
    thingy.delete()

    return redirect("thing:index")

