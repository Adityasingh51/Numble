<<<<<<< HEAD
from django.shortcuts import render , get_object_or_404
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> 60dd21c2f6e693e0cd8e4df3abaa91bb346f1051
from .models import Datasetmanager

# Create your views here.
def browse(request):
<<<<<<< HEAD
    datasetmanagerlist = datasetmanager.objects.all()
    print(datasetmanagerlist)
    context = {
        'datasetmanagerList': datasetmanagerlist,
    }
    return render(request,"browse.html",context)

def datasetDetails(request, datasetmanager_id):

    datasetmanager = get_object_or_404(datasetmanager, id=datasetmanager_id)
    context = {
        "datasetmanager": datasetmanager,
    }

    return render(request,"datasetDetails.html",context=context)
=======
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
>>>>>>> 60dd21c2f6e693e0cd8e4df3abaa91bb346f1051
