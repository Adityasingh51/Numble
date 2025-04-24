from django.shortcuts import render, get_object_or_404
from .models import Datasetmanager

# Create your views here.
def browse(request):
    datasetList = Datasetmanager.objects.all()
    print('datasetList')  # Uncomment for debugging if needed
    context = {
        'datasetList': datasetList,
    }
    return render(request, "browse.html", context)

def datasetDetails(request, dataset_id):
    dataset = get_object_or_404(Datasetmanager, id=dataset_id)
    context = {
        "dataset": dataset,
    }
    return render(request, "datasetDetails.html", context=context)
