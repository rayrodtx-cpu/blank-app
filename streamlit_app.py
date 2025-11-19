import streamlit as st

st.set_page_config(page_title="Real Estate Client FAQ", page_icon="🏠", layout="wide")

st.title("🏠 Real Estate Client FAQ")
st.write("Comprehensive answers to common questions from real estate clients")

# Create tabs for different categories
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Buying", "Selling", "Financing", "Legal & Paperwork", "Market & Investment", "General"
])

# BUYING TAB
with tab1:
    st.header("Buying Real Estate")

    with st.expander("Q: How much house can I afford?"):
        st.write("""
        **A:** Generally, lenders recommend that your monthly housing payment (including mortgage, taxes, and insurance)
        should not exceed 28% of your gross monthly income. Your total debt payments (including housing) should not
        exceed 36% of your gross monthly income. Use a mortgage calculator and get pre-approved to understand your
        specific budget.
        """)

    with st.expander("Q: What is the difference between pre-qualification and pre-approval?"):
        st.write("""
        **A:** Pre-qualification is an informal estimate of how much you might be able to borrow based on self-reported
        financial information. Pre-approval is a formal process where a lender verifies your financial information
        (credit, income, assets) and commits to lending you a specific amount. Pre-approval carries much more weight
        with sellers.
        """)

    with st.expander("Q: How much should I offer on a house?"):
        st.write("""
        **A:** Your offer should be based on:
        - Comparable sales in the area (comps)
        - Current market conditions (buyer's vs. seller's market)
        - The condition of the property
        - How long the property has been on the market
        - Your budget and how much you want the property

        Your real estate agent will help you analyze these factors to make a competitive offer.
        """)

    with st.expander("Q: What is earnest money?"):
        st.write("""
        **A:** Earnest money is a deposit made to demonstrate your serious intent to purchase a property.
        Typically 1-3% of the purchase price, it's held in escrow and applied to your down payment or closing
        costs at closing. If you back out without a valid contingency, you may forfeit this deposit.
        """)

    with st.expander("Q: What are contingencies?"):
        st.write("""
        **A:** Contingencies are conditions that must be met for the sale to proceed. Common contingencies include:
        - **Financing contingency**: Sale depends on obtaining a mortgage
        - **Inspection contingency**: Allows you to back out or renegotiate based on inspection results
        - **Appraisal contingency**: Sale depends on the property appraising at or above the purchase price
        - **Sale contingency**: Sale depends on selling your current home first
        """)

    with st.expander("Q: Do I need a home inspection?"):
        st.write("""
        **A:** Yes! A home inspection is highly recommended and typically costs $300-500. An inspector will
        evaluate the property's condition, identifying potential issues with the foundation, roof, electrical,
        plumbing, HVAC, and more. This can save you thousands in unexpected repairs and gives you negotiating
        power or the option to walk away.
        """)

    with st.expander("Q: What is a buyer's agent and do I need one?"):
        st.write("""
        **A:** A buyer's agent represents your interests in a real estate transaction. Benefits include:
        - Access to MLS listings and market knowledge
        - Negotiation expertise
        - Guidance through the complex buying process
        - Help with paperwork and deadlines

        In most cases, the seller pays the buyer's agent commission, so this service is typically free to you.
        """)

    with st.expander("Q: What closing costs should I expect?"):
        st.write("""
        **A:** Closing costs typically range from 2-5% of the purchase price and may include:
        - Loan origination fees
        - Appraisal fees
        - Title insurance
        - Attorney fees
        - Home inspection fees
        - Property taxes (prorated)
        - Homeowners insurance
        - Recording fees
        - HOA transfer fees (if applicable)
        """)

    with st.expander("Q: Should I buy a new construction or existing home?"):
        st.write("""
        **A:** Each has advantages:

        **New Construction:**
        - Modern design and energy efficiency
        - Customization options
        - Lower maintenance initially
        - Builder warranties
        - May take longer to complete

        **Existing Home:**
        - Established neighborhoods
        - Mature landscaping
        - Often less expensive
        - Move in immediately
        - May need updates or repairs
        """)

    with st.expander("Q: What is PMI and can I avoid it?"):
        st.write("""
        **A:** Private Mortgage Insurance (PMI) is required when you put down less than 20% on a conventional loan.
        It protects the lender if you default. Ways to avoid PMI:
        - Put down 20% or more
        - Use a piggyback loan (80-10-10)
        - Look into lender-paid PMI options
        - Consider VA loans (if eligible) which don't require PMI
        """)

