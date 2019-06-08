from django.shortcuts import render

from .models import RefMaterial


def index(request):
    all_refs = RefMaterial.objects.all()
    context = {'ref_materials': all_refs}

    return render(request, 'search/index.html', context)


def detail(request, ref_material_id):
    ref_material = RefMaterial.objects.get(id=ref_material_id)
    context = {'ref_material': ref_material}

    return render(request, 'search/detail.html', context)