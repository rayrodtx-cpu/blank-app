# AI Realty Autogen Builder - Usage Guide

Complete guide to using the AI Realty Autogen Builder for various real estate scenarios.

---

## 📝 Prompt Templates

### Basic Real Estate Site

**Template:**
```
Build a real estate website for [CITY] with property listings, agent profiles,
blog, contact forms, and [SPECIALTY] focus.
```

**Examples:**

```
Build a real estate website for Austin with property listings, agent profiles,
blog, contact forms, and residential focus.
```

```
Build a real estate website for Miami Beach with property listings, agent profiles,
blog, contact forms, and luxury waterfront focus.
```

### Luxury Real Estate

**Template:**
```
Create a high-end luxury real estate website for [CITY] featuring [PROPERTY_TYPES],
exclusive agent team pages, virtual tours, and premium property showcases.
```

**Examples:**

```
Create a high-end luxury real estate website for Beverly Hills featuring mansions
and estates, exclusive agent team pages, virtual tours, and premium property showcases.
```

### Commercial Real Estate

**Template:**
```
Build a commercial real estate website for [CITY] with [PROPERTY_TYPES],
investment analysis tools, market reports, and tenant resources.
```

**Examples:**

```
Build a commercial real estate website for Chicago with office spaces and retail
locations, investment analysis tools, market reports, and tenant resources.
```

### Property Management

**Template:**
```
Create a property management website for [MARKET] with rental listings,
tenant portal, maintenance requests, and landlord resources.
```

**Examples:**

```
Create a property management website for college students near Ann Arbor with
rental listings, tenant portal, maintenance requests, and landlord resources.
```

### Real Estate Team

**Template:**
```
Build a real estate team website for [TEAM_NAME] in [CITY] with individual
agent pages, team achievements, client testimonials, and market insights.
```

**Examples:**

```
Build a real estate team website for Smith & Associates in Seattle with individual
agent pages, team achievements, client testimonials, and market insights.
```

---

## 🎯 Use Case Scenarios

### Scenario 1: New Agent Launch

**Goal:** Launch a personal brand website in under 5 minutes

**Steps:**
1. Install and activate plugin
2. Go to AI Realty → Settings
3. Enter your city and state
4. Go to AI Realty → Dashboard
5. Enter prompt:
   ```
   Build a professional real estate website for [Your Name] in [City],
   specializing in first-time home buyers and move-up buyers.
   ```
6. Click "Build Site Now"
7. Go to AI Realty → Agents
8. Add your profile with photo
9. Done!

**Time:** 5 minutes
**Result:** Professional website ready to share

---

### Scenario 2: Brokerage Expansion

**Goal:** Launch a new office location website

**Steps:**
1. Install plugin on new WordPress instance
2. Configure with new office details
3. Enter prompt:
   ```
   Build a full-service real estate brokerage website for [Office Name] in [City],
   featuring residential and commercial properties, team directory, and local
   market expertise.
   ```
4. Add all agents via AI Realty → Agents
5. Share agent tracking links with team
6. Monitor leads via AI Realty → Leads

**Time:** 15 minutes
**Result:** Multi-agent brokerage site with lead tracking

---

### Scenario 3: Luxury Niche

**Goal:** Position as luxury market specialist

**Steps:**
1. Install on premium hosting
2. Enter prompt:
   ```
   Create an ultra-luxury real estate website for [City]'s most exclusive
   properties, featuring multimillion-dollar estates, private island listings,
   and white-glove concierge services.
   ```
3. Install Elementor for custom design
4. Replace sample content with luxury-focused copy
5. Add high-quality property images
6. Configure IDX for luxury-only filters

**Time:** 30 minutes (+ customization)
**Result:** High-end luxury real estate portal

---

### Scenario 4: Investment Focus

**Goal:** Attract real estate investors

**Steps:**
1. Install and configure plugin
2. Enter prompt:
   ```
   Build a real estate investment website for [City] with rental properties,
   ROI calculators, market analysis, and investment strategy guides.
   ```
