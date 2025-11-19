#!/usr/bin/env python3
"""
Add SEO-optimized descriptions to each page title
"""

import re
import csv

# Read existing titles
with open('austin_real_estate_page_titles.txt', 'r') as f:
    titles = [line.strip() for line in f if line.strip()]

print(f"Processing {len(titles):,} titles...")

def generate_description(title):
    """Generate SEO-optimized description based on title"""

    # Extract key components from title
    title_lower = title.lower()

    # Determine property type
    prop_type = "properties"
    if "home" in title_lower:
        prop_type = "homes"
    elif "house" in title_lower:
        prop_type = "houses"
    elif "condo" in title_lower:
        prop_type = "condos"
    elif "townhome" in title_lower:
        prop_type = "townhomes"
    elif "estate" in title_lower:
        prop_type = "estate properties"
    elif "villa" in title_lower:
        prop_type = "villas"

    # Extract location
    location = "Austin, TX"
    neighborhoods = [
        "Downtown Austin", "West Lake Hills", "Tarrytown", "Clarksville", "Hyde Park",
        "Mueller", "East Austin", "South Congress", "Zilker", "Barton Hills",
        "Bouldin Creek", "Travis Heights", "Rosedale", "Allandale", "Crestview",
        "North Loop", "Cherrywood", "Windsor Park", "Georgian Acres", "Brentwood",
        "Pemberton Heights", "Old West Austin", "Rollingwood", "Steiner Ranch", "Circle C",
        "Avery Ranch", "Cedar Park", "Round Rock", "Pflugerville", "Manor",
        "Lakeway", "Bee Cave", "Dripping Springs", "Kyle", "Buda"
    ]

    for neighborhood in neighborhoods:
        if neighborhood.lower() in title_lower:
            location = neighborhood
            break

    # Extract bedrooms
    bedrooms = ""
    bed_matches = re.search(r'(\d+)\s+(bed|bedroom)', title_lower)
    if bed_matches:
        bedrooms = f"{bed_matches.group(1)}-bedroom "
    elif "studio" in title_lower:
        bedrooms = "studio "

    # Extract bathrooms
    bathrooms = ""
    bath_matches = re.search(r'(\d+\.?\d*)\s+(bath|bathroom)', title_lower)
    if bath_matches:
        bathrooms = f", {bath_matches.group(1)}-bathroom"

    # Extract features
    features = []
    feature_map = {
        "pool": "swimming pools",
        "2 stor": "two stories",
        "two stor": "two stories",
        "single story": "single-story layouts",
        "one story": "one-story design",
        "garage": "attached garages",
        "2 car garage": "2-car garages",
        "3 car garage": "3-car garages",
        "backyard": "spacious backyards",
        "large lot": "large lots",
        "acreage": "acreage",
        "hardwood": "hardwood floors",
        "updated kitchen": "updated kitchens",
        "modern kitchen": "modern kitchens",
        "granite": "granite countertops",
        "stainless": "stainless steel appliances",
        "master suite": "master suites",
        "walk-in closet": "walk-in closets",
        "home office": "home offices",
        "game room": "game rooms",
        "media room": "media rooms",
        "guest house": "guest houses",
        "mother-in-law": "mother-in-law suites",
        "casita": "casitas",
        "lake view": "lake views",
        "hill country view": "Hill Country views",
        "water view": "water views",
        "greenbelt": "greenbelt access",
        "golf course view": "golf course views",
        "fireplace": "fireplaces",
        "covered patio": "covered patios",
        "outdoor kitchen": "outdoor kitchens",
        "deck": "decks",
        "balcony": "balconies",
        "smart home": "smart home features",
        "solar panel": "solar panels",
        "energy efficient": "energy-efficient features",
        "new construction": "new construction",
        "high ceiling": "high ceilings",
        "vaulted ceiling": "vaulted ceilings",
        "open floor plan": "open floor plans",
        "rv parking": "RV parking",
        "workshop": "workshops",
        "horse property": "horse facilities",
        "equestrian": "equestrian amenities",
        "cul-de-sac": "cul-de-sac locations",
        "gated": "gated community security",
        "waterfront": "waterfront locations",
        "lakefront": "lakefront settings",
        "lake travis": "Lake Travis access",
        "lake austin": "Lake Austin views",
        "pet friendly": "pet-friendly features",
        "spa": "spa amenities",
        "hot tub": "hot tubs",
        "wine cellar": "wine cellars",
        "gym": "home gyms",
        "renovated": "recent renovations",
        "contemporary": "contemporary design",
        "modern": "modern architecture",
        "craftsman": "Craftsman style",
        "victorian": "Victorian charm",
        "mediterranean": "Mediterranean architecture",
        "luxury": "luxury finishes"
    }

    for key, value in feature_map.items():
        if key in title_lower:
            features.append(value)

    # Extract price range
    price_info = ""
    price_matches = re.search(r'under (\d+[km])', title_lower)
    if price_matches:
        price_val = price_matches.group(1).upper()
        price_info = f" under ${price_val.replace('K', '00,000').replace('M', ',000,000')}"
    elif re.search(r'(\d+k)-(\d+k)', title_lower):
        price_match = re.search(r'(\d+)k-(\d+)k', title_lower)
        if price_match:
            price_info = f" ranging from ${price_match.group(1)}00,000 to ${price_match.group(2)}00,000"
    elif "affordable" in title_lower:
        price_info = " at competitive prices"
    elif "luxury" in title_lower or "million dollar" in title_lower:
        price_info = " in the luxury market"

    # Extract square footage
    sqft_info = ""
    sqft_match = re.search(r'(\d+)-(\d+)\s+sq\s+ft', title_lower)
    if sqft_match:
        sqft_info = f" ranging from {sqft_match.group(1)} to {sqft_match.group(2)} square feet"
    elif re.search(r'under (\d+)\s+sq\s+ft', title_lower):
        sqft_match = re.search(r'under (\d+)\s+sq\s+ft', title_lower)
        sqft_info = f" under {sqft_match.group(1)} square feet"

    # School district info
    school_info = ""
    if "austin isd" in title_lower:
        school_info = " in the highly-rated Austin ISD"
    elif "eanes isd" in title_lower:
        school_info = " in the prestigious Eanes ISD"
    elif "round rock isd" in title_lower:
        school_info = " in Round Rock ISD"
    elif "lake travis isd" in title_lower:
        school_info = " in Lake Travis ISD"
    elif "top rated school" in title_lower or "good school" in title_lower:
        school_info = " in top-rated school districts"

    # Special categories
    special_category = ""
    if "investment" in title_lower:
        special_category = "investment "
    elif "starter home" in title_lower:
        special_category = "starter "
    elif "retirement" in title_lower:
        special_category = "retirement "
    elif "family friendly" in title_lower:
        special_category = "family-friendly "

    # Build description
    descriptions_templates = [
        f"Discover {bedrooms}{special_category}{prop_type}{bathrooms} in {location}{price_info}. Browse our current listings featuring {', '.join(features[:3]) if features else 'desirable amenities'}{school_info}. Find your perfect home today with detailed photos, virtual tours, and neighborhood information.",

        f"Explore available {bedrooms}{special_category}{prop_type}{bathrooms} for sale in {location}{price_info}. Our curated selection includes properties with {', '.join(features[:3]) if features else 'modern amenities'}{sqft_info}{school_info}. Schedule a showing and experience the Austin lifestyle.",

        f"Search {bedrooms}{special_category}{prop_type}{bathrooms} in {location}{price_info}. View homes featuring {', '.join(features[:3]) if features else 'quality finishes'}{school_info}. Updated daily with new listings, price changes, and open house schedules.",

        f"Find {bedrooms}{special_category}{prop_type}{bathrooms} in beautiful {location}{price_info}. Our listings showcase properties with {', '.join(features[:3]) if features else 'excellent features'}{sqft_info}. Connect with local real estate experts for personalized service.",

        f"Browse {bedrooms}{special_category}{prop_type}{bathrooms} available in {location}{price_info}. Filter by {', '.join(features[:2]) if features else 'your preferred features'} and more{school_info}. Get instant access to MLS listings, market trends, and comparative market analysis."
    ]

    # Use different templates based on hash of title for variety
    template_index = hash(title) % len(descriptions_templates)
    description = descriptions_templates[template_index]

    # Clean up description
    description = description.replace("  ", " ").replace(" ,", ",").strip()

    return description