# SELLING TAB
with tab2:
    st.header("Selling Real Estate")

    with st.expander("Q: When is the best time to sell my house?"):
        st.write("""
        **A:** Traditionally, spring (March-May) is the busiest selling season, with more buyers and potentially
        higher prices. However, the "best" time depends on:
        - Your local market conditions
        - Your personal circumstances
        - Current interest rates
        - Inventory levels in your area

        In a seller's market, any time can be a good time to sell.
        """)

    with st.expander("Q: How do I price my home correctly?"):
        st.write("""
        **A:** Proper pricing involves:
        - Comparative Market Analysis (CMA) of recently sold similar homes
        - Current market conditions
        - Your home's unique features and condition
        - Time constraints
        - Professional appraisal (optional)

        Your agent will help determine the optimal price. Overpricing can lead to a stale listing;
        underpricing leaves money on the table.
        """)

    with st.expander("Q: What repairs should I make before listing?"):
        st.write("""
        **A:** Focus on:
        - **Essential repairs**: Fix major issues (roof leaks, electrical problems, plumbing)
        - **Curb appeal**: Landscaping, exterior paint, front door
        - **Deep cleaning**: Throughout the entire house
        - **Decluttering**: Remove personal items and excess furniture
        - **Minor cosmetic fixes**: Fresh paint (neutral colors), fix holes, update fixtures

        Avoid major renovations unless they significantly add value. Consult your agent about which
        improvements will provide the best ROI.
        """)

    with st.expander("Q: Should I stage my home?"):
        st.write("""
        **A:** Yes! Staged homes typically sell faster and for more money. Staging helps buyers visualize
        themselves in the space and highlights your home's best features. Options include:
        - Professional staging (most effective)
        - Virtual staging (for photos)
        - DIY staging with agent guidance

        At minimum, declutter, depersonalize, and arrange furniture to maximize space and flow.
        """)

    with st.expander("Q: How long will it take to sell my home?"):
        st.write("""
        **A:** The average time varies by market, but typically:
        - **Hot seller's market**: Days to a few weeks
        - **Balanced market**: 30-60 days
        - **Buyer's market**: 60-90+ days

        Factors affecting timeline:
        - Pricing
        - Condition
        - Location
        - Marketing
        - Season
        - Current market conditions
        """)

    with st.expander("Q: What is a listing agent's commission?"):
        st.write("""
        **A:** Total commission typically ranges from 5-6% of the sale price, split between the listing agent
        and buyer's agent. This covers:
        - Professional photography
        - Marketing and advertising
        - MLS listing
        - Open houses and showings
        - Negotiation
        - Transaction management

        Commission is negotiable and paid at closing from the sale proceeds.
        """)

    with st.expander("Q: Should I be present during showings?"):
        st.write("""
        **A:** No. Buyers feel more comfortable and can envision themselves in the home when the owner isn't
        present. They're also more likely to speak freely with their agent. Make your home available for
        showings with reasonable notice, keep it clean and staged, and let your agent handle the presentations.
        """)

    with st.expander("Q: What happens if I receive multiple offers?"):
        st.write("""
        **A:** In a multiple offer situation:
        - Your agent will present all offers
        - Consider not just price, but also contingencies, closing timeline, and buyer qualifications
        - You can counter all offers, some offers, or accept one
        - Sometimes buyers will submit their "highest and best" in multiple offer situations
        - Your agent will help you evaluate each offer's strength and likelihood of closing
        """)

    with st.expander("Q: Can I sell my house while I still owe money on it?"):
        st.write("""
        **A:** Yes, most homes are sold with an existing mortgage. At closing, the mortgage is paid off
        from the sale proceeds. If you owe more than the home is worth (underwater), you'll need to:
        - Bring cash to closing to cover the difference, or
        - Pursue a short sale (with lender approval), or
        - Wait until you have equity
        """)

    with st.expander("Q: What is a seller's disclosure?"):
        st.write("""
        **A:** A seller's disclosure is a legal document where you disclose known material defects or issues
        with the property. This typically includes:
        - Structural issues
        - Water damage or leaks
        - Pest infestations
        - Environmental hazards
        - HOA issues
        - Property line disputes

        Failing to disclose known issues can result in legal liability after the sale.
        """)

