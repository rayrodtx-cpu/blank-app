#!/usr/bin/env python3
"""
Generate 350,000+ real estate page titles with descriptions for Houston
Combines various property attributes to create unique page titles and SEO descriptions
"""

import itertools
import csv
import random

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

# Description templates for different patterns
description_templates = {
    'area_intro': [
        "Discover exceptional {property_type} in {area}, Houston's premier neighborhood.",
        "Explore beautiful {property_type} available in {area}, one of Houston's most sought-after communities.",
        "Find your dream home among stunning {property_type} in {area}, featuring top-rated schools and amenities.",
        "Browse {property_type} in {area}, offering easy access to shopping, dining, and entertainment.",
        "Search {property_type} in the desirable {area} area with convenient access to major highways.",
    ],
    'feature_highlight': [
        "Each property features {feature}, perfect for Houston's lifestyle.",
        "These homes include {feature}, ideal for comfortable living.",
        "Enjoy the luxury of {feature} in every home.",
        "Properties showcase {feature}, adding value and comfort.",
        "Every listing includes {feature} for enhanced living.",
    ],
    'bedroom_bath': [
        "Spacious {bedrooms} {bathrooms} floor plans designed for modern living.",
        "{Bedrooms} {bathrooms} layouts offering comfort and functionality.",
        "Thoughtfully designed {bedrooms} {bathrooms} homes for growing families.",
        "Comfortable {bedrooms} {bathrooms} configurations to suit your needs.",
        "{Bedrooms} {bathrooms} properties with flexible living spaces.",
    ],
    'call_to_action': [
        "Schedule your showing today and find your perfect Houston home.",
        "Contact us now to view available properties and start your home search.",
        "Explore listings today and discover your ideal Houston residence.",
        "View photos, pricing, and details for all available properties.",
        "Start your home search today with our comprehensive listings.",
    ]
}

# Area-specific information
area_highlights = {
    'Downtown Houston': 'close to business district, cultural attractions, and nightlife',
    'Midtown Houston': 'vibrant urban living with restaurants, bars, and entertainment',
    'Uptown Houston': 'upscale shopping at the Galleria and fine dining',
    'The Heights': 'historic charm with trendy shops and restaurants',
    'Montrose': 'eclectic arts district with museums and galleries',
    'River Oaks': 'prestigious luxury homes and tree-lined streets',
    'Memorial': 'established neighborhoods with excellent schools',
    'Galleria': 'world-class shopping and dining destinations',
    'Katy': 'family-friendly suburbs with top-rated schools',
    'Sugar Land': 'master-planned communities and excellent amenities',
    'The Woodlands': 'resort-style living with golf courses and nature trails',
    'Pearland': 'growing community with great schools and shopping',
    'Cypress': 'affordable family homes near major employers',
    'Spring': 'suburban living with easy highway access',
    'Humble': 'affordable homes near Lake Houston',
    'Kingwood': 'established community surrounded by nature',
    'Clear Lake': 'waterfront living near NASA and Galveston Bay',
    'Friendswood': 'small-town charm with excellent schools',
    'Missouri City': 'diverse community with family amenities',
    'Stafford': 'convenient location near major employment centers',
    'Richmond': 'historic charm with modern conveniences',
    'Rosenberg': 'affordable living in Fort Bend County',
    'Bellaire': 'established neighborhoods with top schools',
    'West University': 'prestigious area near Rice University',
    'Medical Center': 'convenient to Texas Medical Center and museums',
    'Meyerland': 'established community with parks and shopping',
    'Sharpstown': 'diverse neighborhood with affordable options',
    'Alief': 'multicultural community near major highways',
    'Greenspoint': 'affordable homes near IAH Airport',
    'Energy Corridor': 'modern developments near major employers',
    'Cinco Ranch': 'master-planned community with resort amenities',
    'Sienna Plantation': 'family-friendly community with parks and pools',
    'Bridgeland': 'new development with lakes and trails',
    'Elyson': 'modern community with top amenities',
    'League City': 'coastal living near Clear Lake and Kemah',
    'Webster': 'convenient to NASA and medical facilities',
    'Pasadena': 'affordable homes near the Ship Channel',
    'Baytown': 'growing community near Houston refineries',
    'Conroe': 'lakeside living north of Houston',
    'Houston': 'diverse neighborhoods throughout the greater area',
}

