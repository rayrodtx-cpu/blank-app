"""
Real Estate Page Title Generator for San Antonio
Generates 50,000+ unique page titles for SEO
"""

import itertools
import csv

# San Antonio Neighborhoods and Areas
NEIGHBORHOODS = [
    "Alamo Heights", "Stone Oak", "Terrell Hills", "Olmos Park", "The Dominion",
    "Shavano Park", "Leon Valley", "Helotes", "Fair Oaks Ranch", "Boerne",
    "Hollywood Park", "Hill Country Village", "Castle Hills", "Balcones Heights",
    "Downtown San Antonio", "Southtown", "King William", "Monte Vista", "Tobin Hill",
    "Mahncke Park", "Beacon Hill", "Government Hill", "Dignowity Hill", "Lavaca",
    "Medical Center", "UTSA Area", "Northwest San Antonio", "Northeast San Antonio",
    "Southwest San Antonio", "Southeast San Antonio", "North Central", "Far West Side",
    "The Rim", "La Cantera", "Huebner Oaks", "Vance Jackson", "Blanco",
    "Bitters", "Encino Park", "Inwood", "Rogers Ranch", "Sonterra", "Deerfield",
    "Redland Oaks", "Crownridge", "Churchill Estates", "Hunters Creek",
    "Braun Station", "Bulverde", "Spring Branch", "Timberwood Park", "Cibolo",
    "Schertz", "Selma", "Live Oak", "Universal City", "Converse", "Windcrest",
    "Kirby", "China Grove", "Somerset", "Von Ormy", "Lytle", "Atascosa",
    "Elmendorf", "Floresville", "La Vernia", "Adkins", "St Hedwig",
    "Garden Ridge", "New Braunfels", "Seguin", "Canyon Lake", "Bandera",
    "Pipe Creek", "Comfort", "Boerne Stage", "Scenic Oaks", "Culebra",
    "Westover Hills", "Macdona", "Castroville", "Hondo", "Devine",
    "Lackland AFB Area", "JBSA Area", "Fort Sam Houston Area", "Brooks City Base",
    "Mission San Jose", "Mission Concepcion", "South San Antonio", "West San Antonio"
]

# Property Types
PROPERTY_TYPES = [
    "homes", "houses", "properties", "real estate", "condos", "townhomes",
    "townhouses", "single family homes", "estates", "ranches", "land",
    "luxury homes", "mansions", "villas", "bungalows", "cottages",
    "duplexes", "apartments", "new construction homes", "custom homes"
]

# Features
FEATURES = [
    "with pools", "with swimming pools", "with garage", "with 2 car garage",
    "with 3 car garage", "with acreage", "with views", "with hill country views",
    "with hardwood floors", "with granite countertops", "with master suite",
    "with office", "with game room", "with media room", "with chef's kitchen",
    "with outdoor kitchen", "with covered patio", "with fireplace",
    "with multiple fireplaces", "with walk-in closets", "with smart home features",
    "with solar panels", "with updated kitchen", "with updated bathrooms",
    "with gourmet kitchen", "with large backyard", "with fenced yard",
    "with private backyard", "with landscaping", "with mature trees",
    "with tile flooring", "with wood flooring", "with carpet",
    "with stainless steel appliances", "with island kitchen", "with breakfast nook",
    "with formal dining", "with open floor plan", "with high ceilings",
    "with vaulted ceilings", "with crown molding", "with wainscoting",
    "with bay windows", "with French doors", "with pocket doors",
    "with balcony", "with terrace", "with courtyard", "with RV parking",
    "with boat parking", "with workshop", "with barn", "with guest house",
    "with casita", "with in-law suite", "with basement", "with wine cellar",
    "with safe room", "with security system", "with irrigation system",
    "with sprinkler system", "with septic", "with well water", "with city water",
    "with HOA", "without HOA", "with gated entry", "with circle driveway"
]

# Bedrooms/Bathrooms
BEDROOMS = ["1 bedroom", "2 bedroom", "3 bedroom", "4 bedroom", "5 bedroom", "6 bedroom"]
BATHROOMS = ["1 bathroom", "2 bathroom", "2.5 bathroom", "3 bathroom", "3.5 bathroom", "4 bathroom"]

# Stories
STORIES = ["1 story", "2 story", "3 story", "single story", "two story"]

# Price Ranges
PRICE_RANGES = [
    "under 100k", "under 150k", "under 200k", "under 250k", "under 300k",
    "under 350k", "under 400k", "under 500k", "under 600k", "under 700k",
    "under 800k", "under 1 million", "over 1 million", "over 2 million",
    "100k to 200k", "200k to 300k", "300k to 400k", "400k to 500k",
    "500k to 750k", "750k to 1 million", "affordable", "luxury"
]

# Square Footage
SQFT = [
    "under 1000 sqft", "under 1500 sqft", "under 2000 sqft", "under 2500 sqft",
    "under 3000 sqft", "over 2000 sqft", "over 3000 sqft", "over 4000 sqft",
    "1000 to 1500 sqft", "1500 to 2000 sqft", "2000 to 3000 sqft"
]

