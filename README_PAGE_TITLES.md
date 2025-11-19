# Austin Real Estate Page Titles - 364,040+ Pages

This repository contains **364,040 unique, SEO-optimized page titles** with descriptions for an Austin, Texas real estate website.

## 📁 Files Included

### Complete Dataset (Split Files)
Due to GitHub's 100MB file size limit, the complete dataset is split into 4 files:

- `austin_real_estate_titles_part1_of_4.csv` (91,010 rows, 25.5 MB)
- `austin_real_estate_titles_part2_of_4.csv` (91,010 rows, 25.1 MB)
- `austin_real_estate_titles_part3_of_4.csv` (91,010 rows, 25.3 MB)
- `austin_real_estate_titles_part4_of_4.csv` (91,010 rows, 25.4 MB)

**Total: 364,040 unique page titles with descriptions**

### CSV Format
Each CSV file contains:
- **Page Title**: Unique, SEO-optimized title for each page
- **Meta Description**: 150-250 character SEO description
- **Category**: Page categorization (Bedrooms, Price Range, Luxury, Schools, etc.)
- **Keywords**: Extracted keywords for SEO targeting

### Additional Files
- `austin_real_estate_page_titles.txt` - Plain text list of all titles (15 MB)
- `austin_real_estate_page_titles.csv` - Original categorized titles (34 MB)
- `generate_page_titles.py` - Python script to generate titles
- `add_descriptions.py` - Python script to add descriptions

## 🎯 Coverage

### Property Types
- Homes, Houses, Single Family Homes
- Condos, Townhomes
- Luxury Homes, Estate Homes
- Villas, Patio Homes, Ranch Homes

### 70 Austin Neighborhoods & Areas
Downtown Austin, West Lake Hills, Tarrytown, Hyde Park, Mueller, Steiner Ranch, Cedar Park, Round Rock, Pflugerville, Lakeway, and 60+ more locations

### Bedroom/Bathroom Combinations
- Studio through 6+ bedrooms
- All bathroom combinations (1 bath through 5+ baths)
- All common bed/bath ratios (3/2, 4/3, 5/4, etc.)

### 100+ Property Features
**Outdoor & Structure:**
- Pools (swimming pool, private pool, etc.)
- Stories (1-story, 2-story, 3-story, ranch)
- Garages (2-car, 3-car, attached)
- Backyards, large lots, acreage
- Covered patios, decks, outdoor kitchens

**Interior Features:**
- Hardwood floors, granite countertops
- Updated/modern kitchens
- Master suites, walk-in closets
- Home offices, game rooms, media rooms
- Fireplaces, high ceilings, open floor plans

**Views & Location:**
- Lake views (Lake Travis, Lake Austin)
- Hill Country views
- Waterfront, lakefront properties
- Golf course views, greenbelt access

**Modern Amenities:**
- Smart home features
- Solar panels, energy efficient
- New construction (2023, 2024)
- Wine cellars, home gyms

**Architectural Styles:**
- Contemporary, Modern, Mid-Century Modern
- Craftsman, Victorian, Mediterranean
- Traditional, Spanish Style, Texas Ranch

### Price Ranges
- Under 200k through Under 5M
- Range brackets (200k-300k, 300k-400k, etc.)
- Affordable, Budget Friendly, Luxury, Million Dollar

### Square Footage
- Under 1000 sq ft through Over 5000 sq ft
- All common size ranges

### School Districts
- Austin ISD
- Eanes ISD (Westlake)
- Round Rock ISD
- Pflugerville ISD
- Leander ISD
- Lake Travis ISD
- And more...

### Special Categories
- Investment Properties
- Starter Homes, Forever Homes
- Retirement, Downsizing
- Family Friendly, Pet Friendly
- New Construction, Renovated
- Foreclosures, Fixer Uppers
- Waterfront, Equestrian

## 📊 Example Titles & Descriptions

### Example 1: Neighborhood + Features
**Title:** "3 Bedroom 2 Bath Homes with Pool in Steiner Ranch"

