#!/usr/bin/env python3
"""
Generate 50,000+ SEO-optimized page titles for Corpus Christi real estate website.
Combines property types, features, locations, and attributes for comprehensive coverage.
"""

import itertools
from datetime import datetime

# Property types
property_types = [
    "Homes", "Houses", "Properties", "Real Estate", "Condos", "Townhomes",
    "Townhouses", "Single Family Homes", "Luxury Homes", "Estates",
    "Villas", "Bungalows", "Ranch Homes", "Cottages", "Residences"
]

# Bedroom counts
bedrooms = [
    "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom",
    "6 Bedroom", "1 Bed", "2 Bed", "3 Bed", "4 Bed", "5 Bed",
    "One Bedroom", "Two Bedroom", "Three Bedroom", "Four Bedroom", "Five Bedroom"
]

# Bathroom counts
bathrooms = [
    "1 Bathroom", "2 Bathroom", "3 Bathroom", "4 Bathroom", "5 Bathroom",
    "1 Bath", "2 Bath", "3 Bath", "4 Bath", "1.5 Bath", "2.5 Bath", "3.5 Bath"
]

# Property features
features = [
    "with Pool", "with Pools", "with Swimming Pool", "with Inground Pool",
    "with 2 Stories", "with Two Stories", "with 3 Stories", "with Multiple Stories",
    "with Garage", "with 2 Car Garage", "with 3 Car Garage", "with Attached Garage",
    "with Waterfront", "with Bay View", "with Ocean View", "with Water View",
    "with Backyard", "with Large Yard", "with Fenced Yard", "with Big Backyard",
    "with Master Suite", "with Walk-in Closet", "with Updated Kitchen",
    "with Granite Countertops", "with Hardwood Floors", "with Tile Floors",
    "with Open Floor Plan", "with High Ceilings", "with Vaulted Ceilings",
    "with Fireplace", "with Gas Fireplace", "with Wood Fireplace",
    "with Covered Patio", "with Patio", "with Deck", "with Balcony",
    "with AC", "with Central Air", "with New HVAC", "with Energy Efficient",
    "with Solar Panels", "with Smart Home", "with Security System",
    "with Gated Community", "with HOA", "with No HOA",
    "with RV Parking", "with Boat Parking", "with Workshop",
    "with Office", "with Home Office", "with Study", "with Bonus Room",
    "with Game Room", "with Media Room", "with Gym", "with Wet Bar",
    "with Guest House", "with Mother-in-Law Suite", "with Casita",
    "with New Construction", "with Recently Renovated", "with Move-in Ready",
    "with Stainless Steel Appliances", "with Island Kitchen", "with Breakfast Bar",
    "with Formal Dining", "with Eat-in Kitchen", "with Pantry",
    "with Laundry Room", "with Utility Room", "with Mudroom",
    "with Double Vanity", "with Garden Tub", "with Separate Shower",
    "with His and Hers Closets", "with Built-ins", "with Custom Cabinets",
    "with Crown Molding", "with Wainscoting", "with Chair Rail",
    "with Sprinkler System", "with Landscaping", "with Mature Trees",
    "with Privacy Fence", "with Brick Fence", "with Wrought Iron Fence",
    "with Corner Lot", "with Cul-de-sac", "with Oversized Lot",
    "with Deep Lot", "with Wide Lot", "with Acreage",
    "with Golf Course View", "with Park View", "with Greenbelt",
    "with Beach Access", "with Fishing Pier", "with Boat Dock",
    "with Private Beach", "with Deep Water Access", "with Canal Access"
]

