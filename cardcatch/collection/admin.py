from django.contrib import admin
from .models import Collection, Entry


# Register your models here.
class EntryInline(admin.TabularInline):
    """Entry inline."""

    model = Entry


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Collection admin."""

    list_display = ("user",)
    search_fields = ("user",)

    inlines = [
        EntryInline,
    ]


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """Entry admin."""

    list_display = ("collection", "card")
    search_fields = ("collection",)
