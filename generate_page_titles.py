import csv
import itertools

# Define all the attributes we'll combine

# Property types
property_types = [
    "Homes", "Houses", "Properties", "Condos", "Townhomes",
    "Estates", "Villas", "Ranches", "Bungalows", "Duplexes",
    "Single Family Homes", "Luxury Homes", "New Homes", "Resale Homes"
]

# El Paso areas and neighborhoods
areas = [
    "El Paso", "West El Paso", "East El Paso", "Northeast El Paso",
    "Central El Paso", "Mission Valley", "Eastside", "Westside",
    "Far East El Paso", "Lower Valley", "Upper Valley", "Horizon City",
    "Socorro", "San Elizario", "Canutillo", "Anthony", "Sunland Park",
    "Kern Place", "Sunset Heights", "Manhattan Heights", "Coronado",
    "Montecillo", "Cimarron", "East Side", "Northeast Heights"
]

# Features
features = [
    "with Pools", "with Swimming Pools", "with 2 Stories", "with 3 Stories",
    "with 2 Car Garages", "with 3 Car Garages", "with RV Parking",
    "with Mountain Views", "with Courtyards", "with Fireplaces",
    "with Updated Kitchens", "with Granite Countertops", "with Hardwood Floors",
    "with Tile Floors", "with Open Floor Plans", "with Master Suites",
    "with Walk-in Closets", "with Balconies", "with Patios",
    "with Covered Patios", "with Backyards", "with Large Yards",
    "with Desert Landscaping", "with Gourmet Kitchens", "with Stainless Steel Appliances",
    "with Energy Efficient Features", "with Solar Panels", "with Smart Home Features",
    "with Security Systems", "with Vaulted Ceilings", "with Cathedral Ceilings",
    "with Skylights", "with Bonus Rooms", "with Home Offices",
    "with Media Rooms", "with Game Rooms", "with Wet Bars",
    "with Wine Cellars", "with Casitas", "with Guest Houses",
    "in Gated Communities", "in Golf Course Communities", "on Corner Lots",
    "on Cul-de-Sacs", "with City Views", "with Park Views",
    "Near Schools", "Near Shopping", "Near UTEP", "Near Fort Bliss",
    "with Finished Basements", "with Unfinished Basements", "with Lofts",
    "Recently Renovated", "Move-in Ready", "Fixer Uppers",
    "with Attached Garages", "with Detached Garages", "with Carports"
]

# Bedroom counts
bedrooms = [
    "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom",
    "5 Bedroom", "6 Bedroom", "Studio"
]

# Bathroom counts
bathrooms = [
    "1 Bathroom", "1.5 Bathroom", "2 Bathroom", "2.5 Bathroom",
    "3 Bathroom", "3.5 Bathroom", "4 Bathroom", "5 Bathroom"
]

# Price ranges
price_ranges = [
    "Under $100k", "Under $150k", "Under $200k", "Under $250k",
    "$100k to $200k", "$150k to $250k", "$200k to $300k", "$250k to $350k",
    "$300k to $400k", "$350k to $450k", "$400k to $500k", "$500k to $600k",
    "$600k to $700k", "$700k to $800k", "$800k to $900k", "$900k to $1M",
    "Over $500k", "Over $750k", "Over $1M"
]

# Square footage
square_footage = [
    "Under 1000 Sq Ft", "1000-1500 Sq Ft", "1500-2000 Sq Ft",
    "2000-2500 Sq Ft", "2500-3000 Sq Ft", "3000-3500 Sq Ft",
    "3500-4000 Sq Ft", "Over 4000 Sq Ft", "Over 5000 Sq Ft"
]

# Lot sizes
lot_sizes = [
    "Small Lots", "Medium Lots", "Large Lots", "Quarter Acre Lots",
    "Half Acre Lots", "1 Acre Lots", "Multi-Acre Lots"
]

# Year built
year_built = [
    "New Construction", "Built After 2020", "Built After 2015",
    "Built After 2010", "Built After 2000", "Built After 1990",
    "Historic Homes", "Mid-Century Homes"
]

# Additional style descriptors
styles = [
    "Modern", "Contemporary", "Traditional", "Spanish Style",
    "Mediterranean", "Ranch Style", "Craftsman", "Adobe Style",
    "Pueblo Style", "Territorial Style", "Southwestern"
]

# Status
status = [
    "For Sale", "New Listings", "Recently Listed", "Price Reduced",
    "Open Houses", "Coming Soon", "Foreclosures", "Short Sales",
    "Bank Owned", "Investor Friendly"
]

def generate_title_and_description(components):
    """Generate a page title and description from components"""
    title_parts = [c for c in components if c]
    title = " ".join(title_parts)

    # Generate SEO-friendly description
    description = f"Browse {title.lower()} in El Paso, Texas. "
    description += "Find your perfect home with detailed listings, photos, and neighborhood information. "
    description += "Search the latest El Paso real estate with our comprehensive property database."

    return title, description

