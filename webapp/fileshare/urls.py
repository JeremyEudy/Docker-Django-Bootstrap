from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileshareView.as_view(), name="fileshare"),
    path('download', views.FileshareView.as_view(), name="download"),
    path('resources', views.FileshareView.as_view(), name="resources"),
    path('upload', views.FileshareView.as_view(), name="upload"),
    path('webroot', views.FileshareView.as_view(), name="webroot"),
]
