from django.urls import path
from .views import form_page, submit_form

urlpatterns = [
    path("submit_form/", submit_form, name="submit_form"),
    path("", form_page, name="form_page"),
]