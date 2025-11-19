#!/usr/bin/env python3
"""
Real Estate Page Title Generator for McAllen Valley Area, Texas
Generates 50,000+ unique page titles for SEO optimization
"""

import itertools
import json
from typing import List, Set

# Valley area cities and neighborhoods
CITIES = [
    "McAllen", "Edinburg", "Mission", "Pharr", "Weslaco", "Donna", "Alamo",
    "San Juan", "Mercedes", "La Joya", "Palmview", "Hidalgo", "Elsa",
    "Progreso", "Penitas", "Sullivan City", "Granjeno", "Palmhurst",
    "Alton", "Lopezville", "Muniz", "Doffing", "Hargill", "Linn",
    "North McAllen", "South McAllen", "West McAllen", "East McAllen",
    "Downtown McAllen", "North Edinburg", "West Edinburg", "East Mission"
]

# Property types
PROPERTY_TYPES = [
    "Homes", "Houses", "Properties", "Residences", "Real Estate",
    "Single Family Homes", "Family Homes", "Condos", "Condominiums",
    "Townhomes", "Townhouses", "Villas", "Estates", "Ranch Homes",
    "Bungalows", "Cottages", "Patio Homes", "Luxury Homes",
    "Starter Homes", "Investment Properties", "Rental Properties"
]

# Bedroom configurations
BEDROOMS = [
    "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom",
    "6 Bedroom", "1 Bed", "2 Bed", "3 Bed", "4 Bed", "5 Bed", "6 Bed",
    "Studio", "One Bedroom", "Two Bedroom", "Three Bedroom", "Four Bedroom",
    "Five Bedroom", "Six Bedroom", "2-3 Bedroom", "3-4 Bedroom", "4-5 Bedroom"
]

# Bathroom configurations
BATHROOMS = [
    "1 Bath", "2 Bath", "3 Bath", "4 Bath", "5 Bath",
    "1.5 Bath", "2.5 Bath", "3.5 Bath", "1 Bathroom", "2 Bathroom",
    "3 Bathroom", "4 Bathroom", "Half Bath", "Full Bath",
    "Master Bath", "Dual Master Baths"
]

# Property features
FEATURES = [
    "with Pool", "with Swimming Pool", "with Inground Pool",
    "with 2 Stories", "2 Story", "Two Story", "Single Story", "One Story",
    "with Garage", "2 Car Garage", "3 Car Garage", "Attached Garage",
    "with Backyard", "Large Backyard", "Fenced Yard", "Corner Lot",
    "with Covered Patio", "with Patio", "with Deck", "with Balcony",
    "with Fireplace", "with Game Room", "with Office", "with Study",
    "with Walk-In Closets", "with Master Suite", "with Open Floor Plan",
    "Move-In Ready", "Newly Renovated", "Recently Updated",
    "with Granite Countertops", "with Stainless Appliances",
    "with Hardwood Floors", "with Tile Floors", "with Carpet",
    "with Central AC", "with Energy Efficient Features",
    "with Smart Home Features", "with Security System",
    "Gated Community", "HOA Community", "Golf Course Community",
    "with RV Parking", "with Boat Parking", "with Storage Shed",
    "with Laundry Room", "with Utility Room", "with Pantry",
    "with Breakfast Nook", "with Formal Dining", "with Eat-In Kitchen",
    "with Island Kitchen", "with Updated Kitchen", "with Chef's Kitchen",
    "with Split Bedrooms", "with Guest Suite", "with In-Law Suite",
    "with Workshop", "with Man Cave", "with She Shed",
    "with Sprinkler System", "with Landscaping", "Mature Trees",
    "with View", "with City View", "with Park View",
    "Near Schools", "Near Shopping", "Near Medical Center",
    "with No HOA", "Low Maintenance", "Low Taxes",
    "with Detached Garage", "with Carport", "Covered Parking"
]

# Price ranges
PRICE_RANGES = [
    "Under $100k", "Under $150k", "Under $200k", "Under $250k", "Under $300k",
    "$100k-$150k", "$150k-$200k", "$200k-$250k", "$250k-$300k", "$300k-$350k",
    "$350k-$400k", "$400k-$500k", "$500k-$600k", "$600k-$750k", "$750k-$1M",
    "Under $500k", "Under $750k", "Over $500k", "Over $1M",
    "Affordable", "Mid-Range", "Luxury", "High-End"
]