**Description:** "Discover 3-bedroom homes, 2-bathroom in Steiner Ranch. Browse our current listings featuring swimming pools. Find your perfect home today with detailed photos, virtual tours, and neighborhood information."

**Category:** Neighborhood; Bedrooms

**Keywords:** bedroom, bath, homes, pool, steiner, ranch

### Example 2: Luxury + Location
**Title:** "Luxury Homes with Hill Country View in West Lake Hills"

**Description:** "Search homes in West Lake Hills in the luxury market. View homes featuring Hill Country views, luxury finishes. Updated daily with new listings, price changes, and open house schedules."

**Category:** Price Range; Views & Location

**Keywords:** luxury, homes, hill, country, view, west, lake, hills

### Example 3: Price Range
**Title:** "4 Bedroom Single Story Homes Under 500k in Cedar Park"

**Description:** "Browse 4-bedroom homes available in Cedar Park under $500,000. Filter by single-story layouts and more. Get instant access to MLS listings, market trends, and comparative market analysis."

**Category:** Bedrooms; Stories

**Keywords:** bedroom, single, story, homes, under, 500k, cedar, park

## 🔧 How to Use

### Combining Split Files
To combine all CSV files into one:

```bash
# Linux/Mac
cat austin_real_estate_titles_part*.csv > combined.csv
# Then remove duplicate headers

# Or use Python:
python3 << 'EOF'
import csv

with open('combined_all_titles.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    header_written = False

    for i in range(1, 5):
        with open(f'austin_real_estate_titles_part{i}_of_4.csv', 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)

            if not header_written:
                writer.writerow(header)
                header_written = True

            for row in reader:
                writer.writerow(row)

print("Combined successfully!")
EOF
```

### Importing to Database
```python
import csv
import sqlite3

conn = sqlite3.connect('pages.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE page_titles (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT,
        keywords TEXT
    )
''')

for i in range(1, 5):
    with open(f'austin_real_estate_titles_part{i}_of_4.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header

        for row in reader:
            cursor.execute('INSERT INTO page_titles (title, description, category, keywords) VALUES (?, ?, ?, ?)', row)

conn.commit()
```

### Using with CMS (WordPress, etc.)
Import as pages or posts with:
- **Title** → Page Title
- **Meta Description** → SEO meta description field
- **Category** → Page category/tag
- **Keywords** → Focus keywords for SEO plugins

## 💡 SEO Benefits

1. **Long-tail Keywords**: Each title targets specific search queries
2. **Location-based**: All major Austin neighborhoods covered
3. **Feature-specific**: Targets buyers searching for specific amenities
4. **Price-conscious**: Covers all price ranges
5. **Comprehensive**: 364,040 unique pages = massive SEO footprint
6. **User Intent**: Titles match how people actually search for homes

## 🚀 Use Cases

1. **Real Estate Website**: Create individual pages for each search combination
2. **SEO Landing Pages**: Target specific buyer searches
3. **PPC Campaigns**: Use titles for ad groups and landing pages
4. **Content Planning**: Blog post ideas and topics
5. **Market Research**: Understand buyer search patterns
6. **IDX Integration**: Dynamic page generation based on MLS data

## 📈 Statistics

- **Total Unique Titles**: 364,040
- **Neighborhoods Covered**: 70+
- **Features Included**: 100+
- **Property Types**: 15+
- **Price Ranges**: 25+
- **Bedroom Combinations**: All standard sizes
- **Total File Size**: ~101 MB (split into 4 x 25MB files)

## 🛠️ Regeneration

To regenerate or customize the titles:

1. Edit `generate_page_titles.py` to modify:
   - Neighborhoods list
   - Features
   - Price ranges
   - Property types

2. Run: `python3 generate_page_titles.py`

3. Add descriptions: `python3 add_descriptions.py`

## 📝 License

These titles are provided as-is for real estate marketing purposes. Customize and use as needed for your Austin real estate website.

---

**Generated**: November 2024
**Total Pages**: 364,040
**Coverage**: Austin, TX Metropolitan Area