# FINANCING TAB
with tab3:
    st.header("Financing & Mortgages")

    with st.expander("Q: What types of mortgages are available?"):
        st.write("""
        **A:** Common mortgage types:

        - **Conventional**: Not government-backed; requires good credit and typically 3-20% down
        - **FHA**: Government-insured; lower down payment (3.5%); easier credit requirements
        - **VA**: For veterans; no down payment; no PMI
        - **USDA**: For rural properties; no down payment for qualified buyers
        - **Jumbo**: For high-value properties exceeding conventional loan limits
        - **Fixed-rate**: Interest rate stays the same throughout the loan term
        - **Adjustable-rate (ARM)**: Interest rate adjusts periodically based on market conditions
        """)

    with st.expander("Q: What credit score do I need to buy a house?"):
        st.write("""
        **A:** Minimum credit scores vary by loan type:
        - **Conventional**: Typically 620-640 minimum
        - **FHA**: As low as 580 (sometimes 500 with 10% down)
        - **VA**: No official minimum, but most lenders prefer 620+
        - **USDA**: Typically 640+

        Higher credit scores get better interest rates. If your score is low, work on improving it
        before applying for a mortgage.
        """)

    with st.expander("Q: How much should I put down?"):
        st.write("""
        **A:** Down payment options vary:
        - **20%**: Avoids PMI on conventional loans; gets best rates
        - **10-15%**: Common middle ground
        - **5-10%**: May require PMI but more accessible
        - **3-3.5%**: Minimum for many first-time buyer programs
        - **0%**: Available with VA and USDA loans

        More down payment means lower monthly payments and less interest paid over time, but you need
        to balance this with keeping cash reserves for emergencies and closing costs.
        """)

    with st.expander("Q: What is the difference between interest rate and APR?"):
        st.write("""
        **A:**
        - **Interest rate**: The percentage charged on the loan principal
        - **APR (Annual Percentage Rate)**: Includes the interest rate plus other loan costs (fees, points,
          mortgage insurance) expressed as a yearly rate

        APR gives a more complete picture of the loan's true cost. When comparing loans, compare APRs
        rather than just interest rates.
        """)

    with st.expander("Q: Should I choose a 15-year or 30-year mortgage?"):
        st.write("""
        **A:**
        **30-year mortgage:**
        - Lower monthly payments
        - More affordable for most buyers
        - More interest paid over life of loan
        - More flexibility in budget

        **15-year mortgage:**
        - Higher monthly payments
        - Lower interest rate
        - Much less interest paid overall
        - Build equity faster
        - Loan paid off sooner

        Choose based on your financial situation, goals, and other priorities.
        """)

    with st.expander("Q: What documents do I need for a mortgage application?"):
        st.write("""
        **A:** Typical documents required:
        - **Identification**: Driver's license or passport
        - **Income verification**: 2 years of W-2s or tax returns; recent pay stubs
        - **Employment verification**: Contact information for current employer
        - **Assets**: Bank statements (2-3 months); investment account statements
        - **Debts**: Student loans, car loans, credit card statements
        - **Other**: Divorce decree, bankruptcy discharge papers (if applicable)

        Self-employed individuals may need additional documentation like profit/loss statements.
        """)

    with st.expander("Q: What is a rate lock?"):
        st.write("""
        **A:** A rate lock is a guarantee from your lender that your interest rate won't change between
        loan approval and closing, typically for 30-60 days. This protects you if rates increase during
        that period. Some rate locks allow you to "float down" if rates decrease. There may be a fee
        for locking or extending a lock.
        """)

    with st.expander("Q: Can I get a mortgage if I'm self-employed?"):
        st.write("""
        **A:** Yes, but you'll need to provide additional documentation:
        - 2 years of personal and business tax returns
        - Profit and loss statements
        - Balance sheets
        - CPA letter verifying income

        Lenders will average your income over 2 years. Be prepared for more scrutiny and potentially
        higher interest rates. Maintain good credit and low debt-to-income ratio.
        """)

    with st.expander("Q: What are discount points?"):
        st.write("""
        **A:** Discount points are fees paid to the lender at closing to reduce your interest rate.
        One point equals 1% of the loan amount and typically reduces your rate by about 0.25%.

        Example: On a $300,000 loan, one point costs $3,000.

        Points make sense if:
        - You plan to stay in the home long enough to recoup the upfront cost
        - You have extra cash and want to lower monthly payments
        - You're in a high tax bracket (points may be tax deductible)
        """)

    with st.expander("Q: What is debt-to-income ratio and why does it matter?"):
        st.write("""
        **A:** Debt-to-income (DTI) ratio is your total monthly debt payments divided by your gross
        monthly income. Lenders use this to assess your ability to manage monthly payments.

        - **Front-end DTI**: Housing expenses only (should be ≤28%)
        - **Back-end DTI**: All debt including housing (should be ≤36-43%)

        To improve DTI:
        - Pay down debts
        - Increase income
        - Avoid taking on new debt before applying
        """)