# Lot Size
LOT_SIZES = [
    "large lot", "corner lot", "cul-de-sac lot", "0.5 acre", "1 acre",
    "2 acres", "3 acres", "5 acres", "10 acres", "acreage"
]

# School Districts
SCHOOL_DISTRICTS = [
    "Alamo Heights ISD", "North East ISD", "Northside ISD", "North East ISD",
    "San Antonio ISD", "Judson ISD", "East Central ISD", "Schertz-Cibolo-Universal City ISD",
    "Comal ISD", "New Braunfels ISD", "Boerne ISD", "Medina Valley ISD",
    "Southside ISD", "Edgewood ISD", "Harlandale ISD", "Somerset ISD"
]

# Special Categories
SPECIAL = [
    "gated community", "golf course community", "waterfront", "hill country",
    "newly renovated", "move-in ready", "fixer upper", "investment property",
    "short sale", "foreclosure", "new construction", "pre-construction",
    "55+ community", "active adult community", "equestrian property",
    "ranch property", "farm", "commercial property", "residential lots",
    "build-to-suit", "custom build lots", "greenbelt", "park view"
]

# Action Words
ACTIONS = [
    "for sale", "for sale in", "available in", "listings in", "in"
]

# Time-based
TIME = [
    "new listings", "recently listed", "just listed", "coming soon",
    "price reduced", "open house", "new this week"
]

