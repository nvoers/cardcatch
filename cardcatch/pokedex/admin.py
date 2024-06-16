from django.contrib import admin
from .models import Series, Set, Card


# Register your models here.
@admin.register(Series)
class PokedexAdmin(admin.ModelAdmin):
    """Pokedex admin."""

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    """Set admin."""

    list_display = ("name", "total_cards", "release_date", "series")
    search_fields = ("name",)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Card admin."""

    list_display = (
        "name",
        "number",
        "rarity",
        "set",
    )
    search_fields = ("name",)
