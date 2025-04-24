from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import browse, datasetDetails

urlpatterns = [
    
<<<<<<< HEAD
    path("browse/",browse,name="browse"),
    path("view-datails/<int:product_id>", datasetDetails, name="datasetDetails")
=======
    path("browse/", browse, name="browse"),
    path("view-details/<int:dataset_id>", datasetDetails, name="datasetDetails"),
>>>>>>> 60dd21c2f6e693e0cd8e4df3abaa91bb346f1051
   
]