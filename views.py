from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.shortcuts import get_object_or_404

#function-based api for 'GET' request for classes
@api_view(['GET'])
def class_list(request):
    #list all available fitness classes
    classes = FitnessClass.objects.all()
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

#view function to accept POST request for bookings
@api_view(['POST'])
def book_class(request):
    #booking a class, assuming the class has available slots
    class_id = request.data.get('fitness_class')
    name = request.data.get('client_name')
    email = request.data.get('client_email')

    #make sure of all required fields
    if not all([class_id, name, email]):
        return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

    #this should raise 404 if class doesn't exist
    fitness_class = get_object_or_404(FitnessClass, id=class_id)

    if fitness_class.available_slots <= 0:
        return Response({"error": "No slots available"}, status=status.HTTP_400_BAD_REQUEST)

    
    fitness_class.available_slots -= 1
    fitness_class.save()

    #save the booking 
    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=name,
        client_email=email
    )
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

#view function to accept GET request for bookings
@api_view(['GET'])
def booking_list(request):
    email = request.query_params.get('email')
    if not email:
        return Response({"error": "Email query param required"}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
