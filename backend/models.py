from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    embedding = models.BinaryField(null=True, blank=True) # Embeddings as binary data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
