from django.urls import path

from . import views


app_name = 'thing'
urlpatterns = [
    path('', views.index, name='index'),
    path('thingy/<int:thingy_id>/', views.detail_thingy, name='detail_thingy'),
]