# Property conditions
CONDITIONS = [
    "New Construction", "Newly Built", "Brand New",
    "Like New", "Excellent Condition", "Well Maintained",
    "Renovated", "Recently Remodeled", "Updated",
    "Fixer Upper", "Handyman Special", "Investment Opportunity",
    "Foreclosure", "Short Sale", "Bank Owned"
]

# Lot sizes and types
LOT_TYPES = [
    "Small Lot", "Standard Lot", "Large Lot", "Oversized Lot",
    "Quarter Acre", "Half Acre", "1 Acre", "2+ Acres", "5+ Acres",
    "Acreage", "Country Living", "Rural Property",
    "City Lot", "Suburban", "Residential Lot"
]

# Architectural styles
STYLES = [
    "Modern", "Contemporary", "Traditional", "Classic",
    "Spanish Style", "Mediterranean", "Ranch Style",
    "Craftsman", "Colonial", "Victorian", "Farmhouse",
    "Minimalist", "Southwestern", "Texas Style"
]

# Additional descriptors
DESCRIPTORS = [
    "For Sale", "Available", "On Market", "Listed",
    "Pet Friendly", "Family Friendly", "Quiet Neighborhood",
    "Walkable", "Bike Friendly", "Tree-Lined Street",
    "Cul-de-Sac", "Prime Location", "Desirable Area",
    "Growing Area", "Established Neighborhood"
]

# Time-based descriptors
TIME_BASED = [
    "2024", "2025", "This Year", "New Listings",
    "Just Listed", "Fresh on Market", "Recently Listed"
]