def generate_description(title, components):
    """Generate a unique description based on title components"""

    # Extract components
    bedrooms_val = components.get('bedrooms', '')
    bathrooms_val = components.get('bathrooms', '')
    property_type = components.get('property_type', 'properties').lower()
    area = components.get('area', 'Houston')
    feature = components.get('feature', '')
    price = components.get('price', '')
    sqft = components.get('sqft', '')
    style = components.get('style', '')
    story = components.get('story', '')
    qualifier = components.get('qualifier', '')
    category = components.get('category', '')
    secondary = components.get('secondary', '')

    # Start building description
    parts = []

    # Opening line
    if qualifier:
        parts.append(f"{qualifier.replace(':', '')} - ")

    if category:
        parts.append(f"{category} ")

    if style:
        parts.append(f"Browse {style.lower()} ")
    else:
        parts.append(f"Discover ")

    # Main property description
    if bedrooms_val and bathrooms_val:
        parts.append(f"{bedrooms_val.lower()}, {bathrooms_val.lower()} ")
    elif bedrooms_val:
        parts.append(f"{bedrooms_val.lower()} ")

    if story:
        parts.append(f"{story.lower()} ")

    parts.append(f"{property_type}")

    # Feature
    if feature:
        clean_feature = feature.replace('with ', '').lower()
        parts.append(f" {feature.lower()}")

    # Location
    parts.append(f" in {area}")

    # Add area highlight
    if area in area_highlights:
        parts.append(f", {area_highlights[area]}")

    parts.append(". ")

    # Price and size info
    details = []
    if price:
        details.append(f"{price} price range")
    if sqft:
        details.append(f"{sqft.lower()}")
    if secondary:
        details.append(f"{secondary.lower()}")

    if details:
        parts.append("Featuring " + ", ".join(details) + ". ")

    # Call to action
    cta_options = [
        "View available listings, photos, and schedule tours today.",
        "Explore homes for sale with detailed photos, pricing, and property information.",
        "Search listings now to find your perfect Houston home.",
        "Browse current inventory with virtual tours and pricing details.",
        "Contact us today to schedule a private showing.",
    ]
    parts.append(random.choice(cta_options))

    description = ''.join(parts)

    # Ensure reasonable length (under 500 chars is good for meta descriptions)
    if len(description) > 500:
        description = description[:497] + "..."

    return description

