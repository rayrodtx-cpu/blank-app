#!/usr/bin/env python3
"""
Generate 50,000+ real estate page titles for Houston
Combines various property attributes to create unique page titles
"""

import itertools
import csv

# Property types
property_types = [
    "Homes", "Houses", "Properties", "Residences", "Real Estate",
    "Condos", "Townhomes", "Townhouses", "Estates", "Villas"
]

# Bedrooms
bedrooms = ["1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom", "6+ Bedroom"]

# Bathrooms
bathrooms = ["1 Bathroom", "2 Bathroom", "3 Bathroom", "4 Bathroom", "5+ Bathroom"]

# Stories
stories = ["Single Story", "2 Story", "3 Story", "Multi-Story"]

# Primary features
primary_features = [
    "with Pool", "with Pools", "with Swimming Pool",
    "with Garage", "with 2 Car Garage", "with 3 Car Garage",
    "with Backyard", "with Large Yard", "with Fenced Yard",
    "with Patio", "with Deck", "with Balcony",
    "with Fireplace", "with Master Suite", "with Walk-in Closet",
    "with Hardwood Floors", "with Granite Countertops",
    "with Stainless Steel Appliances", "with Updated Kitchen",
    "with Open Floor Plan", "with High Ceilings",
    "with Game Room", "with Media Room", "with Study",
    "with Home Office", "with Gym", "with Workshop"
]

# Secondary features
secondary_features = [
    "Gated Community", "Golf Course View", "Lake View", "Water View",
    "Corner Lot", "Cul-de-sac", "New Construction", "Recently Renovated",
    "Move-in Ready", "Fixer Upper", "Investment Property",
    "Energy Efficient", "Smart Home", "Solar Panels",
    "RV Parking", "Boat Parking", "Covered Parking"
]

# Houston neighborhoods (major areas)
houston_areas = [
    "Houston", "Downtown Houston", "Midtown Houston", "Uptown Houston",
    "The Heights", "Montrose", "River Oaks", "Memorial", "Galleria",
    "Katy", "Sugar Land", "The Woodlands", "Pearland", "Cypress",
    "Spring", "Humble", "Kingwood", "Clear Lake", "Friendswood",
    "Missouri City", "Stafford", "Richmond", "Rosenberg",
    "Bellaire", "West University", "Medical Center", "Meyerland",
    "Sharpstown", "Alief", "Greenspoint", "Energy Corridor",
    "Cinco Ranch", "Sienna Plantation", "Bridgeland", "Elyson",
    "League City", "Webster", "Pasadena", "Baytown", "Conroe"
]

# Price ranges
price_ranges = [
    "Under $200K", "Under $250K", "Under $300K", "Under $400K", "Under $500K",
    "$200K-$300K", "$300K-$400K", "$400K-$500K", "$500K-$750K", "$750K-$1M",
    "Over $500K", "Over $750K", "Over $1M", "Luxury", "Affordable"
]

# Square footage
sqft_ranges = [
    "Under 1500 Sqft", "1500-2000 Sqft", "2000-2500 Sqft", "2500-3000 Sqft",
    "3000-4000 Sqft", "Over 3000 Sqft", "Over 4000 Sqft"
]

# Architectural styles
styles = [
    "Traditional", "Modern", "Contemporary", "Ranch Style", "Craftsman",
    "Colonial", "Mediterranean", "Victorian", "Farmhouse", "Cottage"
]

# Time-based qualifiers
time_qualifiers = [
    "For Sale", "For Rent", "For Lease", "Available Now", "Coming Soon",
    "New Listings", "Just Listed", "Recently Listed", "Price Reduced"
]

# Special categories
special_categories = [
    "Pet Friendly", "Senior Living", "Family Friendly", "First Time Buyer",
    "Foreclosure", "Short Sale", "Estate Sale", "Waterfront",
    "Equestrian", "Farm", "Ranch Land"
]

