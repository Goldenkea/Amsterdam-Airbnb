import pandas as pd
from geopy.distance import great_circle

df = pd.read_csv(r"C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amsterdam Airbnb\filtered_listings.csv")


#Applying distance to the dataframe
city_center = (52.374, 4.889)

def calculate_distance(row):
    return great_circle(city_center, (row['latitude'], row['longitude'])).kilometers
    #Haversine Formula

df['distance'] = df.apply(calculate_distance, axis=1)



#Propotion of airbnbs which are private rooms:
private_room_count = len(df[df['room_type'] == 'Private room'])
Apartment_room_count = len(df) - private_room_count
print(private_room_count)
print(Apartment_room_count)


#Average price for airbnb listings for different distance zones:
    #Zones: 0km - 2.5km, 2.5km - 5km, 5km - 7.5km, 7.5km - 10km, 10km - 12.5km
distance_ranges = [
    (0, 2.5),
    (2.5, 5),
    (5, 7.5),
    (7.5, 10),
    (10, 12.5)
]

average_prices = {}

for start, end in distance_ranges:
    filtered_df = df[(df['distance'] >= start) & (df['distance'] < end)]
    avg_price = filtered_df['price'].mean()
    average_prices[f"{start}-{end} km"] = avg_price

for distance_range, avg_price in average_prices.items():
    print(f"Average price for distance range {distance_range}: {avg_price:.2f}")



#Three closest listings to the city center:
closest_listings = df.nsmallest(3, 'distance')
print(closest_listings[['id', 'name', 'room_type', 'price', 'distance']])

apartment_counts = {}