# Corpus Christi neighborhoods and areas
neighborhoods = [
    "Corpus Christi", "North Corpus Christi", "South Corpus Christi",
    "Downtown Corpus Christi", "Central Corpus Christi", "West Corpus Christi",
    "Padre Island", "North Padre Island", "Flour Bluff", "Calallen",
    "Annaville", "Southside", "Westside", "Northside",
    "Bay Area", "Bayfront", "Ocean Drive", "Oso Bay",
    "King's Crossing", "Cinnamon Shore", "Lakeview", "Del Mar",
    "Mustang Beach", "Port Aransas", "Portland", "Ingleside",
    "Rockport", "Aransas Pass", "Gregory", "Taft",
    "Robstown", "Chapman Ranch", "Violet", "Agua Dulce",
    "Banquete", "Driscoll", "Petronila", "Bishop",
    "Laguna Shores", "Cayo Del Oso", "Island Moorings", "Whitecap Beach",
    "Encantada", "Sunrise Beach", "Newport", "Stone Gate",
    "Tortuga Dunes", "La Bahia", "Kings Landing", "Bluff's Landing",
    "Cimarron", "Timbergate", "Wooldridge Estates", "Carroll Oaks"
]

# Price ranges
price_ranges = [
    "Under $100K", "Under $150K", "Under $200K", "Under $250K", "Under $300K",
    "$100K-$200K", "$200K-$300K", "$300K-$400K", "$400K-$500K", "$500K-$750K",
    "$750K-$1M", "Over $1M", "Luxury", "Affordable", "Budget Friendly"
]

# Property conditions
conditions = [
    "New Construction", "Recently Built", "Newly Renovated", "Updated",
    "Move-in Ready", "Fixer Upper", "As-Is", "Turn Key",
    "Recently Listed", "Just Listed", "New Listing", "Coming Soon"
]

# Additional qualifiers
qualifiers = [
    "Best", "Top", "Affordable", "Luxury", "Premium", "Executive",
    "Family Friendly", "Waterfront", "Beachfront", "Golf Course",
    "Pet Friendly", "Senior Living", "Active Adult", "Gated",
    "Private", "Secluded", "Quiet", "View", "Custom Built"
]

# Action phrases
actions = [
    "for Sale", "for Sale in", "Available in", "Listings in",
    "on the Market in", "to Buy in", "for Sale Near"
]

