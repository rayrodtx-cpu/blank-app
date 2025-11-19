"""
Interactive Title Browser
Browse the 123,322 San Antonio real estate page titles by category
"""

import re

def load_titles():
    """Load all titles from file"""
    with open('san_antonio_real_estate_page_titles.txt', 'r') as f:
        return [line.strip() for line in f]

def search_titles(titles, search_term, case_sensitive=False):
    """Search for titles containing a term"""
    if case_sensitive:
        return [t for t in titles if search_term in t]
    else:
        search_lower = search_term.lower()
        return [t for t in titles if search_lower in t.lower()]

def main():
    print("Loading 123,322 San Antonio real estate page titles...")
    titles = load_titles()
    print(f"Loaded {len(titles):,} titles\n")

    # Show category counts
    categories = {
        "Homes with pools": "with pools",
        "Homes with swimming pools": "with swimming pools",
        "2 story homes": "2 story",
        "1 story homes": "1 story",
        "3 bedroom": "3 bedroom",
        "4 bedroom": "4 bedroom",
        "5 bedroom": "5 bedroom",
        "Alamo Heights": "alamo heights",
        "Stone Oak": "stone oak",
        "The Dominion": "the dominion",
        "Terrell Hills": "terrell hills",
        "Downtown San Antonio": "downtown san antonio",
        "Luxury homes": "luxury",
        "New construction": "new construction",
        "Gated community": "gated community",
        "Golf course": "golf course",
        "Under 300k": "under 300k",
        "Under 500k": "under 500k",
        "Over 1 million": "over 1 million",
        "With garage": "with garage",
        "With 2 car garage": "with 2 car garage",
        "With 3 car garage": "with 3 car garage",
        "With acreage": "with acreage",
        "Hill country views": "hill country views",
        "Condos": "condos",
        "Townhomes": "townhomes",
        "Single family homes": "single family homes",
    }

    print("=" * 70)
    print("CATEGORY COUNTS")
    print("=" * 70)

    for category, search_term in categories.items():
        count = len(search_titles(titles, search_term))
        print(f"{category:30} : {count:6,} titles")

    print("\n" + "=" * 70)
    print("SAMPLE TITLES BY CATEGORY")
    print("=" * 70 + "\n")

    # Show samples from each category
    sample_categories = [
        ("Homes with pools in Alamo Heights", "with pools", "alamo heights"),
        ("2 story homes in Stone Oak", "2 story", "stone oak"),
        ("3 bedroom 2 bathroom homes", "3 bedroom 2 bathroom", None),
        ("Luxury homes in The Dominion", "luxury", "the dominion"),
        ("New construction", "new construction", None),
        ("Homes under 300k", "under 300k", None),
        ("Gated community", "gated community", None),
    ]

    for title, term1, term2 in sample_categories:
        print(f"\n{title.upper()}")
        print("-" * 70)

        results = search_titles(titles, term1)
        if term2:
            results = [t for t in results if term2.lower() in t.lower()]

        for i, t in enumerate(results[:20], 1):
            print(f"{i:2}. {t}")

        if len(results) > 20:
            print(f"... and {len(results) - 20:,} more")
        print(f"Total: {len(results):,} titles")

    # Neighborhood breakdown
    print("\n" + "=" * 70)
    print("TITLES BY NEIGHBORHOOD (Sample counts)")
    print("=" * 70)

    neighborhoods = [
        "Alamo Heights", "Stone Oak", "The Dominion", "Terrell Hills",
        "Olmos Park", "Shavano Park", "Downtown San Antonio", "Medical Center",
        "UTSA Area", "Southtown", "King William", "Monte Vista",
        "Boerne", "Fair Oaks Ranch", "Helotes", "New Braunfels"
    ]

    for neighborhood in neighborhoods:
        count = len(search_titles(titles, neighborhood))
        print(f"{neighborhood:30} : {count:6,} titles")

    # Feature breakdown
    print("\n" + "=" * 70)
    print("TITLES BY FEATURE")
    print("=" * 70)

    features = [
        "with pools", "with garage", "with acreage", "with views",
        "with hill country views", "with hardwood floors", "with granite countertops",
        "with master suite", "with office", "with game room", "with media room",
        "with chef's kitchen", "with outdoor kitchen", "with covered patio",
        "with large backyard", "with fenced yard", "with fireplace",
        "with open floor plan", "with high ceilings", "with smart home features"
    ]

    for feature in features:
        count = len(search_titles(titles, feature))
        print(f"{feature:30} : {count:6,} titles")

    print("\n" + "=" * 70)
    print("HOW TO SEARCH")
    print("=" * 70)
    print("""
To find specific titles, use grep command:

Examples:
  grep -i "pool" san_antonio_real_estate_page_titles.txt
  grep -i "alamo heights" san_antonio_real_estate_page_titles.txt | grep -i "pool"
  grep -i "3 bedroom" san_antonio_real_estate_page_titles.txt | grep -i "stone oak"

Count results:
  grep -ic "pool" san_antonio_real_estate_page_titles.txt

Export to new file:
  grep -i "pool" san_antonio_real_estate_page_titles.txt > pool_homes.txt
    """)

if __name__ == "__main__":
    main()
