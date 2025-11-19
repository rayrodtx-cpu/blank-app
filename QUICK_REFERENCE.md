# San Antonio Real Estate Page Titles - Quick Reference

## Total: 123,322 Unique Page Titles

## Files
- `san_antonio_real_estate_page_titles.txt` - All titles (one per line)
- `san_antonio_real_estate_page_titles.csv` - Titles with URL slugs
- `generate_page_titles.py` - Script to regenerate or customize
- `browse_titles.py` - Interactive browser to explore titles
- `TITLE_SAMPLES_BY_CATEGORY.md` - Detailed samples by category

---

## Quick Stats

| Category | Count |
|----------|------:|
| Total Titles | 123,322 |
| Homes with pools | 2,865 |
| 2 story homes | 5,052 |
| 3 bedroom homes | 5,537 |
| 4 bedroom homes | 5,537 |
| Alamo Heights | 3,002 |
| Stone Oak | 2,922 |
| Luxury homes | 1,328 |
| New construction | 1,208 |
| Gated community | 640 |
| Condos | 14,442 |
| Townhomes | 10,262 |

---

## Your Examples

### "homes with pools"
**2,865 titles including:**
- homes with pools
- homes with pools in Alamo Heights
- homes with pools in Stone Oak
- 1 story homes with pools
- 2 story homes with pools
- 3 bedroom homes with pools
- 4 bedroom homes with pools
- luxury homes with pools
- homes with pools under 500k
- homes with pools over 1 million

### "homes with pools in alamo heights"
**81 titles including:**
- homes with pools in Alamo Heights
- 1 story homes with pools in Alamo Heights
- 2 story homes with pools in Alamo Heights
- 3 bedroom homes with pools in Alamo Heights
- 4 bedroom homes with pools in Alamo Heights
- single family homes with pools in Alamo Heights
- townhomes with pools in Alamo Heights

### "2 story homes in alamo heights"
**182 titles including:**
- 2 story homes in Alamo Heights
- 1 bedroom 2 story homes in Alamo Heights
- 2 bedroom 2 story homes in Alamo Heights
- 3 bedroom 2 story homes in Alamo Heights
- 4 bedroom 2 story homes in Alamo Heights
- 2 story homes with pools in Alamo Heights
- 2 story homes with garage in Alamo Heights
- 2 story homes with acreage in Alamo Heights

---

## All 80+ Neighborhoods Covered

**Premium Areas:**
Alamo Heights, Stone Oak, The Dominion, Terrell Hills, Olmos Park, Shavano Park

**Popular Areas:**
Downtown, Medical Center, UTSA Area, Southtown, King William, Monte Vista

**Growing Areas:**
Boerne, New Braunfels, Helotes, Fair Oaks Ranch, Bulverde, Schertz

**And 60+ more neighborhoods!**

---

## All Property Types

- homes
- houses
- properties
- condos
- townhomes
- single family homes
- luxury homes
- estates
- ranches
- new construction
- custom homes
- and more...

---

## All Features Covered

**Outdoor:**
- with pools (2,865)
- with acreage (2,625)
- with hill country views (2,625)
- with large backyard (960)
- with covered patio (1,485)
- with outdoor kitchen (1,485)

**Parking:**
- with garage (2,625)
- with 2 car garage (2,505)
- with 3 car garage (2,505)
- with RV parking
- with boat parking

**Interior:**
- with hardwood floors (2,505)
- with granite countertops (2,505)
- with master suite (1,965)
- with office (1,965)
- with game room (1,965)
- with media room (1,965)
- with chef's kitchen (1,845)
- with fireplace (1,485)
- with smart home features (960)

**And 40+ more features!**

---

## Price Ranges

- under 100k to under 1 million
- over 1 million, over 2 million
- 100k to 200k increments
- affordable, luxury

---

## Bedroom/Bathroom Combos

**Bedrooms:** 1-6 bedrooms
**Bathrooms:** 1-4+ bathrooms
**All combinations** for each neighborhood and feature

---

## Stories

- 1 story
- 2 story
- 3 story
- single story
- two story

---

## School Districts (16 covered)

- Alamo Heights ISD
- North East ISD
- Northside ISD
- San Antonio ISD
- Judson ISD
- East Central ISD
- Schertz-Cibolo-Universal City ISD
- Comal ISD
- New Braunfels ISD
- Boerne ISD
- And more...

---

## Special Categories

- Gated community (640)
- Golf course community (640)
- New construction (1,208)
- Luxury (1,328)
- 55+ community
- Investment property
- Foreclosure
- Fixer upper
- Ranch/Farm/Equestrian

---

## How to Use

### Search for specific titles:
```bash
# Find all pool homes
grep -i "pool" san_antonio_real_estate_page_titles.txt

# Find 3 bedroom homes in Stone Oak
grep -i "3 bedroom" san_antonio_real_estate_page_titles.txt | grep -i "stone oak"

# Count results
grep -ic "alamo heights" san_antonio_real_estate_page_titles.txt
```

### Browse interactively:
```bash
python browse_titles.py
```

### Export subset:
```bash
# Export all Alamo Heights titles
grep -i "alamo heights" san_antonio_real_estate_page_titles.txt > alamo_heights_titles.txt

# Export all pool homes
grep -i "pool" san_antonio_real_estate_page_titles.txt > pool_homes.txt
```

### Use in website:
1. Open the CSV file in Excel/Google Sheets
2. Column 1 = Page Title (for H1, meta title)
3. Column 2 = URL Slug (for page URL)

**Example:**
- Title: "Homes with Pools in Alamo Heights"
- URL: `/homes-with-pools-in-alamo-heights`
- H1: "Homes with Pools in Alamo Heights"
- Meta: "Homes with Pools in Alamo Heights | San Antonio Real Estate"

---

## Need More Titles?

Run the generator again:
```bash
python generate_page_titles.py
```

Edit `generate_page_titles.py` to:
- Add more neighborhoods
- Add more features
- Add more price ranges
- Create new combination patterns

---

## Pro Tips

1. **Start with high-value areas** - Alamo Heights, Stone Oak, The Dominion
2. **Focus on popular searches** - pools, 3-4 bedrooms, 2 story
3. **Layer in long-tail** - "3 bedroom 2 story homes with pools in Alamo Heights"
4. **Use school district pages** - Parents search by ISD
5. **Create price range pages** - "Homes under 300k" is popular
6. **Neighborhood + feature combos** - Best ROI for SEO

---

## Examples of High-Value Titles

```
homes with pools in Alamo Heights
3 bedroom homes in Stone Oak
luxury homes in The Dominion
homes under 300k in San Antonio
2 story homes with pools in Terrell Hills
4 bedroom 3 bathroom homes in Alamo Heights
new construction in Stone Oak
gated community homes in The Dominion
homes in Alamo Heights ISD
3 bedroom 2 bathroom homes with pools
```

---

**Total Titles: 123,322 ✓**
