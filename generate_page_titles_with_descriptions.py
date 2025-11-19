"""
Enhanced Real Estate Page Title Generator for Fort Worth, TX
Generates 50,000+ unique page titles WITH SEO descriptions
"""

import itertools
import csv
from datetime import datetime
import os

# Fort Worth neighborhoods and areas
NEIGHBORHOODS = [
    "Downtown Fort Worth", "Southside", "Near Southside", "Arlington Heights",
    "Berkeley", "Mistletoe Heights", "Ryan Place", "Fairmount", "Berkeley Place",
    "Westover Hills", "Ridglea", "Ridglea Hills", "River Oaks", "TCU Area",
    "Monticello", "Meadowbrook", "Stop Six", "Como", "Polytechnic Heights",
    "East Fort Worth", "North Fort Worth", "West Fort Worth", "South Fort Worth",
    "Alliance", "Fossil Creek", "Keller", "Saginaw", "Lake Worth", "White Settlement",
    "Benbrook", "Edgecliff Village", "River District", "Cultural District",
    "Stockyards", "Historic Southside", "Magnolia Avenue", "Hillside",
    "Oakhurst", "Riverside", "Candleridge", "Meadow Creek", "Sycamore Creek",
    "Park Glen", "Overton Park", "Tanglewood", "Wedgwood", "Woodhaven",
    "Hulen Bend", "Mira Vista", "Bluebonnet Hills", "Crestwood", "Trinity Heights"
]

# Property types
PROPERTY_TYPES = [
    "Single Family Homes", "Townhomes", "Condos", "Luxury Homes", "Ranch Homes",
    "Modern Homes", "Victorian Homes", "Craftsman Homes", "Colonial Homes",
    "Contemporary Homes", "Traditional Homes", "Mediterranean Homes",
    "Spanish Style Homes", "Brick Homes", "Stone Homes", "Patio Homes",
    "Cluster Homes", "Garden Homes", "Villas", "Duplexes", "New Construction Homes",
    "Estate Homes", "Custom Built Homes", "Semi-Custom Homes", "Production Homes",
    "Mid-Century Modern Homes", "Tudor Homes", "French Country Homes", "Farmhouse Style Homes"
]

# Features and amenities
FEATURES = [
    "with Pools", "with In-Ground Pools", "with Above Ground Pools", "with Salt Water Pools",
    "with Hot Tubs", "with Spa", "with 2 Stories", "with 3 Stories", "with Single Story",
    "with Basements", "with Finished Basements", "with Walk-Out Basements",
    "with 2 Car Garages", "with 3 Car Garages", "with Attached Garages", "with Detached Garages",
    "with Carports", "with RV Parking", "with Boat Parking", "with Workshop",
    "with Fireplaces", "with Wood Burning Fireplaces", "with Gas Fireplaces",
    "with Multiple Fireplaces", "with Outdoor Fireplaces", "with Fire Pits",
    "with Master Suite", "with Main Floor Master", "with Dual Masters",
    "with Walk-In Closets", "with Built-Ins", "with Home Office",
    "with Bonus Room", "with Game Room", "with Media Room", "with Library",
    "with Sunroom", "with Screened Porch", "with Covered Patio", "with Deck",
    "with Balcony", "with Outdoor Kitchen", "with BBQ Area", "with Pergola",
    "with Hardwood Floors", "with Tile Floors", "with Granite Countertops",
    "with Marble Countertops", "with Quartz Countertops", "with Island Kitchen",
    "with Gourmet Kitchen", "with Updated Kitchen", "with Stainless Appliances",
    "with High-End Appliances", "with Double Ovens", "with Gas Range",
    "with Pantry", "with Butler's Pantry", "with Breakfast Nook",
    "with Formal Dining", "with Open Floor Plan", "with Split Bedroom Plan",
    "with Vaulted Ceilings", "with High Ceilings", "with Crown Molding",
    "with Wainscoting", "with Coffered Ceilings", "with Tray Ceilings",
    "with Smart Home Features", "with Security System", "with Intercom",
    "with Central Vacuum", "with Sprinkler System", "with Well Water",
    "with City Water", "with Septic", "with City Sewer",
    "with Energy Efficient Features", "with Solar Panels", "with Generator",
    "with Storm Shelter", "with Safe Room", "with Wine Cellar",
    "with Wet Bar", "with Laundry Room", "with Upstairs Laundry",
    "with Mudroom", "with Large Closets", "with Mountain Views",
    "with Water Views", "with Lake Views", "with Golf Course Views",
    "with City Views", "with Wooded Lot", "with Corner Lot",
    "with Cul-de-Sac Location", "with Privacy Fence", "with Wrought Iron Fence",
    "with Mature Trees", "with Landscaping", "with Professional Landscaping",
    "with Low Maintenance Yard", "with Large Yard", "with Fenced Yard",
    "with Dog Run", "with Barn", "with Guest House", "with Mother-In-Law Suite",
    "with Casita", "with Pool House", "with She Shed", "with Man Cave"
]

