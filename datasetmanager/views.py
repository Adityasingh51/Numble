from django.shortcuts import render, get_object_or_404, redirect
from .models import Datasetmanager, Review  # Import the Review model
from django.contrib import messages  # For user feedback

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

def submit_review(request, dataset_id):
    if request.method == "POST":
        dataset = get_object_or_404(Datasetmanager, id=dataset_id)
        rating = request.POST.get("rating")
        review_text = request.POST.get("review")

        # Save the review
        Review.objects.create(
            dataset=dataset,
            rating=rating,
            text=review_text,
        )

        # Add a success message
        messages.success(request, "Your review has been submitted successfully!")

        # Redirect back to the dataset details page
        return redirect("datasetDetails", dataset_id=dataset_id)
    else:
        # If the request is not POST, redirect to the dataset details page
        return redirect("datasetDetails", dataset_id=dataset_id)
