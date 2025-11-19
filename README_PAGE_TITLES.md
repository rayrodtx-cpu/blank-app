# Corpus Christi Real Estate Page Titles

This repository contains **1,013,036 unique SEO-optimized page titles** for a Corpus Christi, Texas real estate website, complete with meta descriptions and URL slugs.

## 📁 Files

### CSV Files (Split for GitHub)
- `corpus_christi_page_titles_part1.csv` - Rows 1-200,000 (47 MB)
- `corpus_christi_page_titles_part2.csv` - Rows 200,001-400,000 (48 MB)
- `corpus_christi_page_titles_part3.csv` - Rows 400,001-600,000 (49 MB)
- `corpus_christi_page_titles_part4.csv` - Rows 600,001-800,000 (51 MB)
- `corpus_christi_page_titles_part5.csv` - Rows 800,001-1,000,000 (53 MB)
- `corpus_christi_page_titles_part6.csv` - Rows 1,000,001-1,013,036 (3 MB)

### Scripts
- `generate_page_titles_csv.py` - Generate all titles and descriptions
- `split_csv.py` - Split large CSV into smaller files

## 📊 CSV Format

Each CSV file contains three columns:

| Column | Description | Example |
|--------|-------------|---------|
| **title** | Page title / H1 tag | "3 Bedroom Homes with Pool in Padre Island, TX" |
| **description** | SEO meta description (120-160 chars) | "Browse 3 bedroom homes with pool in padre island, tx for sale. Find your perfect homes in Padre Island, TX with our comprehensive listings..." |
| **url_slug** | URL-friendly slug | "3-bedroom-homes-with-pool-in-padre-island-tx" |

## 🏠 Coverage

The page titles cover comprehensive combinations of:

### Property Types (15)
- Homes, Houses, Properties, Real Estate
- Condos, Townhomes, Townhouses
- Single Family Homes, Luxury Homes, Estates
- Villas, Bungalows, Ranch Homes, Cottages, Residences

### Bedrooms (16 configurations)
- 1-6 bedrooms in various formats (e.g., "3 Bedroom", "3 Bed", "Three Bedroom")

### Bathrooms (12 configurations)
- 1-5 bathrooms including half-baths (e.g., "2 Bath", "2.5 Bath", "3 Bathroom")

### Features (90+)
- **Pools & Outdoor**: Pool, Swimming Pool, Inground Pool, Backyard, Large Yard, Fenced Yard
- **Structure**: 2 Stories, 3 Stories, Multiple Stories
- **Garage**: Garage, 2 Car Garage, 3 Car Garage, Attached Garage
- **Views**: Waterfront, Bay View, Ocean View, Water View, Golf Course View, Park View
- **Interior**: Updated Kitchen, Hardwood Floors, Open Floor Plan, High Ceilings, Fireplace
- **Amenities**: Master Suite, Walk-in Closet, Home Office, Game Room, Media Room
- **Modern**: Smart Home, Solar Panels, Energy Efficient, New HVAC
- **Community**: Gated Community, HOA, No HOA
- **Parking**: RV Parking, Boat Parking
- **Lot Features**: Corner Lot, Cul-de-sac, Oversized Lot, Acreage
- **Beach Access**: Beach Access, Fishing Pier, Boat Dock, Private Beach, Deep Water Access

### Locations (44 neighborhoods)
- Corpus Christi (North, South, Downtown, Central, West)
- Padre Island, North Padre Island
- Flour Bluff, Calallen, Annaville
- Ocean Drive, Bayfront, Bay Area, Oso Bay
- Port Aransas, Portland, Ingleside, Rockport, Aransas Pass
- And 25+ more neighborhoods and communities

### Price Ranges (15)
- Under $100K, Under $150K, Under $200K, Under $250K, Under $300K
- $100K-$200K, $200K-$300K, $300K-$400K, $400K-$500K, $500K-$750K
- $750K-$1M, Over $1M
- Luxury, Affordable, Budget Friendly

