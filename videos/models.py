from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Video(models.Model):
    GENRE_CHOICES = [
        ("Comedy", "Comedy"),
        ("Romance", "Romance"),
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Sci-Fi", "Sci-Fi"),
        ("Animation", "Animation"),
        ("Other", "Other"),
    ]
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=120)
    Actor1Name = models.CharField(max_length=120)
    Actor2Name = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120)
    MovieGenre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(datetime.date.today().year)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
