from rest_framework import serializers
from .models import FitnessClass, Booking

#serializer for model classes
class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

#serializer for model bookings
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
