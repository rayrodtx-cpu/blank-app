#!/usr/bin/env python3
"""
Generate 50,000+ real estate page titles for Austin, TX
Combines property features, neighborhoods, price ranges, and more
"""

# Austin neighborhoods and areas
neighborhoods = [
    "Downtown Austin", "West Lake Hills", "Tarrytown", "Clarksville", "Hyde Park",
    "Mueller", "East Austin", "South Congress", "Zilker", "Barton Hills",
    "Bouldin Creek", "Travis Heights", "Rosedale", "Allandale", "Crestview",
    "North Loop", "Cherrywood", "Windsor Park", "Georgian Acres", "Brentwood",
    "Pemberton Heights", "Old West Austin", "Rollingwood", "Steiner Ranch", "Circle C",
    "Avery Ranch", "Cedar Park", "Round Rock", "Pflugerville", "Manor",
    "Lakeway", "Bee Cave", "Dripping Springs", "Kyle", "Buda",
    "Sunset Valley", "Oak Hill", "Southwest Austin", "Northwest Austin", "North Austin",
    "South Austin", "East Side", "West Side", "Lake Travis", "Balcones",
    "Great Hills", "Jester", "Northwest Hills", "Williamson County", "Travis County",
    "Hays County", "Brushy Creek", "Wells Branch", "Anderson Mill", "Jollyville",
    "Onion Creek", "Shady Hollow", "Canyon Creek", "Barton Creek", "River Place",
    "Rob Roy", "Davenport Ranch", "Spanish Oaks", "Westbank", "Eanes",
    "Lost Creek", "Courtyard", "Cat Mountain", "Mesa Park", "Twin Creeks"
]

# Property types
property_types = [
    "Homes", "Houses", "Single Family Homes", "Condos", "Townhomes",
    "Luxury Homes", "Estate Homes", "Villas", "Patio Homes", "Ranch Homes",
    "Properties", "Residences", "Real Estate", "Listings", "Estates"
]

# Bedroom counts
bedrooms = [
    "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom",
    "6 Bedroom", "Studio", "1 Bed", "2 Bed", "3 Bed", "4 Bed", "5 Bed"
]

# Bathroom counts
bathrooms = [
    "1 Bath", "2 Bath", "3 Bath", "4 Bath", "5 Bath",
    "1.5 Bath", "2.5 Bath", "3.5 Bath", "1 Bathroom", "2 Bathroom"
]

# Features
features = [
    "with Pool", "with Pools", "with Swimming Pool", "with Private Pool",
    "with 2 Stories", "with Two Stories", "2 Story", "Two Story",
    "with 3 Stories", "Single Story", "One Story", "Ranch Style",
    "with Garage", "with 2 Car Garage", "with 3 Car Garage", "with Attached Garage",
    "with Backyard", "with Large Backyard", "with Fenced Yard", "with Large Lot",
    "with Acreage", "with Land", "on Large Lots", "with Big Yards",
    "with Hardwood Floors", "with Updated Kitchen", "with Modern Kitchen",
    "with Granite Countertops", "with Stainless Appliances", "with Island Kitchen",
    "with Master Suite", "with Walk-in Closets", "with En-Suite Bath",
    "with Home Office", "with Study", "with Bonus Room", "with Game Room",
    "with Media Room", "with Man Cave", "with She Shed", "with Guest House",
    "with Mother-in-Law Suite", "with Casita", "with ADU", "with Granny Flat",
    "with Lake View", "with Hill Country View", "with Water View", "with Greenbelt",
    "with Panoramic Views", "with Austin Skyline View", "with Golf Course View",
    "with Fireplace", "with Wood Burning Fireplace", "with Gas Fireplace",
    "with Covered Patio", "with Outdoor Kitchen", "with Deck", "with Balcony",
    "with Screened Porch", "with Front Porch", "with Wraparound Porch",
    "with Smart Home", "with Solar Panels", "with Energy Efficient", "with Green Features",
    "with New Construction", "Newly Built", "Brand New", "Custom Built",
    "with Granite", "with Marble", "with Quartz Counters", "with High Ceilings",
    "with Vaulted Ceilings", "with Open Floor Plan", "with Split Bedroom",
    "with RV Parking", "with Boat Parking", "with Workshop", "with Barn",
    "with Horse Property", "Equestrian", "with Stables", "on Cul-de-Sac",
    "Corner Lot", "with Privacy", "Gated Community", "in Golf Community",
    "Waterfront", "Lakefront", "on Lake Travis", "on Lake Austin",
    "Hill Country", "with Texas Hill Country", "with Live Oaks", "with Mature Trees",
    "Pet Friendly", "with Dog Park", "with Spa", "with Hot Tub",
    "with Wine Cellar", "with Library", "with Gym", "with Home Gym",
    "Move-in Ready", "Turnkey", "Renovated", "Recently Updated",
    "with Historic Charm", "Victorian", "Craftsman", "Mediterranean",
    "Contemporary", "Modern", "Mid-Century Modern", "Traditional",
    "Spanish Style", "Texas Ranch", "Tuscan", "Colonial"
]

