from django.shortcuts import render , get_object_or_404
from .models import Datasetmanager

# Create your views here.
def browse(request):
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