# LEGAL & PAPERWORK TAB
with tab4:
    st.header("Legal & Paperwork")

    with st.expander("Q: What is title insurance and do I need it?"):
        st.write("""
        **A:** Title insurance protects you from issues with the property's title (ownership history), such as:
        - Outstanding liens
        - Errors in public records
        - Unknown heirs claiming ownership
        - Forgery or fraud in previous transactions

        There are two types:
        - **Lender's policy**: Required by your mortgage lender (protects them)
        - **Owner's policy**: Optional but recommended (protects you)

        It's a one-time fee paid at closing and protects you as long as you own the property.
        """)

    with st.expander("Q: What happens at closing?"):
        st.write("""
        **A:** Closing is the final step where property ownership transfers. You'll:
        - Sign numerous documents (mortgage note, deed, settlement statement, etc.)
        - Pay closing costs and down payment
        - Receive keys and ownership
        - Review the final Closing Disclosure showing all costs

        Bring:
        - Government-issued ID
        - Cashier's check or proof of wire transfer for closing costs
        - Proof of homeowners insurance

        The process typically takes 1-2 hours.
        """)

    with st.expander("Q: What is escrow?"):
        st.write("""
        **A:** Escrow has two meanings:

        1. **Escrow account during transaction**: A neutral third party holds earnest money and documents
           until all conditions are met and the sale closes.

        2. **Escrow account for taxes and insurance**: Part of your monthly mortgage payment goes into an
           account managed by your lender to pay property taxes and homeowners insurance when they're due.
           This ensures these important bills are paid on time.
        """)

    with st.expander("Q: Do I need a real estate attorney?"):
        st.write("""
        **A:** This depends on your state:
        - Some states **require** an attorney for real estate transactions
        - Some states use escrow companies or title companies instead
        - Even where not required, an attorney can be valuable for complex situations

        An attorney can:
        - Review contracts and documents
        - Identify potential legal issues
        - Negotiate on your behalf
        - Handle closing procedures

        Ask your agent about local requirements and recommendations.
        """)

    with st.expander("Q: What is a home warranty?"):
        st.write("""
        **A:** A home warranty is a service contract that covers repair or replacement of major home
        systems and appliances for a set period (usually 1 year). Coverage typically includes:
        - HVAC systems
        - Plumbing
        - Electrical systems
        - Kitchen appliances
        - Water heater

        Cost: $300-600 annually plus service call fees ($75-125)

        Benefits: Protection against unexpected repair costs, especially useful for older homes or
        first-time buyers. Note: Pre-existing conditions and improper maintenance are typically not covered.
        """)

    with st.expander("Q: What is the difference between a deed and a title?"):
        st.write("""
        **A:**
        - **Title**: The legal right to own, use, and transfer property (a concept, not a document)
        - **Deed**: The physical legal document that transfers title from seller to buyer

        Types of deeds:
        - **Warranty deed**: Seller guarantees clear title
        - **Quitclaim deed**: Transfers whatever interest seller has, with no guarantees
        - **Special warranty deed**: Seller guarantees title only for the period they owned it
        """)

    with st.expander("Q: What are property taxes and how are they calculated?"):
        st.write("""
        **A:** Property taxes are annual taxes based on your property's assessed value, set by local
        government (county, city, school district).

        Calculation: Assessed Value × Tax Rate = Annual Property Tax

        - Assessed value is typically a percentage of market value
        - Tax rates vary widely by location (typically 0.5-2.5% of home value)
        - Taxes fund schools, roads, emergency services, etc.
        - Paid annually or semi-annually, or through monthly escrow
        - May be tax-deductible (consult tax advisor)
        """)

    with st.expander("Q: What is homeowners association (HOA) and what do fees cover?"):
        st.write("""
        **A:** An HOA is an organization that makes and enforces rules for a subdivision, planned community,
        or condominium. HOA fees (typically $100-700/month) may cover:
        - Common area maintenance (landscaping, pools, clubhouses)
        - Exterior building maintenance (in condos)
        - Trash collection
        - Security
        - Insurance for common areas
        - Reserves for major repairs

        HOAs also enforce rules about property appearance, modifications, and use. Review the HOA's
        CC&Rs (Covenants, Conditions & Restrictions) before buying.
        """)

    with st.expander("Q: What is a survey and do I need one?"):
        st.write("""
        **A:** A property survey is a precise measurement and map of the property showing:
        - Exact boundaries
        - Location of structures
        - Easements
        - Encroachments
        - Right-of-ways

        You may need one if:
        - Building a fence or addition
        - There's a boundary dispute
        - Lender requires it
        - Title insurance requires it
        - Buying undeveloped or rural land

        Cost: $400-1,000+ depending on property size and complexity.
        """)

    with st.expander("Q: What is a quitclaim deed?"):
        st.write("""
        **A:** A quitclaim deed transfers whatever ownership interest the grantor has in a property
        without guaranteeing that the title is clear or valid. Common uses:
        - Transferring property between family members
        - Adding/removing spouse from title after marriage/divorce
        - Clearing up title issues
        - Transferring property into a trust

        **Warning**: Provides no protection to the buyer. Not recommended for typical real estate
        purchases with someone you don't know well.
        """)