# Price ranges
price_ranges = [
    "Under 200k", "Under 250k", "Under 300k", "Under 350k", "Under 400k",
    "Under 500k", "Under 600k", "Under 700k", "Under 800k", "Under 900k",
    "Under 1M", "Under 1.5M", "Under 2M", "Under 3M", "Under 5M",
    "200k-300k", "300k-400k", "400k-500k", "500k-600k", "600k-700k",
    "700k-800k", "800k-900k", "900k-1M", "1M-2M", "2M-3M", "3M-5M",
    "Affordable", "Budget Friendly", "Luxury", "High End", "Million Dollar"
]

# Square footage
sqft_ranges = [
    "Under 1000 Sq Ft", "Under 1500 Sq Ft", "Under 2000 Sq Ft", "Under 2500 Sq Ft",
    "Under 3000 Sq Ft", "Under 4000 Sq Ft", "Under 5000 Sq Ft",
    "1000-1500 Sq Ft", "1500-2000 Sq Ft", "2000-2500 Sq Ft", "2500-3000 Sq Ft",
    "3000-4000 Sq Ft", "4000-5000 Sq Ft", "Over 5000 Sq Ft"
]

# Additional modifiers
modifiers = [
    "for Sale", "for Sale by Owner", "New Listings", "Just Listed",
    "Open House", "Price Reduced", "Hot Listings", "Best Deals",
    "Investment Properties", "Fixer Upper", "Foreclosures", "Short Sale",
    "for First Time Buyers", "for Families", "for Retirees", "for Young Professionals",
    "Near Downtown", "Near UT Campus", "Near Domain", "Near Tech Companies",
    "in Good School District", "Top Rated Schools", "Near Parks",
    "Walkable Neighborhood", "Bike Friendly", "Near Trails", "Near Greenbelt"
]

# School districts
schools = [
    "in Austin ISD", "in Eanes ISD", "in Round Rock ISD", "in Pflugerville ISD",
    "in Leander ISD", "in Lake Travis ISD", "in Del Valle ISD", "in Manor ISD",
    "Near Top Rated Schools", "in Westlake Schools"
]

# Year built
year_ranges = [
    "Built 2020+", "Built 2015-2020", "Built 2010-2015", "Built 2000-2010",
    "New Construction 2024", "New Construction 2023", "Historic Homes"
]

# Generate comprehensive title combinations
titles = set()