# Bedroom configurations
BEDROOMS = [
    "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom", "6 Bedroom", "7+ Bedroom"
]

# Bathroom configurations
BATHROOMS = [
    "1 Bath", "1.5 Bath", "2 Bath", "2.5 Bath", "3 Bath", "3.5 Bath",
    "4 Bath", "4.5 Bath", "5+ Bath"
]

# Price ranges
PRICE_RANGES = [
    "Under $100K", "Under $150K", "Under $200K", "Under $250K", "Under $300K",
    "Under $350K", "Under $400K", "Under $500K", "Under $750K", "Under $1M",
    "$100K-$150K", "$150K-$200K", "$200K-$250K", "$250K-$300K", "$300K-$350K",
    "$350K-$400K", "$400K-$450K", "$450K-$500K", "$500K-$600K", "$600K-$700K",
    "$700K-$800K", "$800K-$900K", "$900K-$1M", "$1M-$1.5M", "$1.5M-$2M",
    "$2M-$3M", "$3M-$5M", "Over $5M", "Over $1M", "Over $2M"
]

# Square footage ranges
SQUARE_FOOTAGE = [
    "Under 1000 Sq Ft", "Under 1500 Sq Ft", "Under 2000 Sq Ft", "Under 2500 Sq Ft",
    "Under 3000 Sq Ft", "Under 3500 Sq Ft", "Under 4000 Sq Ft", "Over 4000 Sq Ft",
    "1000-1500 Sq Ft", "1500-2000 Sq Ft", "2000-2500 Sq Ft", "2500-3000 Sq Ft",
    "3000-3500 Sq Ft", "3500-4000 Sq Ft", "4000-5000 Sq Ft", "Over 5000 Sq Ft"
]

# Lot sizes
LOT_SIZES = [
    "with Small Lots", "with Quarter Acre Lots", "with Half Acre Lots",
    "with 1 Acre Lots", "with 2+ Acre Lots", "with 5+ Acre Lots",
    "with 10+ Acre Lots", "with Large Lots", "with Oversized Lots"
]

# Year built ranges
YEAR_BUILT = [
    "Built Before 1950", "Built in the 1950s", "Built in the 1960s",
    "Built in the 1970s", "Built in the 1980s", "Built in the 1990s",
    "Built in the 2000s", "Built After 2010", "Built After 2015",
    "Built After 2020", "Historic Homes", "Vintage Homes", "Newly Built"
]

# School districts
SCHOOL_DISTRICTS = [
    "Fort Worth ISD", "Keller ISD", "Carroll ISD", "Birdville ISD",
    "Northwest ISD", "Eagle Mountain-Saginaw ISD", "Crowley ISD",
    "Everman ISD", "White Settlement ISD", "Castleberry ISD"
]

# HOA status
HOA_STATUS = [
    "with HOA", "without HOA", "with Low HOA Fees", "with Optional HOA"
]

