"""
Configuration file for bank statement categorization
Contains category definitions and keyword mappings for real estate expenses
"""

# Real Estate Business Categories
BUSINESS_CATEGORIES = {
    "Mortgage Interest": [
        "mortgage", "loan payment", "Wells Fargo Home Mortgage", "Chase Mortgage",
        "Bank of America Mortgage", "Quicken Loans", "home loan"
    ],
    "Property Taxes": [
        "property tax", "real estate tax", "county tax", "city tax", "tax collector",
        "treasurer", "assessor"
    ],
    "Repairs & Maintenance": [
        "repair", "maintenance", "handyman", "plumbing", "electrical", "hvac",
        "heating", "cooling", "roofing", "painting", "carpet", "flooring",
        "Home Depot", "Lowes", "Ace Hardware", "hardware store", "appliance repair"
    ],
    "Utilities": [
        "electric", "electricity", "water", "sewer", "gas", "trash", "garbage",
        "utility", "power company", "PG&E", "Duke Energy", "water district"
    ],
    "Insurance": [
        "insurance", "property insurance", "landlord insurance", "liability insurance",
        "State Farm", "Allstate", "Farmers Insurance", "Geico"
    ],
    "Property Management": [
        "property management", "property manager", "management fee", "leasing fee"
    ],
    "Legal & Professional": [
        "attorney", "lawyer", "legal", "accountant", "CPA", "tax prep",
        "consulting", "professional services"
    ],
    "HOA Fees": [
        "HOA", "homeowners association", "condo fee", "association dues"
    ],
    "Advertising": [
        "zillow", "trulia", "apartments.com", "craigslist", "advertising",
        "marketing", "listing fee"
    ],
    "Cleaning & Landscaping": [
        "cleaning", "maid", "janitorial", "lawn", "landscaping", "gardening",
        "yard maintenance", "snow removal"
    ],
    "Supplies": [
        "supplies", "materials", "parts", "equipment"
    ],
    "Travel (Property Related)": [
        "mileage", "gas", "fuel", "parking", "toll"
    ],
    "Other Business Expense": []
}

# Personal Categories
PERSONAL_CATEGORIES = {
    "Groceries": [
        "grocery", "supermarket", "Safeway", "Kroger", "Whole Foods", "Trader Joe",
        "Costco", "Sam's Club", "Walmart", "Target", "food mart"
    ],
    "Dining & Entertainment": [
        "restaurant", "cafe", "coffee", "bar", "dining", "entertainment",
        "movie", "theater", "Starbucks", "McDonald", "pizza", "fast food"
    ],
    "Personal Shopping": [
        "clothing", "clothes", "shoes", "amazon", "mall", "retail",
        "department store", "Macy", "Nordstrom", "Gap", "Nike"
    ],
    "Healthcare": [
        "medical", "doctor", "hospital", "pharmacy", "CVS", "Walgreens",
        "dental", "vision", "health"
    ],
    "Personal Auto": [
        "car payment", "auto loan", "car insurance", "auto insurance",
        "vehicle registration", "DMV"
    ],
    "Personal Utilities": [
        "internet", "cable", "phone", "cell phone", "mobile", "streaming",
        "Netflix", "Spotify", "AT&T", "Verizon", "Comcast"
    ],
    "Personal Insurance": [
        "life insurance", "health insurance", "auto insurance"
    ],
    "Other Personal Expense": []
}

# Combined categories for dropdown
ALL_CATEGORIES = {**BUSINESS_CATEGORIES, **PERSONAL_CATEGORIES}

# Business type markers
BUSINESS_TYPE = "Business"
PERSONAL_TYPE = "Personal"

# Common bank CSV column name mappings
CSV_COLUMN_MAPPINGS = {
    "date": ["date", "transaction date", "posted date", "trans date", "Date"],
    "description": ["description", "memo", "transaction description", "payee", "Description", "Memo"],
    "amount": ["amount", "debit", "withdrawal", "payment", "Amount", "Debit"],
    "credit": ["credit", "deposit", "Credit", "Deposit"],
    "balance": ["balance", "running balance", "Balance"]
}

# Date format patterns to try
DATE_FORMATS = [
    "%m/%d/%Y",  # 12/31/2023
    "%Y-%m-%d",  # 2023-12-31
    "%m-%d-%Y",  # 12-31-2023
    "%m/%d/%y",  # 12/31/23
    "%d/%m/%Y",  # 31/12/2023
    "%Y/%m/%d",  # 2023/12/31
    "%b %d, %Y", # Dec 31, 2023
    "%B %d, %Y", # December 31, 2023
]
