# path is a function that connects an HTTP endpoint to a view
from django.urls import path

from . import views

# different HTTP endpoints and what view they are connected to
urlpatterns = [
    path("", views.index, name="index"),
]