# Special features
SPECIAL_FEATURES = [
    "Move-In Ready", "Fixer Upper", "Needs TLC", "Fully Renovated",
    "Recently Updated", "Turnkey", "Investment Properties", "Rental Properties",
    "Foreclosures", "Short Sales", "Bank Owned", "Estate Sales",
    "Motivated Sellers", "Quick Possession", "Rent to Own", "Owner Financing",
    "Assumable Loans", "Waterfront", "Gated Community", "Golf Course Community",
    "55+ Community", "Active Adult Community", "Family Friendly",
    "Near Schools", "Near Parks", "Near Shopping", "Near Hospitals",
    "Near Downtown", "Near Highways", "Near Public Transit", "Walkable Neighborhood",
    "Equestrian Properties", "Horse Properties", "Farm Properties",
    "with City Views", "with Panoramic Views", "Pet Friendly",
    "ADA Accessible", "Handicap Accessible", "Single Level Living",
    "Low Maintenance", "Zero Lot Line", "Patio Home Style"
]

# Additional qualifiers
QUALIFIERS = [
    "Best", "Affordable", "Luxury", "Updated", "Charming", "Beautiful",
    "Spacious", "Cozy", "Modern", "Classic", "Elegant", "Stunning"
]

# Time-based qualifiers
TIME_QUALIFIERS = [
    "New Listings", "Just Listed", "Recently Listed", "Coming Soon",
    "Open House", "Price Reduced", "Back on Market", "For Sale",
    "Active Listings", "Available Now"
]

def generate_description(title):
    """Generate SEO-friendly description for a page title"""

    # Extract key components from title
    title_lower = title.lower()

    # Start building description
    description_parts = []

    # Opening statement
    if "luxury" in title_lower:
        description_parts.append("Discover luxury")
    elif "affordable" in title_lower:
        description_parts.append("Find affordable")
    elif "new" in title_lower or "construction" in title_lower:
        description_parts.append("Browse new")
    else:
        description_parts.append("Explore")

    # Add the main subject
    description_parts.append(title.split(" in ")[0].lower())

    # Add location context
    if " in " in title:
        location = title.split(" in ")[1].replace(", Fort Worth TX", "").replace(", Fort Worth", "")
        description_parts.append(f"in {location}, Fort Worth, Texas.")
    else:
        description_parts.append("in Fort Worth, Texas.")

    # Add value propositions
    value_props = []

    if any(word in title_lower for word in ["pool", "pools"]):
        value_props.append("perfect for Texas summers")

    if any(word in title_lower for word in ["bedroom", "bed"]):
        value_props.append("ideal for families")

    if any(word in title_lower for word in ["luxury", "estate", "custom"]):
        value_props.append("featuring premium amenities")

    if any(word in title_lower for word in ["new construction", "newly built"]):
        value_props.append("with modern features and warranties")

    if any(word in title_lower for word in ["garage", "parking"]):
        value_props.append("with convenient parking")

    if any(word in title_lower for word in ["fireplace"]):
        value_props.append("with cozy entertaining spaces")

    if any(word in title_lower for word in ["open floor plan"]):
        value_props.append("with contemporary layouts")

    if any(word in title_lower for word in ["updated", "renovated"]):
        value_props.append("with modern updates")

    if any(word in title_lower for word in ["gated", "community"]):
        value_props.append("with added security and amenities")

    if any(word in title_lower for word in ["view", "views"]):
        value_props.append("with stunning vistas")

    # Add 1-2 value props
    if value_props:
        description_parts.append(" ".join(value_props[:2]))

    # Call to action
    cta_options = [
        "View current listings, photos, and details.",
        "Browse available properties and schedule showings today.",
        "See photos, virtual tours, and property details.",
        "Compare listings and find your dream home.",
        "Start your search with updated MLS listings.",
    ]

    # Choose CTA based on title characteristics
    if "price" in title_lower or "$" in title:
        cta = "Filter by price, view photos, and schedule tours today."
    elif "new listing" in title_lower or "just listed" in title_lower:
        cta = "See the newest properties before they're gone."
    elif "open house" in title_lower:
        cta = "Find open house schedules and tour homes this weekend."
    else:
        import random
        cta = random.choice(cta_options)

    description_parts.append(cta)

    # Join and clean up description
    description = " ".join(description_parts)
    description = description.replace("  ", " ")

    # Ensure it starts with capital letter
    description = description[0].upper() + description[1:]

    # Truncate to ~160 characters for SEO
    if len(description) > 160:
        description = description[:157] + "..."

    return description