# MARKET & INVESTMENT TAB
with tab5:
    st.header("Market & Investment")

    with st.expander("Q: What is a buyer's market vs. seller's market?"):
        st.write("""
        **A:**
        **Buyer's Market:**
        - More homes for sale than buyers
        - Homes stay on market longer
        - Prices stable or decreasing
        - Buyers have negotiating power
        - May get concessions from sellers

        **Seller's Market:**
        - More buyers than available homes
        - Homes sell quickly
        - Prices rising
        - Multiple offers common
        - Sellers have negotiating power
        - May need to waive contingencies to compete
        """)

    with st.expander("Q: Is real estate a good investment?"):
        st.write("""
        **A:** Real estate can be a good investment, but it depends on many factors:

        **Advantages:**
        - Potential for appreciation
        - Rental income potential
        - Tax benefits (mortgage interest, property tax deductions)
        - Leverage (use borrowed money to invest)
        - Hedge against inflation
        - Tangible asset

        **Disadvantages:**
        - Illiquid (can't quickly convert to cash)
        - Requires maintenance and management
        - Market risk
        - Transaction costs (6-10% to buy and sell)
        - Property taxes and insurance

        Real estate often performs well long-term but shouldn't be your only investment.
        """)

    with st.expander("Q: How do I know if a rental property is a good investment?"):
        st.write("""
        **A:** Evaluate using these metrics:

        - **1% Rule**: Monthly rent should be at least 1% of purchase price
        - **Cap Rate**: (Annual Net Income / Purchase Price) × 100; aim for 8-12%
        - **Cash-on-Cash Return**: (Annual Cash Flow / Total Cash Invested) × 100
        - **Gross Rent Multiplier**: Purchase Price / Annual Gross Rent; lower is better

        Also consider:
        - Location and rental demand
        - Property condition and maintenance costs
        - Property management costs
        - Vacancy rates
        - Appreciation potential
        - Your experience and time commitment
        """)

    with st.expander("Q: What is equity and how do I build it?"):
        st.write("""
        **A:** Equity is the portion of your home that you own outright (home value minus what you owe).

        **Build equity through:**
        - **Mortgage payments**: Each payment reduces principal
        - **Appreciation**: Property value increases over time
        - **Home improvements**: Strategic renovations add value
        - **Larger down payment**: Start with more equity
        - **Extra principal payments**: Pay down mortgage faster

        Example: $300,000 home with $240,000 mortgage = $60,000 equity (20%)

        You can access equity through home equity loans, HELOCs, or cash-out refinancing.
        """)

    with st.expander("Q: Should I buy or rent?"):
        st.write("""
        **A:** Consider these factors:

        **Buy if:**
        - You plan to stay 5+ years
        - You have stable income and good credit
        - You can afford 20% down (or comfortable with less)
        - You want to build equity
        - You want stability and control
        - Local market favors buying (use rent vs. buy calculators)

        **Rent if:**
        - You need flexibility to move
        - You're not financially ready
        - You're in an expensive market where buying doesn't make financial sense
        - You don't want maintenance responsibilities
        - You're uncertain about career/location

        Run the numbers for your specific situation using online calculators.
        """)

    with st.expander("Q: What is house flipping and how does it work?"):
        st.write("""
        **A:** House flipping involves buying properties, renovating them, and selling for profit.

        **Keys to success:**
        - Buy below market value (foreclosures, distressed properties)
        - Accurate cost estimates for repairs
        - Quick turnaround (6 months or less)
        - Know the market and buyer preferences
        - Build a reliable contractor team
        - Budget for holding costs (mortgage, utilities, taxes)

        **Risks:**
        - Unexpected repairs
        - Market downturns
        - Properties don't sell quickly
        - Overpaying for purchase or renovations

        Not recommended for beginners without construction knowledge or significant capital reserves.
        """)

    with st.expander("Q: What is appreciation and what drives it?"):
        st.write("""
        **A:** Appreciation is the increase in property value over time.

        **Factors that drive appreciation:**
        - **Location**: Desirable neighborhoods, good schools, low crime
        - **Economic growth**: Job growth, new businesses, rising incomes
        - **Supply and demand**: Limited housing supply, population growth
        - **Infrastructure**: New transportation, shopping, amenities
        - **Interest rates**: Lower rates increase buyer demand
        - **Inflation**: General price increases
        - **Property improvements**: Renovations and upgrades

        Historical average: 3-5% annually, but varies greatly by location and timeframe.
        """)

    with st.expander("Q: What are the tax benefits of owning a home?"):
        st.write("""
        **A:** Potential tax benefits include:

        - **Mortgage interest deduction**: On loans up to $750,000 (married) or $375,000 (single)
        - **Property tax deduction**: Up to $10,000 (SALT cap)
        - **Capital gains exclusion**: Up to $250,000 (single) or $500,000 (married) in profit when selling
          your primary residence (must live there 2 of last 5 years)
        - **Home office deduction**: If you're self-employed and use space exclusively for business
        - **Rental property deductions**: Depreciation, expenses, repairs (for investment properties)

        **Note**: Tax laws change. Consult a tax professional for your specific situation.
        """)

    with st.expander("Q: What is a 1031 exchange?"):
        st.write("""
        **A:** A 1031 exchange (like-kind exchange) allows you to defer capital gains taxes when selling
        an investment property by reinvesting proceeds into another similar property.

        **Requirements:**
        - Must be investment or business property (not primary residence)
        - Must identify replacement property within 45 days
        - Must close on replacement property within 180 days
        - Must use qualified intermediary
        - Must reinvest all proceeds to defer all taxes

        This is a complex tax strategy. Work with a qualified intermediary and tax advisor.
        """)

    with st.expander("Q: How do rising interest rates affect the housing market?"):
        st.write("""
        **A:** Rising interest rates impact the market in several ways:

        **Effects:**
        - **Lower affordability**: Higher monthly payments reduce buying power
        - **Decreased demand**: Fewer qualified buyers
        - **Slower price growth**: Or even price declines in extreme cases
        - **Longer time on market**: Homes take longer to sell
        - **Less competition**: Fewer multiple offer situations

        **Opportunities:**
        - More negotiating power for buyers
        - Less competition
        - Potential to refinance later if rates drop

        A 1% interest rate increase can reduce buying power by roughly 10%.
        """)