# Basic neighborhood + property type combinations
for neighborhood in neighborhoods:
    for prop_type in property_types:
        titles.add(f"{prop_type} in {neighborhood}")
        titles.add(f"{neighborhood} {prop_type}")
        titles.add(f"{prop_type} for Sale in {neighborhood}")
        titles.add(f"Best {prop_type} in {neighborhood}")

        # Add bedroom combinations
        for bedroom in bedrooms:
            titles.add(f"{bedroom} {prop_type} in {neighborhood}")
            titles.add(f"{neighborhood} {bedroom} {prop_type}")
            titles.add(f"{bedroom} {prop_type} for Sale in {neighborhood}")

        # Add feature combinations
        for feature in features[:30]:  # Use subset to avoid too many combinations
            titles.add(f"{prop_type} {feature} in {neighborhood}")
            titles.add(f"{neighborhood} {prop_type} {feature}")

        # Add price range combinations
        for price in price_ranges[:15]:
            titles.add(f"{prop_type} in {neighborhood} {price}")
            titles.add(f"{neighborhood} {prop_type} {price}")

# Property type + feature combinations
for prop_type in property_types:
    for feature in features:
        titles.add(f"{prop_type} {feature} in Austin")
        titles.add(f"Austin {prop_type} {feature}")
        titles.add(f"{prop_type} {feature}")

        # Add price to features
        for price in price_ranges:
            titles.add(f"{prop_type} {feature} {price} in Austin")

        # Add bedrooms to features
        for bedroom in bedrooms:
            titles.add(f"{bedroom} {prop_type} {feature} in Austin")
            titles.add(f"{bedroom} {prop_type} {feature}")

# Bedroom + bathroom combinations
for bedroom in bedrooms:
    for bathroom in bathrooms:
        for prop_type in property_types:
            titles.add(f"{bedroom} {bathroom} {prop_type} in Austin")
            titles.add(f"{bedroom}/{bathroom} {prop_type} in Austin")

            # Add neighborhoods
            for neighborhood in neighborhoods[:30]:
                titles.add(f"{bedroom} {bathroom} {prop_type} in {neighborhood}")

# Feature combinations (2 features)
for i, feature1 in enumerate(features):
    for feature2 in features[i+1:i+20]:  # Limit combinations
        for prop_type in property_types[:5]:
            titles.add(f"{prop_type} {feature1} and {feature2} in Austin")
            titles.add(f"Austin {prop_type} {feature1} {feature2}")

# Price + bedroom combinations
for price in price_ranges:
    for bedroom in bedrooms:
        for prop_type in property_types:
            titles.add(f"{bedroom} {prop_type} {price} in Austin")
            titles.add(f"{bedroom} {prop_type} for Sale {price} in Austin")

# Square footage combinations
for sqft in sqft_ranges:
    for prop_type in property_types:
        titles.add(f"{prop_type} {sqft} in Austin")

        for neighborhood in neighborhoods[:20]:
            titles.add(f"{prop_type} {sqft} in {neighborhood}")

# School district combinations
for school in schools:
    for prop_type in property_types:
        titles.add(f"{prop_type} {school}")
        titles.add(f"{prop_type} for Sale {school}")

        for bedroom in bedrooms:
            titles.add(f"{bedroom} {prop_type} {school}")

# Modifier combinations
for modifier in modifiers:
    for prop_type in property_types:
        titles.add(f"{prop_type} {modifier} in Austin")
        titles.add(f"Austin {prop_type} {modifier}")

        for neighborhood in neighborhoods[:25]:
            titles.add(f"{prop_type} {modifier} in {neighborhood}")

# Year built combinations
for year in year_ranges:
    for prop_type in property_types:
        titles.add(f"{prop_type} {year} in Austin")

        for neighborhood in neighborhoods[:15]:
            titles.add(f"{prop_type} {year} in {neighborhood}")

# Triple combinations: neighborhood + bedroom + feature
for neighborhood in neighborhoods:
    for bedroom in bedrooms[:6]:
        for feature in features[:20]:
            titles.add(f"{bedroom} {feature} in {neighborhood}")

# Triple combinations: bedroom + price + neighborhood
for bedroom in bedrooms:
    for price in price_ranges[:10]:
        for neighborhood in neighborhoods[:20]:
            titles.add(f"{bedroom} Homes {price} in {neighborhood}")

