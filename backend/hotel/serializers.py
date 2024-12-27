from rest_framework import serializers
from .import models
from .models import (UserProfile, RoomImage, Hotel, Room,
                     HotelImage, Review, Booking)
from django.db.models import Avg


class ChangePasswordSerializer(serializers.Serializer):
    model = UserProfile
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['image']


class RoomSerializer(serializers.ModelSerializer):
    hotell_room = serializers.SlugRelatedField(
        slug_field='name_hotel',
        queryset=Hotel.objects.all()
    )
    photos = RoomImageSerializer(source='room_images', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_description', 'photos', 'hotell_room',
                  'room_types', 'room_status', 'room_price', 'all_inclusive']


class RoomCreateSerializers(serializers.ModelSerializer):
    hotell_room = serializers.SlugRelatedField(
        slug_field='name_hotel',
        queryset=Hotel.objects.all()
    )
    photos = RoomImageSerializer(source='room_images', many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_description', 'photos', 'hotell_room',
                  'room_types', 'room_status', 'room_price', 'all_inclusive']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['image']


class HotelListSerializers(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['name_hotel', 'country', 'city', 'hotel_images', 'start', 'rating', 'count_review']

    def get_rating(self, obj):
        return obj.reviews.aggregate(avg_stars=Avg('stars'))['avg_stars'] or 0

    def get_count_review(self, obj):
        return obj.get_count_review()


class HotelCreateSerializers(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['name_hotel', 'hotel_description', 'hotel_images', 'country', 'city', 'hotel_images', 'owner', 'hotel_video', 'start', 'rating']


class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()


    class Meta:
        model = Hotel
        fields = ['name_hotel', 'country', 'city', 'hotel_images', 'start', 'rating', 'rooms']

    def get_rating(self, obj):
        return obj.reviews.aggregate(avg_stars=Avg('stars'))['avg_stars'] or 0


class ReviewSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(),
        required=False,
        allow_null=True
    )
    user_name = serializers.SlugRelatedField(
        slug_field='username',
        queryset=UserProfile.objects.all()
    )
    hotel = serializers.SlugRelatedField(
        slug_field='name_hotel',
        queryset=Hotel.objects.all()
    )

    class Meta:
        model = Review
        fields = ['user_name', 'hotel', 'text', 'stars', 'parent']


class BookingSerializer(serializers.ModelSerializer):
    hotel_book = serializers.SlugRelatedField(
        slug_field='name_hotel',
        queryset=Hotel.objects.all()
    )
    room_book = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all()
    )
    user_book = serializers.SlugRelatedField(
        slug_field='username',
        queryset=UserProfile.objects.all()
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['hotel_book', 'room_book', 'user_book', 'check_in_date',
                  'check_out_date', 'total_price', 'status_book']

    def get_total_price(self, obj):
        return (obj.check_out_date - obj.check_in_date).days * obj.room_book.room_price

    def validate(self, data):
        room = data.get('room_book')
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        conflicting_bookings = Booking.objects.filter(
            room_book=room,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date,
            status_book__in=['Бронь', 'подверждено']
        )
        if conflicting_bookings.exists():
            raise serializers.ValidationError('Комната уже забронирована на выбранные даты.')
        return data