def generate_titles():
    """Generate all combinations of real estate page titles"""
    titles = set()

    # Pattern 1: [Bedrooms] [Property Type] in [Area]
    for bedrooms_val, prop_type, area in itertools.product(bedrooms, property_types, houston_areas):
        titles.add(f"{bedrooms_val} {prop_type} in {area}")

    # Pattern 2: [Bedrooms] [Bathrooms] [Property Type] in [Area]
    for bedrooms_val, bathrooms_val, prop_type, area in itertools.product(bedrooms, bathrooms, property_types, houston_areas):
        titles.add(f"{bedrooms_val} {bathrooms_val} {prop_type} in {area}")

    # Pattern 3: [Stories] [Property Type] in [Area]
    for story, prop_type, area in itertools.product(stories, property_types, houston_areas):
        titles.add(f"{story} {prop_type} in {area}")

    # Pattern 4: [Property Type] [Primary Feature] in [Area]
    for prop_type, feature, area in itertools.product(property_types, primary_features, houston_areas):
        titles.add(f"{prop_type} {feature} in {area}")

    # Pattern 5: [Bedrooms] [Property Type] [Primary Feature] in [Area]
    for bedrooms_val, prop_type, feature, area in itertools.product(bedrooms, property_types, primary_features, houston_areas):
        titles.add(f"{bedrooms_val} {prop_type} {feature} in {area}")

    # Pattern 6: [Stories] [Property Type] [Primary Feature] in [Area]
    for story, prop_type, feature, area in itertools.product(stories, property_types, primary_features, houston_areas):
        titles.add(f"{story} {prop_type} {feature} in {area}")

    # Pattern 7: [Price Range] [Property Type] in [Area]
    for price, prop_type, area in itertools.product(price_ranges, property_types, houston_areas):
        titles.add(f"{price} {prop_type} in {area}")

    # Pattern 8: [Style] [Property Type] in [Area]
    for style, prop_type, area in itertools.product(styles, property_types, houston_areas):
        titles.add(f"{style} {prop_type} in {area}")

    # Pattern 9: [Bedrooms] [Bathrooms] [Property Type] [Primary Feature] in [Area]
    for bedrooms_val, bathrooms_val, prop_type, feature, area in itertools.product(bedrooms, bathrooms, property_types, primary_features[:10], houston_areas[:20]):
        titles.add(f"{bedrooms_val} {bathrooms_val} {prop_type} {feature} in {area}")

    # Pattern 10: [Property Type] in [Secondary Feature] in [Area]
    for prop_type, sec_feature, area in itertools.product(property_types, secondary_features, houston_areas):
        titles.add(f"{prop_type} in {sec_feature} in {area}")

    # Pattern 11: [Sqft] [Property Type] in [Area]
    for sqft, prop_type, area in itertools.product(sqft_ranges, property_types, houston_areas):
        titles.add(f"{sqft} {prop_type} in {area}")

    # Pattern 12: [Bedrooms] [Price Range] [Property Type] in [Area]
    for bedrooms_val, price, prop_type, area in itertools.product(bedrooms, price_ranges, property_types, houston_areas[:20]):
        titles.add(f"{bedrooms_val} {price} {prop_type} in {area}")

    # Pattern 13: [Time Qualifier] [Property Type] in [Area]
    for qualifier, prop_type, area in itertools.product(time_qualifiers, property_types, houston_areas):
        titles.add(f"{qualifier}: {prop_type} in {area}")

    # Pattern 14: [Special Category] [Property Type] in [Area]
    for category, prop_type, area in itertools.product(special_categories, property_types, houston_areas):
        titles.add(f"{category} {prop_type} in {area}")

    # Pattern 15: [Style] [Bedrooms] [Property Type] in [Area]
    for style, bedrooms_val, prop_type, area in itertools.product(styles, bedrooms, property_types, houston_areas[:20]):
        titles.add(f"{style} {bedrooms_val} {prop_type} in {area}")

    # Pattern 16: [Price Range] [Bedrooms] [Property Type] [Primary Feature] in [Area]
    for price, bedrooms_val, prop_type, feature, area in itertools.product(price_ranges[:5], bedrooms, property_types, primary_features[:8], houston_areas[:15]):
        titles.add(f"{price} {bedrooms_val} {prop_type} {feature} in {area}")

    # Pattern 17: [Stories] [Bedrooms] [Property Type] in [Area]
    for story, bedrooms_val, prop_type, area in itertools.product(stories, bedrooms, property_types, houston_areas):
        titles.add(f"{story} {bedrooms_val} {prop_type} in {area}")

    # Pattern 18: [Property Type] [Primary Feature] [Price Range] in [Area]
    for prop_type, feature, price, area in itertools.product(property_types, primary_features[:10], price_ranges, houston_areas[:15]):
        titles.add(f"{prop_type} {feature} {price} in {area}")

    # Pattern 19: [Sqft] [Bedrooms] [Property Type] in [Area]
    for sqft, bedrooms_val, prop_type, area in itertools.product(sqft_ranges, bedrooms, property_types, houston_areas[:20]):
        titles.add(f"{sqft} {bedrooms_val} {prop_type} in {area}")

    # Pattern 20: [Style] [Property Type] [Primary Feature] in [Area]
    for style, prop_type, feature, area in itertools.product(styles, property_types, primary_features[:12], houston_areas[:18]):
        titles.add(f"{style} {prop_type} {feature} in {area}")

    return sorted(titles)

def save_to_csv(titles, filename='houston_real_estate_page_titles.csv'):
    """Save titles to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Page Title', 'URL Slug'])
        for title in titles:
            url_slug = title.lower().replace(' ', '-').replace(':', '').replace('$', '').replace('+', 'plus').replace(',', '')
            writer.writerow([title, url_slug])

def save_to_txt(titles, filename='houston_real_estate_page_titles.txt'):
    """Save titles to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')

if __name__ == '__main__':
    print("Generating Houston real estate page titles...")
    titles = generate_titles()

    print(f"\nGenerated {len(titles):,} unique page titles!")

    # Save to both CSV and TXT
    print("\nSaving to CSV...")
    save_to_csv(titles)

    print("Saving to TXT...")
    save_to_txt(titles)

    print("\nFiles created:")
    print("  - houston_real_estate_page_titles.csv (with URL slugs)")
    print("  - houston_real_estate_page_titles.txt")

    print("\nSample titles:")
    for i, title in enumerate(titles[:20], 1):
        print(f"  {i}. {title}")

    print(f"\n... and {len(titles) - 20:,} more!")
