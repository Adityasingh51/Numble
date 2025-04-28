from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import browse, datasetDetails

urlpatterns = [
    path("browse/", browse, name="browse"),
    path("view-details/<int:dataset_id>", datasetDetails, name="datasetDetails"),
]