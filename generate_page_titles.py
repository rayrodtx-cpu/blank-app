"""
Real Estate Page Title Generator for Dallas
Generates 50,000+ unique page titles for SEO optimization
"""

import itertools
import json
from typing import List, Set

class RealEstatePageTitleGenerator:
    def __init__(self):
        self.city = "Dallas"
        self.state = "TX"

        # Property Types
        self.property_types = [
            "Homes", "Houses", "Properties", "Single Family Homes", "Townhomes",
            "Condos", "Luxury Homes", "Estate Homes", "Ranch Homes", "Contemporary Homes",
            "Traditional Homes", "Modern Homes", "Villas", "Patio Homes", "Garden Homes",
            "Duplexes", "Multi-Family Homes", "Investment Properties", "Fixer Uppers",
            "New Construction Homes", "Resale Homes"
        ]

        # Bedrooms
        self.bedrooms = [
            "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom",
            "6 Bedroom", "1-2 Bedroom", "2-3 Bedroom", "3-4 Bedroom", "4-5 Bedroom",
            "5+ Bedroom"
        ]

        # Bathrooms
        self.bathrooms = [
            "1 Bath", "1.5 Bath", "2 Bath", "2.5 Bath", "3 Bath", "3.5 Bath",
            "4 Bath", "4.5 Bath", "5+ Bath"
        ]

        # Stories
        self.stories = [
            "Single Story", "1 Story", "2 Story", "3 Story", "Multi-Story"
        ]

        # Features
        self.features = [
            "with Pool", "with Private Pool", "with Sparkling Pool", "with Saltwater Pool",
            "with Heated Pool", "with Infinity Pool", "with In-Ground Pool", "with Above Ground Pool",
            "with Garage", "with 2 Car Garage", "with 3 Car Garage", "with Attached Garage",
            "with Detached Garage", "with Oversized Garage", "with Tandem Garage",
            "with Fireplace", "with Wood Burning Fireplace", "with Gas Fireplace",
            "with Master Suite", "with Walk-In Closets", "with Updated Kitchen",
            "with Granite Countertops", "with Stainless Steel Appliances", "with Island Kitchen",
            "with Gourmet Kitchen", "with Open Floor Plan", "with High Ceilings",
            "with Vaulted Ceilings", "with Crown Molding", "with Hardwood Floors",
            "with Tile Floors", "with Carpet", "with Laminate Flooring",
            "with Backyard", "with Large Backyard", "with Fenced Yard", "with Covered Patio",
            "with Deck", "with Balcony", "with Screened Porch", "with Front Porch",
            "with Game Room", "with Media Room", "with Home Office", "with Study",
            "with Bonus Room", "with Loft", "with Finished Basement", "with Wine Cellar",
            "with Smart Home Features", "with Security System", "with Energy Efficient Features",
            "with Solar Panels", "with Sprinkler System", "with Landscaping",
            "with Mature Trees", "with Corner Lot", "with Cul-de-Sac Location",
            "with Mountain Views", "with Lake Views", "with City Views", "with Golf Course Views",
            "with Privacy", "with Guest House", "with Mother-In-Law Suite",
            "with RV Parking", "with Boat Parking", "with Workshop", "with Storage",
            "with Laundry Room", "with Mudroom", "with Breakfast Nook", "with Dining Room",
            "with Formal Living Room", "with Den", "with Library", "with Wet Bar",
            "with Butler's Pantry", "with Double Vanity", "with Garden Tub",
            "with Separate Shower", "with His and Hers Closets", "with Jacuzzi",
            "with Central Air", "with Central Heat", "with Dual AC Units",
            "with Tankless Water Heater", "with New Roof", "with New Windows",
            "with Fresh Paint", "with Upgraded Fixtures"
        ]

        # Price Ranges
        self.price_ranges = [
            "Under $100K", "Under $150K", "Under $200K", "Under $250K", "Under $300K",
            "Under $350K", "Under $400K", "Under $450K", "Under $500K", "Under $600K",
            "Under $700K", "Under $800K", "Under $900K", "Under $1M",
            "$100K-$200K", "$200K-$300K", "$300K-$400K", "$400K-$500K", "$500K-$600K",
            "$600K-$700K", "$700K-$800K", "$800K-$900K", "$900K-$1M",
            "$1M-$2M", "$2M-$3M", "$3M+", "Luxury Price Range", "Affordable"
        ]

        # Square Footage
        self.square_footage = [
            "Under 1000 Sq Ft", "Under 1500 Sq Ft", "Under 2000 Sq Ft", "Under 2500 Sq Ft",
            "Under 3000 Sq Ft", "Under 3500 Sq Ft", "Under 4000 Sq Ft", "Under 5000 Sq Ft",
            "1000-1500 Sq Ft", "1500-2000 Sq Ft", "2000-2500 Sq Ft", "2500-3000 Sq Ft",
            "3000-3500 Sq Ft", "3500-4000 Sq Ft", "4000+ Sq Ft", "5000+ Sq Ft"
        ]

        # Lot Size
        self.lot_sizes = [
            "on Large Lot", "on Small Lot", "on Quarter Acre", "on Half Acre",
            "on 1 Acre", "on 2+ Acres", "on 5+ Acres", "on 10+ Acres"
        ]

        # Dallas Neighborhoods
        self.neighborhoods = [
            "in Uptown Dallas", "in Downtown Dallas", "in Oak Lawn", "in Highland Park",
            "in University Park", "in Preston Hollow", "in Lake Highlands", "in East Dallas",
            "in North Dallas", "in South Dallas", "in West Dallas", "in Lakewood",
            "in White Rock Lake", "in Vickery Meadow", "in Pleasant Grove", "in Oak Cliff",
            "in Bishop Arts District", "in Deep Ellum", "in Design District", "in Victory Park",
            "in Turtle Creek", "in Knox Henderson", "in Lower Greenville", "in M Streets",
            "in Kessler Park", "in Stevens Park", "in Winnetka Heights", "in Elmwood",
            "in Cedar Hill", "in DeSoto", "in Duncanville", "in Lancaster",
            "in Grand Prairie", "in Irving", "in Garland", "in Mesquite",
            "in Richardson", "in Plano", "in Frisco", "in McKinney",
            "in Allen", "in Carrollton", "in Farmers Branch", "in Addison",
            "in Coppell", "in Lewisville", "in Flower Mound", "in The Colony",
            "in Little Elm", "in Prosper", "in Celina", "in Rowlett",
            "in Rockwall", "in Wylie", "in Sachse", "in Murphy",
            "near Downtown", "near Uptown", "near SMU", "near DFW Airport",
            "near Love Field", "near Dallas Arboretum", "near Fair Park"
        ]

        # Condition
        self.conditions = [
            "New Construction", "Newly Built", "Recently Renovated", "Recently Updated",
            "Move-In Ready", "Turnkey", "Needs TLC", "Fixer Upper Opportunity",
            "Completely Remodeled", "Like New", "Well Maintained"
        ]

        # Architectural Styles
        self.styles = [
            "Ranch Style", "Colonial Style", "Victorian Style", "Craftsman Style",
            "Mediterranean Style", "Spanish Style", "French Country", "Tudor Style",
            "Mid-Century Modern", "Contemporary Style", "Traditional Style", "Modern Style",
            "Farmhouse Style", "Transitional Style", "Cottage Style", "Bungalow Style"
        ]

        # Time-based
        self.time_based = [
            "Just Listed", "New Listing", "Recently Listed", "Coming Soon",
            "Price Reduced", "Back on Market", "Hot Property"
        ]

        # Buyer Types
        self.buyer_types = [
            "for First Time Buyers", "for Investors", "for Families", "for Retirees",
            "for Downsizers", "for Empty Nesters", "for Young Professionals",
            "for Growing Families", "for Luxury Buyers"
        ]

        # Special Features
        self.special = [
            "with HOA", "No HOA", "Gated Community", "in Golf Course Community",
            "in Master Planned Community", "in Active Adult Community", "in Family Friendly Neighborhood",
            "Walking Distance to Schools", "Near Parks", "Near Shopping", "Near Restaurants",
            "Near Medical Centers", "Near Public Transit", "Easy Highway Access",
            "Quiet Street", "Tree Lined Street", "Award Winning Schools",
            "Top Rated School District", "Pet Friendly"
        ]

    def generate_all_titles(self) -> Set[str]:
        """Generate all possible title combinations"""
        titles = set()

        # Basic templates
        print("Generating basic property type titles...")
        titles.update(self._generate_basic_titles())

        print("Generating bedroom + property type titles...")
        titles.update(self._generate_bedroom_titles())

        print("Generating bedroom + bathroom titles...")
        titles.update(self._generate_bed_bath_titles())

        print("Generating feature-based titles...")
        titles.update(self._generate_feature_titles())

        print("Generating neighborhood titles...")
        titles.update(self._generate_neighborhood_titles())

        print("Generating price range titles...")
        titles.update(self._generate_price_titles())

        print("Generating square footage titles...")
        titles.update(self._generate_sqft_titles())

        print("Generating story-based titles...")
        titles.update(self._generate_story_titles())

        print("Generating style-based titles...")
        titles.update(self._generate_style_titles())

        print("Generating complex combination titles...")
        titles.update(self._generate_complex_titles())

        print("Generating ultra-specific titles...")
        titles.update(self._generate_ultra_specific_titles())

        print("Generating additional variation titles...")
        titles.update(self._generate_additional_variations())

        return titles

    def _generate_basic_titles(self) -> Set[str]:
        """Basic property type titles"""
        titles = set()
        for prop_type in self.property_types:
            titles.add(f"{prop_type} in {self.city}")
            titles.add(f"{prop_type} for Sale in {self.city}")
            titles.add(f"{prop_type} for Sale in {self.city}, {self.state}")
            titles.add(f"Find {prop_type} in {self.city}")
            titles.add(f"Buy {prop_type} in {self.city}")
            titles.add(f"Search {prop_type} in {self.city}")
        return titles

    def _generate_bedroom_titles(self) -> Set[str]:
        """Bedroom + property type combinations"""
        titles = set()
        for bedroom in self.bedrooms:
            for prop_type in self.property_types:
                titles.add(f"{bedroom} {prop_type} in {self.city}")
                titles.add(f"{bedroom} {prop_type} for Sale in {self.city}")
        return titles

    def _generate_bed_bath_titles(self) -> Set[str]:
        """Bedroom + bathroom combinations"""
        titles = set()
        for bedroom in self.bedrooms:
            for bathroom in self.bathrooms:
                for prop_type in self.property_types[:10]:  # Limit to avoid too many
                    titles.add(f"{bedroom} {bathroom} {prop_type} in {self.city}")
                    titles.add(f"{bedroom}, {bathroom} {prop_type} for Sale in {self.city}")
        return titles

    def _generate_feature_titles(self) -> Set[str]:
        """Feature-based titles"""
        titles = set()
        for feature in self.features:
            for prop_type in self.property_types:
                titles.add(f"{prop_type} {feature} in {self.city}")
                titles.add(f"{prop_type} {feature} for Sale in {self.city}")
                titles.add(f"{self.city} {prop_type} {feature}")
        return titles

    def _generate_neighborhood_titles(self) -> Set[str]:
        """Neighborhood-based titles"""
        titles = set()
        for neighborhood in self.neighborhoods:
            for prop_type in self.property_types:
                titles.add(f"{prop_type} {neighborhood}")
                titles.add(f"{prop_type} for Sale {neighborhood}")

            # Add features to neighborhoods
            for feature in self.features[:20]:  # Top features
                titles.add(f"Homes {feature} {neighborhood}")
        return titles

    def _generate_price_titles(self) -> Set[str]:
        """Price range titles"""
        titles = set()
        for price in self.price_ranges:
            for prop_type in self.property_types:
                titles.add(f"{prop_type} {price} in {self.city}")
                titles.add(f"{price} {prop_type} in {self.city}")
                titles.add(f"{price} {prop_type} for Sale in {self.city}")
        return titles

    def _generate_sqft_titles(self) -> Set[str]:
        """Square footage titles"""
        titles = set()
        for sqft in self.square_footage:
            for prop_type in self.property_types[:10]:
                titles.add(f"{prop_type} {sqft} in {self.city}")
                titles.add(f"{sqft} {prop_type} in {self.city}")
        return titles

    def _generate_story_titles(self) -> Set[str]:
        """Story-based titles"""
        titles = set()
        for story in self.stories:
            for prop_type in self.property_types:
                titles.add(f"{story} {prop_type} in {self.city}")
                titles.add(f"{story} {prop_type} for Sale in {self.city}")

            # Stories + features
            for feature in self.features[:30]:
                titles.add(f"{story} Homes {feature} in {self.city}")
        return titles

    def _generate_style_titles(self) -> Set[str]:
        """Architectural style titles"""
        titles = set()
        for style in self.styles:
            for prop_type in self.property_types[:10]:
                titles.add(f"{style} {prop_type} in {self.city}")
                titles.add(f"{style} {prop_type} for Sale in {self.city}")
        return titles

    def _generate_complex_titles(self) -> Set[str]:
        """Complex multi-attribute combinations"""
        titles = set()

        # Bedroom + Feature + Neighborhood
        for bedroom in self.bedrooms[:7]:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{bedroom} Homes {feature} {neighborhood}")

        # Price + Feature + Neighborhood
        for price in self.price_ranges[:10]:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{price} Homes {feature} {neighborhood}")

        # Story + Bedroom + Feature
        for story in self.stories:
            for bedroom in self.bedrooms[:6]:
                for feature in self.features[:20]:
                    titles.add(f"{story} {bedroom} Homes {feature} in {self.city}")

        # Style + Feature + Neighborhood
        for style in self.styles[:10]:
            for feature in self.features[:10]:
                for neighborhood in self.neighborhoods[:10]:
                    titles.add(f"{style} Homes {feature} {neighborhood}")

        return titles

    def _generate_ultra_specific_titles(self) -> Set[str]:
        """Ultra-specific 4+ attribute combinations"""
        titles = set()

        # Bedroom + Bath + Feature + Neighborhood
        for bedroom in self.bedrooms[:5]:
            for bathroom in self.bathrooms[:5]:
                for feature in self.features[:15]:
                    for neighborhood in self.neighborhoods[:15]:
                        titles.add(f"{bedroom} {bathroom} Homes {feature} {neighborhood}")

        # Price + Bedroom + Feature + Neighborhood
        for price in self.price_ranges[:10]:
            for bedroom in self.bedrooms[:5]:
                for feature in self.features[:12]:
                    for neighborhood in self.neighborhoods[:12]:
                        titles.add(f"{price} {bedroom} Homes {feature} {neighborhood}")

        # Story + Style + Feature + Neighborhood
        for story in self.stories[:4]:
            for style in self.styles[:8]:
                for feature in self.features[:10]:
                    for neighborhood in self.neighborhoods[:10]:
                        titles.add(f"{story} {style} Homes {feature} {neighborhood}")

        # Condition + Bedroom + Feature + Price
        for condition in self.conditions[:8]:
            for bedroom in self.bedrooms[:5]:
                for feature in self.features[:10]:
                    for price in self.price_ranges[:8]:
                        titles.add(f"{condition} {bedroom} Homes {feature} {price} in {self.city}")

        # Time-based + Feature + Neighborhood
        for time in self.time_based:
            for feature in self.features[:20]:
                for neighborhood in self.neighborhoods[:25]:
                    titles.add(f"{time} Homes {feature} {neighborhood}")

        # Buyer Type + Feature + Neighborhood
        for buyer in self.buyer_types:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"Homes {feature} {neighborhood} {buyer}")

        # Special + Feature + Neighborhood
        for special in self.special:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"Homes {feature} {special} {neighborhood}")

        # Lot Size + Feature + Neighborhood
        for lot in self.lot_sizes:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"Homes {feature} {lot} {neighborhood}")

        # Additional mega combinations
        # Price + Feature + Special + Neighborhood
        for price in self.price_ranges[:8]:
            for feature in self.features[:8]:
                for special in self.special[:8]:
                    for neighborhood in self.neighborhoods[:8]:
                        titles.add(f"{price} Homes {feature} {special} {neighborhood}")

        # Bedroom + Feature + Special + Neighborhood
        for bedroom in self.bedrooms[:5]:
            for feature in self.features[:10]:
                for special in self.special[:8]:
                    for neighborhood in self.neighborhoods[:10]:
                        titles.add(f"{bedroom} Homes {feature} {special} {neighborhood}")

        # Style + Feature + Price + Neighborhood
        for style in self.styles[:8]:
            for feature in self.features[:8]:
                for price in self.price_ranges[:6]:
                    for neighborhood in self.neighborhoods[:8]:
                        titles.add(f"{style} Homes {feature} {price} {neighborhood}")

        return titles

    def _generate_additional_variations(self) -> Set[str]:
        """Additional variations to push past 50,000"""
        titles = set()

        # Sqft + Feature + Neighborhood
        for sqft in self.square_footage:
            for feature in self.features[:15]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"Homes {sqft} {feature} {neighborhood}")

        # Sqft + Bedroom + Neighborhood
        for sqft in self.square_footage:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{bedroom} Homes {sqft} {neighborhood}")

        # Price + Sqft + Neighborhood
        for price in self.price_ranges[:12]:
            for sqft in self.square_footage:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{price} Homes {sqft} {neighborhood}")

        # Style + Bedroom + Neighborhood
        for style in self.styles:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{style} {bedroom} Homes {neighborhood}")

        # Condition + Feature + Neighborhood
        for condition in self.conditions:
            for feature in self.features[:20]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{condition} Homes {feature} {neighborhood}")

        # Story + Bedroom + Neighborhood
        for story in self.stories:
            for bedroom in self.bedrooms:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{story} {bedroom} Homes {neighborhood}")

        # Bedroom + Bath + Neighborhood
        for bedroom in self.bedrooms[:7]:
            for bathroom in self.bathrooms[:7]:
                for neighborhood in self.neighborhoods:
                    titles.add(f"{bedroom} {bathroom} Homes {neighborhood}")

        # Feature + Special + Neighborhood
        for feature in self.features[:20]:
            for special in self.special[:15]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"Homes {feature} {special} {neighborhood}")

        # Price + Style + Neighborhood
        for price in self.price_ranges[:12]:
            for style in self.styles[:10]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{price} {style} Homes {neighborhood}")

        # Time + Price + Neighborhood
        for time in self.time_based:
            for price in self.price_ranges[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{time} {price} Homes {neighborhood}")

        # Time + Bedroom + Neighborhood
        for time in self.time_based:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:25]:
                    titles.add(f"{time} {bedroom} Homes {neighborhood}")

        # Buyer + Price + Neighborhood
        for buyer in self.buyer_types:
            for price in self.price_ranges[:12]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"Homes {price} {neighborhood} {buyer}")

        # Buyer + Bedroom + Neighborhood
        for buyer in self.buyer_types:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{bedroom} Homes {neighborhood} {buyer}")

        # Lot + Price + Neighborhood
        for lot in self.lot_sizes:
            for price in self.price_ranges[:12]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{price} Homes {lot} {neighborhood}")

        # Lot + Bedroom + Neighborhood
        for lot in self.lot_sizes:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{bedroom} Homes {lot} {neighborhood}")

        # Special + Price + Neighborhood
        for special in self.special[:15]:
            for price in self.price_ranges[:12]:
                for neighborhood in self.neighborhoods[:15]:
                    titles.add(f"{price} Homes {special} {neighborhood}")

        # Special + Bedroom + Neighborhood
        for special in self.special[:15]:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{bedroom} Homes {special} {neighborhood}")

        # Story + Price + Neighborhood
        for story in self.stories:
            for price in self.price_ranges[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{story} {price} Homes {neighborhood}")

        # Style + Price + Feature
        for style in self.styles:
            for price in self.price_ranges[:12]:
                for feature in self.features[:10]:
                    titles.add(f"{style} {price} Homes {feature} in {self.city}")

        # Condition + Price + Neighborhood
        for condition in self.conditions:
            for price in self.price_ranges[:15]:
                for neighborhood in self.neighborhoods[:20]:
                    titles.add(f"{condition} {price} Homes {neighborhood}")

        # Condition + Bedroom + Neighborhood
        for condition in self.conditions:
            for bedroom in self.bedrooms[:7]:
                for neighborhood in self.neighborhoods[:25]:
                    titles.add(f"{condition} {bedroom} Homes {neighborhood}")

        return titles

    def generate_description(self, title: str) -> str:
        """Generate SEO-friendly description for a page title"""
        import random

        # Extract key components from title
        has_pool = "pool" in title.lower()
        has_garage = "garage" in title.lower()
        has_fireplace = "fireplace" in title.lower()
        has_master = "master suite" in title.lower()
        has_updated = "updated" in title.lower() or "remodeled" in title.lower()
        has_new = "new" in title.lower() or "construction" in title.lower()
        has_luxury = "luxury" in title.lower() or "estate" in title.lower()

        # Extract neighborhood if present
        neighborhood = None
        for n in self.neighborhoods:
            if n.lower() in title.lower():
                neighborhood = n.replace("in ", "").replace("near ", "")
                break

        # Extract price range
        price_range = None
        for p in self.price_ranges:
            if p in title:
                price_range = p
                break

        # Extract bedrooms
        bedroom_count = None
        for b in self.bedrooms:
            if b in title:
                bedroom_count = b.lower()
                break

        # Description templates with variations
        descriptions = []

        # Opening phrases
        openings = [
            "Discover amazing",
            "Browse beautiful",
            "Explore stunning",
            "Find your perfect",
            "Search top-rated",
            "View available",
            "Compare the best",
            "See newly listed",
            "Tour premier",
            "Explore exclusive"
        ]

        # Middle phrases based on attributes
        middles = []
        if has_pool:
            middles.extend([
                "featuring sparkling pools",
                "with private swimming pools",
                "including resort-style pools"
            ])
        if has_garage:
            middles.extend([
                "with spacious garages",
                "featuring attached parking"
            ])
        if has_new:
            middles.extend([
                "brand new construction",
                "newly built properties",
                "move-in ready new homes"
            ])
        if has_updated:
            middles.extend([
                "recently renovated",
                "beautifully updated",
                "completely remodeled"
            ])
        if has_luxury:
            middles.extend([
                "upscale luxury properties",
                "prestigious estate homes",
                "high-end residences"
            ])

        # Default middle if no specific features
        if not middles:
            middles = [
                "quality homes",
                "well-maintained properties",
                "desirable residences",
                "prime real estate",
                "exceptional properties"
            ]

        # Closing phrases
        closings = []
        if neighborhood:
            closings.extend([
                f"located {neighborhood}. Schedule your showing today!",
                f"{neighborhood}. Contact us for more details.",
                f"{neighborhood}. Virtual tours available now.",
                f"{neighborhood}. Start your home search here!",
                f"{neighborhood}. Expert local agents ready to help."
            ])
        else:
            closings.extend([
                f"in Dallas, TX. Schedule your tour today!",
                f"throughout Dallas. Contact us to learn more.",
                f"in the Dallas area. Start your search now!",
                f"across Dallas. Professional assistance available.",
                f"in Dallas, Texas. Find your dream home today!"
            ])

        # Add price-specific phrases
        price_phrases = []
        if price_range:
            if "Under" in price_range or "Affordable" in price_range:
                price_phrases.extend([
                    "Affordable options available.",
                    "Great value for your budget.",
                    "Excellent pricing opportunities."
                ])
            elif "$1M" in price_range or "Luxury" in price_range:
                price_phrases.extend([
                    "Premium properties await.",
                    "Luxury living redefined.",
                    "Exceptional quality throughout."
                ])

        # Build description
        opening = random.choice(openings)
        middle = random.choice(middles)
        closing = random.choice(closings)

        description = f"{opening} {middle} {closing}"

        # Add price phrase if available
        if price_phrases and random.random() > 0.5:
            price_phrase = random.choice(price_phrases)
            description = description.replace(".", f". {price_phrase}", 1)

        # Ensure description isn't too long (ideal is 150-160 chars for SEO)
        if len(description) > 160:
            # Try shorter version
            description = f"{opening} {middle} in Dallas. {random.choice(['Call today!', 'View listings now!', 'Schedule tours!', 'Contact us today!'])}"

        return description


def main():
    print("=" * 80)
    print("Dallas Real Estate Page Title Generator")
    print("=" * 80)
    print()

    generator = RealEstatePageTitleGenerator()

    print("Generating titles... This may take a moment.")
    print()

    all_titles = generator.generate_all_titles()

    print()
    print("=" * 80)
    print(f"Total unique titles generated: {len(all_titles):,}")
    print("=" * 80)
    print()

    # Sort titles for easier browsing
    sorted_titles = sorted(list(all_titles))

    # Save to text file
    output_file = "dallas_real_estate_page_titles.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, title in enumerate(sorted_titles, 1):
            f.write(f"{i}. {title}\n")

    print(f"✓ Titles saved to: {output_file}")
    print()

    # Save to JSON for programmatic use
    json_file = "dallas_real_estate_page_titles.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "total_count": len(sorted_titles),
            "city": "Dallas",
            "state": "TX",
            "generated_date": "2025-11-19",
            "titles": sorted_titles
        }, f, indent=2, ensure_ascii=False)

    print(f"✓ Titles saved to JSON: {json_file}")
    print()

    # Save to CSV for spreadsheet use with descriptions
    csv_file = "dallas_real_estate_page_titles.csv"
    print(f"Generating descriptions for {len(sorted_titles):,} titles...")
    print("This may take a few moments...")

    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("ID,Page Title,URL Slug,Description\n")

        # Set random seed for reproducibility
        import random
        random.seed(42)

        for i, title in enumerate(sorted_titles, 1):
            # Generate URL slug
            url_slug = title.lower().replace(' ', '-').replace(',', '').replace('/', '-')
            url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
            url_slug = '-'.join(filter(None, url_slug.split('-')))  # Remove multiple dashes

            # Generate description
            description = generator.generate_description(title)

            # Escape quotes in description
            description = description.replace('"', '""')

            # Write CSV row
            f.write(f'{i},"{title}","{url_slug}","{description}"\n')

            # Progress indicator every 10,000 titles
            if i % 10000 == 0:
                print(f"  Generated {i:,} descriptions...")

    print(f"✓ Titles saved to CSV with descriptions: {csv_file}")
    print()

    # Display sample titles with descriptions
    print("Sample titles with descriptions (first 20):")
    print("-" * 80)
    import random
    random.seed(42)
    for title in sorted_titles[:20]:
        description = generator.generate_description(title)
        print(f"  Title: {title}")
        print(f"  Description: {description}")
        print()
    print(f"... and {len(sorted_titles) - 20:,} more titles with descriptions!")
    print()

    # Statistics
    print("=" * 80)
    print("STATISTICS")
    print("=" * 80)
    print(f"Total unique page titles: {len(sorted_titles):,}")
    print(f"Average title length: {sum(len(t) for t in sorted_titles) / len(sorted_titles):.1f} characters")
    print(f"Shortest title: {min(sorted_titles, key=len)} ({len(min(sorted_titles, key=len))} chars)")
    print(f"Longest title: {max(sorted_titles, key=len)} ({len(max(sorted_titles, key=len))} chars)")
    print()

    print("✓ Generation complete!")


if __name__ == "__main__":
    main()
