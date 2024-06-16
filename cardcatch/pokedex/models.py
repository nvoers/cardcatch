from django.db import models


# Create your models here.
class Series(models.Model):
    """Series model."""

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Series"


class Set(models.Model):
    """Set model."""

    name = models.CharField(max_length=50)
    total_cards = models.IntegerField()
    release_date = models.DateField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    """Card model."""

    RARITIES = [
        ("regular", "Regular"),
        ("illustration_rare", "Illustration Rare"),
        ("special_illustration_rare", "Special Illustration Rare"),
        ("hyper_rare", "Hyper Rare"),
    ]

    name = models.CharField(max_length=50)
    reverse_holo = models.BooleanField(default=False)
    number = models.IntegerField()
    rarity = models.CharField(max_length=50, choices=RARITIES, default="regular")
    generation = models.PositiveSmallIntegerField()
    pokedex_number = models.IntegerField()
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
