from rest_framework import serializers

from .models import Category, Item, Contact, HomepageInfo, Event

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'

class HomepageInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomepageInfo
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