def generate_titles() -> Set[str]:
    """Generate comprehensive set of page titles"""
    titles = set()

    # Pattern 1: City + Property Type
    for city, prop_type in itertools.product(CITIES, PROPERTY_TYPES):
        titles.add(f"{prop_type} in {city}, TX")
        titles.add(f"{city} {prop_type}")
        titles.add(f"{prop_type} for Sale in {city}")
        titles.add(f"{city}, TX {prop_type}")

    # Pattern 2: City + Bedrooms + Property Type
    for city, bed, prop_type in itertools.product(CITIES, BEDROOMS, PROPERTY_TYPES[:10]):
        titles.add(f"{bed} {prop_type} in {city}")
        titles.add(f"{city} {bed} {prop_type}")
        titles.add(f"{bed} {prop_type} for Sale {city}, TX")

    # Pattern 3: City + Bedrooms + Bathrooms + Property Type
    for city, bed, bath, prop_type in itertools.product(
        CITIES[:15], BEDROOMS[:10], BATHROOMS[:8], PROPERTY_TYPES[:8]
    ):
        titles.add(f"{bed} {bath} {prop_type} in {city}")
        titles.add(f"{city} {bed} {bath} {prop_type}")

    # Pattern 4: City + Feature + Property Type
    for city, feature, prop_type in itertools.product(
        CITIES, FEATURES, PROPERTY_TYPES[:12]
    ):
        titles.add(f"{prop_type} {feature} in {city}")
        titles.add(f"{city} {prop_type} {feature}")
        titles.add(f"{feature} {prop_type} {city}, TX")

    # Pattern 5: City + Bedrooms + Feature
    for city, bed, feature in itertools.product(CITIES, BEDROOMS[:12], FEATURES[:30]):
        titles.add(f"{bed} Homes {feature} in {city}")
        titles.add(f"{city} {bed} Homes {feature}")

    # Pattern 6: City + Price Range + Property Type
    for city, price, prop_type in itertools.product(
        CITIES, PRICE_RANGES, PROPERTY_TYPES[:10]
    ):
        titles.add(f"{prop_type} {price} in {city}")
        titles.add(f"{city} {prop_type} {price}")
        titles.add(f"{price} {prop_type} {city}, TX")

    # Pattern 7: City + Condition + Property Type
    for city, condition, prop_type in itertools.product(
        CITIES, CONDITIONS, PROPERTY_TYPES[:10]
    ):
        titles.add(f"{condition} {prop_type} in {city}")
        titles.add(f"{city} {condition} {prop_type}")

    # Pattern 8: City + Lot Type + Property Type
    for city, lot, prop_type in itertools.product(
        CITIES, LOT_TYPES, PROPERTY_TYPES[:10]
    ):
        titles.add(f"{prop_type} on {lot} in {city}")
        titles.add(f"{city} {prop_type} {lot}")

    # Pattern 9: City + Style + Property Type
    for city, style, prop_type in itertools.product(
        CITIES, STYLES, PROPERTY_TYPES[:10]
    ):
        titles.add(f"{style} {prop_type} in {city}")
        titles.add(f"{city} {style} {prop_type}")

    # Pattern 10: City + Multiple Features
    for city, f1, f2 in itertools.product(CITIES[:20], FEATURES[:20], FEATURES[20:40]):
        titles.add(f"Homes {f1} and {f2} in {city}")
        titles.add(f"{city} Homes {f1} {f2}")

    # Pattern 11: Bedrooms + Bathrooms + Feature
    for bed, bath, feature in itertools.product(
        BEDROOMS[:10], BATHROOMS[:8], FEATURES[:25]
    ):
        titles.add(f"{bed} {bath} Homes {feature} McAllen Valley")
        titles.add(f"{bed} {bath} {feature} Homes Rio Grande Valley")

    # Pattern 12: Price Range + Feature + City
    for price, feature, city in itertools.product(
        PRICE_RANGES[:15], FEATURES[:20], CITIES[:15]
    ):
        titles.add(f"{price} Homes {feature} in {city}")

    # Pattern 13: Bedrooms + Feature + Price Range
    for bed, feature, price in itertools.product(
        BEDROOMS[:8], FEATURES[:15], PRICE_RANGES[:12]
    ):
        titles.add(f"{bed} Homes {feature} {price} McAllen Area")

    # Pattern 14: City + Descriptor + Property Type
    for city, desc, prop_type in itertools.product(
        CITIES, DESCRIPTORS, PROPERTY_TYPES[:10]
    ):
        titles.add(f"{desc} {prop_type} in {city}")
        titles.add(f"{city} {desc} {prop_type}")

    # Pattern 15: Time-based + City + Property Type
    for time, city, prop_type in itertools.product(
        TIME_BASED, CITIES[:15], PROPERTY_TYPES[:8]
    ):
        titles.add(f"{time} {prop_type} in {city}")
        titles.add(f"{city} {prop_type} {time}")

    # Pattern 16: Complex combinations (3+ attributes)
    for city, bed, feature, price in itertools.product(
        CITIES[:10], BEDROOMS[:6], FEATURES[:10], PRICE_RANGES[:8]
    ):
        titles.add(f"{bed} Homes {feature} {price} in {city}")

    # Pattern 17: Style + Bedrooms + Feature + City
    for style, bed, feature, city in itertools.product(
        STYLES[:8], BEDROOMS[:6], FEATURES[:8], CITIES[:10]
    ):
        titles.add(f"{style} {bed} Homes {feature} in {city}")

    # Pattern 18: Condition + Bedrooms + Price + City
    for cond, bed, price, city in itertools.product(
        CONDITIONS[:8], BEDROOMS[:6], PRICE_RANGES[:8], CITIES[:10]
    ):
        titles.add(f"{cond} {bed} Homes {price} in {city}")

    # Pattern 19: Regional variations
    regional_areas = [
        "Rio Grande Valley", "RGV", "South Texas", "Deep South Texas",
        "The Valley", "Lower Rio Grande Valley", "LRGV"
    ]
    for region, prop_type in itertools.product(regional_areas, PROPERTY_TYPES):
        titles.add(f"{prop_type} in {region}")
        titles.add(f"{region} {prop_type}")

    for region, bed, feature in itertools.product(
        regional_areas, BEDROOMS[:10], FEATURES[:20]
    ):
        titles.add(f"{bed} Homes {feature} in {region}")

    # Pattern 20: Multiple cities combined
    city_combos = [
        "McAllen-Edinburg-Mission",
        "McAllen-Pharr-Mission",
        "McAllen and Surrounding Areas",
        "Tri-City Area"
    ]
    for combo, prop_type in itertools.product(city_combos, PROPERTY_TYPES[:15]):
        titles.add(f"{prop_type} in {combo}")

    # Pattern 21: Specific feature combinations
    feature_combos = [
        ("with Pool", "2 Story"),
        ("with Pool", "2 Car Garage"),
        ("with Pool", "Large Backyard"),
        ("2 Story", "2 Car Garage"),
        ("with Pool", "Move-In Ready"),
        ("Gated Community", "with Pool"),
        ("New Construction", "with Pool"),
        ("with Pool", "with Game Room"),
    ]
    for city, (f1, f2), bed in itertools.product(
        CITIES[:15], feature_combos, BEDROOMS[:8]
    ):
        titles.add(f"{bed} Homes {f1} and {f2} in {city}")

    return titles

