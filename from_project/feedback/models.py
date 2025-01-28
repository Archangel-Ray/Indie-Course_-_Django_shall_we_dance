from django.core.validators import MinLengthValidator
from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(5)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()
