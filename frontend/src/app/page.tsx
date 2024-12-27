"use client";
import { useGetHotelListQuery } from "@/redux/api/data";
import React from "react";
import styles from "./page.module.scss";
import { Star } from "lucide-react";
import Image from "next/image";

const Page = () => {
  const { data } = useGetHotelListQuery();
  console.log(data, "data");

  const defaultImage = "/api/placeholder/300/200";

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Hotels</h1>
      <div className={styles.hotelGrid}>
        {data?.map((hotel, index) => (
          <div key={index} className={styles.hotelCard}>
            <div className={styles.imageContainer}>
              {hotel.hotel_images?.length > 0 ? (
                <Image
                  src={hotel.hotel_images[0].image} // Changed this line to access image property
                  alt={hotel.name_hotel}
                  width={700}
                  height={500}
                  className={styles.hotelImage}
                />
              ) : (
                <Image
                  src={defaultImage}
                  alt="default hotel image"
                  width={700}
                  height={500}
                  className={styles.hotelImage}
                />
              )}
            </div>
            <div className={styles.hotelInfo}>
              <h2 className={styles.hotelName}>{hotel.name_hotel}</h2>
              <p className={styles.location}>
                {hotel.city}, {hotel.country}
              </p>
              <div className={styles.ratingContainer}>
                <div className={styles.stars}>
                  {[...Array(hotel.start)].map((_, i) => (
                    <Star
                      key={i}
                      size={20}
                      className={styles.star}
                      fill="#FFD700"
                      color="#FFD700"
                    />
                  ))}
                </div>
                <span className={styles.rating}>
                  Rating: {hotel.rating}/5 ({hotel.count_review} reviews)
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Page;
