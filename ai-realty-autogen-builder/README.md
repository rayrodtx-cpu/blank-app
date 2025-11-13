# AI Realty Autogen Builder

**Autonomous AI-powered WordPress plugin for building complete real estate websites from natural language prompts.**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/ai-realty-autogen-builder)
[![License](https://img.shields.io/badge/license-GPL--2.0+-orange.svg)](https://www.gnu.org/licenses/gpl-2.0.html)
[![WordPress](https://img.shields.io/badge/WordPress-6.0+-green.svg)](https://wordpress.org)

---

## 🚀 What Is This?

The **AI Realty Autogen Builder** is a revolutionary WordPress plugin that lets you build an entire real estate website with a single natural language prompt. It integrates seamlessly with Claude AI via Model Context Protocol (MCP) and uses only **free WordPress tools**.

### Key Features

- **🤖 Autonomous Site Building** - Describe your site in plain English, press build, and watch it come to life
- **🏠 Full Real Estate Suite** - Pages, listings, agents, blog, contact forms, SEO, and more
- **🔌 Free Plugin Integration** - Works with Elementor, Contact Form 7, Rank Math, WPForms, and more
- **🏢 IDX Support** - Auto-integrates with iHomeFinder Optima Express for live property listings
- **📊 CRM Integration** - Syncs leads to GoHighLevel automatically
- **🍪 Agent Attribution** - Cookie-based lead tracking for agent commissions
- **🔧 Claude MCP Integration** - Full REST API for AI-powered updates and management
- **💰 100% Free** - No paid dependencies (optional premium tools supported)

---

## 📦 What Gets Built Automatically?

When you activate this plugin and hit "Build Site," it creates:

### Pages
- **Home** - Hero section with property search
- **Properties** - Listings gallery (IDX or custom)
- **Search Properties** - Advanced search functionality
- **Our Agents** - Agent directory with bios
- **About Us** - Company information
- **Contact Us** - Lead capture forms
- **Blog** - Real estate news and tips

### Content
- Sample blog posts about real estate
- Agent profiles with tracking links
- Property listings (if no IDX)
- Navigation menus
- SEO metadata (titles, descriptions, keywords)

### Functionality
- Contact forms with lead capture
- Agent attribution cookies
- GoHighLevel CRM sync
- Featured images (Unsplash API)
- Schema markup for SEO
- Mobile-responsive design

---

## 🛠️ Installation

### Requirements

- WordPress 6.0 or higher
- PHP 8.0 or higher
- MySQL 5.7 or higher

### Quick Setup

1. **Upload the plugin:**
   ```bash
   # Via FTP
   Upload the ai-realty-autogen-builder folder to /wp-content/plugins/

   # Via WordPress Admin
   Go to Plugins → Add New → Upload Plugin
   ```

2. **Activate the plugin:**
   - Navigate to **Plugins** in WordPress admin
   - Find "AI Realty Autogen Builder"
   - Click **Activate**

3. **Configure settings:**
   - Go to **AI Realty → Settings**
   - Enter your city and state
   - (Optional) Add API keys for enhanced features

4. **Build your site:**
   - Go to **AI Realty → Dashboard**
   - Enter a prompt or use defaults
   - Click **Build Site Now**
   - Wait 30-60 seconds
   - Done! 🎉

---

## 🔧 Configuration

### Basic Settings

Navigate to **AI Realty → Settings**:

| Setting | Description | Required |
|---------|-------------|----------|
| Default City | Your primary market (e.g., Austin) | Yes |
| Default State | State abbreviation (e.g., TX) | Yes |
| Unsplash API Key | Free images for pages/posts | Optional |

### API Integrations

#### Unsplash (Free Featured Images)
1. Sign up at [unsplash.com/developers](https://unsplash.com/developers)
2. Create a new application
3. Copy your Access Key
4. Paste in **Settings → Unsplash API Key**

#### iHomeFinder IDX (Property Listings)
1. Install **Optima Express** plugin from WordPress.org
2. Sign up for iHomeFinder account
3. Configure Optima Express with your credentials
4. This plugin will auto-detect and use IDX shortcodes

#### GoHighLevel (CRM Integration)
1. Log in to your GoHighLevel account
2. Go to **Settings → API**
3. Create a new API key
4. Copy your **Location ID** from Settings → Business Profile
5. Enter both in **AI Realty → Settings**

---

## 🎯 Usage

### Build Your First Site

**Option 1: Use Default Settings**
```
1. Go to AI Realty → Dashboard
2. Click "Build Site Now"
3. Wait for completion
4. Visit your site!
```

**Option 2: Custom Prompt**
```
1. Go to AI Realty → Dashboard
2. Enter a prompt like:
   "Build a luxury real estate website for Miami Beach with
    IDX listings, agent profiles, blog, and lead capture forms"
3. Click "Build Site Now"
4. Watch the magic happen!
```

### Example Prompts

**Basic Real Estate Site:**
```
Build a real estate website for Austin agents with property listings,
blog, agent profiles, and contact forms.
```

**Luxury Focus:**
```
Create a high-end real estate site for Beverly Hills with luxury property
showcases, agent team pages, and virtual tour integration.
```

**Commercial Real Estate:**
```
Build a commercial real estate website for Chicago with office listings,
investment properties, market reports, and tenant resources.
```

### Managing Agents

1. Go to **AI Realty → Agents**
2. Click **Add New Agent**
3. Fill in agent details
4. Copy their tracking link
5. Share with agent for lead attribution

**Agent Tracking Links:**
```
https://yoursite.com/?agent=agent001
```

When visitors click an agent's link, a cookie is set for 30 days. All form submissions during that time are attributed to that agent.

### Viewing Leads

1. Go to **AI Realty → Leads**
2. View all captured leads
3. See which agent referred each lead
4. Sync to GoHighLevel with one click

---

## 🤖 Claude MCP Integration

This plugin exposes a complete REST API for Claude AI to interact with your site.

### API Base URL
```
https://yoursite.com/wp-json/ai-builder/v1/
```

### Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/build-site` | POST | Build entire site from prompt |
| `/status` | GET | Get site build status |
| `/create-page` | POST | Create a new page |
| `/update-page` | POST | Update existing page |
| `/delete-page/:id` | DELETE | Delete a page |
| `/pages` | GET | List all pages |
| `/create-agent` | POST | Add new agent |
| `/agents` | GET | List all agents |
| `/leads` | GET | Get all leads |
| `/sync-leads` | POST | Sync leads to GoHighLevel |
| `/settings` | POST | Update plugin settings |

### Example API Usage

**Build Site:**
```bash
curl -X POST https://yoursite.com/wp-json/ai-builder/v1/build-site \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Build a real estate website for Austin"}'
```

**Create Page:**
```bash
curl -X POST https://yoursite.com/wp-json/ai-builder/v1/create-page \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Luxury Condos",
    "content": "<h2>Explore our luxury condo listings</h2>"
  }'
```

**Get Status:**
```bash
curl https://yoursite.com/wp-json/ai-builder/v1/status
```

### MCP Manifest

The `mcp/manifest.json` file defines all available tools and endpoints for Claude integration. Claude can use this to understand how to interact with your WordPress site.

---

## 🎨 Recommended Free Plugins

While the plugin works standalone, these free plugins enhance functionality:

### Essential (Recommended)
- **Elementor** - Visual page builder
- **Contact Form 7** - Lead capture forms
- **Rank Math SEO** - SEO optimization
- **Optima Express** - iHomeFinder IDX integration

### Optional
- **WPForms Lite** - Alternative form builder
- **Yoast SEO** - Alternative SEO plugin
- **Jetpack** - Security and performance

### Installing Recommended Plugins

```
1. Go to Plugins → Add New
2. Search for plugin name
3. Click "Install Now"
4. Click "Activate"
5. Return to AI Realty → Dashboard to rebuild with new integrations
```

---

## 📊 Features Breakdown

### 1. Autonomous Site Building

The plugin creates:
- ✅ All core pages (Home, Listings, Agents, Contact, Blog, etc.)
- ✅ Navigation menus with proper hierarchy
- ✅ Sample blog posts about real estate
- ✅ Agent profiles with tracking links
- ✅ Contact forms with hidden agent fields
- ✅ SEO metadata for every page
- ✅ Featured images from Unsplash
- ✅ Homepage and blog page settings

### 2. Agent Attribution System

**How it works:**
1. Agent gets unique link: `yoursite.com/?agent=agent001`
2. Visitor clicks link → cookie is set for 30 days
3. Visitor submits any form → agent ID is included
4. Lead saved to database with agent attribution
5. Commission tracking made easy!

**Cookie Details:**
- Name: `agent_ref` (configurable)
- Expiry: 30 days (configurable)
- Domain-wide tracking
- Works with all forms (CF7, WPForms, custom)

### 3. Lead Management

**Captured from:**
- Contact Form 7 submissions
- WPForms submissions
- iHomeFinder IDX inquiries
- Custom forms with email fields

**Lead data includes:**
- Name, email, phone
- Message/inquiry details
- Source (which form)
- Agent ID (if attributed)
- GHL sync status
- Timestamp

### 4. CRM Integration

**GoHighLevel Sync:**
- Automatic or manual sync
- Creates/updates contacts
- Adds tags for segmentation
- Includes agent attribution
- Rate-limited to avoid API throttling

### 5. IDX Integration

**iHomeFinder Support:**
- Auto-detects Optima Express plugin
- Injects shortcodes automatically:
  - `[ihf-quick-search]` on homepage
  - `[ihf-property-gallery]` on listings page
  - `[ihf-property-search]` on search page
  - `[ihf-featured-listings]` on homepage
- Adds agent ID to all IDX forms
- Full MarketBoost compatibility

### 6. SEO Optimization

**Rank Math Integration:**
- Auto-generates meta titles
- Auto-generates descriptions
- Focus keywords for each page
- Schema markup (RealEstateAgent)
- XML sitemap configuration
- OpenGraph tags

---

## 🧠 How Claude Uses This Plugin

With MCP integration, Claude can:

1. **Build complete sites autonomously**
   ```
   Claude: "I'll build a real estate website for you."
   [Calls /build-site endpoint]
   Claude: "Done! Your site is live with 7 pages, 3 blog posts, and 2 sample agents."
   ```

2. **Update content on command**
   ```
   You: "Update the About page to mention we've been in business since 1995."
   Claude: [Calls /update-page with new content]
   Claude: "Updated! The About page now mentions your 1995 founding."
   ```

3. **Manage agents**
   ```
   You: "Add a new agent named Sarah Johnson."
   Claude: [Calls /create-agent]
   Claude: "Added Sarah! Her tracking link is yoursite.com/?agent=agent003"
   ```

4. **Sync leads**
   ```
   You: "How many leads do we have?"
   Claude: [Calls /leads endpoint]
   Claude: "You have 47 leads. 23 are not synced to GoHighLevel yet."
   You: "Sync them please."
   Claude: [Calls /sync-leads]
   Claude: "Done! All 23 leads synced successfully."
   ```

---

## 🔒 Security

- All API endpoints check user permissions
- Settings stored securely with WordPress options API
- SQL injection protection via $wpdb->prepare()
- XSS protection via esc_html(), esc_attr(), etc.
- CSRF protection via nonces
- Sanitization of all user inputs
- No plain-text API keys in code

---

## 🐛 Troubleshooting

### Site Build Fails

**Check:**
1. PHP version 8.0+ (Settings → Site Health)
2. Memory limit ≥ 256MB (increase in wp-config.php if needed)
3. File permissions (wp-content/uploads should be writable)
4. Conflicting plugins (disable others temporarily)

**Error Log:**
Check **AI Realty → Dashboard** for build log details

### Leads Not Captured

**Check:**
1. Contact Form 7 or WPForms is installed and active
2. Forms have email fields
3. Database tables exist (deactivate/reactivate plugin)
4. JavaScript console for errors

### Cookie Not Set

**Check:**
1. URL has `?agent=XXXX` parameter
2. Agent ID exists in database
3. Browser allows cookies
4. No JavaScript errors in console

### GoHighLevel Sync Fails

**Check:**
1. API key is correct
2. Location ID is correct
3. Test connection in Settings
4. Check error log for API response

---

## 📖 File Structure

```
ai-realty-autogen-builder/
├── ai-realty-autogen-builder.php    # Main plugin file
├── README.md                         # This file
├── includes/
│   ├── class-ai-realty-autogen.php           # Core plugin class
│   ├── class-ai-realty-autogen-loader.php    # Hook loader
│   ├── class-ai-realty-autogen-admin.php     # Admin functionality
│   ├── class-ai-realty-autogen-public.php    # Public functionality
│   ├── class-ai-realty-autogen-activator.php # Activation tasks
│   ├── class-ai-realty-autogen-deactivator.php # Deactivation tasks
│   ├── class-ai-realty-site-builder.php      # Autonomous builder engine
│   ├── class-ai-realty-agent-attribution.php # Cookie & lead tracking
│   └── integrations/
│       ├── class-elementor-integration.php
│       ├── class-rankmath-integration.php
│       ├── class-contact-form-7-integration.php
│       ├── class-wpforms-integration.php
│       ├── class-ihomefinder-integration.php
│       └── class-gohighlevel-integration.php
├── mcp/
│   ├── manifest.json                 # MCP server manifest
│   └── class-ai-realty-mcp-api.php  # REST API handler
├── templates/
│   ├── admin-dashboard.php
│   ├── admin-settings.php
│   ├── admin-leads.php
│   └── admin-agents.php
└── assets/
    ├── js/
    │   ├── ai-realty-autogen-admin.js
    │   └── ai-realty-autogen-public.js
    └── css/
        ├── ai-realty-autogen-admin.css
        └── ai-realty-autogen-public.css
```

---

## 🎓 Example Use Cases

### 1. New Brokerage Website
**Scenario:** Starting a new real estate brokerage in Dallas
**Prompt:** "Build a modern real estate website for Dallas with team pages, IDX integration, and blog"
**Result:** Complete site in 60 seconds with Dallas-specific content

### 2. Single Agent Site
**Scenario:** Solo agent wants personal branding site
**Prompt:** "Build a personal real estate site for luxury homes in Scottsdale"
**Result:** Professional single-agent site with luxury focus

### 3. Property Management Company
**Scenario:** Managing rental properties
**Prompt:** "Build a rental property website for college apartments near Austin"
**Result:** Rental-focused site with tenant resources

### 4. Commercial Real Estate
**Scenario:** Office and retail leasing
**Prompt:** "Build a commercial real estate site for Chicago office spaces"
**Result:** Commercial-focused site with investment pages

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This plugin is licensed under the **GPL-2.0+** license.

---

## 🆘 Support

- **Documentation:** This README
- **Issues:** [GitHub Issues](https://github.com/yourusername/ai-realty-autogen-builder/issues)
- **Community:** WordPress.org forums

---

## 🎉 Credits

Built with ❤️ by the AI Realty Dev Team

**Integrations:**
- WordPress REST API
- Elementor
- Rank Math SEO
- Contact Form 7
- WPForms
- iHomeFinder Optima Express
- GoHighLevel API
- Unsplash API
- Claude AI (Anthropic)

---

## 🚀 Roadmap

**Coming Soon:**
- [ ] Multi-language support
- [ ] More IDX providers (Showcase IDX, IDX Broker)
- [ ] Additional CRM integrations (HubSpot, Salesforce)
- [ ] AI-generated property descriptions
- [ ] Video tour integration
- [ ] Virtual staging with AI
- [ ] Automated email campaigns
- [ ] Client portal

---

## 💡 Tips & Best Practices

1. **Start with recommended plugins installed** for best results
2. **Configure API keys before building** to enable all features
3. **Test agent tracking links** before sharing with your team
4. **Regularly sync leads to GoHighLevel** to keep CRM updated
5. **Customize pages after building** to match your brand
6. **Use Elementor** for advanced page design
7. **Add real agent photos** to replace placeholder images
8. **Write unique content** after initial build for better SEO

---

**Ready to build your real estate empire? Let's go! 🏠✨**
