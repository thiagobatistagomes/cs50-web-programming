from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("thiago", views.thiago, name="thiago"),
    path("jhonson", views.jhonson, name="jhonson")
]