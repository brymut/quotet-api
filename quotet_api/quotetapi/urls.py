from django.urls import path

from .apiviews import ItemList, ItemDetail, EventList, EventDetail, CategoryList, CategoryItemList

urlpatterns = [
    path("items/", ItemList.as_view(), name="items_list"),
    path("items/<int:pk>/", ItemDetail.as_view(), name="items_detail"),
    path("events/", EventList.as_view(), name="events_list"),
    path("events/<int:pk>/", EventDetail.as_view(), name="events_detail"),
    path("categories/", CategoryList.as_view(), name="categories_list"),
    path("categories/<int:pk>/items/", CategoryItemList.as_view(), name="category_items_list")

]