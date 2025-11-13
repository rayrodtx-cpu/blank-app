# Mobile-First Real Estate Website (Apple iPhone App Style)

A comprehensive, mobile-first real estate website template styled to mimic an Apple iPhone native app UI, powered by iHomefinder IDX widgets for seamless MLS integration.

## 📱 Overview

This website provides a complete real estate solution with:
- **Apple iOS-inspired design**: Clean, minimalist interface using Apple's system fonts and design patterns
- **Mobile-first approach**: Optimized for mobile devices with responsive layouts
- **iHomefinder IDX integration**: Full MLS search, listings, and lead capture functionality
- **19 specialized pages**: From property search to agent profiles and market reports
- **Custom CTA buttons**: "Tour Now" and "More Details" on every listing card

## 🎨 Design Philosophy

The design follows Apple's Human Interface Guidelines:
- **iOS Blue accent color** (#007AFF) for all interactive elements
- **Apple system fonts** (-apple-system, San Francisco)
- **Rounded corners** (8px-12px) for cards and buttons
- **Subtle shadows** for depth and hierarchy
- **Large tap targets** (minimum 44x44 points) for mobile usability
- **Clean spacing** and typography for readability

## 📂 Project Structure

```
blank-app/
├── css/
│   └── idx-global-styles.css      # Global iOS-inspired styles for IDX widgets
├── js/
│   └── idx-cta-buttons.js         # Script to inject CTA buttons on listings
├── pages/
│   ├── home.html                  # Hero search + featured carousel
│   ├── listing-search.html        # Full MLS search
│   ├── featured-listings.html     # Agent's active listings
│   ├── pending-listings.html      # Properties under contract
│   ├── sold-listings.html         # Past sales
│   ├── open-house-listings.html   # Upcoming open houses
│   ├── markets.html               # Communities/neighborhoods
│   ├── listing-report.html        # Daily new listings (MarketBoost)
│   ├── open-home-report.html      # Weekly open houses (MarketBoost)
│   ├── market-report.html         # Monthly market stats (MarketBoost)
│   ├── agent-profile.html         # Individual agent page
│   ├── agents-directory.html      # All agents listing
│   ├── property-organizer.html    # Save favorites/login
│   ├── email-alerts.html          # Listing alerts signup
│   ├── mortgage-calculator.html   # Payment calculator
│   ├── valuation-request.html     # Home valuation form
│   └── contact.html               # General contact form
└── README.md                      # This file
```

## 🚀 Getting Started

### Prerequisites

1. **iHomefinder Account**: You need an active iHomefinder IDX account
2. **iHomefinder Activation Script**: Obtain your activation script from iHomefinder
3. **Web Hosting**: GHL (GoHighLevel), WordPress, or any platform supporting custom HTML/CSS/JS

### Installation Steps

#### Step 1: Configure iHomefinder

1. Log into your iHomefinder control panel
2. Navigate to **Settings** → **Activation**
3. Copy your iHomefinder activation script (looks like):
   ```html
   <script src="https://your-domain.ihomefinder.com/activation.js"></script>
   ```

#### Step 2: Add Global CSS to iHomefinder

1. In iHomefinder control panel, go to **Settings** → **IDX Stylesheet**
2. Copy the entire contents of `css/idx-global-styles.css`
3. Paste into the IDX Stylesheet settings
4. Save changes

This applies the iOS-inspired styling to all IDX widgets across your site.

#### Step 3: Set Up Pages in Your CMS

For **GoHighLevel (GHL)**:

1. Go to **Sites** → **Funnels/Websites**
2. For each page you want to add:
   - Create a new custom page
   - Copy the HTML content from the corresponding file in `pages/`
   - **IMPORTANT**: Add your iHomefinder activation script in the page `<head>` section
   - Paste the page content in the body
   - Set appropriate page URL (e.g., `/homes` for home.html)
   - Save and publish

For **WordPress**:

1. Install a page builder that supports custom HTML (Elementor, Divi, etc.)
2. Create a new page for each HTML file
3. Add your iHomefinder activation script to the theme header or use a plugin like "Insert Headers and Footers"
4. Add the page HTML content using an HTML widget/module
5. Publish

For **Other Platforms**:

- Ensure you can add custom HTML, CSS, and JavaScript
- Include the iHomefinder activation script in your site's `<head>`
- Add the CSS globally or per-page
- Copy each page's HTML into your CMS

#### Step 4: Add the CTA Buttons Script

The `js/idx-cta-buttons.js` script adds "Tour Now" and "More Details" buttons to all listing cards.

**Option 1: Global Footer (Recommended)**
- Add the script to your site's global footer so it runs on all pages:
  ```html
  <script src="/js/idx-cta-buttons.js"></script>
  ```

**Option 2: iHomefinder Code Injection**
- If iHomefinder offers an "Add Code to IDX Content" option, paste the script there
- This ensures it runs on all IDX-generated content

**Option 3: Per-Page**
- Add the script tag at the end of each listing page (already included in HTML files)

#### Step 5: Configure iHomefinder SEO Pages

1. In iHomefinder control panel, go to **SEO Pages**
2. Set up these pages with their corresponding URLs:
   - **Home**: `/` or `/homes`
   - **Listing Search**: `/search`
   - **Featured Listings**: `/featured`
   - **Pending Listings**: `/pending`
   - **Sold Listings**: `/sold`
   - **Open House Listings**: `/open-houses`
   - **Markets**: `/markets`
   - **Listing Report**: `/listing-report`
   - **Open Home Report**: `/open-home-report`
   - **Market Report**: `/market-report`
   - **Agent Profile**: `/agent`
   - **Agents Directory**: `/agents`
   - **Property Organizer**: `/organizer`
   - **Email Alerts**: `/alerts`
   - **Contact**: `/contact`

3. For each page, use the embed codes provided in the HTML files

## 📄 Page Descriptions

### Core Search & Listings Pages

| Page | Purpose | Key Features |
|------|---------|--------------|
| **Home** | Landing page | Quick search widget, featured listings carousel |
| **Listing Search** | Full MLS search | Advanced filters, results grid/list |
| **Featured Listings** | Agent's active listings | Shows properties for sale |
| **Pending Listings** | Under-contract properties | Shows pending sales |
| **Sold Listings** | Past sales | Portfolio of closed deals |
| **Open House Listings** | Upcoming events | Properties with scheduled open houses |

### Market & Community Pages

| Page | Purpose |
|------|---------|
| **Markets** | Community/neighborhood search pages |
| **Listing Report** | Daily new listings for a market (MarketBoost) |
| **Open Home Report** | Weekly open houses for a market (MarketBoost) |
| **Market Report** | Monthly statistics and trends (MarketBoost) |

### Agent & Contact Pages

| Page | Purpose |
|------|---------|
| **Agent Profile** | Individual agent bio and listings |
| **Agents Directory** | Team roster with photos and contact info |
| **Contact** | General contact form |

### Tools & Lead Capture

| Page | Purpose |
|------|---------|
| **Property Organizer** | User login to save favorite listings |
| **Email Alerts** | Subscribe to new listing notifications |
| **Mortgage Calculator** | Estimate monthly payments |
| **Valuation Request** | Home seller lead capture form |

## 🎨 Customization

### Changing the Accent Color

The default iOS blue (#007AFF) can be changed:

1. Open `css/idx-global-styles.css`
2. Modify the `:root` variable:
   ```css
   :root {
     --ios-blue: #FF6B35;  /* Your custom color */
   }
   ```
3. Save and re-upload to iHomefinder IDX Stylesheet settings

### Adjusting Button Styles

Edit the button styles in `css/idx-global-styles.css`:

```css
/* Primary buttons */
button, input[type=submit] {
  background-color: var(--ios-blue);
  border-radius: 8px;  /* Adjust roundness */
  padding: 0.6em 1em;  /* Adjust size */
}
```

### Customizing CTA Button Links

In `js/idx-cta-buttons.js`, modify where buttons link:

```javascript
// Change "Tour Now" destination
tourBtn.href = '/schedule-tour?listing=' + listingId;

// Change "More Details" behavior
detailsBtn.href = detailLink.href + '?ref=cta';
```

### Adding Your Logo

Add a logo to the hero section in `pages/home.html`:

```html
<div class="hero-search">
  <img src="/path/to/logo.png" alt="Your Logo" style="max-width: 200px; margin: 0 auto 1em;">
  <h1>Find Your Dream Home</h1>
  ...
</div>
```

## 🔧 Technical Details

### Browser Compatibility

- **Safari (iOS)**: Full support, optimized for
- **Chrome/Edge (Mobile)**: Full support
- **Firefox (Mobile)**: Full support
- **Desktop browsers**: Responsive, scales up nicely

### Performance

- **Minimal dependencies**: Uses vanilla JavaScript (no jQuery)
- **Optimized CSS**: Targets only necessary elements
- **Lazy loading**: iHomefinder widgets load on-demand
- **Mobile-first**: Smaller payloads for mobile devices

### Accessibility

- **Font size**: 16px minimum to prevent zoom on mobile
- **Tap targets**: 44x44 points minimum (Apple HIG)
- **Color contrast**: WCAG AA compliant with blue accent
- **Semantic HTML**: Proper heading hierarchy

## 📱 Mobile Features

### Touch Gestures
- **Swipe**: Featured listings carousel supports swipe
- **Tap**: Large buttons for easy interaction
- **Scroll**: Smooth scrolling on all pages

### iOS-Specific
- **Safe area**: Content respects iPhone notch/island
- **System fonts**: Uses San Francisco on iOS
- **Status bar**: Integrates with iOS status bar color

## 🐛 Troubleshooting

### iHomefinder Widgets Not Showing

1. **Check activation script**: Ensure it's in the `<head>` of every page
2. **Verify account status**: Log into iHomefinder to confirm active subscription
3. **Browser console**: Check for JavaScript errors (F12 → Console)
4. **Clear cache**: Clear browser cache and reload

### CTA Buttons Not Appearing

1. **Script loaded?**: Verify `idx-cta-buttons.js` is loaded (check Network tab)
2. **Timing issue**: Script may run before listings load; increase poll attempts:
   ```javascript
   if (++tries > 20 || anyListing) {  // Increase from 10 to 20
   ```
3. **Check selectors**: Ensure `.ihf-grid-result-container` exists on page

### Styling Not Applied

1. **CSS uploaded?**: Verify `idx-global-styles.css` is in iHomefinder settings
2. **Specificity**: Add `!important` if needed to override iHomefinder defaults
3. **Clear iHomefinder cache**: Some CDN caching may occur

### Mobile Layout Issues

1. **Viewport meta tag**: Ensure present in `<head>`:
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```
2. **Test on real device**: Simulators may not reflect actual rendering
3. **Check media queries**: Adjust breakpoints in CSS if needed

## 📞 Support & Resources

### iHomefinder Documentation
- [iHomefinder Knowledge Base](https://support.ihomefinder.com/)
- [Widget Builder Documentation](https://www.ihomefinder.com/idx-widgets/)
- [API Reference](https://www.ihomefinder.com/api/)

### Design Resources
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [iOS Design Themes](https://developer.apple.com/design/human-interface-guidelines/color)
- [SF Symbols](https://developer.apple.com/sf-symbols/) (optional icons)

## 📝 License

This template is provided as-is for use with iHomefinder IDX services. Modify freely for your real estate website needs.

## 🎯 Next Steps

1. ✅ Set up iHomefinder account and get activation script
2. ✅ Upload global CSS to iHomefinder settings
3. ✅ Create pages in your CMS using the HTML templates
4. ✅ Add CTA buttons script to global footer
5. ✅ Configure iHomefinder SEO pages
6. ✅ Test all pages on mobile devices
7. ✅ Customize colors and branding
8. ✅ Add your logo and agent information
9. ✅ Set up email alerts and lead routing
10. ✅ Launch and promote your site!

## 🙏 Credits

- **Design inspiration**: Apple iOS design language
- **IDX provider**: iHomefinder
- **Fonts**: Apple System Fonts (-apple-system, San Francisco)

---

**Need help?** Contact your iHomefinder representative or web developer for assistance with setup and customization.

**Last updated**: November 2025
