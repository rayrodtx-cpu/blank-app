"""
Real Estate Page Title Generator for Fort Worth, TX
Generates 50,000+ unique page titles for SEO optimization
"""

import itertools
import csv
from datetime import datetime

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

def generate_titles():
    """Generate all possible page title combinations"""
    titles = set()

    # Format: [Location] + [Property Type] + [Feature]
    print("Generating: Location + Property Type + Feature combinations...")
    for neighborhood, prop_type, feature in itertools.product(NEIGHBORHOODS, PROPERTY_TYPES, FEATURES):
        titles.add(f"{prop_type} {feature} in {neighborhood}, Fort Worth TX")
        titles.add(f"{neighborhood} {prop_type} {feature}")
        titles.add(f"Find {prop_type} {feature} in {neighborhood}")

    # Format: [Property Type] + [Bedrooms] + [Bathrooms] + [Location]
    print("Generating: Property Type + Beds + Baths + Location combinations...")
    for prop_type, beds, baths, neighborhood in itertools.product(PROPERTY_TYPES, BEDROOMS, BATHROOMS, NEIGHBORHOODS):
        titles.add(f"{beds} {baths} {prop_type} in {neighborhood}, Fort Worth")
        titles.add(f"{neighborhood} {beds} {baths} {prop_type}")

    # Format: [Property Type] + [Price Range] + [Location]
    print("Generating: Property Type + Price + Location combinations...")
    for prop_type, price, neighborhood in itertools.product(PROPERTY_TYPES, PRICE_RANGES, NEIGHBORHOODS):
        titles.add(f"{prop_type} {price} in {neighborhood}, Fort Worth TX")
        titles.add(f"{neighborhood} {prop_type} {price}")
        titles.add(f"Homes For Sale {price} in {neighborhood}")

    # Format: [Property Type] + [Square Footage] + [Location]
    print("Generating: Property Type + Square Footage + Location combinations...")
    for prop_type, sqft, neighborhood in itertools.product(PROPERTY_TYPES, SQUARE_FOOTAGE, NEIGHBORHOODS):
        titles.add(f"{prop_type} {sqft} in {neighborhood}, Fort Worth")
        titles.add(f"{neighborhood} {prop_type} {sqft}")

    # Format: [Bedrooms] + [Feature] + [Location]
    print("Generating: Bedrooms + Feature + Location combinations...")
    for beds, feature, neighborhood in itertools.product(BEDROOMS, FEATURES, NEIGHBORHOODS):
        titles.add(f"{beds} Homes {feature} in {neighborhood}, Fort Worth")
        titles.add(f"{neighborhood} {beds} Homes {feature}")

    # Format: [Property Type] + [Year Built] + [Location]
    print("Generating: Property Type + Year Built + Location combinations...")
    for prop_type, year, neighborhood in itertools.product(PROPERTY_TYPES, YEAR_BUILT, NEIGHBORHOODS):
        titles.add(f"{prop_type} {year} in {neighborhood}, Fort Worth")

    # Format: [Property Type] + [Lot Size] + [Location]
    print("Generating: Property Type + Lot Size + Location combinations...")
    for prop_type, lot, neighborhood in itertools.product(PROPERTY_TYPES, LOT_SIZES, NEIGHBORHOODS):
        titles.add(f"{prop_type} {lot} in {neighborhood}, Fort Worth")

    # Format: [School District] + [Property Type] + [Feature]
    print("Generating: School District + Property Type + Feature combinations...")
    for district, prop_type, feature in itertools.product(SCHOOL_DISTRICTS, PROPERTY_TYPES, FEATURES):
        titles.add(f"{prop_type} {feature} in {district}, Fort Worth")
        titles.add(f"{district} {prop_type} {feature}")

    # Format: [Property Type] + [HOA] + [Location]
    print("Generating: Property Type + HOA + Location combinations...")
    for prop_type, hoa, neighborhood in itertools.product(PROPERTY_TYPES, HOA_STATUS, NEIGHBORHOODS):
        titles.add(f"{prop_type} {hoa} in {neighborhood}, Fort Worth")

    # Format: [Special Feature] + [Property Type] + [Location]
    print("Generating: Special Feature + Property Type + Location combinations...")
    for special, prop_type, neighborhood in itertools.product(SPECIAL_FEATURES, PROPERTY_TYPES, NEIGHBORHOODS):
        titles.add(f"{special} {prop_type} in {neighborhood}, Fort Worth")

    # Format: [Qualifier] + [Property Type] + [Feature] + [Location]
    print("Generating: Qualifier + Property Type + Feature + Location combinations...")
    for qualifier, prop_type, feature, neighborhood in itertools.product(QUALIFIERS, PROPERTY_TYPES, FEATURES[:20], NEIGHBORHOODS[:20]):
        titles.add(f"{qualifier} {prop_type} {feature} in {neighborhood}")

    # Format: [Time Qualifier] + [Property Type] + [Location]
    print("Generating: Time Qualifier + Property Type + Location combinations...")
    for time_qual, prop_type, neighborhood in itertools.product(TIME_QUALIFIERS, PROPERTY_TYPES, NEIGHBORHOODS):
        titles.add(f"{time_qual}: {prop_type} in {neighborhood}, Fort Worth")

    # Format: [Bedrooms] + [Bathrooms] + [Feature] + [Location]
    print("Generating: Beds + Baths + Feature + Location combinations...")
    for beds, baths, feature, neighborhood in itertools.product(BEDROOMS, BATHROOMS, FEATURES[:30], NEIGHBORHOODS[:30]):
        titles.add(f"{beds} {baths} Homes {feature} in {neighborhood}")

    # Format: [Price Range] + [Feature] + [Location]
    print("Generating: Price Range + Feature + Location combinations...")
    for price, feature, neighborhood in itertools.product(PRICE_RANGES, FEATURES, NEIGHBORHOODS):
        titles.add(f"Homes For Sale {price} {feature} in {neighborhood}")

    # Additional specific combinations
    print("Generating: Additional specific combinations...")
    for neighborhood in NEIGHBORHOODS:
        titles.add(f"Homes For Sale in {neighborhood}, Fort Worth TX")
        titles.add(f"{neighborhood} Real Estate")
        titles.add(f"{neighborhood} Houses For Sale")
        titles.add(f"Buy a Home in {neighborhood}, Fort Worth")
        titles.add(f"{neighborhood} Property Listings")

        for beds in BEDROOMS:
            titles.add(f"{beds} Homes in {neighborhood}, Fort Worth")
            for price in PRICE_RANGES:
                titles.add(f"{beds} Homes {price} in {neighborhood}")

    # Multi-feature combinations
    print("Generating: Multi-feature combinations...")
    feature_pairs = [(FEATURES[i], FEATURES[j]) for i in range(0, min(30, len(FEATURES)))
                     for j in range(i+1, min(30, len(FEATURES)))]
    for (feat1, feat2), neighborhood in itertools.product(feature_pairs[:100], NEIGHBORHOODS[:30]):
        titles.add(f"Homes {feat1} and {feat2} in {neighborhood}, Fort Worth")

    # Price + Beds + Baths combinations
    print("Generating: Price + Beds + Baths combinations...")
    for price, beds, baths in itertools.product(PRICE_RANGES, BEDROOMS, BATHROOMS):
        titles.add(f"{beds} {baths} Homes {price} in Fort Worth TX")

    # School District + Price combinations
    print("Generating: School District + Price combinations...")
    for district, price, beds in itertools.product(SCHOOL_DISTRICTS, PRICE_RANGES, BEDROOMS):
        titles.add(f"{beds} Homes {price} in {district}, Fort Worth")

    return sorted(list(titles))

