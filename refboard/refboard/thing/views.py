from django.shortcuts import render

from .models import Thing, Thingy

# from .models import Question


def index(request):
    all_the_things = Thing.objects.all()
    context = {'things': all_the_things}

    return render(request, 'thing/index.html', context)

def detail_thingy(request, thingy_id):
    thingy = Thingy.objects.get(id=thingy_id)
    context = {'thingy': thingy}

    return render(request, 'thing/detail_thingy.html', context)