def generate_titles_with_descriptions():
    """Generate all combinations of real estate page titles with descriptions"""
    titles_data = []
    count = 0

    print("Generating titles with descriptions...")

    # Pattern 1: [Bedrooms] [Property Type] in [Area]
    print("  Pattern 1: Bedrooms + Property Type + Area")
    for bedrooms_val, prop_type, area in itertools.product(bedrooms, property_types, houston_areas):
        title = f"{bedrooms_val} {prop_type} in {area}"
        components = {
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 2: [Bedrooms] [Bathrooms] [Property Type] in [Area]
    print("  Pattern 2: Bedrooms + Bathrooms + Property Type + Area")
    for bedrooms_val, bathrooms_val, prop_type, area in itertools.product(bedrooms, bathrooms, property_types, houston_areas):
        title = f"{bedrooms_val} {bathrooms_val} {prop_type} in {area}"
        components = {
            'bedrooms': bedrooms_val,
            'bathrooms': bathrooms_val,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 3: [Stories] [Property Type] in [Area]
    print("  Pattern 3: Stories + Property Type + Area")
    for story, prop_type, area in itertools.product(stories, property_types, houston_areas):
        title = f"{story} {prop_type} in {area}"
        components = {
            'story': story,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 4: [Property Type] [Primary Feature] in [Area]
    print("  Pattern 4: Property Type + Primary Feature + Area")
    for prop_type, feature, area in itertools.product(property_types, primary_features, houston_areas):
        title = f"{prop_type} {feature} in {area}"
        components = {
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 5: [Bedrooms] [Property Type] [Primary Feature] in [Area]
    print("  Pattern 5: Bedrooms + Property Type + Primary Feature + Area")
    for bedrooms_val, prop_type, feature, area in itertools.product(bedrooms, property_types, primary_features, houston_areas):
        title = f"{bedrooms_val} {prop_type} {feature} in {area}"
        components = {
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 6: [Stories] [Property Type] [Primary Feature] in [Area]
    print("  Pattern 6: Stories + Property Type + Primary Feature + Area")
    for story, prop_type, feature, area in itertools.product(stories, property_types, primary_features, houston_areas):
        title = f"{story} {prop_type} {feature} in {area}"
        components = {
            'story': story,
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 7: [Price Range] [Property Type] in [Area]
    print("  Pattern 7: Price Range + Property Type + Area")
    for price, prop_type, area in itertools.product(price_ranges, property_types, houston_areas):
        title = f"{price} {prop_type} in {area}"
        components = {
            'price': price,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 8: [Style] [Property Type] in [Area]
    print("  Pattern 8: Style + Property Type + Area")
    for style, prop_type, area in itertools.product(styles, property_types, houston_areas):
        title = f"{style} {prop_type} in {area}"
        components = {
            'style': style,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 9: [Bedrooms] [Bathrooms] [Property Type] [Primary Feature] in [Area]
    print("  Pattern 9: Bedrooms + Bathrooms + Property Type + Primary Feature + Area (limited)")
    for bedrooms_val, bathrooms_val, prop_type, feature, area in itertools.product(bedrooms, bathrooms, property_types, primary_features[:10], houston_areas[:20]):
        title = f"{bedrooms_val} {bathrooms_val} {prop_type} {feature} in {area}"
        components = {
            'bedrooms': bedrooms_val,
            'bathrooms': bathrooms_val,
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 10: [Property Type] in [Secondary Feature] in [Area]
    print("  Pattern 10: Property Type + Secondary Feature + Area")
    for prop_type, sec_feature, area in itertools.product(property_types, secondary_features, houston_areas):
        title = f"{prop_type} in {sec_feature} in {area}"
        components = {
            'property_type': prop_type,
            'secondary': sec_feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 11: [Sqft] [Property Type] in [Area]
    print("  Pattern 11: Sqft + Property Type + Area")
    for sqft, prop_type, area in itertools.product(sqft_ranges, property_types, houston_areas):
        title = f"{sqft} {prop_type} in {area}"
        components = {
            'sqft': sqft,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 12: [Bedrooms] [Price Range] [Property Type] in [Area]
    print("  Pattern 12: Bedrooms + Price Range + Property Type + Area (limited)")
    for bedrooms_val, price, prop_type, area in itertools.product(bedrooms, price_ranges, property_types, houston_areas[:20]):
        title = f"{bedrooms_val} {price} {prop_type} in {area}"
        components = {
            'bedrooms': bedrooms_val,
            'price': price,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 13: [Time Qualifier] [Property Type] in [Area]
    print("  Pattern 13: Time Qualifier + Property Type + Area")
    for qualifier, prop_type, area in itertools.product(time_qualifiers, property_types, houston_areas):
        title = f"{qualifier}: {prop_type} in {area}"
        components = {
            'qualifier': qualifier,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 14: [Special Category] [Property Type] in [Area]
    print("  Pattern 14: Special Category + Property Type + Area")
    for category, prop_type, area in itertools.product(special_categories, property_types, houston_areas):
        title = f"{category} {prop_type} in {area}"
        components = {
            'category': category,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 15: [Style] [Bedrooms] [Property Type] in [Area]
    print("  Pattern 15: Style + Bedrooms + Property Type + Area (limited)")
    for style, bedrooms_val, prop_type, area in itertools.product(styles, bedrooms, property_types, houston_areas[:20]):
        title = f"{style} {bedrooms_val} {prop_type} in {area}"
        components = {
            'style': style,
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 16: [Price Range] [Bedrooms] [Property Type] [Primary Feature] in [Area]
    print("  Pattern 16: Price Range + Bedrooms + Property Type + Primary Feature + Area (limited)")
    for price, bedrooms_val, prop_type, feature, area in itertools.product(price_ranges[:5], bedrooms, property_types, primary_features[:8], houston_areas[:15]):
        title = f"{price} {bedrooms_val} {prop_type} {feature} in {area}"
        components = {
            'price': price,
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 17: [Stories] [Bedrooms] [Property Type] in [Area]
    print("  Pattern 17: Stories + Bedrooms + Property Type + Area")
    for story, bedrooms_val, prop_type, area in itertools.product(stories, bedrooms, property_types, houston_areas):
        title = f"{story} {bedrooms_val} {prop_type} in {area}"
        components = {
            'story': story,
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 18: [Property Type] [Primary Feature] [Price Range] in [Area]
    print("  Pattern 18: Property Type + Primary Feature + Price Range + Area (limited)")
    for prop_type, feature, price, area in itertools.product(property_types, primary_features[:10], price_ranges, houston_areas[:15]):
        title = f"{prop_type} {feature} {price} in {area}"
        components = {
            'property_type': prop_type,
            'feature': feature,
            'price': price,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 19: [Sqft] [Bedrooms] [Property Type] in [Area]
    print("  Pattern 19: Sqft + Bedrooms + Property Type + Area (limited)")
    for sqft, bedrooms_val, prop_type, area in itertools.product(sqft_ranges, bedrooms, property_types, houston_areas[:20]):
        title = f"{sqft} {bedrooms_val} {prop_type} in {area}"
        components = {
            'sqft': sqft,
            'bedrooms': bedrooms_val,
            'property_type': prop_type,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    # Pattern 20: [Style] [Property Type] [Primary Feature] in [Area]
    print("  Pattern 20: Style + Property Type + Primary Feature + Area (limited)")
    for style, prop_type, feature, area in itertools.product(styles, property_types, primary_features[:12], houston_areas[:18]):
        title = f"{style} {prop_type} {feature} in {area}"
        components = {
            'style': style,
            'property_type': prop_type,
            'feature': feature,
            'area': area
        }
        description = generate_description(title, components)
        titles_data.append((title, description, components))
        count += 1
        if count % 10000 == 0:
            print(f"    Generated {count:,} titles...")

    print(f"\n  Total generated: {count:,} titles")
    return titles_data

def save_to_csv(titles_data, filename='houston_real_estate_complete.csv'):
    """Save titles and descriptions to CSV file"""
    print(f"\nSaving to {filename}...")

    # Remove duplicates based on title
    unique_titles = {}
    for title, description, components in titles_data:
        if title not in unique_titles:
            unique_titles[title] = (description, components)

    # Sort by title
    sorted_titles = sorted(unique_titles.items())

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Page Title', 'URL Slug', 'Meta Description'])

        for title, (description, components) in sorted_titles:
            url_slug = title.lower().replace(' ', '-').replace(':', '').replace('$', '').replace('+', 'plus').replace(',', '')
            writer.writerow([title, url_slug, description])

    return len(sorted_titles)

if __name__ == '__main__':
    # Set random seed for consistent descriptions
    random.seed(42)

    print("="*80)
    print("Houston Real Estate Page Title & Description Generator")
    print("="*80)

    titles_data = generate_titles_with_descriptions()

    unique_count = save_to_csv(titles_data)

    print(f"\n{'='*80}")
    print(f"COMPLETE! Generated {unique_count:,} unique page titles with descriptions!")
    print(f"{'='*80}")
    print("\nFile created:")
    print("  - houston_real_estate_complete.csv")
    print("\nColumns:")
    print("  1. Page Title")
    print("  2. URL Slug (SEO-friendly)")
    print("  3. Meta Description (unique for each page)")
    print(f"\n{'='*80}")