def save_titles(titles: Set[str], filename: str = "page_titles.txt"):
    """Save titles to file"""
    sorted_titles = sorted(list(titles))

    with open(filename, 'w', encoding='utf-8') as f:
        for title in sorted_titles:
            f.write(f"{title}\n")

    print(f"Generated {len(sorted_titles):,} unique page titles")
    print(f"Saved to {filename}")

    # Also save as JSON for easier programmatic use
    json_filename = filename.replace('.txt', '.json')
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(sorted_titles, f, indent=2)
    print(f"Also saved as JSON: {json_filename}")

    # Create a categorized version
    categorized = categorize_titles(sorted_titles)
    cat_filename = filename.replace('.txt', '_categorized.json')
    with open(cat_filename, 'w', encoding='utf-8') as f:
        json.dump(categorized, f, indent=2)
    print(f"Categorized version: {cat_filename}")

def categorize_titles(titles: List[str]) -> dict:
    """Categorize titles by city and features"""
    categorized = {
        'by_city': {},
        'by_features': {},
        'by_bedrooms': {},
        'by_price_range': {}
    }

    for title in titles:
        # Categorize by city
        for city in CITIES:
            if city in title:
                if city not in categorized['by_city']:
                    categorized['by_city'][city] = []
                categorized['by_city'][city].append(title)

        # Categorize by features
        if 'Pool' in title or 'pool' in title:
            categorized['by_features'].setdefault('pool', []).append(title)
        if '2 Story' in title or 'Two Story' in title:
            categorized['by_features'].setdefault('2_story', []).append(title)
        if 'Garage' in title:
            categorized['by_features'].setdefault('garage', []).append(title)
        if 'New Construction' in title or 'Newly Built' in title:
            categorized['by_features'].setdefault('new_construction', []).append(title)

        # Categorize by bedrooms
        for i in range(1, 7):
            if f'{i} Bed' in title or f'{i} Bed' in title:
                categorized['by_bedrooms'].setdefault(f'{i}_bedroom', []).append(title)

    return categorized

def print_sample_titles(titles: Set[str], sample_size: int = 50):
    """Print sample of generated titles"""
    print(f"\n{'='*60}")
    print(f"SAMPLE OF GENERATED PAGE TITLES ({sample_size} random samples)")
    print(f"{'='*60}\n")

    import random
    samples = random.sample(list(titles), min(sample_size, len(titles)))
    for i, title in enumerate(samples, 1):
        print(f"{i:3d}. {title}")

if __name__ == "__main__":
    print("Generating real estate page titles for McAllen Valley area...")
    print("This may take a moment...\n")

    titles = generate_titles()

    save_titles(titles, "page_titles.txt")
    print_sample_titles(titles, 100)

    print(f"\n{'='*60}")
    print(f"GENERATION COMPLETE!")
    print(f"{'='*60}")
    print(f"Total unique titles: {len(titles):,}")
    print(f"\nFiles created:")
    print(f"  - page_titles.txt (all titles, one per line)")
    print(f"  - page_titles.json (JSON format)")
    print(f"  - page_titles_categorized.json (organized by categories)")
