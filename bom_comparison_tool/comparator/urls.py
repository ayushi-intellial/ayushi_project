from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_view, name="upload"),
    path("download/json/", views.download_json, name="download_json"),
    path("download/excel/", views.download_excel, name="download_excel"),
]
