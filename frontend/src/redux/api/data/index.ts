import { api as index } from "..";

const ENDPOINTS = process.env.NEXT_PUBLIC_ENDPOINT || "default_endpoint_here"; // Optional fallback

const api = index.injectEndpoints({
  endpoints: (build) => ({
    getHotelList: build.query<
      HOTELS.GetHotelListResponse,
      HOTELS.GetHotelListRequest
    >({
      query: () => ({
        url: `${ENDPOINTS}/hotel_list`,
        method: "GET",
      }),
      providesTags: ["data"],
    }),
  }),
});

export const { useGetHotelListQuery } = api;
