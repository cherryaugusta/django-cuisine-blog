from django.urls import path
from .views import CuisineListView, CuisineDetailView, cuisine_list_fbv

app_name = "cuisine"

urlpatterns = [
    path("fbv/", cuisine_list_fbv, name="cuisine_list_fbv"),
    path("", CuisineListView.as_view(), name="cuisine_list"),
    path("<slug:slug>/", CuisineDetailView.as_view(), name="cuisine_detail"),
]
