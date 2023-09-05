from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length = 250)
    movie_release = models.IntegerField()
    movie_description = models.TextField()
    movie_image = models.ImageField(upload_to= 'pics')

    def __str__(self):
        return self.movie_name
