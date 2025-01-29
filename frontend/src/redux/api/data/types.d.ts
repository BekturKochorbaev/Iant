namespace HOTELS {
  interface hotel_list {
    id?: string;
    name_hotel: string;
    country: string;
    city: string;
    images: string[];
    rating: string;
    count_review: string;
  }

  type GetHotelListResponse = IOlympian[];
  type GetHotelListRequest = void;
}