3. Add investment-focused blog posts
4. Create resources page with calculators
5. Set up lead magnets (free investment guides)

**Time:** 20 minutes
**Result:** Investor-focused property portal

---

### Scenario 5: Vacation Rentals

**Goal:** Showcase vacation rental properties

**Steps:**
1. Install on vacation rental site
2. Enter prompt:
   ```
   Build a vacation rental website for [Destination] with property listings,
   booking information, local attractions guide, and guest resources.
   ```
3. Add property pages manually or via IDX
4. Configure booking calendar integration
5. Add local area guides

**Time:** 25 minutes
**Result:** Vacation rental showcase site

---

## 🔧 Advanced Configuration

### Custom Shortcodes

The plugin recognizes and auto-injects these shortcodes:

**iHomeFinder IDX:**
- `[ihf-quick-search]` - Quick search widget
- `[ihf-property-gallery]` - Property grid
- `[ihf-property-search]` - Advanced search
- `[ihf-featured-listings]` - Featured properties
- `[ihf-open-homes]` - Open houses
- `[ihf-sold-properties]` - Recently sold
- `[ihf-home-valuation]` - Home value estimator
- `[ihf-market-report]` - Market reports
- `[ihf-contact-form]` - IDX contact form

**Contact Form 7:**
- `[contact-form-7 id="123"]` - Contact form

**WPForms:**
- `[wpforms id="123"]` - WPForms form

### Agent Tracking Setup

**Create Custom Tracking Links:**

1. Go to AI Realty → Agents
2. Add each agent
3. Copy their tracking link
4. Distribute to agents

**Tracking Link Format:**
```
https://yoursite.com/?agent=agent001
```

**Advanced Tracking:**

Add UTM parameters for campaign tracking:
```
https://yoursite.com/?agent=agent001&utm_source=facebook&utm_campaign=spring2024
```

**QR Codes:**