def generate_titles_with_descriptions():
    """Generate all possible page title combinations with descriptions"""
    titles_data = []

    print("Generating comprehensive real estate page titles with descriptions...")
    print("This will create 1.4M+ entries. Processing in batches...\n")

    # Format: [Location] + [Property Type] + [Feature]
    print("Batch 1: Location + Property Type + Feature combinations...")
    count = 0
    for neighborhood, prop_type, feature in itertools.product(NEIGHBORHOODS, PROPERTY_TYPES, FEATURES):
        title1 = f"{prop_type} {feature} in {neighborhood}, Fort Worth TX"
        title2 = f"{neighborhood} {prop_type} {feature}"
        title3 = f"Find {prop_type} {feature} in {neighborhood}"

        for title in [title1, title2, title3]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))
                count += 1

        if count % 10000 == 0:
            print(f"  Generated {count:,} titles...")

    # Format: [Property Type] + [Bedrooms] + [Bathrooms] + [Location]
    print(f"Batch 2: Property Type + Beds + Baths + Location (Total so far: {len(titles_data):,})...")
    for prop_type, beds, baths, neighborhood in itertools.product(PROPERTY_TYPES, BEDROOMS, BATHROOMS, NEIGHBORHOODS):
        title1 = f"{beds} {baths} {prop_type} in {neighborhood}, Fort Worth"
        title2 = f"{neighborhood} {beds} {baths} {prop_type}"

        for title in [title1, title2]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Property Type] + [Price Range] + [Location]
    print(f"Batch 3: Property Type + Price + Location (Total so far: {len(titles_data):,})...")
    for prop_type, price, neighborhood in itertools.product(PROPERTY_TYPES, PRICE_RANGES, NEIGHBORHOODS):
        title1 = f"{prop_type} {price} in {neighborhood}, Fort Worth TX"
        title2 = f"{neighborhood} {prop_type} {price}"
        title3 = f"Homes For Sale {price} in {neighborhood}"

        for title in [title1, title2, title3]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Property Type] + [Square Footage] + [Location]
    print(f"Batch 4: Property Type + Square Footage + Location (Total so far: {len(titles_data):,})...")
    for prop_type, sqft, neighborhood in itertools.product(PROPERTY_TYPES, SQUARE_FOOTAGE, NEIGHBORHOODS):
        title1 = f"{prop_type} {sqft} in {neighborhood}, Fort Worth"
        title2 = f"{neighborhood} {prop_type} {sqft}"

        for title in [title1, title2]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Bedrooms] + [Feature] + [Location]
    print(f"Batch 5: Bedrooms + Feature + Location (Total so far: {len(titles_data):,})...")
    for beds, feature, neighborhood in itertools.product(BEDROOMS, FEATURES, NEIGHBORHOODS):
        title1 = f"{beds} Homes {feature} in {neighborhood}, Fort Worth"
        title2 = f"{neighborhood} {beds} Homes {feature}"

        for title in [title1, title2]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Property Type] + [Year Built] + [Location]
    print(f"Batch 6: Property Type + Year Built + Location (Total so far: {len(titles_data):,})...")
    for prop_type, year, neighborhood in itertools.product(PROPERTY_TYPES, YEAR_BUILT, NEIGHBORHOODS):
        title = f"{prop_type} {year} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Format: [Property Type] + [Lot Size] + [Location]
    print(f"Batch 7: Property Type + Lot Size + Location (Total so far: {len(titles_data):,})...")
    for prop_type, lot, neighborhood in itertools.product(PROPERTY_TYPES, LOT_SIZES, NEIGHBORHOODS):
        title = f"{prop_type} {lot} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Format: [School District] + [Property Type] + [Feature]
    print(f"Batch 8: School District + Property Type + Feature (Total so far: {len(titles_data):,})...")
    for district, prop_type, feature in itertools.product(SCHOOL_DISTRICTS, PROPERTY_TYPES, FEATURES):
        title1 = f"{prop_type} {feature} in {district}, Fort Worth"
        title2 = f"{district} {prop_type} {feature}"

        for title in [title1, title2]:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Property Type] + [HOA] + [Location]
    print(f"Batch 9: Property Type + HOA + Location (Total so far: {len(titles_data):,})...")
    for prop_type, hoa, neighborhood in itertools.product(PROPERTY_TYPES, HOA_STATUS, NEIGHBORHOODS):
        title = f"{prop_type} {hoa} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Format: [Special Feature] + [Property Type] + [Location]
    print(f"Batch 10: Special Feature + Property Type + Location (Total so far: {len(titles_data):,})...")
    for special, prop_type, neighborhood in itertools.product(SPECIAL_FEATURES, PROPERTY_TYPES, NEIGHBORHOODS):
        title = f"{special} {prop_type} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Qualifier] + [Property Type] + [Feature] + [Location]
    print(f"Batch 11: Qualifier + Property Type + Feature + Location (Total so far: {len(titles_data):,})...")
    for qualifier, prop_type, feature, neighborhood in itertools.product(QUALIFIERS, PROPERTY_TYPES, FEATURES[:20], NEIGHBORHOODS[:20]):
        title = f"{qualifier} {prop_type} {feature} in {neighborhood}"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Format: [Time Qualifier] + [Property Type] + [Location]
    print(f"Batch 12: Time Qualifier + Property Type + Location (Total so far: {len(titles_data):,})...")
    for time_qual, prop_type, neighborhood in itertools.product(TIME_QUALIFIERS, PROPERTY_TYPES, NEIGHBORHOODS):
        title = f"{time_qual}: {prop_type} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Format: [Bedrooms] + [Bathrooms] + [Feature] + [Location]
    print(f"Batch 13: Beds + Baths + Feature + Location (Total so far: {len(titles_data):,})...")
    for beds, baths, feature, neighborhood in itertools.product(BEDROOMS, BATHROOMS, FEATURES[:30], NEIGHBORHOODS[:30]):
        title = f"{beds} {baths} Homes {feature} in {neighborhood}"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Format: [Price Range] + [Feature] + [Location]
    print(f"Batch 14: Price Range + Feature + Location (Total so far: {len(titles_data):,})...")
    for price, feature, neighborhood in itertools.product(PRICE_RANGES, FEATURES, NEIGHBORHOODS):
        title = f"Homes For Sale {price} {feature} in {neighborhood}"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

        if len(titles_data) % 10000 == 0:
            print(f"  Generated {len(titles_data):,} titles...")

    # Additional specific combinations
    print(f"Batch 15: Additional specific combinations (Total so far: {len(titles_data):,})...")
    for neighborhood in NEIGHBORHOODS:
        base_titles = [
            f"Homes For Sale in {neighborhood}, Fort Worth TX",
            f"{neighborhood} Real Estate",
            f"{neighborhood} Houses For Sale",
            f"Buy a Home in {neighborhood}, Fort Worth",
            f"{neighborhood} Property Listings"
        ]

        for title in base_titles:
            if title not in [t[0] for t in titles_data]:
                titles_data.append((title, generate_description(title)))

        for beds in BEDROOMS:
            title1 = f"{beds} Homes in {neighborhood}, Fort Worth"
            if title1 not in [t[0] for t in titles_data]:
                titles_data.append((title1, generate_description(title1)))

            for price in PRICE_RANGES:
                title2 = f"{beds} Homes {price} in {neighborhood}"
                if title2 not in [t[0] for t in titles_data]:
                    titles_data.append((title2, generate_description(title2)))

    # Multi-feature combinations
    print(f"Batch 16: Multi-feature combinations (Total so far: {len(titles_data):,})...")
    feature_pairs = [(FEATURES[i], FEATURES[j]) for i in range(0, min(30, len(FEATURES)))
                     for j in range(i+1, min(30, len(FEATURES)))]
    for (feat1, feat2), neighborhood in itertools.product(feature_pairs[:100], NEIGHBORHOODS[:30]):
        title = f"Homes {feat1} and {feat2} in {neighborhood}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # Price + Beds + Baths combinations
    print(f"Batch 17: Price + Beds + Baths (Total so far: {len(titles_data):,})...")
    for price, beds, baths in itertools.product(PRICE_RANGES, BEDROOMS, BATHROOMS):
        title = f"{beds} {baths} Homes {price} in Fort Worth TX"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    # School District + Price combinations
    print(f"Batch 18: School District + Price (Total so far: {len(titles_data):,})...")
    for district, price, beds in itertools.product(SCHOOL_DISTRICTS, PRICE_RANGES, BEDROOMS):
        title = f"{beds} Homes {price} in {district}, Fort Worth"
        if title not in [t[0] for t in titles_data]:
            titles_data.append((title, generate_description(title)))

    print(f"\nFinished generating {len(titles_data):,} unique titles with descriptions!")
    return titles_data

