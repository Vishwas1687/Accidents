from django.urls import path
from .views import Index, IndexPage

urlpatterns = [
    path("raw-data/", Index.as_view(), name="index"),
    path("raw-data-entity/<int:id>", IndexPage.as_view(), name="index"),
]