def generate_titles():
    """Generate comprehensive page titles with multiple combination strategies."""
    titles = set()  # Using set to avoid duplicates

    # Strategy 1: Property Type + Feature + Location
    for prop, feat, loc in itertools.product(property_types, features, neighborhoods):
        titles.add(f"{prop} {feat} in {loc}, TX")
        titles.add(f"{loc} {prop} {feat}")
        titles.add(f"{feat.replace('with ', '')} {prop} in {loc}")

    # Strategy 2: Bedrooms + Property Type + Location
    for bed, prop, loc in itertools.product(bedrooms, property_types, neighborhoods):
        titles.add(f"{bed} {prop} in {loc}, TX")
        titles.add(f"{loc} {bed} {prop} for Sale")
        titles.add(f"{bed} {prop} for Sale in {loc}")

    # Strategy 3: Bedrooms + Bathrooms + Location
    for bed, bath, loc in itertools.product(bedrooms, bathrooms, neighborhoods):
        titles.add(f"{bed} {bath} Homes in {loc}, TX")
        titles.add(f"{bed}/{bath} Homes for Sale in {loc}")
        titles.add(f"{loc} {bed} {bath} Properties")

    # Strategy 4: Price Range + Property Type + Location
    for price, prop, loc in itertools.product(price_ranges, property_types, neighborhoods):
        titles.add(f"{prop} {price} in {loc}, TX")
        titles.add(f"{price} {prop} for Sale in {loc}")
        titles.add(f"{loc} {prop} {price}")

    # Strategy 5: Bedrooms + Feature + Location
    for bed, feat, loc in itertools.product(bedrooms, features, neighborhoods):
        titles.add(f"{bed} Homes {feat} in {loc}, TX")
        titles.add(f"{loc} {bed} Homes {feat}")
        titles.add(f"{bed} {feat.replace('with ', '')} Homes in {loc}")

    # Strategy 6: Property Type + Condition + Location
    for prop, cond, loc in itertools.product(property_types, conditions, neighborhoods):
        titles.add(f"{cond} {prop} in {loc}, TX")
        titles.add(f"{loc} {cond} {prop} for Sale")
        titles.add(f"{prop} {cond} in {loc}")

    # Strategy 7: Qualifier + Property Type + Feature
    for qual, prop, feat in itertools.product(qualifiers, property_types, features):
        titles.add(f"{qual} {prop} {feat} in Corpus Christi, TX")
        titles.add(f"{qual} {feat.replace('with ', '')} {prop} Corpus Christi")

    # Strategy 8: Price Range + Bedrooms + Location
    for price, bed, loc in itertools.product(price_ranges, bedrooms, neighborhoods):
        titles.add(f"{bed} Homes {price} in {loc}, TX")
        titles.add(f"{price} {bed} Homes for Sale in {loc}")

    # Strategy 9: Feature + Bedrooms + Bathrooms + Location
    for feat, bed, bath, loc in itertools.product(
        features[:20], bedrooms[:8], bathrooms[:8], neighborhoods[:20]
    ):
        titles.add(f"{bed} {bath} Homes {feat} in {loc}, TX")
        titles.add(f"{loc} {bed}/{bath} Homes {feat}")

    # Strategy 10: Multiple Features + Location
    for feat1, feat2, loc in itertools.product(
        features[:30], features[30:60], neighborhoods
    ):
        titles.add(f"Homes {feat1} and {feat2} in {loc}, TX")
        titles.add(f"{loc} Homes {feat1} and {feat2}")

    # Strategy 11: Action + Property Type + Location
    for action, prop, loc in itertools.product(actions, property_types, neighborhoods):
        titles.add(f"{prop} {action} {loc}, TX")
        titles.add(f"{loc}, TX {prop} {action}")

    # Strategy 12: Bedrooms + Bathrooms + Feature + Location
    for bed, bath, feat, loc in itertools.product(
        bedrooms[:8], bathrooms[:6], features[:25], neighborhoods[:15]
    ):
        titles.add(f"{bed} {bath} {feat.replace('with ', '')} Homes in {loc}")

    # Strategy 13: Property Type + Multiple Features
    for prop, feat1, feat2 in itertools.product(
        property_types, features[:40], features[40:80]
    ):
        titles.add(f"{prop} {feat1} {feat2} Corpus Christi")

    # Strategy 14: Price + Bedrooms + Bathrooms + Location
    for price, bed, bath, loc in itertools.product(
        price_ranges, bedrooms[:10], bathrooms[:8], neighborhoods[:10]
    ):
        titles.add(f"{bed} {bath} Homes {price} in {loc}, TX")

    # Strategy 15: Qualifier + Bedrooms + Feature + Location
    for qual, bed, feat, loc in itertools.product(
        qualifiers[:15], bedrooms[:10], features[:30], neighborhoods[:15]
    ):
        titles.add(f"{qual} {bed} Homes {feat} in {loc}")

    return sorted(list(titles))

def save_titles_to_file(titles, filename="corpus_christi_page_titles.txt"):
    """Save the generated titles to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Corpus Christi Real Estate Page Titles\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Total Titles: {len(titles):,}\n")
        f.write(f"#\n")
        f.write(f"# These titles can be used for:\n")
        f.write(f"# - SEO landing pages\n")
        f.write(f"# - Dynamic page generation\n")
        f.write(f"# - Meta titles and H1 tags\n")
        f.write(f"# - Internal linking structure\n")
        f.write(f"#\n\n")

        for i, title in enumerate(titles, 1):
            f.write(f"{title}\n")

    print(f"✓ Generated {len(titles):,} unique page titles")
    print(f"✓ Saved to: {filename}")
    return len(titles)

def main():
    print("Generating Corpus Christi real estate page titles...")
    print("This may take a few moments...\n")

    titles = generate_titles()
    total = save_titles_to_file(titles)

    print(f"\nGeneration complete!")
    print(f"Total unique titles: {total:,}")

    if total >= 50000:
        print(f"✓ Target of 50,000+ titles achieved!")
    else:
        print(f"⚠ Generated {total:,} titles (target was 50,000+)")

    # Show some sample titles
    print("\nSample titles:")
    for i in range(min(20, len(titles))):
        print(f"  {i+1}. {titles[i]}")

if __name__ == "__main__":
    main()
