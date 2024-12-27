from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name_hotel', 'address', 'hotel_description', 'city', 'country')