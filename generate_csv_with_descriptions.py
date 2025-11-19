#!/usr/bin/env python3
"""
Generate CSV with page titles and SEO descriptions for McAllen Valley real estate
"""

import csv
import json
import re
from typing import Dict, List

def load_titles(filename: str = "page_titles.json") -> List[str]:
    """Load titles from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_url_slug(title: str) -> str:
    """Create SEO-friendly URL slug from title"""
    # Remove special characters and convert to lowercase
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = slug.strip('-')
    return slug

def extract_features(title: str) -> Dict[str, any]:
    """Extract key features from title for description generation"""
    features = {
        'bedrooms': None,
        'bathrooms': None,
        'has_pool': False,
        'stories': None,
        'garage': None,
        'price_range': None,
        'city': None,
        'property_type': 'homes',
        'special_features': [],
        'condition': None,
        'style': None,
        'lot_type': None
    }

    title_lower = title.lower()

    # Extract bedrooms
    bed_patterns = [
        r'(\d+)\s*bed(?:room)?(?:s)?',
        r'(one|two|three|four|five|six)\s*bed(?:room)?(?:s)?',
        r'studio'
    ]
    for pattern in bed_patterns:
        match = re.search(pattern, title_lower)
        if match:
            if 'studio' in match.group(0):
                features['bedrooms'] = 'studio'
            else:
                bed_num = match.group(1)
                features['bedrooms'] = bed_num
            break

    # Extract bathrooms
    bath_match = re.search(r'(\d+(?:\.\d+)?)\s*bath(?:room)?(?:s)?', title_lower)
    if bath_match:
        features['bathrooms'] = bath_match.group(1)

    # Check for pool
    if 'pool' in title_lower:
        features['has_pool'] = True

    # Extract stories
    if '2 story' in title_lower or 'two story' in title_lower:
        features['stories'] = '2'
    elif 'single story' in title_lower or 'one story' in title_lower:
        features['stories'] = '1'

    # Extract garage info
    garage_match = re.search(r'(\d+)\s*car\s*garage', title_lower)
    if garage_match:
        features['garage'] = garage_match.group(1)
    elif 'garage' in title_lower or 'carport' in title_lower:
        features['garage'] = 'yes'

    # Extract price range
    price_patterns = [
        r'\$[\d,]+-\$[\d,]+[km]?',
        r'under \$[\d,]+[km]?',
        r'over \$[\d,]+[km]?',
        r'affordable|luxury|mid-range|high-end'
    ]
    for pattern in price_patterns:
        match = re.search(pattern, title_lower)
        if match:
            features['price_range'] = match.group(0)
            break

    # Extract city
    cities = [
        'mcallen', 'edinburg', 'mission', 'pharr', 'weslaco', 'donna', 'alamo',
        'san juan', 'mercedes', 'la joya', 'palmview', 'hidalgo', 'elsa',
        'progreso', 'penitas', 'sullivan city', 'granjeno', 'palmhurst',
        'alton', 'lopezville', 'muniz', 'doffing', 'hargill', 'linn'
    ]
    for city in cities:
        if city in title_lower:
            features['city'] = city.title()
            break

    # Check for regional terms
    if not features['city']:
        if 'rio grande valley' in title_lower or 'rgv' in title_lower:
            features['city'] = 'Rio Grande Valley'
        elif 'the valley' in title_lower or 'south texas' in title_lower:
            features['city'] = 'the Valley'

    # Extract property type
    prop_types = {
        'condo': 'condos',
        'townhome': 'townhomes',
        'townhouse': 'townhouses',
        'villa': 'villas',
        'estate': 'estates',
        'ranch': 'ranch homes',
        'luxury home': 'luxury homes',
        'single family': 'single family homes'
    }
    for key, value in prop_types.items():
        if key in title_lower:
            features['property_type'] = value
            break

    # Special features
    feature_keywords = [
        'gated community', 'golf course', 'new construction', 'newly built',
        'move-in ready', 'renovated', 'updated', 'game room', 'master suite',
        'open floor plan', 'granite countertops', 'stainless appliances',
        'hardwood floors', 'fireplace', 'backyard', 'covered patio',
        'energy efficient', 'smart home', 'walk-in closets', 'office',
        'rv parking', 'boat parking', 'landscaping', 'sprinkler system',
        "chef's kitchen", 'guest suite', 'workshop', 'fenced yard'
    ]
    for feature in feature_keywords:
        if feature in title_lower:
            features['special_features'].append(feature)

    # Condition
    conditions = [
        'new construction', 'newly built', 'brand new', 'renovated',
        'updated', 'like new', 'fixer upper', 'foreclosure'
    ]
    for condition in conditions:
        if condition in title_lower:
            features['condition'] = condition
            break

    # Style
    styles = [
        'modern', 'contemporary', 'traditional', 'spanish style',
        'mediterranean', 'ranch style', 'craftsman', 'colonial'
    ]
    for style in styles:
        if style in title_lower:
            features['style'] = style
            break

    # Lot type
    lot_types = [
        'large lot', 'oversized lot', 'corner lot', 'acreage',
        'acre', 'acres', 'country living'
    ]
    for lot_type in lot_types:
        if lot_type in title_lower:
            features['lot_type'] = lot_type
            break

    return features

def generate_description(title: str, features: Dict) -> str:
    """Generate unique SEO-optimized description based on title and features"""

    # Opening phrases - vary based on content
    openings = []

    if features['condition'] == 'new construction' or features['condition'] == 'newly built':
        openings.append(f"Discover brand new {features['property_type']}")
    elif features['condition'] == 'renovated' or features['condition'] == 'updated':
        openings.append(f"Explore beautifully updated {features['property_type']}")
    elif features['condition'] == 'fixer upper':
        openings.append(f"Find great investment opportunities with {features['property_type']}")
    elif features['has_pool']:
        openings.append(f"Find your dream home with a pool - browse {features['property_type']}")
    elif features['price_range'] and 'luxury' in features['price_range']:
        openings.append(f"Browse luxury {features['property_type']}")
    elif features['price_range'] and 'affordable' in features['price_range']:
        openings.append(f"Discover affordable {features['property_type']}")
    else:
        openings.append(f"Search {features['property_type']}")

    # Build middle section with specific features
    middle_parts = []

    # Bedroom/bathroom info
    if features['bedrooms'] and features['bathrooms']:
        if features['bedrooms'] == 'studio':
            middle_parts.append(f"featuring studio layouts with {features['bathrooms']} bathrooms")
        else:
            middle_parts.append(f"with {features['bedrooms']} bedrooms and {features['bathrooms']} bathrooms")
    elif features['bedrooms']:
        if features['bedrooms'] == 'studio':
            middle_parts.append(f"in studio layouts")
        else:
            middle_parts.append(f"featuring {features['bedrooms']} bedrooms")

    # Special features
    if features['has_pool']:
        pool_types = ['swimming pools', 'inground pools', 'sparkling pools']
        import random
        middle_parts.append(pool_types[hash(title) % len(pool_types)])

    if features['stories'] == '2':
        middle_parts.append("two-story designs")
    elif features['stories'] == '1':
        middle_parts.append("convenient single-story layouts")

    if features['garage']:
        if features['garage'].isdigit():
            middle_parts.append(f"{features['garage']}-car garages")
        else:
            middle_parts.append("attached garages")

    # Add some special features
    if features['special_features']:
        # Add up to 2 special features
        special = features['special_features'][:2]
        for feat in special:
            middle_parts.append(feat)

    # Location section
    location_part = ""
    if features['city']:
        city_descriptions = {
            'McAllen': "in McAllen, the heart of the Rio Grande Valley",
            'Edinburg': "in Edinburg, home to UTRGV and family-friendly communities",
            'Mission': "in Mission, known for its affordable living and great amenities",
            'Pharr': "in Pharr, offering convenient access to shopping and entertainment",
            'Weslaco': "in Weslaco, a charming city in the heart of the Valley",
            'Mercedes': "in Mercedes, perfect for those seeking small-town charm",
            'Rio Grande Valley': "throughout the Rio Grande Valley",
            'the Valley': "in South Texas's Rio Grande Valley"
        }
        location_part = city_descriptions.get(
            features['city'],
            f"in {features['city']}, TX"
        )
    else:
        location_part = "in the McAllen area"

    # Price information
    price_part = ""
    if features['price_range']:
        if 'under' in features['price_range']:
            price_part = f"Homes {features['price_range']}. "
        elif 'luxury' in features['price_range'] or 'high-end' in features['price_range']:
            price_part = "Luxury properties available. "
        elif 'affordable' in features['price_range']:
            price_part = "Affordable options available. "
        else:
            price_part = f"Properties {features['price_range']}. "

    # Closing with call-to-action - vary these
    closings = [
        "Browse listings, schedule tours, and find your perfect home today.",
        "View photos, get pricing details, and contact us to schedule a showing.",
        "Explore available properties and connect with local real estate experts.",
        "See all listings, compare prices, and start your home search now.",
        "Find your dream home - search listings and schedule viewings today.",
        "View detailed listings with photos, prices, and property information.",
        "Contact local agents to tour these homes and make an offer today.",
        "Start your home search with detailed listings and expert guidance.",
        "Browse current listings, check availability, and schedule tours.",
        "Discover your next home - view listings and connect with agents today."
    ]

    # Assemble description
    opening = openings[0]

    # Create middle section
    if middle_parts:
        if len(middle_parts) == 1:
            middle = f"{middle_parts[0]}"
        elif len(middle_parts) == 2:
            middle = f"{middle_parts[0]} and {middle_parts[1]}"
        else:
            middle = f"{', '.join(middle_parts[:-1])}, and {middle_parts[-1]}"
    else:
        middle = ""

    # Use hash for consistent but varied closings
    closing = closings[hash(title) % len(closings)]

    # Assemble full description
    parts = [opening]
    if middle:
        parts.append(middle)
    parts.append(location_part + ".")
    if price_part:
        parts.append(price_part)
    parts.append(closing)

    description = " ".join(parts)

    # Ensure description is between 120-160 characters for meta description
    # But for page content, we can be longer
    if len(description) < 100:
        description += " The Rio Grande Valley offers excellent weather, affordable living, and a thriving community."

    return description

def generate_csv(titles: List[str], output_file: str = "page_titles_with_descriptions.csv"):
    """Generate CSV with titles, descriptions, and URL slugs"""

    print(f"Generating descriptions for {len(titles):,} titles...")
    print("This may take a few minutes...\n")

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Description', 'URL_Slug', 'City', 'Property_Type',
                      'Bedrooms', 'Bathrooms', 'Has_Pool', 'Price_Range']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        count = 0
        for title in titles:
            features = extract_features(title)
            description = generate_description(title, features)
            url_slug = create_url_slug(title)

            writer.writerow({
                'Title': title,
                'Description': description,
                'URL_Slug': url_slug,
                'City': features.get('city', ''),
                'Property_Type': features.get('property_type', 'homes'),
                'Bedrooms': features.get('bedrooms', ''),
                'Bathrooms': features.get('bathrooms', ''),
                'Has_Pool': 'Yes' if features.get('has_pool') else 'No',
                'Price_Range': features.get('price_range', '')
            })

            count += 1
            if count % 10000 == 0:
                print(f"  Processed {count:,} titles...")

    print(f"\n✓ Generated {len(titles):,} titles with descriptions")
    print(f"✓ Saved to {output_file}")

    # Show file size
    import os
    file_size = os.path.getsize(output_file)
    size_mb = file_size / (1024 * 1024)
    print(f"✓ File size: {size_mb:.1f} MB")

def show_samples(filename: str, num_samples: int = 20):
    """Show sample rows from CSV"""
    print(f"\n{'='*80}")
    print(f"SAMPLE ENTRIES FROM CSV ({num_samples} examples)")
    print(f"{'='*80}\n")

    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        import random
        samples = random.sample(rows, min(num_samples, len(rows)))

        for i, row in enumerate(samples, 1):
            print(f"{i}. TITLE: {row['Title']}")
            print(f"   DESCRIPTION: {row['Description']}")
            print(f"   URL: /{row['URL_Slug']}")
            print(f"   CITY: {row['City']} | BEDS: {row['Bedrooms']} | BATHS: {row['Bathrooms']} | POOL: {row['Has_Pool']}")
            print()

if __name__ == "__main__":
    print("="*80)
    print("REAL ESTATE PAGE TITLES CSV GENERATOR")
    print("McAllen Valley Area, Texas")
    print("="*80)
    print()

    # Load titles
    print("Loading titles...")
    titles = load_titles("page_titles.json")
    print(f"✓ Loaded {len(titles):,} titles\n")

    # Generate CSV
    output_file = "page_titles_with_descriptions.csv"
    generate_csv(titles, output_file)

    # Show samples
    show_samples(output_file, 25)

    print("="*80)
    print("COMPLETE!")
    print("="*80)
    print(f"\nYour CSV file is ready: {output_file}")
    print("\nColumns included:")
    print("  - Title: The page title")
    print("  - Description: SEO-optimized description (120-200+ chars)")
    print("  - URL_Slug: SEO-friendly URL path")
    print("  - City: Extracted city name")
    print("  - Property_Type: Type of property")
    print("  - Bedrooms: Number of bedrooms")
    print("  - Bathrooms: Number of bathrooms")
    print("  - Has_Pool: Yes/No")
    print("  - Price_Range: Price range if specified")
