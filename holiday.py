flight_prices = {
    "madrid": 129,
    "florida": 455,
    "cape town": 802,
    "london": 8
}
print(f"The avalible flight destinations are:")
for city in flight_prices:
    print("-", city)

while True:
    city_flight = input("Enter the city you want to fly to:").lower()
    if city_flight in flight_prices:
        break
    else:
        print("Sorry, that city is not avalible.")


num_nights = int(input("How many nights will you be staying in a hotel?"))
print(f"You will be staying in your hotel for {num_nights} nights.")

rental_days = int(input("How many days will you be hiring a car for?"))
print(f"You will be hiring a car for {rental_days} days.")

def plane_cost(city):
    return flight_prices[city]
    
def hotel_cost(nights, rate = 150):
    return nights * rate

def car_rental(days, rate=50):
    return days * rate


def holiday_cost(city, nights, days):
    flight = plane_cost(city)
    hotel = hotel_cost(nights)
    car = car_rental(days)

    total = flight + hotel + car
    print(f"\n### COST BREAKDOWN###")
    print(f"Flight cost: £{flight}")
    print(f"Hotel cost: £{hotel}")
    print(f"Car rental cost £{car}")
    print(f" Total holidat cost: £{total}")

    return total

holiday_cost(city_flight, num_nights, rental_days)