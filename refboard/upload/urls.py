from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("file-upload/", views.file_upload, name="file_upload"),
]