# Generate combinations
page_titles = []

print("Generating page titles...")

# Base combinations: Property Type + Area
for prop_type, area in itertools.product(property_types, areas):
    title, desc = generate_title_and_description([prop_type, "in", area])
    page_titles.append((title, desc))

# Property Type + Area + Feature
for prop_type, area, feature in itertools.product(property_types, areas, features):
    title, desc = generate_title_and_description([prop_type, feature, "in", area])
    page_titles.append((title, desc))

# Property Type + Bedrooms + Area
for prop_type, bedroom, area in itertools.product(property_types, bedrooms, areas):
    title, desc = generate_title_and_description([bedroom, prop_type, "in", area])
    page_titles.append((title, desc))

# Property Type + Bedrooms + Bathrooms + Area
for prop_type, bedroom, bathroom, area in itertools.product(property_types, bedrooms, bathrooms, areas[:10]):  # Limit areas for this combo
    title, desc = generate_title_and_description([bedroom, bathroom, prop_type, "in", area])
    page_titles.append((title, desc))

# Property Type + Price Range + Area
for prop_type, price, area in itertools.product(property_types, price_ranges, areas):
    title, desc = generate_title_and_description([prop_type, price, "in", area])
    page_titles.append((title, desc))

# Property Type + Feature + Bedrooms
for prop_type, feature, bedroom in itertools.product(property_types, features[:30], bedrooms):  # Limit features
    title, desc = generate_title_and_description([bedroom, prop_type, feature, "in El Paso"])
    page_titles.append((title, desc))

# Property Type + Square Footage + Area
for prop_type, sqft, area in itertools.product(property_types, square_footage, areas[:15]):
    title, desc = generate_title_and_description([prop_type, sqft, "in", area])
    page_titles.append((title, desc))

# Property Type + Lot Size + Area
for prop_type, lot_size, area in itertools.product(property_types, lot_sizes, areas[:15]):
    title, desc = generate_title_and_description([prop_type, "on", lot_size, "in", area])
    page_titles.append((title, desc))

# Property Type + Year Built + Area
for prop_type, year, area in itertools.product(property_types, year_built, areas[:15]):
    title, desc = generate_title_and_description([year, prop_type, "in", area])
    page_titles.append((title, desc))

# Style + Property Type + Area
for style, prop_type, area in itertools.product(styles, property_types, areas):
    title, desc = generate_title_and_description([style, prop_type, "in", area])
    page_titles.append((title, desc))

# Status + Property Type + Area
for stat, prop_type, area in itertools.product(status, property_types, areas):
    title, desc = generate_title_and_description([prop_type, stat, "in", area])
    page_titles.append((title, desc))

# Price Range + Bedrooms + Area
for price, bedroom, area in itertools.product(price_ranges, bedrooms, areas):
    title, desc = generate_title_and_description([bedroom, "Homes", price, "in", area])
    page_titles.append((title, desc))

# Feature + Bedrooms + Price Range + Area (limited)
for feature, bedroom, price, area in itertools.product(features[:20], bedrooms, price_ranges[:10], areas[:8]):
    title, desc = generate_title_and_description([bedroom, "Homes", feature, price, "in", area])
    page_titles.append((title, desc))

# Style + Feature + Area
for style, feature, area in itertools.product(styles, features[:25], areas[:15]):
    title, desc = generate_title_and_description([style, "Homes", feature, "in", area])
    page_titles.append((title, desc))

# Bedrooms + Feature + Area
for bedroom, feature, area in itertools.product(bedrooms, features, areas):
    title, desc = generate_title_and_description([bedroom, "Homes", feature, "in", area])
    page_titles.append((title, desc))

# Price + Feature + Area
for price, feature, area in itertools.product(price_ranges, features[:30], areas[:12]):
    title, desc = generate_title_and_description(["Homes", price, feature, "in", area])
    page_titles.append((title, desc))

# Square Footage + Feature + Area (limited)
for sqft, feature, area in itertools.product(square_footage, features[:20], areas[:10]):
    title, desc = generate_title_and_description(["Homes", sqft, feature, "in", area])
    page_titles.append((title, desc))

# Style + Bedrooms + Area
for style, bedroom, area in itertools.product(styles, bedrooms, areas):
    title, desc = generate_title_and_description([style, bedroom, "Homes", "in", area])
    page_titles.append((title, desc))

# Year Built + Feature + Area (limited)
for year, feature, area in itertools.product(year_built, features[:20], areas[:10]):
    title, desc = generate_title_and_description([year, "Homes", feature, "in", area])
    page_titles.append((title, desc))

print(f"Generated {len(page_titles)} unique page titles!")

# Write to CSV
with open('el_paso_real_estate_page_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Page Title', 'Meta Description'])
    writer.writerows(page_titles)

print(f"CSV file created with {len(page_titles)} page titles!")