def save_titles(titles, filename='fort_worth_page_titles.csv'):
    """Save titles to CSV file"""
    print(f"\nSaving {len(titles)} titles to {filename}...")

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page Title', 'SEO-Friendly URL Slug'])

        for title in titles:
            # Create URL slug
            slug = title.lower()
            slug = slug.replace(' ', '-')
            slug = slug.replace(',', '')
            slug = slug.replace('+', 'plus')
            slug = slug.replace('$', '')
            slug = slug.replace('.', '')
            slug = slug.replace('/', '-')
            slug = slug.replace('&', 'and')
            # Remove multiple dashes
            while '--' in slug:
                slug = slug.replace('--', '-')
            slug = slug.strip('-')

            writer.writerow([title, slug])

    print(f"✓ Successfully saved {len(titles)} page titles!")

def main():
    print("=" * 70)
    print("Fort Worth Real Estate Page Title Generator")
    print("=" * 70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    titles = generate_titles()

    print("\n" + "=" * 70)
    print(f"Generated {len(titles):,} unique page titles!")
    print("=" * 70)

    # Show some examples
    print("\nExample titles:")
    for i, title in enumerate(titles[:20], 1):
        print(f"{i}. {title}")

    save_titles(titles)

    print(f"\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nThe titles have been saved to 'fort_worth_page_titles.csv'")
    print("Each title includes an SEO-friendly URL slug for easy implementation.")

if __name__ == "__main__":
    main()
