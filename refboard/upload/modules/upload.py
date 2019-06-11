import secrets
import os
from PIL import Image, ImageOps

from django.core.files.storage import default_storage


def _rename_file(filename):
    name, ext = os.path.splitext(filename)

    if ext == ".jpeg":
        ext = ".jpg"
    else:
        pass

    token = secrets.token_urlsafe(6)

    return f"{name}_{token}{ext}"


def fetch_files(request):
    inMemFiles = []
    for k, v in request.FILES.items():
        inMemFiles.append(request.FILES[k])

    return inMemFiles


def upload_to_server(memory_file):
    renamed = _rename_file(memory_file.name)
    file_obj = memory_file

    with default_storage.open(renamed, "wb+") as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return (memory_file.name, renamed)


def make_medium(location, filename):
    name, ext = os.path.splitext(filename)
    med_name = f"{name}_med{ext}"

    basewidth = 500
    img = Image.open(os.path.join(location, filename))

    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))

    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(os.path.join(location, med_name), format="JPEG")

    return med_name


def make_thumb(location, filename):
    name, ext = os.path.splitext(filename)
    thumb_name = f"{name}_thumb{ext}"

    im = Image.open(os.path.join(location, filename))
    size = (100, 100)
    thumb = ImageOps.fit(im, size, Image.LANCZOS)

    thumb.save(os.path.join(location, thumb_name), format="JPEG")

    return thumb_name

