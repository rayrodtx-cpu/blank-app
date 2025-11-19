"""
Optimized Real Estate Page Title Generator for Fort Worth, TX
Generates 100,000 HIGH-PRIORITY page titles with descriptions
Fast generation - focuses on most valuable SEO combinations
"""

import itertools
import csv
from datetime import datetime
import random

# Fort Worth neighborhoods (expanded for 50K+ titles)
NEIGHBORHOODS = [
    "Downtown Fort Worth", "Southside", "Near Southside", "Arlington Heights",
    "Berkeley", "Mistletoe Heights", "Ryan Place", "Fairmount", "Berkeley Place",
    "Westover Hills", "Ridglea", "Ridglea Hills", "River Oaks", "TCU Area",
    "Monticello", "Meadowbrook", "Como", "Polytechnic Heights",
    "East Fort Worth", "North Fort Worth", "West Fort Worth", "South Fort Worth",
    "Alliance", "Fossil Creek", "Keller", "Lake Worth",
    "Benbrook", "River District", "Cultural District", "Stockyards",
    "Historic Southside", "Magnolia Avenue", "Hillside", "Oakhurst",
    "Candleridge", "Meadow Creek", "Park Glen", "Overton Park",
    "Tanglewood", "Wedgwood", "Hulen Bend", "Mira Vista",
    "Bluebonnet Hills", "Crestwood", "Trinity Heights"
]

# Property types (expanded)
PROPERTY_TYPES = [
    "Single Family Homes", "Townhomes", "Condos", "Luxury Homes",
    "Ranch Homes", "Modern Homes", "Victorian Homes", "Craftsman Homes",
    "Contemporary Homes", "Traditional Homes", "Brick Homes",
    "New Construction Homes", "Estate Homes", "Custom Built Homes",
    "Patio Homes", "Villas"
]

# Features (expanded for 50K+ titles)
FEATURES = [
    "with Pools", "with In-Ground Pools", "with Salt Water Pools",
    "with 2 Stories", "with 3 Stories", "with Single Story",
    "with Basements", "with Finished Basements", "with 2 Car Garages",
    "with 3 Car Garages", "with Attached Garages", "with RV Parking",
    "with Fireplaces", "with Wood Burning Fireplaces", "with Outdoor Fireplaces",
    "with Master Suite", "with Main Floor Master", "with Walk-In Closets",
    "with Home Office", "with Bonus Room", "with Game Room",
    "with Media Room", "with Sunroom", "with Screened Porch",
    "with Covered Patio", "with Deck", "with Outdoor Kitchen",
    "with Hardwood Floors", "with Tile Floors", "with Granite Countertops",
    "with Island Kitchen", "with Gourmet Kitchen", "with Updated Kitchen",
    "with Open Floor Plan", "with Split Bedroom Plan", "with Vaulted Ceilings",
    "with High Ceilings", "with Smart Home Features", "with Security System",
    "with Energy Efficient Features", "with Solar Panels", "with Sprinkler System",
    "with Lake Views", "with Golf Course Views", "with City Views",
    "with Corner Lot", "with Cul-de-Sac Location", "with Privacy Fence",
    "with Mature Trees", "with Landscaping", "with Large Yard",
    "with Fenced Yard", "with Guest House", "with Mother-In-Law Suite"
]

# Bedrooms
BEDROOMS = ["2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom"]

# Bathrooms
BATHROOMS = ["2 Bath", "2.5 Bath", "3 Bath", "3.5 Bath", "4 Bath"]

# Price ranges (most searched)
PRICE_RANGES = [
    "Under $200K", "Under $300K", "Under $400K", "Under $500K",
    "$200K-$300K", "$300K-$400K", "$400K-$500K", "$500K-$750K",
    "Over $500K", "Over $1M"
]

# Square footage
SQUARE_FOOTAGE = [
    "Under 2000 Sq Ft", "2000-2500 Sq Ft", "2500-3000 Sq Ft",
    "3000-4000 Sq Ft", "Over 4000 Sq Ft"
]

# School districts
SCHOOL_DISTRICTS = ["Fort Worth ISD", "Keller ISD", "Carroll ISD", "Northwest ISD"]

# Special features
SPECIAL_FEATURES = [
    "Move-In Ready", "Fully Renovated", "Recently Updated",
    "Gated Community", "Golf Course Community", "Waterfront",
    "Near Schools", "Walkable Neighborhood"
]

