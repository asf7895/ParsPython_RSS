from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("del11/", views.del11, name="del11"),
    path("pars11/", views.pars11, name="pars11"),
    path("news1/<int:page1>/", views.news1, name="news1"),
    path("initdb/", views.initdb, name="initdb"),
    path("categ1/", views.categ1, name="categ1"),
    path("canal1/", views.canal1, name="canal1"),
    path("", views.index, name="index"),
]