# Luxury specific combinations
luxury_features = ["with Pool", "with 2 Stories", "with 3 Car Garage", "with Hill Country View",
                   "Waterfront", "with Guest House", "with Wine Cellar", "with Home Theater"]
for lux_feat in luxury_features:
    for neighborhood in neighborhoods:
        titles.add(f"Luxury Homes {lux_feat} in {neighborhood}")
        titles.add(f"Million Dollar Homes {lux_feat} in {neighborhood}")

# Specific popular combinations
popular_combos = [
    ("3 Bedroom", "2 Bath", "with Pool"),
    ("4 Bedroom", "3 Bath", "with 2 Stories"),
    ("5 Bedroom", "4 Bath", "with Pool"),
    ("3 Bedroom", "2 Bath", "Single Story"),
    ("4 Bedroom", "2.5 Bath", "with Garage"),
]

for bed, bath, feature in popular_combos:
    for neighborhood in neighborhoods:
        titles.add(f"{bed} {bath} Homes {feature} in {neighborhood}")
        titles.add(f"{bed}/{bath} {feature} {neighborhood}")

    for price in price_ranges:
        titles.add(f"{bed} {bath} Homes {feature} {price} Austin")

# Investment and special purpose
special_types = ["Investment", "Rental", "Vacation", "Second Home", "Starter Home",
                 "Forever Home", "Retirement", "Downsizing"]
for special in special_types:
    for prop_type in property_types[:5]:
        titles.add(f"{special} {prop_type} in Austin")

        for neighborhood in neighborhoods[:15]:
            titles.add(f"{special} {prop_type} in {neighborhood}")

# Lifestyle combinations
lifestyles = ["Family Friendly", "Urban Living", "Suburban", "Country Living",
              "Active Lifestyle", "Quiet Neighborhood", "Vibrant Community"]
for lifestyle in lifestyles:
    for prop_type in property_types[:5]:
        titles.add(f"{lifestyle} {prop_type} in Austin")

        for neighborhood in neighborhoods[:10]:
            titles.add(f"{lifestyle} {prop_type} in {neighborhood}")

# Commute-focused
commute_areas = ["Near Apple Campus", "Near Tesla", "Near Domain", "Near Downtown",
                 "Near Airport", "Near I-35", "Near Mopac", "Near 183"]
for commute in commute_areas:
    for prop_type in property_types[:5]:
        titles.add(f"{prop_type} {commute}")
        titles.add(f"{prop_type} for Sale {commute}")

# Convert set to sorted list
titles_list = sorted(list(titles))

# Save to file
output_file = "austin_real_estate_page_titles.txt"
with open(output_file, 'w') as f:
    for title in titles_list:
        f.write(f"{title}\n")

print(f"Generated {len(titles_list):,} unique page titles")
print(f"Saved to: {output_file}")

# Also create a CSV version with categorization
csv_file = "austin_real_estate_page_titles.csv"
with open(csv_file, 'w') as f:
    f.write("Page Title,Category,Target Keywords\n")

    for title in titles_list:
        # Determine category
        category = "General"
        if any(n in title for n in neighborhoods):
            category = "Neighborhood"
        if any(b in title for b in bedrooms):
            category = "Bedrooms"
        if any(p in title for p in price_ranges):
            category = "Price Range"
        if "Luxury" in title or "Million" in title:
            category = "Luxury"
        if any(f in title for f in ["Pool", "Stories", "Garage"]):
            category = "Features"

        # Extract keywords (simplified)
        keywords = title.lower().replace(" in ", ", ").replace(" for sale", "").replace(" and ", ", ")

        f.write(f'"{title}","{category}","{keywords}"\n')

print(f"CSV version saved to: {csv_file}")
print("\nSample titles:")
for i, title in enumerate(titles_list[:20]):
    print(f"  {i+1}. {title}")
print("  ...")
