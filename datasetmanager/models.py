from django.db import models


class Datasetmanager(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='datasets/', default="")  # Supports image, video, or zipped datasets
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
    ])

    def __str__(self):
        return self.name


class Review(models.Model):
    dataset = models.ForeignKey(Datasetmanager, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.dataset.name} - {self.rating} Stars"
