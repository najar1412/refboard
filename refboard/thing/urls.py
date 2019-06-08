from django.urls import path

from . import views


app_name = "thing"
urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:thing_id>/", views.delete_thing, name="delete_thing"),
    path("thingy/delete/<int:thingy_id>/", views.delete_thingy, name="delete_thingy"),
    path("<int:thing_id>/search/", views.detail_thing, name="detail_thing"),
    path("thingy/<int:thingy_id>/", views.detail_thingy, name="detail_thingy"),
    path("add/", views.add_thing, name="add_thing"),
    path("<int:thing_id>/thingy/add/", views.add_thingy, name="add_thingy"),
]