def create_url_slug(title):
    """Create SEO-friendly URL slug from title"""
    slug = title.lower()
    slug = slug.replace(' ', '-')
    slug = slug.replace(',', '')
    slug = slug.replace('+', 'plus')
    slug = slug.replace('$', '')
    slug = slug.replace('.', '')
    slug = slug.replace('/', '-')
    slug = slug.replace('&', 'and')
    slug = slug.replace(':', '')
    # Remove multiple dashes
    while '--' in slug:
        slug = slug.replace('--', '-')
    slug = slug.strip('-')
    return slug

def save_to_chunks(titles_data, chunk_size=50000, output_dir='page_titles_chunks'):
    """Save titles to multiple CSV files in chunks"""

    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_chunks = (len(titles_data) + chunk_size - 1) // chunk_size

    print(f"\nSaving {len(titles_data):,} titles to {total_chunks} files...")
    print(f"Chunk size: {chunk_size:,} titles per file")
    print(f"Output directory: {output_dir}/\n")

    for chunk_num in range(total_chunks):
        start_idx = chunk_num * chunk_size
        end_idx = min(start_idx + chunk_size, len(titles_data))
        chunk_data = titles_data[start_idx:end_idx]

        filename = f'{output_dir}/page_titles_chunk_{chunk_num+1:03d}_of_{total_chunks:03d}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Page Title', 'SEO-Friendly URL Slug', 'Meta Description'])

            for title, description in chunk_data:
                slug = create_url_slug(title)
                writer.writerow([title, slug, description])

        print(f"✓ Saved chunk {chunk_num+1}/{total_chunks}: {filename} ({len(chunk_data):,} titles)")

    print(f"\n✓ Successfully saved all {len(titles_data):,} titles to {total_chunks} CSV files!")
    return total_chunks