def categorize_title(title):
    """Categorize the title"""
    title_lower = title.lower()

    categories = []

    # Primary category
    if any(n.lower() in title_lower for n in ["downtown", "mueller", "steiner", "cedar park", "tarrytown"]):
        categories.append("Neighborhood")

    if any(b in title_lower for b in ["bedroom", "bed", "studio"]):
        categories.append("Bedrooms")

    if any(p in title_lower for p in ["under", "affordable", "luxury", "million"]):
        categories.append("Price Range")

    if "pool" in title_lower:
        categories.append("Pool")

    if any(s in title_lower for s in ["story", "stories"]):
        categories.append("Stories")

    if "garage" in title_lower:
        categories.append("Garage")

    if any(v in title_lower for v in ["view", "lake", "waterfront", "hill country"]):
        categories.append("Views & Location")

    if any(f in title_lower for f in ["luxury", "estate", "million"]):
        categories.append("Luxury")

    if any(s in title_lower for s in ["isd", "school"]):
        categories.append("Schools")

    if any(f in title_lower for f in ["new construction", "renovated", "updated"]):
        categories.append("Condition")

    if not categories:
        categories.append("General")

    return "; ".join(categories[:2])  # Limit to 2 main categories

def extract_keywords(title):
    """Extract keywords from title"""
    # Remove common words and create keyword list
    common_words = ["in", "for", "sale", "the", "a", "an", "and", "or", "with", "by"]
    words = title.lower().replace(",", "").split()
    keywords = [w for w in words if w not in common_words and len(w) > 2]

    # Add location-based keywords
    if "austin" in title.lower():
        keywords.extend(["austin tx", "austin texas", "atx"])

    return ", ".join(keywords[:10])  # Limit keywords

# Generate CSV with descriptions
output_file = "austin_real_estate_page_titles_with_descriptions.csv"
count = 0

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Page Title", "Meta Description", "Category", "Keywords"])

    for title in titles:
        description = generate_description(title)
        category = categorize_title(title)
        keywords = extract_keywords(title)

        writer.writerow([title, description, category, keywords])

        count += 1
        if count % 10000 == 0:
            print(f"  Processed {count:,} titles...")

print(f"\n✓ Successfully generated {count:,} titles with descriptions")
print(f"✓ Saved to: {output_file}")

# Show file size
import os
file_size = os.path.getsize(output_file)
print(f"✓ File size: {file_size / (1024*1024):.1f} MB")

# Show sample
print("\nSample entries:")
with open(output_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for i, row in enumerate(reader):
        if i < 5:
            print(f"\n{i+1}. Title: {row[0]}")
            print(f"   Description: {row[1][:100]}...")
            print(f"   Category: {row[2]}")
        else:
            break
