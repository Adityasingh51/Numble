from django.shortcuts import render, get_object_or_404, redirect
from .models import Datasetmanager, Review 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def browse(request):
    query = request.GET.get('q') 
    if query:
        datasetList = Datasetmanager.objects.filter(name__icontains=query)  
    else:
        datasetList = Datasetmanager.objects.all() 
    return render(request, "browse.html", {"datasetList": datasetList})

def datasetDetails(request, dataset_id):
    dataset = get_object_or_404(Datasetmanager, id=dataset_id)
    context = {
        "dataset": dataset,
    }
    return render(request, "datasetDetails.html", context=context)

def submit_review(request, dataset_id):
    if request.method == "POST":
        dataset = get_object_or_404(Datasetmanager, id=dataset_id)
        rating = request.POST.get("rating")
        review_text = request.POST.get("review")

        Review.objects.create(
            dataset=dataset,
            rating=rating,
            text=review_text,
        )

        messages.success(request, "Your review has been submitted successfully!")

        
        return redirect("datasetDetails", dataset_id=dataset_id)
    else:
        
        return redirect("datasetDetails", dataset_id=dataset_id)

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
