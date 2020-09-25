from django.contrib import admin
from .models import Link, Click
# Register your models here.
class ClickInline(admin.TabularInline):
    model = Click

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    inlines = [
        ClickInline
    ]

