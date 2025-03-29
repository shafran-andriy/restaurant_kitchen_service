from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_type/",
        DishTypeListView.as_view(),
        name="dish_type-list",
    ),
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create",
    ),
    path(
        "dish_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update",
    ),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete",
    ),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/",
         DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/",
         DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dish/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path(
        "cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path(
        "cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "kitchen_service"
