import os

from django.shortcuts import render
from django.conf import settings

from .models import RefMaterial
from .modules import upload


def index(request):
    test_data = {"some": "data", "to": "test"}
    context = {"data_test": test_data}

    return render(request, "upload/index.html", context)


def file_upload(request):
    if request.method == "POST":
        mem_files = upload.fetch_files(request)
        for mem_file in mem_files:
            orig_name, renamed = upload.upload_to_server(mem_file)
            medium_size_name = upload.make_medium(settings.MEDIA_ROOT, renamed)
            thumb_name = upload.make_thumb(settings.MEDIA_ROOT, renamed)
            # TODO: upload files to online storage
            new_ref = RefMaterial(
                name=orig_name,
                filename=renamed,
                thumbnail=thumb_name,
                medium=medium_size_name,
            )
            new_ref.save()

    return render(request, "upload/index.html")
