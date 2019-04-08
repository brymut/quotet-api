from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Category, Item, Contact, HomepageInfo, Event
from  .serializers import ItemSerializer, CategorySerializer, HomepageInfoSerializer, EventSerializer, ContactSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryItemList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Item.objects.filter(category=self.kwargs["pk"])
        return queryset
    serializer_class = ItemSerializer


