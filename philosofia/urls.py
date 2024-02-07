"""Urls configuration for the 'philosophies' app."""

from django.urls import path

from . import views



urlpatterns = [
    path("", views.home, name="medi-home"),
    path("meditations/<int:id>/", views.meditation, name="medi-meditation"),
]