Generate QR codes for print materials:
1. Visit [qr-code-generator.com](https://www.qr-code-generator.com)
2. Enter agent tracking link
3. Download QR code
4. Add to business cards, flyers, etc.

### Lead Flow Automation

**GoHighLevel Workflow:**

1. Lead submits form → captured in WordPress
2. Lead synced to GoHighLevel → contact created
3. GoHighLevel automation triggers:
   - Welcome email sent
   - Agent notification sent
   - Follow-up sequence started
   - SMS reminder scheduled

**Setup:**
1. Configure GoHighLevel API in Settings
2. Create automation in GoHighLevel:
   - Trigger: Contact added with tag "website-lead"
   - Actions: Your email/SMS sequence
3. Test with sample lead
4. Monitor in AI Realty → Leads

---

## 🎨 Customization Tips

### After Build Customization

1. **Branding:**
   - Upload logo in Customizer
   - Set brand colors
   - Choose fonts

2. **Content:**
   - Rewrite About page with real info
   - Replace sample blog posts
   - Add real agent bios and photos

3. **Design:**
   - Use Elementor to redesign pages
   - Add custom widgets
   - Create unique layouts

4. **SEO:**
   - Update meta descriptions in Rank Math
   - Add focus keywords
   - Generate XML sitemap

### Recommended Page Additions

Add these pages manually after build:

1. **Home Valuation** - CMA request form
2. **Testimonials** - Client reviews
3. **Sold Properties** - Success stories
4. **Neighborhoods** - Area guides
5. **Buyer Resources** - First-time buyer info
6. **Seller Resources** - Home selling guide
7. **Market Reports** - Monthly stats
8. **Team** - Extended team bios

### Widget Areas

Add to sidebar/footer:

1. Property search widget
2. Featured listings widget
3. Recent blog posts
4. Newsletter signup
5. Social media links
6. Contact information
7. Office hours

---

## 📊 Analytics & Tracking

### Google Analytics Setup

1. Install Google Site Kit plugin
2. Connect Google Analytics
3. Track these goals:
   - Contact form submissions
   - Property inquiries
   - Newsletter signups
   - Phone clicks

### Lead Source Attribution

Track where leads come from:

1. **Agent Tracking:**
   - Agent referrals via `?agent=XXX`
   - View in AI Realty → Leads

2. **Campaign Tracking:**
   - Add UTM parameters to ads
   - Track in Google Analytics

3. **Form Source:**
   - Automatically logged (Contact Form 7, WPForms, IDX)

### Performance Metrics

Monitor in AI Realty → Dashboard:

- Total pages created
- Total leads captured
- Total agents active
- Integration status

---

## 🚀 Growth Strategies

### 1. Content Marketing

**Monthly Blog Posts:**
- Local market updates
- Home buying tips
- Seller advice
- Neighborhood spotlights
- Industry trends

**Use the plugin:**
```
1. Go to Posts → Add New
2. Write valuable content
3. Add SEO keywords in Rank Math
4. Publish and share
```

### 2. Lead Magnets

**Free Resources:**
- Home buyer checklist PDF
- Seller's guide
- Market reports
- Neighborhood guides
- Investment calculators

**Setup:**
1. Create resource page
2. Add download form (WPForms)
3. Collect emails
4. Follow up via GoHighLevel

### 3. Agent Recruitment

**Use tracking for recruiting:**

1. Create recruitment landing page
2. Share tracking link with recruits
3. Show them real-time leads they'd receive
4. Close more agents!

### 4. Social Media Integration

**Amplify your site:**

1. Auto-post new listings to Facebook
2. Share blog posts on LinkedIn
3. Instagram Stories with property photos
4. YouTube virtual tours embedded

---

## 🔄 Maintenance Tasks

### Weekly
- [ ] Check new leads
- [ ] Sync leads to GoHighLevel
- [ ] Respond to inquiries
- [ ] Post new blog content

### Monthly
- [ ] Update market statistics
- [ ] Review agent tracking performance
- [ ] Check for plugin updates
- [ ] Backup database
- [ ] Review SEO rankings

### Quarterly
- [ ] Refresh homepage content
- [ ] Update agent photos/bios
- [ ] Review and optimize forms
- [ ] Analyze lead sources
- [ ] Plan content calendar

---

## 🆘 Common Questions

### Can I rebuild my site multiple times?

Yes! Click "Rebuild Site" anytime. It will:
- Keep existing content
- Add missing pages
- Update integrations
- Preserve settings

### How do I customize the built pages?

Use WordPress editor or Elementor:
1. Go to Pages → All Pages
2. Click Edit on any page
3. Modify content
4. Update

### Can I use a different theme?

Yes! The plugin works with any WordPress theme. For best results:
- Use a real estate theme
- Or use a page builder (Elementor)
- Or use a block theme (FSE)

### What if I don't have IDX?

No problem! The plugin creates:
- Custom property post type
- Sample property listings
- Manual property entry

### Can I disable agent tracking?

Yes, but not recommended. To disable:
1. Deactivate the tracking JS
2. Or don't share agent links
3. Leads will still be captured

---

## 💡 Pro Tips

1. **Set up Google My Business** before building - better local SEO
2. **Get video testimonials** - add to homepage
3. **Use professional photos** - replace Unsplash images
4. **Set up call tracking** - use CallRail or similar
5. **A/B test forms** - optimize conversion rates
6. **Build email list** - offer valuable content
7. **Retarget website visitors** - Facebook Pixel
8. **Claim your listings** - on Zillow, Realtor.com
9. **Guest blog** - build backlinks
10. **Video tours** - embed YouTube/Vimeo

---

## 🎓 Training Resources

### For New Agents
1. WordPress basics tutorial
2. How to add a blog post
3. How to check your leads
4. How to share your tracking link

### For Admins
1. How to manage agents
2. How to customize pages
3. How to integrate IDX
4. How to sync with CRM

### For Developers
1. REST API documentation (see manifest.json)
2. Hook reference
3. Filter reference
4. Custom integration guide

---

**Need more help? Check the main README.md or open an issue on GitHub!**