# GENERAL TAB
with tab6:
    st.header("General Questions")

    with st.expander("Q: How long does the home buying process take?"):
        st.write("""
        **A:** The typical timeline is 30-45 days from offer acceptance to closing, but the full process includes:

        - **Pre-approval**: 1-3 days
        - **House hunting**: Varies (weeks to months)
        - **Offer to acceptance**: 1-7 days
        - **Inspection period**: 7-10 days
        - **Financing and appraisal**: 2-3 weeks
        - **Final walkthrough and closing**: 1 day

        Cash purchases can close in as little as 1-2 weeks. Complications (appraisal issues, repairs)
        can extend the timeline.
        """)

    with st.expander("Q: What is the difference between a condo and a townhouse?"):
        st.write("""
        **A:**
        **Condo:**
        - You own the interior space
        - HOA owns building exterior, land, common areas
        - HOA handles all exterior maintenance
        - Typically attached units
        - May have shared walls, floors, ceilings
        - Usually higher HOA fees

        **Townhouse:**
        - You own the structure and land beneath it
        - Responsible for exterior maintenance
        - Typically multi-story attached units
        - May have small yard
        - Lower HOA fees (only common areas)
        - More privacy and control
        """)

    with st.expander("Q: What questions should I ask at an open house?"):
        st.write("""
        **A:** Important questions to ask:

        - Why is the owner selling?
        - How long has it been on the market?
        - What's included in the sale?
        - Any recent renovations or repairs?
        - Age of major systems (roof, HVAC, water heater)?
        - Average utility costs?
        - Any issues with the home?
        - What are property taxes?
        - HOA fees and rules (if applicable)?
        - School district information?
        - Internet/cell service quality?
        - Neighborhood noise levels?
        - Any planned development nearby?
        """)

    with st.expander("Q: What is a short sale?"):
        st.write("""
        **A:** A short sale occurs when a homeowner sells their property for less than what they owe
        on the mortgage, with the lender's approval.

        **Buyer considerations:**
        - Can take 2-6 months to close
        - Bank must approve the sale
        - Sold "as-is" with no repairs
        - May get a good deal
        - Requires patience and flexibility

        **Seller considerations:**
        - Avoid foreclosure
        - Still damages credit (but less than foreclosure)
        - May owe taxes on forgiven debt
        - Must prove financial hardship
        """)

    with st.expander("Q: What is a foreclosure and should I buy one?"):
        st.write("""
        **A:** Foreclosure occurs when a lender takes possession of a property due to the owner's
        failure to pay the mortgage.

        **Types:**
        - **Pre-foreclosure**: Owner hasn't paid, but bank hasn't taken possession
        - **Auction**: Bank sells at public auction
        - **REO (Real Estate Owned)**: Bank owns and lists through agent

        **Pros:**
        - Potentially below-market prices
        - Less competition than traditional sales

        **Cons:**
        - Sold "as-is" with unknown condition
        - May have liens or title issues
        - Often need repairs
        - Cash or special financing often required
        - Complex process
        """)

    with st.expander("Q: What is a home appraisal?"):
        st.write("""
        **A:** An appraisal is an unbiased professional opinion of a home's value, required by lenders
        before approving a mortgage.

        **Appraiser evaluates:**
        - Property characteristics (size, features, condition)
        - Recent comparable sales
        - Current market conditions
        - Location

        **If appraisal comes in low:**
        - Negotiate lower price with seller
        - Bring more cash to closing to cover difference
        - Challenge the appraisal (if errors exist)
        - Walk away (if you have appraisal contingency)

        Cost: $300-500, paid by buyer
        """)

    with st.expander("Q: What is curb appeal and why does it matter?"):
        st.write("""
        **A:** Curb appeal is the attractiveness of a property from the street. It matters because:

        - First impressions influence buyers' perception of the entire property
        - Good curb appeal can increase home value 5-10%
        - Draws more buyers to viewings
        - Homes with good curb appeal sell faster

        **Improve curb appeal:**
        - Fresh paint on front door and trim
        - Maintain landscaping (mow, trim, mulch)
        - Clean walkways and driveway
        - Update house numbers and mailbox
        - Add outdoor lighting
        - Power wash exterior
        - Add potted plants or flowers
        """)

    with st.expander("Q: What is radon and should I test for it?"):
        st.write("""
        **A:** Radon is a radioactive gas that comes from the natural decay of uranium in soil and rock.
        It can seep into homes and cause lung cancer with long-term exposure.

        **Testing:**
        - Recommended for all homes
        - Inexpensive ($20-150)
        - Part of home inspection or separate
        - EPA action level: 4 pCi/L or higher

        **Mitigation:**
        - If levels are high, install radon mitigation system
        - Cost: $800-2,500
        - Reduces radon to safe levels
        - You can negotiate with seller to install system or reduce price
        """)

    with st.expander("Q: What is the fair housing act?"):
        st.write("""
        **A:** The Fair Housing Act prohibits discrimination in housing based on:
        - Race
        - Color
        - National origin
        - Religion
        - Sex (including sexual orientation and gender identity)
        - Familial status
        - Disability

        **This means:**
        - Sellers cannot refuse to sell based on these factors
        - Agents cannot steer buyers to certain neighborhoods based on these factors
        - Landlords cannot refuse to rent based on these factors
        - Lenders cannot discriminate in lending

        If you experience discrimination, file a complaint with HUD (Department of Housing and Urban Development).
        """)

    with st.expander("Q: Should I get a home inspection even on new construction?"):
        st.write("""
        **A:** Yes! Even new homes can have issues:
        - Construction defects
        - Code violations
        - Incomplete work
        - Substandard materials
        - Installation errors

        A new construction inspection (during various construction phases) can catch problems before
        they're covered by drywall and finishes. Builder warranties don't replace the value of an
        independent inspection.

        Consider specialized inspections: foundation, framing, plumbing, electrical, HVAC, and final walkthrough.
        """)
