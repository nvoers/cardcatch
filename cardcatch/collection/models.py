from django.db import models
from django.contrib.auth.models import User
from pokedex.models import Card


# Create your models here.
class Entry(models.Model):
    """Entry model."""

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card.__str__()

    class Meta:
        verbose_name_plural = "Entries"


class Collection(models.Model):
    """Collection model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "'s collection"
