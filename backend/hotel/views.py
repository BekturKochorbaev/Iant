from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import update_session_auth_hash

from .models import Hotel, Review, Booking
from .serializers import ChangePasswordSerializer, HotelListSerializers, HotelDetailSerializer, HotelCreateSerializers, \
    RoomCreateSerializers, ReviewSerializer, BookingSerializer


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'PUT':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers


class HotelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class HotelCreateAPIView(generics.CreateAPIView):
    serializer_class = HotelCreateSerializers


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomCreateSerializers


class ReviewCreateListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailUpdateDelteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        total_price = (serializer.validated_data['check_out_date'] - serializer.validated_data['check_in_date']).days \
                      * serializer.validated_data['room_book'].room_price
        serializer.save(total_price=total_price)



