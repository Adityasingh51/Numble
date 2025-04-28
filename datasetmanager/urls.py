from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import browse, datasetDetails, submit_review  # Import the new view

urlpatterns = [
    path("browse/", browse, name="browse"),
    path("view-details/<int:dataset_id>", datasetDetails, name="datasetDetails"),
    path("submit-review/<int:dataset_id>/", submit_review, name="submit_review"),  # Add this line
]