### Property Conditions (10)
- New Construction, Recently Built, Newly Renovated, Updated
- Move-in Ready, Fixer Upper, As-Is, Turn Key
- Recently Listed, Just Listed, New Listing, Coming Soon

### Qualifiers (19)
- Best, Top, Affordable, Luxury, Premium, Executive
- Family Friendly, Waterfront, Beachfront, Golf Course
- Pet Friendly, Senior Living, Active Adult, Gated
- Private, Secluded, Quiet, View, Custom Built

## 💡 Use Cases

### SEO Landing Pages
Generate individual landing pages for each title to capture long-tail search traffic.

### Dynamic Page Generation
Use the CSV to dynamically generate pages based on user search criteria.

### Meta Tags
Use the title and description columns for SEO meta tags:
```html
<title>3 Bedroom Homes with Pool in Padre Island, TX</title>
<meta name="description" content="Browse 3 bedroom homes with pool in padre island, tx for sale...">
```

### URL Structure
Use the url_slug column for clean, SEO-friendly URLs:
```
https://yoursite.com/listings/3-bedroom-homes-with-pool-in-padre-island-tx
```

### Internal Linking
Create comprehensive internal linking structure using all variations.

### Content Templates
Use titles as templates for creating detailed property listing pages.

## 🔧 How to Use

### Combine Split Files (Optional)
If you need all data in a single file:

```bash
# On Linux/Mac
cat corpus_christi_page_titles_part*.csv > corpus_christi_page_titles_full.csv

# Remove duplicate headers
tail -n +2 corpus_christi_page_titles_part2.csv >> temp.csv
tail -n +2 corpus_christi_page_titles_part3.csv >> temp.csv
tail -n +2 corpus_christi_page_titles_part4.csv >> temp.csv
tail -n +2 corpus_christi_page_titles_part5.csv >> temp.csv
tail -n +2 corpus_christi_page_titles_part6.csv >> temp.csv
cat corpus_christi_page_titles_part1.csv temp.csv > corpus_christi_page_titles_full.csv
rm temp.csv
```

### Import to Database
```python
import pandas as pd

# Read CSV
df = pd.read_csv('corpus_christi_page_titles_part1.csv')

# Import to database (example with SQLite)
import sqlite3
conn = sqlite3.connect('real_estate.db')
df.to_sql('page_titles', conn, if_exists='append', index=False)
```

### Import to CMS
Most CMS platforms (WordPress, Drupal, etc.) can import CSV files directly through plugins or built-in importers.

### Use in Web Application
```python
import csv

with open('corpus_christi_page_titles_part1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row['title']
        description = row['description']
        slug = row['url_slug']
        # Create your page/route here
```

## 📈 Statistics

- **Total Titles**: 1,013,036
- **Total File Size**: ~252 MB (all parts combined)
- **Average Title Length**: ~45 characters
- **Average Description Length**: ~145 characters
- **Average URL Slug Length**: ~42 characters

## 🔄 Regenerating

To regenerate the titles with different parameters:

```bash
# Generate new titles
python3 generate_page_titles_csv.py

# Split into smaller files
python3 split_csv.py
```

## 📝 Notes

- All titles are unique and SEO-optimized
- Descriptions include CTAs (calls-to-action)
- Neighborhood-specific highlights included where applicable
- URL slugs are lowercase and hyphenated for SEO best practices
- Descriptions range from 120-160 characters (optimal for search engines)

## 🎯 SEO Benefits

1. **Long-tail Keywords**: Captures specific search queries
2. **Local SEO**: Includes 44 Corpus Christi neighborhoods
3. **Feature Targeting**: 90+ property features for specific searches
4. **Price Point Pages**: 15 price ranges for budget-specific searches
5. **Comprehensive Coverage**: Over 1 million unique combinations

## 📞 Support

For questions or custom title generation needs, please refer to the generator scripts included in this repository.

---

**Generated**: 2025-11-19
**Total Records**: 1,013,036
**Format**: CSV (UTF-8)
