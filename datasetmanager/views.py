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

# For Search Functionality
def browse(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        datasetList = Datasetmanager.objects.filter(name__icontains=query)  # Filter datasets by name
    else:
        datasetList = Datasetmanager.objects.all()  # Show all datasets if no query
    return render(request, "browse.html", {"datasetList": datasetList})

def datasetDetails(request, dataset_id):
    dataset = get_object_or_404(Datasetmanager, id=dataset_id)
    context = {
        "dataset": dataset,
    }
    return render(request, "datasetDetails.html", context=context)
