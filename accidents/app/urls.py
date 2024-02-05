from django.urls import path
from .views import (
    AccidentsView,
    AccidentView,
    AccidentCategoryView,
    AccidentCategoryViewWithCrossFilters,
    AccidentGroupedByPercentageLocation,
    AccidentCategoryPercentageByLocation,
    AccidentGroupedCategoryByCumulative,
)

urlpatterns = [
    path("raw-data/", AccidentsView.as_view(), name="raw-data"),
    path("raw-data-entity/<int:id>", AccidentView.as_view(), name="raw-data-entity"),
    path(
        "accidents-by-category/<str:category>",
        AccidentCategoryView.as_view(),
        name="accidents-by-category",
    ),
    path(
        "accidents-by-category-cross-filters/<str:category>",
        AccidentCategoryViewWithCrossFilters.as_view(),
        name="accidents-by-category-cross-filters",
    ),
    path(
        "accidents-grouped-by-location-percentage/<str:category>",
        AccidentGroupedByPercentageLocation.as_view(),
        name="accidents-grouped-by-location",
    ),
    path(
        "accidents-category-percentage-by-location/<str:category>/<str:category_value>",
        AccidentCategoryPercentageByLocation.as_view(),
        name="accident-category-percentage-by-location",
    ),
    path(
        "accidents-grouped-category-by-cumulative/<str:category>",
        AccidentGroupedCategoryByCumulative.as_view(),
        name="accident-grouped-category-by-cumulative",
    ),
]
