#!/usr/bin/env python3
"""
Generate 1M+ SEO-optimized page titles with descriptions in CSV format
for Corpus Christi real estate website.
"""

import itertools
import csv
import re
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

# Neighborhood descriptions for variety
neighborhood_highlights = {
    "Corpus Christi": "the coastal heart of South Texas with stunning bay views and beach access",
    "Padre Island": "Texas's premier barrier island offering pristine beaches and coastal living",
    "Flour Bluff": "a family-friendly community with excellent schools and easy beach access",
    "Calallen": "a highly-rated school district area with suburban charm",
    "Ocean Drive": "an upscale waterfront community with magnificent bay views",
    "Downtown Corpus Christi": "the vibrant urban core with cultural attractions and waterfront dining",
    "North Padre Island": "beachfront paradise with resort-style amenities",
    "Port Aransas": "a charming beach town with relaxed island atmosphere",
    "Southside": "an established area with diverse housing and convenient amenities",
    "Bay Area": "waterfront living with boating and fishing opportunities",
}

def create_url_slug(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def generate_description(title, components):
    """Generate SEO-optimized description based on title components."""
    prop_type = components.get('property_type', 'homes')
    location = components.get('location', 'Corpus Christi')
    bedroom = components.get('bedroom', '')
    bathroom = components.get('bathroom', '')
    feature = components.get('feature', '')
    price = components.get('price', '')
    condition = components.get('condition', '')
    qualifier = components.get('qualifier', '')

    # Base description templates
    templates = [
        f"Browse {title.lower()} for sale. Find your perfect {prop_type.lower()} in {location}, TX with our comprehensive listings. Updated daily with new properties, photos, and pricing.",
        f"Discover {title.lower()} in the Corpus Christi area. View photos, prices, and details for {prop_type.lower()} currently available in {location}. Schedule your showing today.",
        f"Search {title.lower()} with our easy-to-use property finder. Explore {prop_type.lower()} in {location}, Texas featuring detailed listings, virtual tours, and neighborhood information.",
        f"Find {title.lower()} that match your criteria. Browse current listings in {location}, TX with high-quality photos, pricing, and property details. Contact us to schedule a tour.",
        f"Explore {title.lower()} on the market now. Our {location} real estate listings feature {prop_type.lower()} with complete details, photos, and pricing information.",
    ]

    # Add specific details based on components
    details = []

    if bedroom:
        details.append(f"spacious {bedroom.lower()} layouts")
    if bathroom:
        details.append(f"{bathroom.lower()} configurations")
    if feature:
        feat_clean = feature.replace("with ", "").lower()
        details.append(f"featuring {feat_clean}")
    if price:
        details.append(f"priced {price.lower()}")
    if condition:
        details.append(f"{condition.lower()} properties")
    if qualifier:
        details.append(f"{qualifier.lower()} options")

    # Select base template
    import random
    random.seed(hash(title))  # Consistent randomization based on title
    base = random.choice(templates)

    # Add neighborhood highlight if available
    neighborhood_info = ""
    for hood, highlight in neighborhood_highlights.items():
        if hood in location:
            neighborhood_info = f" {location} is {highlight}."
            break

    # Add details if available
    detail_text = ""
    if details:
        if len(details) == 1:
            detail_text = f" Featuring {details[0]}."
        elif len(details) == 2:
            detail_text = f" Featuring {details[0]} and {details[1]}."
        else:
            detail_text = f" Featuring {', '.join(details[:2])}, and more."

    # Add call to action
    cta_options = [
        " Start your home search today!",
        " Contact our experienced agents for personalized service.",
        " Schedule a private showing at your convenience.",
        " Request more information on available properties.",
        " Find your dream home in Corpus Christi today!",
    ]
    cta = random.choice(cta_options)

    description = base + neighborhood_info + detail_text + cta

    # Ensure description is between 120-160 characters for SEO
    if len(description) > 160:
        description = description[:157] + "..."

    return description

def generate_titles_with_descriptions():
    """Generate comprehensive page titles with descriptions."""
    rows = []
    seen_titles = set()

    print("Generating titles and descriptions...")
    print("This will take several minutes...\n")

    counter = 0

    # Strategy 1: Property Type + Feature + Location
    print("Strategy 1: Property Type + Feature + Location...")
    for prop, feat, loc in itertools.product(property_types, features, neighborhoods):
        for title_format in [
            f"{prop} {feat} in {loc}, TX",
            f"{loc} {prop} {feat}",
            f"{feat.replace('with ', '')} {prop} in {loc}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'feature': feat,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 2: Bedrooms + Property Type + Location
    print("Strategy 2: Bedrooms + Property Type + Location...")
    for bed, prop, loc in itertools.product(bedrooms, property_types, neighborhoods):
        for title_format in [
            f"{bed} {prop} in {loc}, TX",
            f"{loc} {bed} {prop} for Sale",
            f"{bed} {prop} for Sale in {loc}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'bedroom': bed,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 3: Bedrooms + Bathrooms + Location
    print("Strategy 3: Bedrooms + Bathrooms + Location...")
    for bed, bath, loc in itertools.product(bedrooms, bathrooms, neighborhoods):
        for title_format in [
            f"{bed} {bath} Homes in {loc}, TX",
            f"{bed}/{bath} Homes for Sale in {loc}",
            f"{loc} {bed} {bath} Properties",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': 'Homes',
                    'bedroom': bed,
                    'bathroom': bath,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 4: Price Range + Property Type + Location
    print("Strategy 4: Price Range + Property Type + Location...")
    for price, prop, loc in itertools.product(price_ranges, property_types, neighborhoods):
        for title_format in [
            f"{prop} {price} in {loc}, TX",
            f"{price} {prop} for Sale in {loc}",
            f"{loc} {prop} {price}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'price': price,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 5: Bedrooms + Feature + Location
    print("Strategy 5: Bedrooms + Feature + Location...")
    for bed, feat, loc in itertools.product(bedrooms, features, neighborhoods):
        for title_format in [
            f"{bed} Homes {feat} in {loc}, TX",
            f"{loc} {bed} Homes {feat}",
            f"{bed} {feat.replace('with ', '')} Homes in {loc}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': 'Homes',
                    'bedroom': bed,
                    'feature': feat,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 6: Property Type + Condition + Location
    print("Strategy 6: Property Type + Condition + Location...")
    for prop, cond, loc in itertools.product(property_types, conditions, neighborhoods):
        for title_format in [
            f"{cond} {prop} in {loc}, TX",
            f"{loc} {cond} {prop} for Sale",
            f"{prop} {cond} in {loc}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'condition': cond,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 7: Qualifier + Property Type + Feature
    print("Strategy 7: Qualifier + Property Type + Feature...")
    for qual, prop, feat in itertools.product(qualifiers, property_types, features):
        for title_format in [
            f"{qual} {prop} {feat} in Corpus Christi, TX",
            f"{qual} {feat.replace('with ', '')} {prop} Corpus Christi",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'feature': feat,
                    'qualifier': qual,
                    'location': 'Corpus Christi'
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 8: Price Range + Bedrooms + Location
    print("Strategy 8: Price Range + Bedrooms + Location...")
    for price, bed, loc in itertools.product(price_ranges, bedrooms, neighborhoods):
        for title_format in [
            f"{bed} Homes {price} in {loc}, TX",
            f"{price} {bed} Homes for Sale in {loc}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': 'Homes',
                    'bedroom': bed,
                    'price': price,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 9: Feature + Bedrooms + Bathrooms + Location (limited)
    print("Strategy 9: Feature + Bedrooms + Bathrooms + Location...")
    for feat, bed, bath, loc in itertools.product(
        features[:20], bedrooms[:8], bathrooms[:8], neighborhoods[:20]
    ):
        for title_format in [
            f"{bed} {bath} Homes {feat} in {loc}, TX",
            f"{loc} {bed}/{bath} Homes {feat}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': 'Homes',
                    'bedroom': bed,
                    'bathroom': bath,
                    'feature': feat,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 10: Multiple Features + Location
    print("Strategy 10: Multiple Features + Location...")
    for feat1, feat2, loc in itertools.product(
        features[:30], features[30:60], neighborhoods
    ):
        for title_format in [
            f"Homes {feat1} and {feat2} in {loc}, TX",
            f"{loc} Homes {feat1} and {feat2}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': 'Homes',
                    'feature': f"{feat1} and {feat2}",
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 11: Action + Property Type + Location
    print("Strategy 11: Action + Property Type + Location...")
    for action, prop, loc in itertools.product(actions, property_types, neighborhoods):
        for title_format in [
            f"{prop} {action} {loc}, TX",
            f"{loc}, TX {prop} {action}",
        ]:
            if title_format not in seen_titles:
                seen_titles.add(title_format)
                components = {
                    'property_type': prop,
                    'location': loc
                }
                desc = generate_description(title_format, components)
                slug = create_url_slug(title_format)
                rows.append({
                    'title': title_format,
                    'description': desc,
                    'url_slug': slug
                })
                counter += 1
                if counter % 10000 == 0:
                    print(f"  Generated {counter:,} titles...")

    # Strategy 12: Bedrooms + Bathrooms + Feature + Location (limited)
    print("Strategy 12: Bedrooms + Bathrooms + Feature + Location...")
    for bed, bath, feat, loc in itertools.product(
        bedrooms[:8], bathrooms[:6], features[:25], neighborhoods[:15]
    ):
        title_format = f"{bed} {bath} {feat.replace('with ', '')} Homes in {loc}"
        if title_format not in seen_titles:
            seen_titles.add(title_format)
            components = {
                'property_type': 'Homes',
                'bedroom': bed,
                'bathroom': bath,
                'feature': feat,
                'location': loc
            }
            desc = generate_description(title_format, components)
            slug = create_url_slug(title_format)
            rows.append({
                'title': title_format,
                'description': desc,
                'url_slug': slug
            })
            counter += 1
            if counter % 10000 == 0:
                print(f"  Generated {counter:,} titles...")

    # Strategy 13: Property Type + Multiple Features
    print("Strategy 13: Property Type + Multiple Features...")
    for prop, feat1, feat2 in itertools.product(
        property_types, features[:40], features[40:80]
    ):
        title_format = f"{prop} {feat1} {feat2} Corpus Christi"
        if title_format not in seen_titles:
            seen_titles.add(title_format)
            components = {
                'property_type': prop,
                'feature': f"{feat1} {feat2}",
                'location': 'Corpus Christi'
            }
            desc = generate_description(title_format, components)
            slug = create_url_slug(title_format)
            rows.append({
                'title': title_format,
                'description': desc,
                'url_slug': slug
            })
            counter += 1
            if counter % 10000 == 0:
                print(f"  Generated {counter:,} titles...")

    # Strategy 14: Price + Bedrooms + Bathrooms + Location (limited)
    print("Strategy 14: Price + Bedrooms + Bathrooms + Location...")
    for price, bed, bath, loc in itertools.product(
        price_ranges, bedrooms[:10], bathrooms[:8], neighborhoods[:10]
    ):
        title_format = f"{bed} {bath} Homes {price} in {loc}, TX"
        if title_format not in seen_titles:
            seen_titles.add(title_format)
            components = {
                'property_type': 'Homes',
                'bedroom': bed,
                'bathroom': bath,
                'price': price,
                'location': loc
            }
            desc = generate_description(title_format, components)
            slug = create_url_slug(title_format)
            rows.append({
                'title': title_format,
                'description': desc,
                'url_slug': slug
            })
            counter += 1
            if counter % 10000 == 0:
                print(f"  Generated {counter:,} titles...")

    # Strategy 15: Qualifier + Bedrooms + Feature + Location (limited)
    print("Strategy 15: Qualifier + Bedrooms + Feature + Location...")
    for qual, bed, feat, loc in itertools.product(
        qualifiers[:15], bedrooms[:10], features[:30], neighborhoods[:15]
    ):
        title_format = f"{qual} {bed} Homes {feat} in {loc}"
        if title_format not in seen_titles:
            seen_titles.add(title_format)
            components = {
                'property_type': 'Homes',
                'bedroom': bed,
                'feature': feat,
                'qualifier': qual,
                'location': loc
            }
            desc = generate_description(title_format, components)
            slug = create_url_slug(title_format)
            rows.append({
                'title': title_format,
                'description': desc,
                'url_slug': slug
            })
            counter += 1
            if counter % 10000 == 0:
                print(f"  Generated {counter:,} titles...")

    print(f"\nTotal unique titles generated: {len(rows):,}")
    return rows

def save_to_csv(rows, filename="corpus_christi_page_titles.csv"):
    """Save the generated titles and descriptions to CSV file."""
    print(f"\nSaving to {filename}...")

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description', 'url_slug']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for i, row in enumerate(rows, 1):
            writer.writerow(row)
            if i % 50000 == 0:
                print(f"  Wrote {i:,} rows...")

    print(f"✓ Saved {len(rows):,} rows to {filename}")
    return len(rows)

def main():
    print("=" * 70)
    print("Corpus Christi Real Estate Page Title & Description Generator")
    print("=" * 70)
    print()

    rows = generate_titles_with_descriptions()
    total = save_to_csv(rows)

    print("\n" + "=" * 70)
    print("GENERATION COMPLETE!")
    print("=" * 70)
    print(f"Total rows: {total:,}")

    if total >= 50000:
        print(f"✓ Target of 50,000+ titles achieved!")

    # Show sample rows
    print("\n📋 Sample rows:")
    print("-" * 70)
    for i in range(min(5, len(rows))):
        print(f"\nRow {i+1}:")
        print(f"  Title: {rows[i]['title']}")
        print(f"  Description: {rows[i]['description']}")
        print(f"  URL Slug: {rows[i]['url_slug']}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