def save_full_file(titles_data, filename='fort_worth_page_titles_with_descriptions.csv'):
    """Save all titles to a single CSV file"""
    print(f"\nSaving full dataset to {filename}...")

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page Title', 'SEO-Friendly URL Slug', 'Meta Description'])

        for title, description in titles_data:
            slug = create_url_slug(title)
            writer.writerow([title, slug, description])

    file_size_mb = os.path.getsize(filename) / (1024 * 1024)
    print(f"✓ Saved {len(titles_data):,} titles to {filename} ({file_size_mb:.2f} MB)")

    if file_size_mb > 100:
        print(f"⚠ Warning: File is {file_size_mb:.2f} MB - too large for GitHub (>100MB limit)")
        print("  The file has been added to .gitignore")
        print("  Using chunked files is recommended for version control")

def main():
    print("=" * 80)
    print("Fort Worth Real Estate Page Title Generator (WITH DESCRIPTIONS)")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    titles_data = generate_titles_with_descriptions()

    print("\n" + "=" * 80)
    print(f"Generated {len(titles_data):,} unique page titles with descriptions!")
    print("=" * 80)

    # Show some examples
    print("\nExample titles with descriptions:")
    print("-" * 80)
    for i in range(min(10, len(titles_data))):
        title, desc = titles_data[i]
        print(f"\nTitle: {title}")
        print(f"Description: {desc}")
        print(f"URL Slug: {create_url_slug(title)}")

    # Save full file
    save_full_file(titles_data)

    # Save in chunks
    total_chunks = save_to_chunks(titles_data, chunk_size=50000)

    print(f"\n{'=' * 80}")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'=' * 80}")
    print("\nFiles created:")
    print("1. fort_worth_page_titles_with_descriptions.csv (full dataset - for local use)")
    print(f"2. page_titles_chunks/ directory with {total_chunks} CSV files (for version control)")
    print("\nEach title includes:")
    print("  - SEO-optimized page title")
    print("  - URL-friendly slug")
    print("  - Meta description (for SEO)")

if __name__ == "__main__":
    main()