def generate_titles():
    """Generate comprehensive list of real estate page titles"""
    titles = set()  # Use set to avoid duplicates

    # Pattern 1: [Property Type] in [Neighborhood]
    for prop_type in PROPERTY_TYPES:
        for neighborhood in NEIGHBORHOODS:
            titles.add(f"{prop_type} in {neighborhood}")
            titles.add(f"{prop_type} for sale in {neighborhood}")
            titles.add(f"{neighborhood} {prop_type}")
            titles.add(f"{neighborhood} {prop_type} for sale")

    # Pattern 2: [Property Type] with [Feature] in [Neighborhood]
    for prop_type in PROPERTY_TYPES[:10]:  # Use subset to manage combinations
        for feature in FEATURES[:30]:
            for neighborhood in NEIGHBORHOODS[:40]:
                titles.add(f"{prop_type} {feature} in {neighborhood}")
                titles.add(f"{neighborhood} {prop_type} {feature}")

    # Pattern 3: [Bedrooms] [Property Type] in [Neighborhood]
    for bedrooms in BEDROOMS:
        for prop_type in PROPERTY_TYPES[:8]:
            for neighborhood in NEIGHBORHOODS:
                titles.add(f"{bedrooms} {prop_type} in {neighborhood}")
                titles.add(f"{neighborhood} {bedrooms} {prop_type}")

    # Pattern 4: [Stories] [Property Type] in [Neighborhood]
    for stories in STORIES:
        for prop_type in PROPERTY_TYPES[:8]:
            for neighborhood in NEIGHBORHOODS[:50]:
                titles.add(f"{stories} {prop_type} in {neighborhood}")
                titles.add(f"{neighborhood} {stories} {prop_type}")

    # Pattern 5: [Bedrooms] [Bathrooms] [Property Type] in [Neighborhood]
    for bedrooms in BEDROOMS:
        for bathrooms in BATHROOMS:
            for prop_type in PROPERTY_TYPES[:6]:
                for neighborhood in NEIGHBORHOODS[:30]:
                    titles.add(f"{bedrooms} {bathrooms} {prop_type} in {neighborhood}")

    # Pattern 6: [Stories] [Property Type] with [Feature] in [Neighborhood]
    for stories in STORIES:
        for prop_type in PROPERTY_TYPES[:5]:
            for feature in FEATURES[:20]:
                for neighborhood in NEIGHBORHOODS[:25]:
                    titles.add(f"{stories} {prop_type} {feature} in {neighborhood}")

    # Pattern 7: [Price Range] [Property Type] in [Neighborhood]
    for price in PRICE_RANGES:
        for prop_type in PROPERTY_TYPES[:10]:
            for neighborhood in NEIGHBORHOODS[:40]:
                titles.add(f"{prop_type} {price} in {neighborhood}")
                titles.add(f"{neighborhood} {prop_type} {price}")

    # Pattern 8: [Property Type] with [Feature]
    for prop_type in PROPERTY_TYPES:
        for feature in FEATURES:
            titles.add(f"{prop_type} {feature}")
            titles.add(f"{prop_type} {feature} in San Antonio")

    # Pattern 9: [Bedrooms] [Bathrooms] [Property Type] with [Feature]
    for bedrooms in BEDROOMS:
        for bathrooms in BATHROOMS:
            for prop_type in PROPERTY_TYPES[:5]:
                for feature in FEATURES[:15]:
                    titles.add(f"{bedrooms} {bathrooms} {prop_type} {feature}")
                    titles.add(f"{bedrooms} {bathrooms} {prop_type} {feature} in San Antonio")

    # Pattern 10: [Special] [Property Type] in [Neighborhood]
    for special in SPECIAL:
        for prop_type in PROPERTY_TYPES[:8]:
            for neighborhood in NEIGHBORHOODS[:40]:
                titles.add(f"{special} {prop_type} in {neighborhood}")
                titles.add(f"{neighborhood} {special} {prop_type}")

    # Pattern 11: [School District] [Property Type]
    for district in SCHOOL_DISTRICTS:
        for prop_type in PROPERTY_TYPES[:10]:
            titles.add(f"{prop_type} in {district}")
            titles.add(f"{district} {prop_type}")
            for bedrooms in BEDROOMS:
                titles.add(f"{bedrooms} {prop_type} in {district}")

    # Pattern 12: [Time] [Property Type] in [Neighborhood]
    for time_desc in TIME:
        for prop_type in PROPERTY_TYPES[:8]:
            for neighborhood in NEIGHBORHOODS[:30]:
                titles.add(f"{time_desc} {prop_type} in {neighborhood}")

    # Pattern 13: [SQFT] [Property Type] in [Neighborhood]
    for sqft in SQFT:
        for prop_type in PROPERTY_TYPES[:6]:
            for neighborhood in NEIGHBORHOODS[:30]:
                titles.add(f"{prop_type} {sqft} in {neighborhood}")

    # Pattern 14: [Property Type] on [Lot Size] in [Neighborhood]
    for prop_type in PROPERTY_TYPES[:8]:
        for lot_size in LOT_SIZES:
            for neighborhood in NEIGHBORHOODS[:25]:
                titles.add(f"{prop_type} on {lot_size} in {neighborhood}")

    # Pattern 15: Combined features
    for bedrooms in BEDROOMS:
        for stories in STORIES[:3]:
            for feature in FEATURES[:10]:
                for neighborhood in NEIGHBORHOODS[:20]:
                    titles.add(f"{bedrooms} {stories} {feature} in {neighborhood}")

    # Pattern 16: Price + Bedrooms + Neighborhood
    for price in PRICE_RANGES[:15]:
        for bedrooms in BEDROOMS:
            for neighborhood in NEIGHBORHOODS[:25]:
                titles.add(f"{bedrooms} homes {price} in {neighborhood}")

    # Pattern 17: Multiple features combined
    feature_pairs = [
        ("with pools", "with garage"),
        ("with pools", "with large backyard"),
        ("with master suite", "with office"),
        ("with game room", "with media room"),
        ("new construction", "with smart home features"),
        ("with acreage", "with barn"),
        ("with hill country views", "with pools"),
    ]

    for feature1, feature2 in feature_pairs:
        for prop_type in PROPERTY_TYPES[:6]:
            for neighborhood in NEIGHBORHOODS[:20]:
                titles.add(f"{prop_type} {feature1} and {feature2} in {neighborhood}")

    # Pattern 18: General San Antonio searches
    for prop_type in PROPERTY_TYPES:
        titles.add(f"{prop_type} in San Antonio")
        titles.add(f"{prop_type} for sale in San Antonio")
        titles.add(f"San Antonio {prop_type}")
        titles.add(f"San Antonio {prop_type} for sale")

        for feature in FEATURES[:20]:
            titles.add(f"San Antonio {prop_type} {feature}")

    # Pattern 19: Bedrooms + Stories + Neighborhood
    for bedrooms in BEDROOMS:
        for stories in STORIES:
            for neighborhood in NEIGHBORHOODS:
                titles.add(f"{bedrooms} {stories} homes in {neighborhood}")

    # Pattern 20: Additional specific combinations
    for prop_type in PROPERTY_TYPES[:5]:
        for bedrooms in BEDROOMS:
            for feature in FEATURES[:10]:
                for price in PRICE_RANGES[:10]:
                    titles.add(f"{bedrooms} {prop_type} {feature} {price}")

    return sorted(list(titles))

def main():
    print("Generating real estate page titles for San Antonio...")
    titles = generate_titles()

    print(f"Generated {len(titles):,} unique page titles")

    # Save to CSV
    csv_filename = "san_antonio_real_estate_page_titles.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Page Title', 'URL Slug'])

        for title in titles:
            # Create URL-friendly slug
            slug = title.lower()
            slug = slug.replace(' ', '-')
            slug = slug.replace('+', 'plus')
            slug = slug.replace('.', '')
            slug = slug.replace(',', '')
            slug = slug.replace("'", '')
            slug = slug.replace('/', '-')

            writer.writerow([title, slug])

    print(f"Saved to {csv_filename}")

    # Save to text file as well
    txt_filename = "san_antonio_real_estate_page_titles.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(f"{title}\n")

    print(f"Saved to {txt_filename}")

    # Print sample titles
    print("\nSample titles (first 50):")
    for i, title in enumerate(titles[:50], 1):
        print(f"{i}. {title}")

if __name__ == "__main__":
    main()