def generate_description(title):
    """Generate SEO-friendly description for a page title"""
    title_lower = title.lower()
    description_parts = []

    # Opening statement
    if "luxury" in title_lower:
        description_parts.append("Discover luxury")
    elif "new construction" in title_lower:
        description_parts.append("Browse new")
    else:
        description_parts.append("Explore")

    # Main subject
    description_parts.append(title.split(" in ")[0].lower())

    # Location
    if " in " in title:
        location = title.split(" in ")[1].replace(", Fort Worth TX", "").replace(", Fort Worth", "")
        description_parts.append(f"in {location}, Fort Worth, TX.")
    else:
        description_parts.append("in Fort Worth, TX.")

    # Value propositions
    value_props = []
    if "pool" in title_lower:
        value_props.append("Perfect for Texas summers")
    if any(bed in title_lower for bed in ["3 bedroom", "4 bedroom", "5 bedroom"]):
        value_props.append("ideal for families")
    if "luxury" in title_lower or "custom" in title_lower:
        value_props.append("featuring premium amenities")
    if "new construction" in title_lower:
        value_props.append("with modern features and warranties")
    if "updated" in title_lower or "renovated" in title_lower:
        value_props.append("with modern updates")
    if "gated" in title_lower:
        value_props.append("offering security and privacy")
    if "open floor plan" in title_lower:
        value_props.append("with contemporary layouts")

    if value_props:
        description_parts.append(". ".join(value_props[:2]) + ".")

    # CTA
    if "price" in title_lower or "$" in title:
        cta = "View listings, filter by price, and schedule tours."
    elif "new" in title_lower:
        cta = "See the newest properties with photos and details."
    else:
        cta = "Browse current listings with photos and virtual tours."

    description_parts.append(cta)

    description = " ".join(description_parts)
    description = description.replace("  ", " ").replace("..", ".")
    description = description[0].upper() + description[1:]

    # Truncate to 160 chars
    if len(description) > 160:
        description = description[:157] + "..."

    return description

def create_url_slug(title):
    """Create SEO-friendly URL slug"""
    slug = title.lower()
    for old, new in [(' ', '-'), (',', ''), ('+', 'plus'), ('$', ''), ('.', ''),
                     ('/', '-'), ('&', 'and'), (':', ''), ('  ', ' ')]:
        slug = slug.replace(old, new)
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-')

