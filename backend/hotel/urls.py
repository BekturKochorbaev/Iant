from django.urls import path, include


from .views import change_password, HotelListAPIView, HotelDetailAPIView, \
    HotelCreateAPIView, RoomCreateAPIView, ReviewCreateListAPIView, ReviewDetailDeleteView, BookingListCreateAPIView, \
    BookingDetailUpdateDelteAPIView

urlpatterns = [
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


    path('hotel_list/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel_list/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('hotel_create', HotelCreateAPIView .as_view(), name='hotel_create'),

    path('room_create/', RoomCreateAPIView.as_view(), name='room_create'),

    path('review_create/', ReviewCreateListAPIView.as_view(), name='review_create'),
    path('review_create/<int:pk>/', ReviewDetailDeleteView.as_view(), name='review_detail_delete'),

    path('booking/', BookingListCreateAPIView.as_view(), name='booking_create'),
    path('booking/<int:pk>/', BookingDetailUpdateDelteAPIView.as_view(), name='booking_detail'),
]