def generate_sample_titles():
    """Generate high-priority page titles with descriptions"""
    titles_data = {}  # Use dict to avoid duplicates

    print("Generating high-priority Fort Worth real estate page titles...\n")

    # Priority 1: Neighborhood + Beds + Price (HIGH CONVERSION)
    print("Category 1: Neighborhood + Bedrooms + Price...")
    for neighborhood, beds, price in itertools.product(NEIGHBORHOODS, BEDROOMS, PRICE_RANGES):
        title = f"{beds} Homes {price} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 2: Property Type + Feature + Neighborhood
    print("Category 2: Property Type + Feature + Neighborhood...")
    for prop_type, feature, neighborhood in itertools.product(PROPERTY_TYPES, FEATURES, NEIGHBORHOODS):
        title = f"{prop_type} {feature} in {neighborhood}, Fort Worth TX"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 3: Beds + Baths + Neighborhood
    print("Category 3: Beds + Baths + Neighborhood...")
    for beds, baths, neighborhood in itertools.product(BEDROOMS, BATHROOMS, NEIGHBORHOODS):
        title = f"{beds} {baths} Homes in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 4: Property Type + Price + Neighborhood
    print("Category 4: Property Type + Price + Neighborhood...")
    for prop_type, price, neighborhood in itertools.product(PROPERTY_TYPES, PRICE_RANGES, NEIGHBORHOODS):
        title = f"{prop_type} {price} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 5: Beds + Feature + Neighborhood
    print("Category 5: Bedrooms + Feature + Neighborhood...")
    for beds, feature, neighborhood in itertools.product(BEDROOMS, FEATURES, NEIGHBORHOODS):
        title = f"{beds} Homes {feature} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 6: Property Type + Square Footage + Neighborhood
    print("Category 6: Property Type + Square Footage + Neighborhood...")
    for prop_type, sqft, neighborhood in itertools.product(PROPERTY_TYPES, SQUARE_FOOTAGE, NEIGHBORHOODS):
        title = f"{prop_type} {sqft} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 7: Beds + Baths + Price
    print("Category 7: Beds + Baths + Price...")
    for beds, baths, price in itertools.product(BEDROOMS, BATHROOMS, PRICE_RANGES):
        title = f"{beds} {baths} Homes {price} in Fort Worth TX"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 8: School District + Beds + Price
    print("Category 8: School District + Beds + Price...")
    for district, beds, price in itertools.product(SCHOOL_DISTRICTS, BEDROOMS, PRICE_RANGES):
        title = f"{beds} Homes {price} in {district}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 9: Special Feature + Property Type + Neighborhood
    print("Category 9: Special Feature + Property Type + Neighborhood...")
    for special, prop_type, neighborhood in itertools.product(SPECIAL_FEATURES, PROPERTY_TYPES, NEIGHBORHOODS):
        title = f"{special} {prop_type} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 10: Base neighborhood pages
    print("Category 10: Base Neighborhood & Property Type Pages...")
    for neighborhood in NEIGHBORHOODS:
        base_titles = [
            f"Homes For Sale in {neighborhood}, Fort Worth TX",
            f"{neighborhood} Real Estate",
            f"{neighborhood} Houses For Sale"
        ]
        for title in base_titles:
            if title not in titles_data:
                titles_data[title] = generate_description(title)

        for prop_type in PROPERTY_TYPES:
            title = f"{prop_type} in {neighborhood}, Fort Worth"
            if title not in titles_data:
                titles_data[title] = generate_description(title)

    print(f"  Total: {len(titles_data):,} titles")

    # Priority 11: Price + Feature combinations
    print("Category 11: Price + Feature + Neighborhood...")
    for price, feature, neighborhood in itertools.product(PRICE_RANGES[:6], FEATURES[:10], NEIGHBORHOODS):
        title = f"Homes {price} {feature} in {neighborhood}, Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    # Priority 12: Beds + Baths + Feature combinations
    print("Category 12: Beds + Baths + Feature...")
    for beds, baths, feature in itertools.product(BEDROOMS, BATHROOMS[:3], FEATURES[:10]):
        title = f"{beds} {baths} Homes {feature} in Fort Worth"
        if title not in titles_data:
            titles_data[title] = generate_description(title)
    print(f"  Total: {len(titles_data):,} titles")

    return titles_data

def save_to_csv(titles_data, filename='fort_worth_50k_titles_with_descriptions.csv'):
    """Save titles to CSV"""
    print(f"\nSaving {len(titles_data):,} titles to {filename}...")

    # Convert dict to sorted list
    sorted_titles = sorted(titles_data.items(), key=lambda x: x[0])

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page Title', 'SEO-Friendly URL Slug', 'Meta Description'])

        for title, description in sorted_titles:
            slug = create_url_slug(title)
            writer.writerow([title, slug, description])

    import os
    file_size_mb = os.path.getsize(filename) / (1024 * 1024)
    print(f"✓ Successfully saved {len(titles_data):,} titles to {filename}")
    print(f"  File size: {file_size_mb:.2f} MB")

    return filename

def main():
    print("=" * 80)
    print("Fort Worth Real Estate - HIGH-PRIORITY Page Titles with Descriptions")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    titles_data = generate_sample_titles()

    print("\n" + "=" * 80)
    print(f"Generated {len(titles_data):,} unique high-priority page titles!")
    print("=" * 80)

    # Show examples
    print("\nSample Titles with Descriptions:")
    print("-" * 80)

    sample_titles = list(titles_data.items())[:15]
    for i, (title, description) in enumerate(sample_titles, 1):
        print(f"\n{i}. Title: {title}")
        print(f"   Description: {description}")
        print(f"   URL: {create_url_slug(title)}")

    # Save to CSV
    filename = save_to_csv(titles_data)

    print(f"\n" + "=" * 80)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print("\nWhat's included:")
    print("✓ Page titles optimized for highest conversion keywords")
    print("✓ SEO-friendly URL slugs")
    print("✓ Ready-to-use meta descriptions (~160 chars)")
    print("\nCategories covered:")
    print("  - Neighborhood + Bedroom + Price combinations")
    print("  - Property Type + Feature + Location")
    print("  - School District searches")
    print("  - Special features (Gated, Waterfront, etc.)")
    print("  - And more...")

if __name__ == "__main__":
    main()
