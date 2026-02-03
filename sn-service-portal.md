# Service Portal / Employee Center

## Resources

### 📘 Courses

- [x] [Service Portal Fundamentals (Xanadu)](https://learning.servicenow.com/lxp/en/now-platform/service-portal-fundamentals-on-demand?id=learning_course_prev&course_id=46bbccf647435250ac2f89c2e36d437a)
- [ ] [UI Builder Fundamentals (Yokohama)](https://learning.servicenow.com/lxp/en/now-platform/ui-builder-fundamentals-washington?id=learning_course_prev&course_id=be3c198e97bf5ed4a916b4be2153af4b)
- [x] [Employee Center Essentials](https://nowlearning.servicenow.com/lxp/en/hr-service-delivery/hr-service-deliveryname?id=learning_course_prev&course_id=167dea289374b5103cc0322d6cba1019)
- [ ] [AI Search: Indexing (Now Learning)](https://nowlearning.servicenow.com/lxp/en/now-platform/ai-search-indexing?id=learning_course_prev&course_id=beb44c4147cb29142a090dcbd36d435c)
- [ ] [Hands-on AI Search Lab](https://nowlearning.servicenow.com/lxp/en/now-platform/ai-search-explore-ai-search-with-a-hands-on-lab?id=learning_course_prev&course_id=fa0c0ccdc38f29545922751ce001319d)
- [x] [Train Users at Scale with Guided Tour Designer](https://learning.servicenow.com/lxp/en/now-platform/train-users-at-scale-with-guided-tour-designer?id=learning_course_prev&course_id=b09eab94dbe410503e73166e139619ef&s=1&ssa=3)

### 📄 ServiceNow Documentation

- [Employee Center Product Docs](https://docs.servicenow.com/csh?version=latest&topicname=employee-center-landing-page)
  - [Unified Taxonomy for Employee Center](https://docs.servicenow.com/csh?version=latest&topicname=config-taxonomy)
- [Accessibility Conformance Report for Service Portal](https://www.servicenow.com/docs/bundle/accessibility/page/administer/accessibility-508-compliance/concept/available-accessibility-conformance-reports.html)
- [CSS Primer](https://docs.servicenow.com/csh?version=latest&topicname=scss-primer)
- [Widget Library](https://docs.servicenow.com/csh?version=latest&topicname=widget-showcase)
- [General Widget Guidelines](https://docs.servicenow.com/csh?version=latest&topicname=general-guidelines-developing-widgets)
- [Developer Share Projects](https://developer.servicenow.com/connect.do#!/share/contents?category=Service_Portal_Widgets&page=1)
- [Mega Menu](https://docs.servicenow.com/csh?version=latest&topicname=config-mega-menu)
- [Global Header Options](https://docs.servicenow.com/csh?version=latest&topicname=config-global-header-components)
- [Docs: AI Search](https://docs.servicenow.com/csh?version=latest&topicname=overview-ais)
  - [Enable & Configure](https://docs.servicenow.com/csh?version=latest&topicname=ai-search)
- User Experience Analytics (UEA)
  - [UEA for Service Portal](https://docs.servicenow.com/csh?version=latest&topicname=sp-analytics)
  - [UEA Product Documentation](https://docs.servicenow.com/csh?version=latest&topicname=user-exp-analytics-landing)
  - Documentation: [SNAnalytics - Client API](https://docs.servicenow.com/csh?version=latest&topicname=SNAnalyticsClientAPI)
  - Detailed roles: [UEA Roles Documentation](https://docs.servicenow.com/csh?version=latest&topicname=sp-analytics-roles)
- [User criteria for Service Portal – Product Docs](https://docs.servicenow.com/csh?version=latest&topicname=user-criteria)

### 🧠 Community

- [Employee Center Community Forum](https://www.servicenow.com/community/employee-center/ct-p/employee-center)
  - [Employee Center’s Mega Menu Configurations](https://www.servicenow.com/community/employee-center-articles/employee-center-s-mega-menu-configurations/ta-p/2877634)
  - [How do I associate my taxonomy with the employee center?](https://www.servicenow.com/community/employee-center-forum/how-do-i-associate-my-taxonomy-with-the-employee-center/m-p/236678)
- [Employee Center Academy Sessions](https://www.servicenow.com/community/employee-center-articles/employee-center-academy-upcoming-recorded-sessions/ta-p/2320507)
- [Employee Center YouTube Playlist](https://www.youtube.com/playlist?list=PLkGSnjw5y2U5SRs6n1KBRVNzRjJ1ztbjH)
- [Quick Start Guide](https://www.servicenow.com/community/ai-intelligence-articles/ai-search-quick-start-guide/ta-p/2307562)
- [Define Searchable Content](https://www.servicenow.com/community/ai-intelligence-articles/define-searchable-content-for-ai-search/ta-p/2307364)

### 📚 External Resources

- [WCAG 2.1 Standards](https://www.w3.org/WAI/WCAG21/Understanding/intro)
- CSS Guides
  - [Bootstrap CSS](http://getbootstrap.com/css)
  - [Font Awesome](https://fontawesome.com/)
- [AI Academy YouTube](https://www.youtube.com/playlist?list=PLkGSnjw5y2U407_1UQQaVVrD13-MFi5ia)

## Service Portal Basics

### Service Portal Overview

- **Service Portal** is a user-focused alternative interface to the standard ServiceNow UI:

  - Collection of pages for accessing services, tasks, and information.
  - Visual layer customizing look-and-feel of ServiceNow.
  - Mobile-friendly, responsive design.
  - Easy configuration, customization, and extension.
  - Built with industry-standard technologies.

- **Key Features:**

  - Modular, themeable, single-page application.
  - Highly customizable branding and design.
  - Supports modern tech stack:
    - HTML, CSS (SASS/SCSS), Bootstrap, AngularJS, JavaScript.

- **Knowledge Integration:**

  - Built on Knowledge V3 technology.
  - Supports multiple knowledge bases with distinct workflows.
  - Flexible, multi-level category structures.
  - Permissions defined by user criteria per knowledge base/article.
  - Users can search, sort/filter articles, and provide feedback.

- **Service Catalog Integration:**

  - Supports request items, record producers, and order guides.
  - Single-page application enhances ease of use.
  - Fully compatible with client scripts and UI policies.

- **Accessibility (WCAG 2.1 AA compliant):**

  - Improved accessibility for users with visual, cognitive, or mobility impairments.
  - Accessible baseline portals:
    - Service Portal (`/sp`)
    - Knowledge Portal (`/kb`)
    - Customer Service Portal (`/csm`)
    - Consumer Service Portal (`/csp`)
    - Employee Center (`/esc`)
    - Mobile Experience Portal
  - Accessibility preferences in core UI do **not** affect Service Portal.

- **Benefits of Service Portal:**

  - Users:
    - Intuitive, engaging UI.
    - Quick access to common services and tasks.
  - Administrators:
    - Modular UI framework for portals and dashboards.
    - Easy presentation and management of services.
    - Platform features: analytics, authentication, presence, search, multi-language, security, web services.

- **Portal Strategy – Single vs. Multiple:**

  - **Single Portal:**

    - Ideal for smaller organizations.
    - Simplifies URL management and navigation.
    - Less administrative overhead.

  - **Multiple Portals:**
    - Suitable for large, multi-departmental organizations.
    - Useful for governance, distinct branding/theming, confidentiality, or segregating customer vs. employee services.
    - Multiple designers/admins distribute workload.
    - Standard platform security ensures user-specific access control.

- **AngularJS Support:**

  - Despite Google's LTS ending in 2021, ServiceNow maintains a supported version of AngularJS.
  - Customers can safely continue developing and deploying AngularJS-based portals.

- **UI Builder vs. Service Portal:**

  - **Service Portal:**

    - Target: Requesters.
    - Best for large, enterprise-level portals.
    - Responsive, pixel-perfect layouts.
    - Fully supports Service Catalog and public pages.
    - Compatible with ATF testing.
    - Built on AngularJS.

  - **UI Builder (Next Experience UI Framework):**
    - Target: Fulfillers.
    - Suitable for workspaces, small/departmental portals.
    - Limited responsiveness and pixel-perfect capabilities.
    - Minimal support for Service Catalog and public pages.
    - No migration from Service Portal; new portals must be built from scratch.

- **Recommended Approach:**
  - Continue using Service Portal for enterprise portals (e.g., Employee Center).
  - Use UI Builder primarily for creating unique custom applications and departmental portals.

### Plugins and Store Applications

- **Baseline Plugins (No License Required)**

  - **Service Portal for Enterprise Service Management** (_com.glide.service-portal.esm_)
    - Core plugin to enable Service Portal framework.
  - **Knowledge Management - Service Portal (`com.snc.knowledge_serviceportal`)**
    - Required for Knowledge Portal (`/kb`).
  - **Service Portal User Criteria Support** (_com.glide.service-portal.user-criteria_)
    - Adds user criteria-based access controls.

- **Optional Plugins (License Required)**

  - **Employee Center Pro (`/esc`)** (_sn_ex_sp_pro_)
    - Adds ML content targeting, campaigns, communities, virtual agent.
    - Requires **HRSD Pro**, **HRSD Enterprise**, or equivalent license.
  - **Customer Service Portal** (_sn_csm_portal_)
    - B2B customer self-service portal.
    - Requires **Customer Service Management (CSM)** license.
  - **Consumer Service Portal** (_sn_csp_portal_)
    - B2C customer self-service portal.
    - Requires **Customer Service Management (CSM)** license.
  - **Communities** (_com.sn_communities_)
    - Enables discussion forums, community Q&A.
    - Requires **Customer Service Management (CSM)** or related Community license.

- **Store Applications Commonly Used**
  - **Baseline (Free):**
    - Employee Center
      - Employee Experience Foundation
      - Employee Center Core
      - Employee Experience Taxonomy
    - Advanced AI Search Management Tools
  - **Subscription Required:**
    - HR Taxonomy
    - Legal Counsel Center Classic
    - Workplace Service Delivery Professional

### Service Portal Development and Administration

- **User Types** (Portal Audiences):

  - **External Users**: No organizational affiliation.
  - **Customers**: Consume organizational products/services.
  - **Employees**: Work for the organization.
  - **Fulfillers**: Employees tasked with resolving assigned records.
  - **Approvers**: Employees approving records prior to fulfillment.

- **Roles & Permissions**:

  - **admin**:

    - Full system access and can override ACLs.
    - Can activate plugins (assign with caution).

  - **sp_admin**:
    - Design, build, manage Service Portals.
    - Access to Service Portal modules (no Update Set or Studio access).

- **Developer Types**:

  - **No-Code Admins**:

    - Drag-and-drop web dev tasks.
    - Apply branding via portal interface.

  - **Low-Code Admins**:

    - Modify portal elements, activate plugins, basic configuration.
    - Familiar with HTML, CSS, Bootstrap.

  - **Pro-Code Developers**:
    - Create elements using AngularJS, ServiceNow APIs.
    - Advanced scripting and web technologies (HTML, CSS, JavaScript).

- **Delegated Development**:

  - Allows non-admin developers specific module access (including Designer & Studio).
  - Access managed via Studio (`File > Manage Developers`).
  - Non-admin scope limitation: Ensure proper scope selection before accessing `/sp_config` or 404 errors occur.
  - **Note**: Source control commits may omit certain files.

- **Baseline Elements**:

  - Reusable, modular portal components provided by default:
    - **Service Portals**: 8+
    - **Themes**: 10+
    - **Menus**: 10+
    - **Pages**: 100+
    - **Widgets**: 250+

- **Baseline Portals** (Default):

  - **Employee Center (`/esc`)**:
    - Unified employee portal (knowledge, requests, chat).
  - **Service Portal (`/sp`)**:
    - Basic requests, incidents, approvals, status.
  - **Knowledge Portal (`/kb`)**:
    - Knowledge base browsing, searching, feedback.
    - Requires plugin: `com.snc.knowledge_serviceportal`.
  - **Change Advisory Board Workbench (`/cab`)**:
    - Manage CAB meetings and change requests.

- **Licensed Portals**:

  - **Employee Center Pro (`/esc`)**:
    - Advanced features: ML-driven content, communities, virtual agent.
    - Requires HRSD Pro/Enterprise license or separate subscription.
  - **Community (`/community`)**:
    - Collaboration portal for customers, partners, prospects.
  - **Customer Support (`/csm`)**:
    - B2B customer interactions and support.
  - **Customer Service (Consumer Service, `/sp`)**:
    - B2C customer information/support.

- _All > Service Portal > Properties_ (admin role required):

  - Centralized configuration options:
    - Default 404 pages, error notifications, max stream entries, message auto-dismiss timing, announcement order.
    - Enable user criteria for portal access, specify roles to bypass criteria.

- **`/sp_config` Homepage**:

  - Central hub for portal configurations/components.
  - Access via:
    - Unified Navigation: `Service Portal > Service Portal Configuration`
    - URL suffix: `/sp_config`
  - Menu mimics application navigator, lists/forms mirror core UI functionality.

- **Unsupported Features (not on roadmap)**:
  - Domain Separation
  - UI Macros
  - Formatters
  - Client UI Actions
  - Nested Container Catalog Variables
  - Click-through/pop-up functionality

### Employee Center Portal

- **Overview**

  - **Employee Center**: Modern Service Portal for multi-department service delivery.

    - Baseline: Free for all customers.
    - Includes service catalog, knowledge base, AI search, chat (Agent, Virtual Agent), curated experiences (taxonomies), task management, and unified employee profiles.

  - **Employee Center Pro**: Extends Employee Center with employee communication & engagement.
    - Requires **HRSD Pro**, **HRSD Enterprise**, or separate license.
    - Adds employee communications (news, campaigns, governance), dynamic topic microsites, enterprise search (SharePoint), integrations (App Launcher, Approval Hub), Manager Hub, org charts, feedback systems, and employee forums.

- **Key Capabilities**

  - **Employee Center**

    - Report issues, request items/services.
    - Complete tasks, manage requests, and to-dos.
    - Unified experience across departments.
    - ML-driven personalized recommendations and favorites across channels.

  - **Employee Center Pro**
    - Enhanced content experiences and targeted employee communications.
    - Integration-powered features (App Launcher, Approval Hub).
    - Manager-specific capabilities (Manager Hub).
    - Dynamic content and microsite management.

- **Recommended Practice**

  - New development: Start with **Employee Center** (`/esc`).
  - Existing `/sp` portal users: Recommended to migrate to `/esc`.
    - **Migration Steps**:
      1. Download & activate Employee Center from ServiceNow Store.
      2. Evaluate & compare `/esc` with current `/sp`.
      3. Prioritize features to adopt.
      4. Configure `/esc` with unified taxonomy and content tagging.
      5. Deactivate `/sp` and update `/esc` suffix to `/sp`.
      6. Use page route maps to redirect legacy pages.
      7. Roll out `/esc` (consider staggered deployment).

- **Unified Taxonomy**

  - Organizes content (requests, articles, quick links) across departments.
  - Drives **Mega Menu** structure.
  - Baseline taxonomy covers IT, HR, Workplace, Legal, Procurement.
  - **Three Parts**:
    1. **Content Taxonomy (Data Model)**: Hierarchical topics.
    2. **Content Authoring**: Tag/manage content.
    3. **Mapped Employee Content**: OOB content mapped into taxonomy.
  - **Docs**: [Unified Taxonomy for Employee Center](https://docs.servicenow.com/csh?version=latest&topicname=config-taxonomy)

  - Step-by-Step Setup
    - **Prepare the Taxonomy**:
      1. Navigate to: **All > Content Taxonomy > Taxonomies > Employee**.
      2. **Clone** the baseline taxonomy.
      3. Open the cloned taxonomy and customize according to your organization's needs (add/remove topics, adjust hierarchy).
    - **Associate Taxonomy with Employee Center**:
      1. Navigate to: **All > Employee Center > Administration > Portal configuration**.
      2. Ensure Application Scope is set to **Employee Center Core**.
      3. Go to the related list **Taxonomy**, click **Edit**, and select your customized taxonomy.
    - **Configure Mega Menu (Advanced Portal Navigation)**:
      1. Navigate to: **All > Employee Center > Advanced Portal Navigation**.
      2. To configure or fix Mega Menu visibility issues:
         - Do **not** click on `Employee Center` in the `Portal` column.
         - Instead, click on the value (`true`) in the `Active` column to activate/deactivate or configure the Advanced Portal Navigation settings.

- **Home Page Highlights**

  - Modern Portal Theme with dynamic Mega Menu.
  - Widgets include Popular Topics, Quick Links, My Active Items, My Favorites, Recommended for You (ML/popularity-driven).
  - Employee Profile widget (key user fields overview).

- **Dynamic Topic Pages**

  - Auto-created based on taxonomy tags.
  - Structured components include headers, unified content browsing, subtopic navigation, AI-powered search.
  - Pro widgets: Videos, News, Employee Communications, Applications, Rich Content.

- **Search Capabilities**

  - Global AI Search (autocomplete, spellcheck, multilingual, machine learning relevancy).
  - Pro capabilities: News and Microsite searches, SharePoint connector.
  - Recommended topic facet filters to narrow search results.

- **Employee Communications (Pro)**

  - Targeted and scheduled content experiences.
  - Content Library: manage, design, preview, and publish content.
  - Formats: Portal pages, mobile content, notifications (email, Teams, SMS), to-dos, forums.
  - Analytics via dashboards and PA Packs to measure content success.
  - Persona-driven (Employees, Content Creators, Communications Leads).

- **Task Management and Integrations**

  - Widgets/pages: My Active Items, To-dos, Requests.
  - Integration-powered features include SSO-based App Launcher and Approvals Hub.
  - Manager Hub for team management, tasks overview, team insights, and resources.

- **Integrated Feedback (Pro)**

  - Feedback on features, topic pages, home page, service workflows.
  - Options: scales (5-point, smiley, thumbs), comments.
  - Feedback channels: in-page widgets, Outlook integration.

- **References**
  - [Employee Center Community Forum](https://www.servicenow.com/community/employee-center/ct-p/employee-center)
  - [Employee Center Academy Sessions](https://www.servicenow.com/community/employee-center-articles/employee-center-academy-upcoming-recorded-sessions/ta-p/2320507)
  - [Employee Center YouTube Playlist](https://www.youtube.com/playlist?list=PLkGSnjw5y2U5SRs6n1KBRVNzRjJ1ztbjH)
  - [Employee Center Product Docs](https://docs.servicenow.com/csh?version=latest&topicname=employee-center-landing-page)
  - [Now Learning: Employee Center Essentials](https://nowlearning.servicenow.com/lxp/en/hr-service-delivery/hr-service-deliveryname?id=learning_course_prev&course_id=167dea289374b5103cc0322d6cba1019)

---

## Portals and Components

### Service Portals

- **Architecture**

  - Example:
    - The suffix `/esc` identifies the Portal record that holds:
      - Theme, homepage, menus.
      - Logo/Icon.
      - Knowledge Bases, Catalogs.
      - Taxonomy.
      - AI Search and configuration.

- **Portal Record**

  - Behaves as the main configuration for how the portal works.
  - **Key Fields:**
    - **Title** — browser tab text.
    - **URL Suffix** — unique suffix at the end of the URL (e.g., `/esc`).
    - **Homepage** — page loaded when no page is specified.
    - **KB Homepage** — page for launching Knowledge Base.
    - **Login Page** — page for user authentication.
    - **Logo** — shown in nav bar.
    - **Icon** — mobile homepage/browser tab icon.
    - **Default** — one portal can be set as the default (marked with green dot).
    - **Application** — scope of the portal.
    - **404 Page** — fallback when a page is not found.
    - **Catalog Home Page** — landing page for Service Catalog.
    - **Catalog Category Home Page** — landing for catalog categories.
    - **Main Menu** — navigation menu for the portal.
    - **Theme** — styles and widgets collection.
    - **Quick Start Config** — JSON config for Branding Editor options.
    - **CSS Variables** — overrides theme-level styles for this portal only.
    - **Hide Portal Name** — hides portal name in the page title.
    - **Enable Certificate-Based Authentication** — optional secure login.
    - **Enable AI Search** — toggle for AI Search.
    - **Search Application** — configures the search engine/settings.
    - **Search Results Configuration** — defines search results display.

- **Portal Record Related Lists**

  - **Knowledge Bases**
    - Select one or more KBs for the portal.
    - KBs appear on pages like `kb_home`, `kb_view`, or `esc_knowledge_home`.
    - If none specified, ALL KBs accessible to the user are visible.
  - **Catalogs**
    - Select one or more Catalogs to include.
    - Categories and items appear on pages like `sc_home`, `sc_category`, `esc_sc_category`.
    - If none specified, ALL Catalogs accessible to the user are visible.
  - **Taxonomy**
    - Defines hierarchical topics.
    - Controls Mega Menu and Topic Pages in Employee Center.
    - If none specified, no Mega Menu or Topic Pages are shown.
    - Search results are always based on configured AI Search sources — not just KBs, Catalogs, or Taxonomy.

- **Best Practice**
  - Always define the homepage, main menu, theme, and suffix to ensure correct display.
  - Validate search settings, KBs, Catalogs, and Taxonomy to align content and navigation.

### Themes

- **What is a Theme?**

  - Defines consistent branding for a Service Portal.
  - Controls Header and Footer shown on every page.
  - Allows more customization than the Branding Editor.
  - Multiple portals can share the same Theme.
  - A single portal can only use one Theme.

- **When to Use**

  - Use when Branding Editor limits styling flexibility.
  - Good for advanced branding and reusability.

- **Create a Theme**

  - Navigate: **All menu → Service Portal → Themes → New**.
  - Required steps:
    - Create custom style properties in **CSS variables**.
    - Identify **Header** and **Footer**.
    - Save and reuse for multiple portals.

- **Theme Form Fields**

  - **Name** — Theme name.
  - **Application** — Scope of the Theme.
  - **Header** — Header to use on all pages.
  - **Footer** — Footer to use on all pages.
  - **Fixed header** — Locks header at top.
  - **Fixed footer** — Locks footer at bottom.
  - **CSS variables** — Theme-level style definitions.
    - **Important:** Theme-level CSS variables override Branding Editor variables unless marked with `!default`.
      - Example: `§navbar-inverse-bg: #293e40 !default;`
    - Bootstrap defaults apply if no CSS is defined.

- **Style Sheets**

  - Use for additional or external CSS.
  - Stored in the `[sp_css]` table.
  - Navigate:
    - `/sp_config → Portal Tables → Style Sheets → New`
    - Or: **All menu → Service Portal → CSS → New**
  - **Style Sheet Fields:**
    - **Name** — Name of CSS Include.
    - **Application** — Scope.
    - **CSS** — Paste your style code here.
  - Style sheets load **after** CSS variables execute.
    - Variables in `CSS variables` field cannot reference style sheet code.

- **Attach Style Sheets to a Theme**

  - In Theme record, open **CSS Includes** related list.
  - Select **New**.
  - Complete form:
    - **Name** — Name of CSS Include.
    - **Source:**
      - **Style Sheet** — Use existing `[sp_css]` record.
      - **URL** — External CSS file link.
    - **Lazy Load:** Load asynchronously for performance. Must be the same for all includes in a Theme.

- **Add a Custom Font**

  - Three methods:
    1. Use Google Fonts.
    2. Encode font with base64 in CSS Include.
    3. Upload font files as attachments to CSS Includes.
  - **Google Fonts Example:**

    - Copy the Google Fonts URL.
    - Add a new CSS Include → Source: URL → Paste URL.
    - Reference the font in your CSS:

      ```css
      h1 {
        font-family: "Lobster", cursive;
      }
      ```

- **UI Scripts**

  - Use to add internal or external JavaScript.
  - Navigate: **All menu → System UI → UI Scripts → New**
  - **UI Script Fields:**
    - **Script Name** — Unique name.
    - **API Name** — Full API name.
    - **UI Type** — `All` or `Mobile/Service Portal` only.
    - **Application** — Scope.
    - **Active** — Must be active to run.
    - **Description** — Purpose of script.
    - **Script** — Client-side JavaScript.

- **Attach JavaScript to a Theme**
  - In Theme, open **JS Includes** related list.
  - Select **New**.
  - Complete:
    - **Display Name** — Name of JS Include.
    - **Source:**
      - **UI Script** — Internal ServiceNow record.
      - **URL** — External JS file.
    - **Application** — Scope.
    - **Package:** Auto-populated with Service Portal package.

#### Introduction to CSS

- **Selector:** Defines what HTML to style (`h2`).
- **Declaration:** Defines the property and value (`color: gray;`).
- **Declaration Block:** One or more declarations.
- Example:

  ```css
  h2 {
    color: gray;
    text-decoration: none;
  }
  ```

- Write once, reuse across pages.
- Use Service Portal SCSS Primer: [SCSS Primer](https://docs.servicenow.com/csh?version=latest&topicname=scss-primer)
- Reference Bootstrap and Font Awesome:
  - [Bootstrap CSS](http://getbootstrap.com/css)
  - [Font Awesome](https://fontawesome.com/)

### Pages

- **What is a Page?**

  - A reusable, unique piece of Service Portal content with its own **URL**.
  - Uses **containers**, **rows**, **columns**, and **widgets** to display content.
  - Styled by the portal’s **Theme**.
  - Fully mobile-optimized using Bootstrap’s grid.

- **Key Principles**

  - Pages are **independent** — not owned by a portal but styled by it.
  - **Reusable** — changes apply everywhere the Page is used.
  - Keep each Page focused on **one clear purpose**.
  - Use baseline Pages when possible — over 100 provided.

- **Create a Page**

  - Go to **/sp_config → Designer**.
  - Select **Add a new Page**.
  - Enter:
    - **Title** — friendly name.
    - **Page ID** — unique, no spaces/special chars.
  - Creates a record in `[sp_page]`.

- **Access Syntax**

  - `/sp` → portal homepage.
  - `/esc.do?id={Page ID}` → direct link.
  - `/nav_to.do?uri={Portal URL suffix}` → homepage in platform view.
  - Note: `index` is reserved — use with a prefix/suffix if needed.

- **Using the Designer**

  - Drag/drop:
    - **Containers** → top-level sections.
    - **Rows** → divide containers horizontally.
    - **Columns** → divide rows vertically.
    - **Widgets** → dropped inside columns.
  - Changes auto-save.
  - Icons for Add/Delete/Modify.
  - Widgets show edit/delete icons.
  - Preview in:
    - Desktop / Tablet / Mobile.
  - Always test on a real device.

- **Bootstrap**

  - Built on Bootstrap’s **12-column grid**:
    - Mobile-first, responsive.
    - Columns can be grouped (e.g., 3/6/3).
    - More than 12 columns = columns stack.
    - [Bootstrap 3.3 Docs](https://getbootstrap.com/docs/3.3/)

- **Containers**

  - First container auto-added.
  - Add more:
    - Drag from **Element Selector**.
    - Or click **Add (+)** in canvas.
  - Stored in `[sp_container]`.

- **Rows & Columns**

  - Add rows inside containers:
    1. Use blue icon.
    2. Or drag from selector.
  - Add columns inside rows.
  - Stored in `[sp_row]` and `[sp_column]`.

- **Element Selector**

  - Layouts, Widgets, Pages tabs.
  - Use **Filter Widget** or **Filter Page** to find items quickly.

- **Page Properties**

  - Access:
    - Designer → **Page** button.
    - `/sp_config` → **Pages**.
    - **All menu → Service Portal → Pages**.
  - Fields:
    - **Title**, **ID**, **Application**.
    - **Public** — no login required.
    - **Draft** — only admins see it.
    - **Roles** — restricts access.
    - **Short Description**.
    - **Page Specific CSS** — overrides Theme/Portal CSS.

- **Page Editor**

  - Visual map view.
  - Access from `/sp_config`.
  - Steps:
    1. Select Page.
    2. Click an element.
    3. Edit.
    4. Save.
  - No built-in preview — open the Page live in another tab.

- **Set Default Pages**

  - Configure in Portal record:
    - Homepage
    - KB Homepage
    - Login Page
    - 404 Page
    - Catalog Homepage
    - Catalog Category Homepage

- **Clone a Page**
  - Speeds up layout reuse.
  - Cloned Page keeps containers, rows, columns.
  - New Widget Instances created.
  - Clone from `[sp_page]` form or Page Editor.

### Branding Editor

- **Branding Editor Purpose**

  - No-code tool for quickly customizing Service Portals.
  - Adjust titles, logos, colors, and themes without scripting.
  - Preview changes in real time on the live canvas.
  - Ideal for no-code admins wanting fast, safe visual updates.

- **How to Access**

  - Open `/sp_config` homepage.
  - Select **Branding Editor** to launch configuration.

- **Important Behavior**

  - Changes only affect the display of the selected Portal.
  - Changes auto-save when you close the editor or reload the page.
  - Use **Reset Changes** to discard edits and restore previous state.

- **Configuration Options**

  - **Quick Setup Tab**

    - Title
    - Logo
    - Tag Line (appears in Homepage Search Widget)
    - Background Image

  - **Theme Colors Tab**

    - Navbar: Header bar colors.
    - Brand: Page elements and display colors.
    - Text: Text color on all pages.
    - Tag Line color
    - Homepage background color

  - **Canvas**
    - Shows real-time preview as changes are made.

- **Add Quick Setup for New Portals**

  - By default, new Portals have no Tag Line or Background Image fields linked.
  - Copy `Quick start config` code from a baseline portal record.
  - Paste into the new Portal record.
  - Update `sys_ids` to link:
    - Tag Line → `[sp_instance]`
    - Background Image → `[sp_container]`

- **Where Changes Are Stored**

  - Changes may impact:
    - **Portal `[sp_portal]`**: Logo, CSS variables.
    - **Widget Instance**: Portal title.
    - **Container `[sp_container]`**: Background image.

- **Rollback Tip**
  - To undo changes:
    - Manually revert the affected records to their previous version.
    - Use settings from another instance if needed (dev/test/sandbox).
    - For baseline portals, use a fresh Developer instance as a reference.

---

## Widgets and Widget Development

### Widgets

- **Definition**

  - Reusable, self-contained components for data, actions, or services.
  - 200+ widgets baseline.
  - Reusable across multiple pages; each instance can have unique settings.

- **Key Facts**

  - Widgets are secure and modular.
  - Typical uses: search, lists, forms, links, approvals, static/dynamic content.
  - See [Widget Library](https://docs.servicenow.com/csh?version=latest&topicname=widget-showcase) for baseline widgets.

- **Examples**

  - **Homepage Search:** Search portal content.
  - **Simple List:** Dynamic list of records with fields, avatars, actions.
  - **Icon Link:** Links to pages, URLs, Catalogs, KBs. Customizable icon, style.
  - **KB Widgets:** KB Categories, KB Most Viewed, KB Top Rated.
  - **SC Widgets:** SC Categories, SC Catalog Item.
  - **HTML:** Add text/images with Rich Text Editor or HTML.
  - **Approvals:** Shows tasks to approve/reject.
  - **Cool Clocks:** Shows time by time zone (black = PM, white = AM).
  - **Breadcrumbs:** Shows location path.
  - **Typeahead Search:** Site-wide quick search.

- **Best Practice**

  - Prefix custom widgets: `KB` for Knowledge, `SC` for Catalog — appear with baseline widgets.
  - Use Breadcrumbs + Typeahead on all pages except home.

- **How to Add**
  - Find in **Element Selector** → Filter Widget → drag to column.
  - Multiple widgets can share a column.

### Widget Instances

- **Definition**

  - A **widget instance** is a unique record created when you drop a widget on a page.
  - Holds instance-specific settings: title, data source, styling, HTML, etc.
  - One widget → multiple unique instances → different behavior or appearance.

- **Configure an Instance**

  - In Page Designer, click the widget’s **Edit Options** icon.
  - Configure options like:
    - Table
    - Filter
    - Display field(s)
    - Glyph
    - Bootstrap color
    - Title / Short description
  - Behavior is controlled by the base widget’s scripts/templates plus the instance settings.

- **Access a Widget Instance**

  - Open in two ways:
    1. Use **Open in platform** in the widget’s options menu.
    2. Go to **Service Portal → Widget Instances** in the All menu.
  - Records are stored in:
    - **Instance table**
    - Or related tables (e.g., Carousel, Simple List) — found via **Portal Tables** on `/sp_config`.

- **Context Menu (Live Page)**
  - **Ctrl + right-click** a widget to open context menu.
  - Options:
    - **Instance Options:** Edit instance properties.
    - **Instance in Page Editor:** Open in Page Editor.
    - **Page in Designer:** Open Designer with widget selected.
    - **Edit Container Background:** Change container.
    - **Widget Options Schema:** View/add widget properties.
    - **Widget in Form Modal:** Open widget in modal.
    - **Widget in Editor:** Open base widget in Widget Editor.
  - **Tip:** If `Ctrl+right-click` fails, use `Shift+Ctrl+right-click` (older Windows versions).

### Develop Widgets

- **Clone Baseline Widgets**

  - Always review the [Widget Library](https://docs.servicenow.com/csh?version=latest&topicname=widget-showcase) first.
  - Use baseline widgets when possible — they’re read-only to stay upgrade-safe.
  - Clone to customize:
    1. Widget Editor → **Clone** from context menu.
    2. Widgets Module → **Clone Widget** button.
  - Changes to a widget apply to **all its instances** — check **Included in Pages** & **Instances** related lists.

- **Widget Editor**

  - Single-page IDE for creating/updating widgets.
  - Access: `/sp_config` → **Widget Editor** or Widgets menu.
  - Options:
    - Create new widget.
    - Edit existing.
    - Use **Hello World Example** to learn.
  - Tips:
    - Pencil icon in Page Designer opens the Widget Editor.
    - Use `Ctrl+S` or `Cmd+S` to save.
    - `Ctrl+A` → Select all, `Shift+Tab` → Format code.

- **Widget Editor Features**

  - **Widget Selector:** Switch templates.
  - **Show:** Toggle script editors.
  - **Preview:** See real-time result.
  - **Context Menu:** Clone, create, edit options schema, mark Public, Open in Platform.

- **Core Technologies**

  - AngularJS 1.5 (ServiceNow maintained)
  - Bootstrap 3.3.6
  - JavaScript, Lodash/Underscore
  - HTML, CSS, SCSS/Sass, Font Awesome
  - ServiceNow APIs

- **MVC Pattern**

  - **Model:** Data.
  - **View:** HTML Template.
  - **Controller:** Client Script.

- **How Widgets Work**

  - **HTML:** Renders the view, binds data.
  - **Client Script:** Processes/display data, handles input, calls `server.update()`.
  - **Server Script:** Loads initial data, handles server-side logic.
  - **CSS/Bootstrap:** Styles.
  - **Link Function:** Direct DOM manipulation.
  - **Option Schema:** Defines configurable instance options.
  - **Dependencies:** Extra JS/CSS files.
  - **Angular Providers:** Share context, sync widgets.

- **Global Objects**

  - **data:** Server → Client.
  - **input:** Client → Server.
  - **options:** Widget instance config (read-only).

- **Widget Execution Flow**

  - **Server Script:**
    1. Init empty `data` & `input`.
    2. Load `options`.
    3. Send `data` JSON to client.
  - **Client Script:**
    - Use `c.data` and `c.options`.
    - Call `c.server.update()` to post back.

- **Option Schema**

  - Use **Edit Option Schema** in Widget Editor or `Ctrl+right-click → Instance Options` on live portal.
  - Common fields:
    - **Label, Name** (snake_case), **Type, Hint, Default Value, Form Section**
  - Syntax:
    - HTML: `{{:options.title}}`
    - Client: `c.options.text_color`
    - Server: `$sp.log(options.text_color)`

- **Five-Step Dev Strategy**

  1. Load server data (Server Script).
  2. Display data (HTML).
  3. Accept input (Client Script).
  4. Process input (Server Script).
  5. Update view (HTML).

  - Docs: [General Widget Guidelines](https://docs.servicenow.com/csh?version=latest&topicname=general-guidelines-developing-widgets)

- **Share Custom Widgets**
  - [Developer Share Projects](https://developer.servicenow.com/connect.do#!/share/contents?category=Service_Portal_Widgets&page=1)
  - Not officially supported — use at your own risk.
  - Custom widgets may become baseline — keep current.

### Widget Debugging

- **Built-In Debugging**

  - Server-side logs are visible in the **browser JavaScript console**.
  - Baseline widgets rarely fail — issues usually come from custom widgets.

- **Key Debug Tools**

  - `$scope.data` → Data sent from server.
  - `$scope` → All controller variables.
  - `console.log()` → Log to browser console.
  - `spUtil.addErrorMessage()`, `spUtil.addInfoMessage()`, `spModal.alert` → Client-side alerts.
  - `gs.log()`, `gs.debug()`, `gs.info()`, `gs.warn()`, `gs.error()` → Server-side logs.
  - `sp.log()` → Logs server-side output if user has `sp_admin` role.
  - Review logs: **System Log → Script Log Statements**.

- **Widget Diagnostic Tool**

  - Use **Show Widget Customizations** in widget context menu (`Ctrl+right-click`).
  - Color codes:
    - Green → Baseline
    - Yellow → Cloned
    - Blue → New
    - Red → Customized
  - Click **info icon (i)** to inspect code.
  - Limitations:
    - Can’t fix/revert directly — edit in Widget Editor.
    - Tool stops if you navigate away.
    - First-level dependencies only — check deeper in widget record.
    - Not color-blind friendly.

- **Portal Analyzer**

  - Runs on demand — reports on **all widgets** across **all pages**.
  - Stores:
    - Page, Page ID
    - Widget, Widget ID
    - Status: OOTB, Cloned, Customized, New
    - Page views, Unique user count
  - Data: **Service Portal Analyzer table** (`sp_portal_analyzer`).
  - Each job clears old records first.

- **Tips**
  - `debugger` command → sets browser breakpoint (Chrome/Firefox).
  - Stuck dragging widget in Designer? Likely a script error. Check Widget Editor → fix syntax → add debug logs.

## Menus and Navigation

- **What is a Header Menu?**

  - Top-of-page navigation for Service Portal.
  - Combines:
    - **Header** (branding/behavior, defined in Theme)
    - **Main Menu** (navigation items, defined in Portal record)

- **Baseline Example**

  - **Employee Center**: quick links to Requests, Tasks, More Menu, User Menu (profile, impersonate, logout), Shopping Cart, Guided Tours.

- **Config Steps**

  1. Add a **Theme** with a Header.
  2. Add a **Main Menu** with menu items.
  3. Result: Together they build the visible Header Menu.

- **Mega Menu**

  - Requires a **Taxonomy**.
  - Primary navigation for **Employee Center**.
  - 2D view of topics, includes:
    - **Taxonomy items**
    - **Simple links** (manual)
    - **More drop down** (nested items, JSON config)
    - **Quick links**
  - Docs:
    - [Mega Menu](https://docs.servicenow.com/csh?version=latest&topicname=config-mega-menu)
    - [Global Header Options](https://docs.servicenow.com/csh?version=latest&topicname=config-global-header-components)

- **Create a New Menu**

  - Go to:
    - **Portal Tables → Instance with Menu** (via `/sp_config`)
    - Or **Service Portal → Menus** (All menu)
  - Click **New**.
  - Fields:
    - **Title**
    - **Additional Options** (JSON) — e.g., enable Shopping Cart, My Requests.
    - **Application Scope**
    - **Widget**: must be `Instance with Menu`.

- **Add Menu Items**

  - Use **Menu Items related list**.
  - Fields:
    - **Label** — clear name.
    - **Parent Menu** — if nested.
    - **Type** — defines what the link opens.
    - **Order** — 3 digits, lower = leftmost.
    - **Condition** — server-side logic to show/hide.
    - **Glyph** — optional icon.
  - Other fields vary by Type: **Page**, **URL**, **Catalog**, **KB**, **Table**, **Filter**, **Display fields**, etc.

- **Nested Menu Items**

  - Add child items:
    1. Open parent **Menu Item**.
    2. Use its **Menu Items related list**.
    3. Set **Parent Menu Item**.

- **Testing**
  - Use **Impersonate** to verify conditions.
  - Example: `My Approvals` visible only for users with `approver_user` role.

---

## AI Search Integration

### AI: Overview

**AI Search** delivers a modern, ML-powered search experience in ServiceNow.

- Google-like: smart, intuitive, fast.
- Replaces or supplements legacy Zing search.
- Works in Service Portal, Mobile, Virtual Agent, Next Experience.

### AI: Benefits & Key Features

- **Smart**
  - Machine Learning for relevancy.
  - Personalizes results using user metadata.
  - Genius Results (answer cards with actions).
  - Extracts direct answers from KBs.
- **Natural**
  - Natural language queries, synonyms, typos.
  - Hit highlighting.
  - Typeahead suggestions.
  - Tabs & facets for easy filtering.
- **Easy**
  - Intuitive configuration.
  - Strong analytics & dashboards.
  - Internationalization: supports multiple languages.

### AI: Using AI Search in Portals

- **Employee Center Example**
  - Recent searches.
  - Suggestions.
  - Genius Result cards.
  - Highlighted keywords.
  - Filters by tabs & facets.
- **Resources**
  - [AI Academy YouTube](https://www.youtube.com/playlist?list=PLkGSnjw5y2U407_1UQQaVVrD13-MFi5ia)
  - [Docs: AI Search](https://docs.servicenow.com/csh?version=latest&topicname=overview-ais)

### AI: Query Syntax & Behavior

| Pattern              | Meaning                       |
| -------------------- | ----------------------------- |
| `office`             | Any record with _office_      |
| `"microsoft office"` | Exact phrase                  |
| `A OR B`             | Either term                   |
| `-B`                 | Exclude term B                |
| `%`                  | Match any single character    |
| `*`                  | Match zero or more characters |
| `***`                | Match all records             |

- **Automatic Resubmit**
  - If too few results: `AND` → `OR`.
  - Single-term or long queries (8+ terms) skip this.

### AI: Enabling & Configuring AI Search

- **Default Status**
  - **Plugin:** `com.glide.ais` → Active by default.
  - **New Portals:** AI Search on by default.
  - **Upgrades:** Admin must check **Enable AI Search** in portal record.
- **Config**
  - Search Application: controls search behavior.
  - Search Results Configuration: controls how results display.
  - Classic Zing remains available.
- **Key:**
  - Enabling hides Search Sources related list.
  - Prepopulates defaults for new/existing portals.
- docs:
  - 🔗 [Enable & Configure](https://docs.servicenow.com/csh?version=latest&topicname=ai-search)

### AI: Guided Setup & Process Lifecycle

Use **AI Search > Guided Setup** to configure step-by-step:

1. **Indexed Source:** Tables + child tables made searchable.
2. **Search Source:** Limits records via filters.
3. **Search Profile:** Ties sources + dictionaries (synonyms, stop words, typos) + Genius Results + Result Improvements.
4. **Search Application:** Defines UI behavior → tabs, facets, highlighting, suggestions, post-processors.

### AI: Definitions

- **Synonyms:** Same meaning terms.
- **Stop Words:** Common words removed.
- **Typo Handling:** Suggest corrections.
- **Genius Results:** Top answer cards.
- **Result Improvements:** Boost/block records by rules.
- **Auto-suggestions:** Populates field as user types.
- **Scripted Post Processors:** Adjust final results.

📌 _Tables like `sys_log`, `sys_email`, `sys_audit` can’t be indexed._

### AI: Using Preconfigured Records

Good practice:

- Use prebuilt Search Sources & Profiles.
- Clone → adjust filters, e.g. align to your **taxonomy**.

**Steps:**

1. `All > AI Search > Search Experience > Search Sources`
2. Pick Source (e.g. _ESC Portal Catalogs_).
3. Add Taxonomy filter.
4. Update.
5. Repeat for each.

### AI: Search Results Action

**Use:** Define where results redirect + query params.

**Config Path:**  
`Service Portal > AI Search > Search Results Action`

**Key Fields:**

- Short description.
- Portals included.
- AI Search Source.
- Action name (Navigation only).
- Order (lower = higher priority).
- Portal page.
- Payload Query Params.
- Additional Params (e.g., `view=sp`).

### AI: Widget Integration

To use different Search Apps/Results Config per widget:

- Set **widget instance options** on:
  - Homepage Search Widget
  - Typeahead Search Widget
  - Catalog Homepage Search Widget
  - Knowledge Breadcrumbs Widget

**Fix:** For cloned/legacy widgets, run the **Reclassify Search Widgets** fix script if needed.

### AI: Theming

Style AI Search via CSS vars in your **sp_theme** record.

[📚 Theming Reference](https://docs.servicenow.com/csh?version=latest&topicname=ais-sp-css-vars)

### AI: External Content

- **Plugin:** _External Content for AI Search_ (separate license).
- Use External Content Ingestion REST API.
- Maps user/group security from source system → Now Platform.

[📚 Indexing External Content](https://docs.servicenow.com/csh?version=latest&topicname=external-content-ais)

### Special Widget: AI Search Assist

Displays top matches inside a record producer as the user types.

- Example: Baseline in **Create Incident**.

### AI: Analytics & Reporting

✅ Install **Advanced AI Search Management Tools** (free from Store).

Provides:

- Dashboards: **Search Profile**, **Search Index**.
- Trends: usage, query traffic, performance.
- Search Preview UI: test queries with admin tools.

**Install:**  
`System Applications > All Available Applications > Obtain from Store`

**Preview Tabs:**

- **Data:** Summary + NLU triggers.
- **Alert:** Query feedback.
- **Feedback:** Dictionary, NLU intent, debugging.
- **Context:** Specify user context.
- **User:** Test user or locale.

**Dashboards may take ~1 hour to populate.**

### AI: Further Learning

- [AI Search: Indexing (Now Learning)](https://nowlearning.servicenow.com/lxp/en/now-platform/ai-search-indexing?id=learning_course_prev&course_id=beb44c4147cb29142a090dcbd36d435c)
- [Hands-on Lab](https://nowlearning.servicenow.com/lxp/en/now-platform/ai-search-explore-ai-search-with-a-hands-on-lab?id=learning_course_prev&course_id=fa0c0ccdc38f29545922751ce001319d)
- [Quick Start Guide](https://www.servicenow.com/community/ai-intelligence-articles/ai-search-quick-start-guide/ta-p/2307562)
- [Define Searchable Content](https://www.servicenow.com/community/ai-intelligence-articles/define-searchable-content-for-ai-search/ta-p/2307364)

---

## SP Extras

### User Experience Analytics (UEA)

- User Experience Analytics (UEA) enables visualization and analysis of user interactions within Service Portals.
- Included baseline with Service Portal (cloud instances only).
- **Not supported on-premise** instances.
- Provides dashboards to track Service Portal KPIs and user engagement metrics.
- Documentation:
  - [UEA for Service Portal](https://docs.servicenow.com/csh?version=latest&topicname=sp-analytics)
  - [UEA Product Documentation](https://docs.servicenow.com/csh?version=latest&topicname=user-exp-analytics-landing)

#### Dashboard Menu Metrics

- **Overview:** Visual summary of KPIs.
- **Sessions:** User sessions (filterable, drill-down, exportable).
- **Users:** User list and analytics (filterable, drill-down, exportable).
- **UI Analysis:** Insights into portal UI interactions.
- **Analysis:** Usage details, technical info (browser, OS, devices), geography, events, retention.
- **Funnels:** Custom funnel reports tracking conversion processes.
- **Cohorts:** Custom cohort reports based on user actions.
- **Search Analysis:** AI Search usage metrics (requires Advanced AI Search Management Tools plugin).

#### Configuring User Experience Analytics

- **Plugin**: "Service Portal Analytics" active by default.
- To enable analytics tracking for a portal:
  - Navigate to **Service Portal > Portals**.
  - Open portal record.
  - Click **Create Analytics Settings** (creates record in `sys_analytics_bucket` table).
- Access analytics dashboard: **User Experience Analytics > Dashboard**.
- Default tracking applies to **authenticated users only**.
- To track unauthenticated users:
  - Navigate to **User Experience Analytics Settings** record.
  - Select **Enable Unauthenticated User Tracking** checkbox.

#### Baseline UEA Events

- Analytics data helps optimize Service Catalog, Knowledge Base, search, and login tracking.
- Baseline tracked events:
  - **Submit Catalog Request**: Tracks submitted catalog item requests (request ID, item count).
  - **Order Catalog Item**: Tracks ordered catalog items (item name, ID, request ID).
  - **Submit Record Producer Request**: Tracks submissions via record producers.
  - **View Knowledge Article**: Tracks viewed articles (name, ID, language).
  - **Initiate Search**: Tracks search keywords (Faceted and Typeahead widgets).
  - **Search Result Selected**: Tracks clicks on Faceted search results (click rank, sys_id).
  - **Successful Login**: Tracks user login events.
  - **PortalPageLoad**: Tracks visited pages and languages.
  - **SP File Attach**: Tracks file attachments via upload, clipboard, drag-and-drop.
- Custom events and user properties supported via **SNAnalytics API**:
  - Documentation: [SNAnalytics - Client API](https://docs.servicenow.com/csh?version=latest&topicname=SNAnalyticsClientAPI).

#### UEA Roles

- **Portal Analytics Admin** (`portal_analytics_admin`):
  - Access to Dashboard & Settings modules.
  - Can create/update UEA settings.
- **Portal Analytics Viewer** (`portal_analytics_viewer`):
  - View-only access to Dashboard module.
- Additional Analytics Roles:
  - `analytics_admin`, `analytics_viewer`
  - `mobile_analytics_admin`, `mobile_analytics_viewer`
  - `web_analytics_admin`, `web_analytics_viewer`
- Detailed roles: [UEA Roles Documentation](https://docs.servicenow.com/csh?version=latest&topicname=sp-analytics-roles)

#### User Consent Policies

- Configure user consent via: **User Experience Analytics > Consent Policies**.
- Customizable by geographic location:
  - US users (default: **No Consent Required**)
  - EU, EFTA\*, UK users (default: **Explicit Opt-In**)
  - Other users (default: **Notice**)
- Consent policy types:
  - **Explicit Opt-In**: Users explicitly choose to allow tracking.
  - **Notice**: Users informed of tracking (automatic).
  - **No Consent Required**: Automatic tracking without user notification.
  - **Basic Tracking**: Limited user data tracking (hashed IDs, partial session details).
  - **Disabled**: No analytics tracking.
- Customizable consent message text via **System UI > Messages**:
  - Keys:
    - `glide.analytics.consent.text.notice`
    - `glide.analytics.consent.text.explicit_opt_in`

#### Enabling/Disabling User Analytics

- Users can toggle analytics tracking via their **Profile > Preferences > User Experience** section.

#### Privacy Notice for Unauthenticated Users

- Optional privacy notice to inform unauthenticated users of tracking:
  1. Navigate to **All > Service Portal > Announcements**.
  2. Open inactive record **Privacy Notice**.
  3. Select **Active** checkbox.
  4. Edit text in **Summary** (optional).
  5. Select applicable portal(s) under **Portals** section.
  - Default setting: shown to unauthenticated users only.

(\*EFTA = European Free Trade Association)

### Announcements

- Announcements broadcast messages to Service Portal users as:
  - **Banner** (top of portal pages)
  - **Widget** (using Announcement widget)
- **Creating Announcements**:
  - Navigate: **Service Portal > Announcements**
  - Configure fields:
    - Name, Title, Summary, Type
    - Active dates (**From/To**)
    - Audience (**Public** for unauthenticated users only)
- **Customizing Display Styles**:
  - Navigate: Type `announcement_style.list` in the menu filter, press **Enter**
  - Create new style record with fields:
    - **Name**
    - **Background color** (color name or HEX)
    - **Foreground color** (text color name or HEX)
    - **Alignment** (horizontal text alignment)
    - **Application** (scope of style usage)
  - Banner announcements use the style directly set in the Announcement record.
  - For Announcement widget instances, enable **Use Display Style** option.

### User Criteria

- **Purpose**:

  - Define access conditions for pages, widgets, widget instances, and search sources.
  - Replaces role-based access control for Service Portal components (when enabled).
  - Portal records are only visible if user passes evaluation logic.

- **Evaluation Logic**:

  - User has role in **Override List** → ✅ Pass
  - Else:
    - User matches criteria in **Cannot View List** → ❌ Fail
    - Else:
      - **No Can View criteria** → ✅ Pass
      - Else:
        - User matches criteria in **Can View List** → ✅ Pass
        - Else → ❌ Fail

- **Enable User Criteria Support**:

  1. Activate plugin: `Service Portal User Criteria Support`
     - Navigate: **Admin Center > Application Manager**
     - Search and install the plugin
  2. Enable system property:
     - Navigate: **Service Portal > Properties**
     - Check **Enable use of User Criteria records instead of Roles fields**
     - Click **Save**

  - When enabled:
    - Existing **Roles fields** on components are converted into **User Criteria** records
  - To disable: uncheck the property to revert to role-based access (default)

- **Apply User Criteria to Components**:

  - Use **Can View** and **Cannot View** related lists on:
    - Page records
    - Widget records
    - Widget Instance records
  - To configure:
    - Select **New** to create new User Criteria
    - Select **Edit** to apply existing criteria
  - In **Page Editor**:
    1. Load a portal page
    2. Select a node (Page, Widget, Widget Instance)
    3. Open **Can View** or **Cannot View** related list
    4. Select **New**, choose criteria from dropdown
    5. Click **Save**

- **User Criteria Record Fields**: Name, Users, Groups, Roles, Companies, Locations, Departments

  - **Match All** – require user to meet all conditions (unchecked = match any)
  - **Advanced** – toggle to enable scripting
    - **Script** – must return `true` or `false`
  - **Application** – scope of the record
  - **Active** – toggle to enable/disable criteria

- **Note**:
  - User Criteria records must be created/edited via the **Core UI**.
  - For visual task flow diagrams and evaluation logic, see:  
    [User criteria for Service Portal – Product Docs](https://docs.servicenow.com/csh?version=latest&topicname=user-criteria)

### Guided Tours

- course: [Train Users at Scale with Guided Tour Designer](https://learning.servicenow.com/lxp/en/now-platform/train-users-at-scale-with-guided-tour-designer?id=learning_course_prev&course_id=b09eab94dbe410503e73166e139619ef&s=1&ssa=3)
- **Purpose**:

  - Demonstrate navigation and usage of Service Portal pages/features
  - Tours can span multiple pages
  - Access via **Tours** menu item in the header (visible only if present)

- **Availability**:

  - Enabled by default
  - Controlled by system properties:
    - `com.snc.guided_tours.standard_ui.enable` → Enables for standard UI
    - `com.snc.guided_tours.sp.enable` → Enables for Service Portal
  - Check/modify via:
    1. Enter `sys_properties.list` in the navigator
    2. Search for `*guided_tours`
    3. Update values as needed

- **Important Considerations**:

  - Tours menu item only appears if **Header menu** is present
  - If using **Page Route Maps**, tours may not appear as expected
  - **IFRAME-based pages** (e.g., Branding Editor) are not supported in Guided Tour Designer

- **Demo Tour: Employee Center Portal**

  1. Navigate to `/esc`
  2. Click **Tours** in the header menu
  3. Select **Employee Center Portal**
  4. Click **Begin Tour**
  5. Use **Next** to proceed through callouts
  6. Click **Complete** on final step

- **Creating a Guided Tour**

  - Navigate: **Guided Tour Designer > Create Tour**
  - Fill form:
    - **Name** – tour title
    - **Tour Type** – Standard UI, Service Portal, Workspaces, Custom
    - **Portal** – name of Service Portal
    - **Starting Page** – Service Portal page name or form name
    - **Roles** – All or specific roles allowed to access tour
  - Click **Create Tour** → Opens in **Draft** status

- **Using Guided Tour Designer**

  1. Click **Create an Introduction** – customize opening text
  2. Add **Steps**:
     - Drag callout onto UI element (highlighted in purple)
     - Enter instructions
     - Select a **Trigger Type**
     - Click **Save**
  3. Click **Create a Conclusion** – customize closing text
  4. Click **Preview** to test
  5. Click **Publish** to make it available to users

- **Callout Trigger Types**:

  - **Next Button** – User clicks "Next" in the callout
  - **Click the Element** – Triggered by clicking the targeted element
  - **Mouse over the Element** – Triggered by hovering over the element
  - **Right-click the Element** – Triggered by right-clicking the element
  - **Press Enter Key** – Triggered when user presses Enter
  - **Change Element Value** – Triggered by changing the field value and clicking outside
  - **Press any key** – Triggered by any key press
  - **Callout Adjustments**:
    - Use gray icon on top of callout to change arrow direction

## Redirecting in Service Portal

### Page Route Maps

- Use **Page Route Maps** to redirect users from a deprecated page to a replacement without updating hardcoded page IDs in widgets.
- Reduces maintenance by allowing seamless page replacements.
- **Example**: `/esc` users routed from `sc_request` to `order_status` via Page Route Map.

**Create a Page Route Map**:

1. Navigate to **Service Portal > Page Route Maps**
2. Click **New**
3. Complete the form:
   - **Source page** (original page)
   - **Destination page** (new target page)
4. Click **Submit**

### Redirect unauthenticated users to login page

- Create a **system property** to redirect users to the login page defined in the Default portal:
  - **Name**: `glide.entry.page.script`
  - **Type**: `string`
  - **Value**: `new SPEntryPage().getLoginURL()`

**Steps**:

1. Enter `sys_properties.list` in the navigation filter
2. Create a new record with values above

- `SPEntryPage.getLoginURL()` locates the login page specified in the Default Service Portal record
- To customize the behavior:
  - Clone and modify the `SPEntryPage` Script Include
  - Update system property to reference the new Script Include
  - ⚠️ **Modifying baseline Script Includes prevents automatic upgrades**

### Conditionally redirect after login

- Redirect specific users based on role to Service Portal or Core UI:
  - Create system property:
    - **Name**: `glide.entry.first.page.script`
    - **Type**: `string`
    - **Value**: `new SPEntryPage().getFirstPageURL()`

**Use case**:

- Users with `admin` or `itil` roles → Core UI
- All others → Service Portal

**Custom logic (example)**:

```javascript
getFirstPageURL: function () {
  var session = gs.getSession();
  var nt = session.getProperty("nav_to");
  var isServicePortalURL = new GlideSPScriptable().isServicePortalURL(nt);
  var redirectURL = session.getProperty("login_redirect");

  if ((gs.hasRole("admin") || gs.hasRole("itil")) && !redirectURL && !isServicePortalURL) {
    return; // Redirect to UI16
  }
  // Otherwise redirect to Service Portal
}
```

---

## Labs

### Lab 1.5.1 - Explore Your Student Instance

🎯 **Goal**: Download required lab files and review Service Portal Knowledge Base articles.

- **A. Prepare for Labs**

  - Navigate to **Self-Service > Knowledge** on the Unified Navigation header.
  - Select `Class Knowledge Base`.
  - Select the `LabResources.zip` article to download the file.
  - Locate `LabResources.zip` on your computer and double-click it to extract the files.
  - Remember the folder location for uploading images in future labs.

- **B. Review Additional Service Portal Resources**
  - In `Class Knowledge Base`, review optional articles:
    - `Service Portal Design` (covers web design techniques and best practices)
    - `Domain Separation in Service Portal` (explains Domain Separation)
    - `Configuring Zing Search in Service Portal` (explains classic Zing Search)
  - Select any article to download for additional learning.

### Lab 1.5.2 - Enable AI Search

🎯 **Goal**: Enable the AI Search engine in your student instance.

- **A. Enable AI Search in Your Instance**
  - Log out of your instance.
  - Log in using:
    - Username: `aislab.admin`
    - Password: `aislab.admin`
  - Navigate to **Lab Management > Repair Machine Learning Settings** on the Unified Navigation header.
  - Click _Reset Machine Learning Settings_ to run the configuration script.
  - Navigate to **AI Search > AI Search Status** on the Application Navigator.
  - Confirm the message `AI Search is ready` or `AI Search is enabled` appears.
  - If no message appears, notify your instructor.
  - Log out and log back in as the `System Administrator`.

### Lab 1.5.3 - Use the Branding Editor

🎯 **Goal**: Use the Branding Editor to update and reset a Service Portal’s look.

- **A. Update an Existing Portal**

  - Navigate to **Service Portal > Portals** on the Unified Navigation header.
  - Open the `SPF Demo` record.
  - Click the _Try it_ button to open `/spfdemo` in a new browser tab.
  - In the original tab, navigate to **Service Portal > Service Portal Configuration** to launch `/sp_config` in another tab.
  - Click the _Branding Editor_ tile or select it from the header menu.
  - Select `SPF Demo` in the _Service Portal_ drop-down.
  - On the _Quick Setup_ tab:
    - Replace _Portal title_ with `Cloud Dimensions`.
    - Upload `cloud_dimensions_logo.png` (from `LabResources.zip`).
    - Replace _Tag Line_ with `Welcome`.
    - Set _Tag Line color_ to `#ece5de`.
    - Upload `cloud_dimensions_header.jpg` as _Background Image_.
  - On the _Theme Colors_ tab:
    - _Navbar background_: `#000000`
    - _Navbar divider_: `#ffffff`
    - _Navbar link color_: `#ece5de`
    - _Navbar link hover_: `#2d80c3`
  - In the `/spfdemo` tab, refresh the page to view changes.
  - In the `SPF Demo` portal record tab, refresh and confirm new CSS variables.

- **B. Undo the Changes**
  - Return to the Branding Editor tab.
  - Click the yellow _Reset Changes_ button.
  - In the `/spfdemo` tab, refresh and verify original styling restored.
  - In the `SPF Demo` portal record tab, refresh and verify CSS variables cleared.

---

### Lab 2.2.1 - Create a New Theme and Portal

🎯 **Goal**: Create a Cloud Dimensions theme and apply it to a new Service Portal.

- **A. Bring in External CSS**

  - Navigate to **Service Portal > CSS**.
  - Click _New_.
  - Enter `cloud_links.css` for _Name_.
  - Copy and paste:

    ```css
    a {
      color: #2d80c3;
    }
    a:visited {
      color: #2d80c3;
    }
    a:hover {
      color: #ece5de;
    }
    ```

    into the _CSS_ field.

  - Click _Submit_.

- **B. Create a New Theme**

  - Navigate to **Service Portal > Themes**.
  - Click _New_.
  - Enter `Cloud Dimensions` for _Name_.
  - Set _Header_ to `Employee Center Header`.
  - Check _Fixed header_.
  - Leave _Fixed footer_ unchecked.
  - Paste the CSS variables into the _CSS variables_ field:

    ```css
    /* CLOUD DIMENSIONS OFFICIAL COLORS */
    $cloud-Primary: #2d80c3;
    $cloud-Secondary: #ebf2f4;
    $cloud-CloudWhite: #ece5de;
    $cloud-CloudBlack: #323232;
    /* ELEMENT SPECIFIC CSS */
    $sp-tagline-color: $cloud-CloudWhite !default;
    $navbar-inverse-bg: #000000 !default;
    $navbar-inverse-link-color: $cloud-CloudWhite !default;
    $navbar-inverse-link-hover-color: $cloud-Primary !default;
    $body-bg: $cloud-Secondary !default;
    ```

  - Click _Save_.
  - Under _CSS Includes_, click _New_.
  - Enter `Cloud Links` for _Name_.
  - Set _Source_ to `Style Sheet`.
  - Set _Style Sheet_ to `cloud_links.css`.
  - Click _Submit_.

- **C. Test the Theme**

  - Navigate to **Service Portal > Service Portal Home** and note the current header bar and link hover colors.
  - Navigate to **Service Portal > Portals**.
  - Open the `Service Portal` record.
  - Set _Theme_ to `Cloud Dimensions`.
  - Click _Update_.
  - Refresh `/sp` and verify the header bar and navbar link hover colors.
  - To adjust the Mega Menu bar, open `Cloud Dimensions` theme.
  - Add:

    ```css
    $sp-navbar-divider-color: #000000 !default;
    ```

    to _CSS variables_.

  - Click _Update_.
  - Refresh `/sp` and confirm the Mega Menu bar is black.
  - Navigate back to the `Service Portal` record.
  - Change _Theme_ back to `La Jolla`.
  - Click _Update_.

- **D. Create a New Portal**
  - Navigate to **Service Portal > Portals**.
  - Click _New_.
  - Enter:
    - _Title_: `Cloud Dimensions`
    - _URL suffix_: `cdsp`
    - _Default_: Checked
    - _Main menu_: `Employee Center Menu`
    - _Theme_: `Cloud Dimensions`
  - Click the _Logo_ field’s link, choose `cloud_dimensions_logo.png` and click _OK_.
  - Under _Knowledge Bases_, click _Edit_.
  - Add `IT` and `Human Resources General Knowledge` and click _Save_.
  - Under _Catalogs_, click _Edit_.
  - Add `Service Catalog` and `Technical Catalog` and click _Save_.
  - Under _Taxonomy_, click _Edit_.
  - Add `Employee Taxonomy` and click _Save_.
  - Click _Update_ to save the portal.

### Lab 2.2.2 - Include a Custom Font

🎯 **Goal**: Add a Google Font to a Service Portal theme.

- **A. Review the Baseline Font**

  - Navigate to **Service Portal > Service Portal Home** and keep the `/sp` homepage open.

- **B. Select a Google Font**

  - Open [Google Fonts](https://fonts.google.com) in a new tab.
  - Search for `Lobster` and select it.
  - Click _Get font_.
  - Click `<> Get embed code` and copy the stylesheet URL, e.g. `https://fonts.googleapis.com/css2?family=Lobster&display=swap`.

- **C. Link the Google Font to the Theme**

  - Navigate to **Service Portal > Themes**.
  - Open the `La Jolla` theme.
  - Under _CSS Includes_, click _New_.
  - Enter:
    - _Name_: `Google Font - Lobster`
    - _Source_: `URL`
    - _CSS file URL_: Paste the copied URL.
  - Click _Submit_.

- **D. Reference the Font in CSS**

  - In _CSS variables_ of the `La Jolla` theme, paste:

    ```css
    h1,
    h2 {
      font-family: "Lobster", serif;
    }
    ```

  - Click _Update_.
  - Remove the added code and click _Update_ again to reset.

### Lab 2.3.1 - Create a New Page

🎯 **Goal**: Create a new homepage for the Cloud Dimensions Service Portal and set up its layout.

- **A. Switch Service Portals**

  - Navigate to **Service Portal > Service Portal Configuration** in the Unified Navigation header.
  - On `/sp_config`, select the _Designer_ tile or _Designer_ on the header bar.
  - Click the `sp` (or `spfdemo`) link on the header bar.
  - Select the `Cloud Dimensions (cdsp)` Service Portal file.

- **B. Create the New Page**

  - Click _Add a new Page_.
  - Set:
    - _Page title_: `Cloud Dimensions`
    - _Page ID_: `cd_index`
  - Click _Submit_.

- **C. Add Containers, Rows, and Columns**

  - Click the blue `+` icon in the middle of the container. If you see a green `+` icon, drag a row with a 12-column span instead.
  - Add a row with a 12-column span.
  - Drag a second container below Container 1.
  - Add a row with two columns `(9 | 3)` to Container 2.
  - Drag a third container below Container 2.
  - Add a row with three columns `(4 | 4 | 4)` to Container 3.
  - Verify the structure matches the design reference.

- **D. Configure Each Container**

  - Select Container 1 so its border turns blue and breadcrumb shows `Container`.
  - Click the edit (pencil) icon on the header bar.
  - Set:
    - _Background color_: `#2d80c3`
    - _Background image_: `cloud_dimensions_header.jpg`
    - _Background style_: `Cover`
  - Click _Save_.
  - Select Container 2, click the edit icon, set:
    - _Background color_: `#ffffff`
  - Click _Save_.
  - Select Container 3, click the edit icon, set:
    - _Background color_: `#ebf2f4`
  - Click _Save_.

- **E. Test Your Work**
  - Click _Preview_ on the header bar.
  - Review the Cloud Dimensions homepage layout.
  - Click _Edit_ to return to the Designer.

### Lab 2.3.2 - Explore Existing Pages

🎯 **Goal**: Explore baseline Service Portal pages and configure the Cloud Dimensions portal to use them.

- **A. Explore Baseline Pages**

  - In the Page Designer, click _Pages_ on the Element Selector.
  - Enter `User Pro` in the Filter Page search field.
  - Select `User Profile - user_profile` page.
  - Click _Preview_ on the header bar.
  - Use the icons to review rendering for desktop, mobile, and tablet.
  - Click _Edit_ to return to Designer.
  - Repeat for:
    - `Service Portal - landing`
    - `Catalog Categories - sc_category`
    - `System Status - services_status`
  - Preview these baseline pages to add to the Cloud Dimensions portal:
    - `Catalogs - esc_sc_category`
    - `Knowledge - esc_knowledge_home`
    - `Not Found - 404`
  - Document any additional pages you review.

- **B. Add Existing Pages to the Cloud Dimensions Portal**

  - Click _Portal_ on the header bar.
  - Update the Cloud Dimensions portal record:
    - _Homepage_: `cd_index`
    - _KB home page_: `esc_knowledge_home`
    - _Login page_: `landing`
    - _404 page_: `404`
    - _Catalog home page_: `esc_sc_category`
  - Click _Save_.

- **C. Test Your Work**
  - In Core UI, click the System Administrator avatar.
  - Click _Log out_.
  - In the same tab, go to `<your_instance>.lab.service-now.com/cdsp`.
  - Confirm the login page displays.
  - Log in as System Administrator.
  - Remove `/cdsp` from the URL to return to Core UI.

---

### Lab 3.2.1 - Add Widgets to a Page

🎯 **Goal**: Add widgets to all containers and columns on the Cloud Dimensions homepage and configure their options.

- **A. Add Widgets to Container 1**

  - In Page Designer with `[cd_index]` open, enter `homepage` in the Filter Widget search.
  - Drag the `Homepage Search` widget to the only column in Container 1.
  - Select the Homepage Search widget instance.
  - Click the edit icon.
    - _Title_: `How can we help?`
    - _Placeholder_: `Keyword search`
  - Click _Save_.
  - Click _Open in new window_ to launch the live view.
  - Verify Container 1 displays correctly. Leave the tab open for testing.

- **B. Add Widgets to Container 2**

  - In Page Designer, drag the `Quick Links` widget to the left column of Container 2.
  - Click the edit icon.
    - _Card Display Style_: `Thumbnail`
    - _Card Tile Size_: `Small`
    - _Card Content Alignment_: `Center`
    - _Quick Links_: `Request Standing Desk`, `Password reset`, `System status`
  - Click _Save_.
  - Refresh `/cdsp` and verify.
  - Drag an `HTML` widget to the right column of Container 2.
  - Click the edit icon.
  - Click the _Source code_ icon `<>`
  - Paste:

```html
<h3 style="text-align: center;"><strong>Our Community</strong></h3>
<p style="text-align: center;">
  <a
    title="Connect with Cloud Dimensions team members around the world"
    href="/community"
    ><img
      style="max-width: 75%; max-height: 250px;"
      src="our_community.png"
      alt=""
  /></a>
</p>
```

- Save the source and the widget instance.
- Refresh `/cdsp` and test hover and click on the image.

- **C. Add Widgets to Container 3**

  - Drag the `Approvals` widget to the left column.
  - Drag the `Simple List` widget below `Approvals` in the left column.
  - Edit the `Simple List` widget.
    - _Table_: `Task [task]`
    - _Display field_: `Number`
    - _Secondary fields_: `Short description`, `Opened`
    - _Link to this page_: `form`
    - _Show even when empty_: `True`
  - Click _Save_.
  - Edit the `Simple List` widget again.
  - Click _Menu_ > _Open in platform_ (opens new tab).
  - Ensure that you are using the _Default_ view
  - In Menu > Configure > Form Builder, drag _Order_ under _Title_.
  - Save and close Form Builder.
  - Refresh the record form and update:
    - _Title_: `My Tasks`
    - _Order_: `200`
    - _Filter_: `Active | is | true` AND `Assigned to | is (dynamic) | Me`
  - Click _Update_.
  - Close the tab. Return to Designer but do NOT save this record again. Click anywhere outside of the form to close without saving.
  - Impersonate `Don Goodliffe`.
  - Refresh `/cdsp` and verify Container 3 left column shows tasks.
  - End impersonation.
  - Drag the `News Ticker` widget to Container 3’s middle column.
  - Click the edit icon.
  - Click _Open in platform_.
  - Ensure that you are using the _Default_ view
  - Configure:
    - _Title_: `Company News`
    - _Table_: `Knowledge [kb_knowledge]`
    - _Filter_: `Active | is | true` AND `Topic | is | News`
    - _Display field_: `Short description`
  - Click _Update_.
  - Close the tab. Do not save again in Designer.
  - Refresh `/cdsp` and verify the News Ticker works.
  - Drag the `KB Most Viewed` widget to Container 3’s right column.
  - Click the edit icon.
    - _Title_: `Most Viewed KB Articles`
    - _Max Number_: `5`
  - Click _Save_.
  - Refresh `/cdsp` and verify KB articles display.

- **D. Adjust Spacing**

  - On `/sp_config`, select the Page Editor or Pages.
  - Load `[cd_index]` page.
  - Select `cd_index` node.
  - In Page Specific CSS, add:

```css
/*  Removes white space between Header and Container 1  */
section.page,
main.body {
  padding-top: 0px !important;
}

h3 {
  color: #323232;
}

.paddingtop_20 {
  padding-top: 20px;
}
```

- Click _Save_.
- Select `cd_index > Container 2 > Row 1` node.
- Add `paddingtop_20` to the _CSS class_.
- Save.
- Repeat for `cd_index > Container 3 > Row 1`.

- **E. Test and Verify**
  - Refresh `/cdsp`.
  - Verify all widgets display with correct spacing.

### Lab 3.4.1 - Clone an Existing Widget

🎯 **Goal**: Clone and customize the Approvals widget for Cloud Dimensions.

- **A. Clone an Existing Widget**

  - On the `/sp_config` homepage, select the _Widget Editor_ tile or _Widgets_ on the header bar.
  - Enter `Approvals` in the Select a widget drop-down and select the first result.
  - Select _Clone "Approvals"_ in the context menu.
  - Enter `Approvals CD` in the _Widget name_ field.
  - Click _Submit_.
  - Load `Approvals CD` from the Widget drop-down.

- **B. Add Configuration Item and Risk Fields**

  - In _Server Script_, insert:

    ```javascript
    t.cmdb_ci = task.cmdb_ci.getDisplayValue();
    t.risk = task.risk.getDisplayValue();
    ```

    unter line 72 `t.short_description = task.short_description.toString();`.

  - In _HTML Template_, insert:

```html
<div ng-if="approval.task.cmdb_ci">
  <label>${CI}</label>: {{::approval.task.cmdb_ci}}
</div>
<div ng-if="approval.task.risk">
  <label>${Risk}</label>: {{::approval.task.risk}}
</div>
```

under line 33 `<div ng-if="approval.task.approver"><label>${Approver}</label> {{::approval.task.approver}}</div>`.

- Ensure labels on lines 32–44 have colons between label and value.
- Click _Save_.

- **C. Use the New Widget**
  - In Page Designer, refresh the `[cd_index]` page.
  - Drag `Approvals CD` below the existing Approvals widget in Container 3’s left column.
  - Impersonate `Don Goodliffe` and refresh `/cdsp`.
  - Verify the widget displays correctly.
  - End impersonation.
  - Delete the original Approvals widget in Container 3 using the trash icon.
  - Confirm deletion and refresh `/cdsp`.

---

### Lab 3.4.2 - Develop a Custom Footer Widget

🎯 **Goal**: Create and apply a custom footer widget for the Cloud Dimensions Service Portal.

- **A. Create a New Widget**

  - On the `/sp_config` homepage, select the _Widget Editor_ tile or _Widgets_ on the header bar.
  - Click _Create a new widget_.
  - Enter:
    - _Widget Name_: `Cloud Dimensions Footer`
  - Click _Submit_.

- **B. Create and Style the Widget**

  - Replace HTML Template with:

```html
<div class="footerStyle">
  <div class="contactIT">
    <p><strong>CONTACT IT</strong></p>
    <p>Americas: +1 XXX 555 1234</p>
    <p>EMEA: +XX 55 555 1234</p>
    <p>APAC: +XX 55 555 1234</p>
  </div>
  <div class="contactSecurity">
    <p><strong>CONTACT SECURITY</strong></p>
    <p>Americas: +1 XXX 555 4321</p>
    <p>EMEA: +XX 55 555 4321</p>
    <p>APAC: +XX 55 555 4321</p>
  </div>
  <div class="copyright">
    <p>&copy; 2024 ServiceNow Inc. All Rights Reserved</p>
  </div>
  <div class="social" id="footer">
    <a
      class="fa fa-linkedin"
      href="https://www.linkedin.com/company/servicenow"
      target="_blank"
    ></a>
    &nbsp;
    <a
      class="fa fa-twitter"
      href="https://www.twitter.com/servicenow"
      target="_blank"
    ></a>
    &nbsp;
    <a
      class="fa fa-youtube"
      href="https://www.youtube.com/servicenowinc"
      target="_blank"
    ></a>
    &nbsp;
    <a
      class="fa fa-facebook"
      href="https://www.facebook.com/servicenow"
      target="_blank"
    ></a>
    &nbsp;
    <a
      class="fa fa-instagram"
      href="https://www.instagram.com/lifeatnow"
      target="_blank"
    ></a>
    &nbsp;
    <a
      class="fa fa-power-off"
      href="https://www.servicenow.com/community/"
      target="_blank"
    ></a>
  </div>
</div>
```

- Add to CSS - SCSS:

```scss
.footerStyle {
  width: 100%;
  background-color: #000000;
  color: $cloud-CloudWhite;
  text-align: center;
  font-size: 125%;
  margin-left: auto;
  margin-right: auto;
  padding-top: 25px;
}
.contactIT,
.contactSecurity {
  width: 275px;
  display: inline-block;
  text-align: left;
  vertical-align: top;
}
.copyright {
  width: 400px;
  display: inline-block;
  text-align: left;
  vertical-align: top;
}
.social {
  display: inline-block;
  text-align: left;
  vertical-align: top;
  font-size: 150%;
}
```

- Mark the widget as _Public_ using the context menu.
- Click _Save_.

- **C. Identify the Widget as a Footer**

  - Click the ServiceNow logo to close Widget Editor.
  - Navigate to **Service Portal > Widgets**.
  - Locate `Cloud Dimensions Footer`.
  - Add the _Class_ column in list view.
  - Edit _Class_ to `Header | Footer`.
  - Save the update.

- **D. Add the Footer to the Theme**
  - Navigate to **Service Portal > Themes**.
  - Open the `Cloud Dimensions` theme.
  - Set _Footer_ to `Cloud Dimensions Footer`.
  - Click _Update_.
  - Refresh `/cdsp` and test while logged out.
  - Verify the footer displays on the landing page.

---

### Lab 3.4.3 - Develop a Custom Widget with Options

🎯 **Goal**: Create a Support Contacts widget with configurable options.

- **A. Create a New Widget**

  - On the `/sp_config` homepage, select the _Widget Editor_ or _Widgets_.
  - Click _Create a new widget_.
  - Enter:
    - _Widget Name_: `Support Contacts`
    - _Create test page_: `True`
  - Click _Submit_.

- **B. Add Options**

  - Click _Menu_ > _Edit option schema_.
  - Add 5 options:
    - Label: `Title`  
      Type: `string`  
      Form section: `Presentation`
    - Label: `Daytime phone`  
      Type: `string`  
      Form section: `Data`
    - Label: `Emergency phone`  
      Type: `string`  
      Form section: `Data`
    - Label: `KB URL`  
      Type: `string`  
      Form section: `Data`
    - Label: `KB Title`  
      Type: `string`  
      Form section: `Data`
  - Save.

- **C. Add Display HTML and Style**

  - Replace HTML Template:

```html
<form class="form-horizontal">
  <h3 class="text-primary">{{::c.options.title}}</h3>
  <div class="contact-row">
    <div class="label-left">${Safety and Security - During Business Hours}</div>
    <div class="label-right">
      <a href="tel:{{c.options.daytime_phone}}"
        >{{::c.options.daytime_phone}}</a
      >
    </div>
  </div>
  <div class="contact-row">
    <div class="label-left">${Safety and Security - After Hours}</div>
    <div class="label-right">
      <a href="tel:{{c.options.emergency_phone}}"
        >{{::c.options.emergency_phone}}</a
      >
    </div>
  </div>
  <div class="contact-row" ng-if="c.data.show_link">
    <div class="label-left">${Our Corporate Safety and Security Standards}</div>
    <div class="label-right">
      <a href="{{::c.options.kb_url}}" target="_blank"
        >{{::c.options.kb_title}}</a
      >
    </div>
  </div>
</form>
```

- Add to CSS:

```scss
.contact-row {
  overflow: auto;
  padding: 10px;
  border-bottom: 2px solid #f7f7f7;
}
.label-left {
  float: left;
  width: 35%;
  font-weight: bold;
}
.label-right {
  float: right;
  width: 65%;
}
a {
  color: #000000;
}
```

- Click _Save_.

- **D. Add Client Script**

  - Inside the Client Script function (after line 3, before closing bracket):

```javascript
if (c.options.title == "" || !c.options.title) {
  c.options.title = "Safety & Security Contacts";
}
c.data.show_link = false;
if (c.options.kb_url && c.options.kb_url != "") {
  c.data.show_link = true;
  if (c.options.kb_title == "") {
    c.options.kb_title = c.options.kb_url;
  }
}
```

- Click _Save_.

- **E. Test**
  - Visit: `https://<your_instance>.lab.service-now.com/$sp.do?id=support_contacts`
  - Ctrl + Right-click > _Instance Options_.
  - Fill fields, Save, verify display.

---

### Lab 3.4.4 - Develop a Modal Widget

🎯 **Goal**: Create a widget to open a KB article inside a modal.

- **A. Add Page-Level CSS**

  - **Purpose**: Add shared CSS once so multiple widgets can reuse the same styles and stay consistent.
  - Navigate to the **Page Editor**, load `[cd_index]`.
  - select **cd-index** node
  - Add below current code in **Page Specific CSS**:

```css
.cdWidgetTitleBar {
  background-color: #f5f5f5;
  border: 1px solid #e6e6e6;
  border-radius: 5px 5px 0 0;
  padding: 10px 0 0 15px;
  font-size: 120%;
}
.cdWidgetContentArea {
  background-color: white;
  border: 1px solid #d9d9d9;
  border-radius: 0 0 5px 5px;
  padding: 15px;
  margin-bottom: 18px;
}
```

- Save.

- **B. Clone KB Article Widget**

  - Open **Widgets**, search `KB Article Page`.
  - Select _Clone "KB Article Page"_.
  - Name: `KB Article Modal`. Submit.
  - Load `KB Article Modal`.
  - In Server Script, comment lines 6–7 and add below:

```javascript
articleGR
  .addQuery("sys_id", input.sys_id)
  .addOrCondition("number", input.sys_id);
```

- Save.

- **C. Create Modal Link Widget**

  - Create new widget:
    - _Name_: `KB Link Modal`
  - Save.

- **D. Add Options**

  - Edit option schema - add 3 options:
    - Label: `Title`  
      Type: `string`  
      Form section: `Presentation`
    - Label: `Link Title`  
      Type: `string`  
      Form section: `Data`
    - Label: `KB Article`  
      Type: `reference`  
      Ref Table: `Knowledge [kb_knowledge]`  
      Default value: `KB0000001`
      Form section: `Data`
  - Save options and widget.

- **E. Display HTML**

  - Replace HTML:

```html
<div class="cdWidgetTitleBar">
  <p>{{::options.title}}</p>
</div>
<div class="cdWidgetContentArea">
  <p>
    <a
      class="btn btn-info"
      href="javascript:void(0);"
      data-article="{{options.kb_article}}"
      ng-click="c.openOverlay($event)"
      >{{::options.link_title}}</a
    >
  </p>
</div>
```

- **F. Add Client Script**

  - In Client Script (replace existing code):

```javascript
api.controller = function (spModal) {
  /* widget controller */
  var c = this;

  c.openOverlay = function ($event) {
    //pull data-article attribute from clicked element
    var articleId = $event.currentTarget.dataset.article;

    //open modal
    spModal.open({
      //load our custom kb article widget
      widget: "kb_article_modal",

      //pass article id to article widget
      widgetInput: { sys_id: articleId },

      //force modal to large size
      size: "lg",
    });
  };
};
```

- Save.

- **G. Add Widget to Page**

  - In Page Designer, refresh `[cd_index]`.
  - Search `modal` in Filter Widget.
  - Drag `KB Link Modal` above the KB Most Viewed widget in right column of Container 3.
  - Edit instance:
    - _Link Title_: `Recover Deleted Emails`
    - _KB Article_: `KB0000030`
    - _Title_: `Service Desk - Top Call This Week`
  - Save.

- **H. Test**
  - Refresh `/cdsp`.
  - Click the button, verify modal opens.

---

### Lab 4.1.1 - Create a Header Menu

🎯 **Goal**: Create and configure a new header menu with nested items and add it to the Cloud Dimensions Service Portal.

- **A. Lab Preparation**

  - Navigate to **Survey > View Surveys**.
  - Open `Customer Satisfaction Survey`.
  - Select _Assign Survey_.
  - In the reference field, search `admin` and select `System Administrator`, then select _OK_.
  - Repeat to assign `Helpdesk Satisfaction Survey` to `System Administrator`.

- **B. Create a New Menu**

  - Navigate to **Service Portal > Menus**.
  - Select _New_.
  - Set:
    - Title: `CD Header Menu`
    - Widget: `Header Menu`
  - In _Additional options, JSON format_ paste:
    - `enable_more_items` will be updated later

```json
{
  "enable_cart": {
    "displayValue": "true",
    "value": true
  },
  "exclude_search_on_homepage": {
    "displayValue": "true",
    "value": true
  },
  "enable_requests": {
    "displayValue": "true",
    "value": true
  },
  "enable_tasks": {
    "displayValue": "false",
    "value": false
  },
  "enable_more_items": {
    "displayValue": "true",
    "value": true,
    "sysId": "[UPDATE THIS VALUE]"
  }
}
```

- Click _Submit_.

- **C. Add the Menu to the Portal**

  - Navigate to **Service Portal > Portals**.
  - Open the `Cloud Dimensions` portal record.
  - Set _Main menu_ to `CD Header Menu`.
  - Click _Update_.
  - Refresh `/cdsp` and verify the header menu.

- **D. Create a More Menu Item**

  - Navigate to **Service Portal > Menus**.
  - Open `CD Header Menu`.
  - In _Menu Items_ related list, select _New_.
  - Set:
    - Label: `More`
    - Type: `URL`
    - Order: `100`
  - Click _Submit_.
  - Right-click the `More` item row and select _Copy sys_id_.
  - In _Additional options, JSON format_, replace `[UPDATE THIS VALUE]` with the copied `sys_id`.
  - Click _Save_.
  - Refresh `/cdsp`. Confirm `More` is not visible (needs at least two nested items).
  - Open the `More` record.
  - In _Menu Items_ related list, select _New_.
  - Set:
    - Label: `My Surveys`
    - Type: `Page`
    - Order: `100`
    - Page: `my_surveys`
  - Click _Submit_.
  - Refresh `/cdsp`. Confirm `My Surveys` appears.
  - In _Menu Items_ related list, select _New_.
  - Set:
    - Label: `My Org Chart`
    - Type: `Page`
    - Order: `200`
    - Page: `my_org_chart`
  - Click _Submit_.

- **E. Add a Menu Item to the Mega Menu**

  - Return to `CD Header Menu`.
  - In _Menu Items_ related list, select _New_.
  - Set:
    - Label: `Knowledge Base`
    - Type: `Page`
    - Page: `kb_home`
  - Click _Submit_.

- **F. Test**
  - Refresh `/cdsp`.
  - Confirm the `More` menu displays with both nested items.
  - Test both nested items for correct page routing.
  - Confirm `Knowledge Base` appears on the Mega Menu and opens `kb_home`.

---

### Lab 5.4.1 - Configure AI Search

🎯 **Goal**: Configure AI Search so Cloud Dimensions users can search for US office locations with state-based filtering.

- **A. Review Current Search Results**

  - Navigate to **AI Search > AI Search Status** and confirm: _AI Search is ready_.
  - Open `/cdsp` and search `washington` in the Keyword Search field.
  - Confirm no results are returned.

- **B. Index Existing Source**

  - Navigate to **AI Search > AI Search Index > Indexed Sources**.
  - Open the `Location Table` record.
  - Select _Index All Tables_.
  - On the Indexed Source History form, right-click the header and select _Reload form_ until _Ingestion State_ is `indexed`.

- **C. Create a Search Source**

  - Navigate to **AI Search > Search Experience > Search Sources**.
  - Click _New_ and configure:
    - Name: `US Locations`
    - Indexed Source: `Location Table`
    - Conditions:
      - Country `is` `USA`
      - AND State / Province `is not empty`
      - AND Zip / Postal Code `is not empty`
  - Click _Save_.
  - Click _Click to preview_.
  - Verify only US locations with State/Province and Zip/Postal Code appear. Personalize columns as needed.

- **D. Update Default Search Profile**

  - Navigate to **AI Search > Search Experience > Search Profiles**.
  - Open `Service Portal Default Search Profile`.
  - In _Search Sources_, click _Link Existing_.
  - Link `US Locations`. Click _Submit_.
  - Click _Publish_.

- **E. Preview Changes**

  - Navigate to **AI Search > Preview > Search Preview (New)**.
  - Select `Service Portal Default Search Application`.
  - Enter `***` and press `<Enter>`.
  - Click the `Location Table` facet. Confirm only Location Name is shown.

- **F. Add a Field Mapping**

  - Navigate to **AI Search > AI Search Index > Indexed Sources**.
  - Open `Location Table`.
  - In _Field Settings & Mapping_, click _New_:
    - Attribute: `map_to`
    - Field: `zip`
    - Value: `text`
  - Click _Submit_.
  - On `Location Table`, select _Index All Tables_.
  - After indexing, return to **Search Preview (New)**.
  - Select `Service Portal Default Search Application`, enter `***`, press `<Enter>`.
  - Click `Location Table` facet and verify both Name and Zip/Postal Code display.

- **G. Add a Facet**

  - Navigate to **AI Search > Search Experience > Search Applications**.
  - Open `Service Portal Default Search Application`.
  - In _Facets_, click _New_:
    - Name: `State`
    - Label: `State`
    - Facet Field: `cmn_location.state`
    - Type: `Multi Select Or`
  - Click _Submit_.

- **H. Test**
  - Return to `/cdsp`.
  - Search `washington` in the Keyword Search field.
  - Confirm Location records display.
  - Use the `State` facet to filter and verify results.

---

### Lab 6.4.1 - Announcements

🎯 **Goal**: Create and display a styled announcement on the Cloud Dimensions Service Portal.

- **A. Create an Announcement Display Style**

  - Navigate by entering `announcement_style.list` in the Filter navigator.
  - Select _New_.
  - Set `Name`: `Cloud Dimensions Corporate`
  - Set `Background color`: `#208000`
  - Set `Foreground color`: `#ece5de`
  - Set `Alignment`: `Left align`
  - Select _Submit_.

- **B. Create a New Announcement**

  - Navigate to **Service Portal > Announcements**.
  - Select _New_.
  - Set `Name`: `Infinity Demo Days`
  - Check `Active`
  - Set `Title`: `Infinity is Ready`
  - Set `From`: [yesterday’s date, current time]
  - Set `To`: [next Monday, 17:00:00]
  - Set `Display style`: `Cloud Dimensions Corporate`
  - Set `Type`: `Banner, Widget`
  - Set `Glyph`: [any image]
  - Uncheck `Public`
  - Set `Summary`:

    ```txt
    Cloud Dimensions is happy to announce the release of Infinity - our new Portable Holographic Projector (PHP). Join us all day next Monday for live demonstrations in Meeting Room Nova 3 and try the simulator yourself!
    ```

  - Select _Behavior_ tab:
    - Set `Click target`: `-- None --`
    - Set `Dismiss options`: `User can dismiss for current session only`
  - Select _Portals_ tab:
    - Insert row: `Cloud Dimensions`
    - Select green checkmark to save
  - Select _Submit_.

- **C. Add Announcements Widget to Homepage**

  - Open the **Cloud Dimensions [cd_index]** page in Page Designer.
  - Drag the **Announcements** widget below the **News Ticker** widget in container 3.

- **D. Test Your Work**
  - Refresh the live view of `/cdsp`.
  - Confirm the banner announcement displays.
  - Confirm the Announcements widget also shows the message.
  - Click the _X_ on the banner announcement to dismiss.
  - Refresh `/cdsp` — banner should not reappear.
  - Ctrl + Right-click the Announcements widget > _Instance Options_.
  - Check `Use Display Style`.
  - Select _Save_.
  - Refresh `/cdsp` — announcement now styled using display style.

### Lab 6.4.2 - Create a Dashboard Page

🎯 **Goal**: Build an ITSM Dashboard with reports and add a role-restricted widget link to the homepage.

- **A. Create a New Page with Breadcrumbs and Search**

  - In Page Designer, select the **Cloud Dimensions** logo to return home.
  - Create new page:
    - `Page Title`: `ITSM Dashboard`
    - `Page ID`: `itsm_dashboard`
  - Insert a row with 9 | 3 column split into container 1.
  - Edit left column:
    - Set `Size-md`: `8`
    - Add **Breadcrumbs** widget.
  - Edit right column:
    - Set `Size-md`: `4`

- **B. Build Container 2**

  - Add new container below container 1.
  - Insert a single-column (12) row.
  - Add **HTML** widget.
  - Edit widget:
    - Font-size: _Heading 1_
    - Align: _Center_
    - Text: `ITSM Dashboard`

- **C. Build Container 3**

  - Add container 3, insert row with 4 | 4 | 4 column split.
  - Add **Report** widget to each column.
  - Configure:
    - Left report: `Open Incidents by Priority`
    - Middle report: `Open Incidents by Category`
    - Right report: `Open Incidents by Group`

- **D. Build Container 4**

  - Add container 4 with 6 | 6 column split.
  - Configure:
    - Left report: `This Weeks Change Requests by Category`
    - Right report: `Standard Change success report`

- **E. Style the Page**

  - Navigate to **Page Editor** > load `itsm_dashboard`.
  - Select the `itsm_dashboard` node.
  - Paste into _Page Specific CSS_:

```css
/*  Removes white space between Header and Container 1  */
section.page,
main.body {
  padding-top: 0px !important;
}

/*  Style the Page  */
section.page {
  background-color: black;
}

/*  Style Heading 1  */
h1 {
  color: white;
}

/*  Borders  */
.blueTopBorder {
  border-top: 10px solid blue;
  margin-top: 20px;
}

.blueBottomBorder {
  border-bottom: 10px solid blue;
  margin-bottom: 20px;
}
```

- Save.
- Apply `blueTopBorder blueBottomBorder` to `Container 2 > Row 1` CSS class
- Apply `blueBottomBorder` to `Container 4 > Row 1` CSS class

- **F. Create a Widget to Launch the Page**

  - Navigate to **Widget Editor**, select _Create new widget_.
    - `Widget Name`: `Quick Links ITIL`, _Submit_
  - In **Server Script** (into the existing function): `data.hasItilRole = gs.hasRole("itil");`
  - In **HTML Template** (replace existing code):

```html
<div ng-show="c.data.hasItilRole">
  <div class="cdWidgetTitleBar">
    <p>Quick Links</p>
  </div>
  <div class="cdWidgetContentArea">
    <p>
      <a class="btn btn-info whiteText" href="?id=itsm_dashboard"
        >ITSM Dashboard</a
      >
    </p>
  </div>
</div>
```

- In **CSS - SCSS Editor**:

```css
.whiteText {
  color: white;
}
```

- Save.

- **G. Add Widget to Homepage**
  - In Page Designer, load `cd_index`.
  - Drag **Quick Links ITIL** widget below **KB Link Modal** in container 3 right column.
  - Refresh `/cdsp`, verify:
    - Button redirects to ITSM Dashboard.
    - Impersonate `Abel Tuter` (no `itil` role) — widget is hidden.
  - End impersonation.

### Lab 6.4.3 - Create a Guided Tour

🎯 **Goal**: Build a guided tour that walks users through resetting a password.

- **A. Create a Guided Tour**

  - Navigate to **Guided Tour Designer > Create Tour**.
  - Configure:
    - `Name`: `How to Reset a Password`
    - `Tour Type`: `Service Portal`
    - `Portal`: `Cloud Dimensions`
    - `Starting Page`: `Cloud Dimensions (cd_index)`
  - Select _Create Tour_.

- **B. Create the Callouts**

  - _Introduction_:
    - Title: `How to Reset a Password`
    - Text: `This will guide you through requesting a password reset within the Cloud Dimensions portal.`
  - Callout 1:
    - Target: **Password Reset** card
    - Placement: `Above`
    - Text: `Click Password reset`
    - Trigger: `Click`
  - Click the Password Reset card to continue to form.
  - Callout 2:
    - Target: `What application password do you need reset?` field
    - Placement: `Above`
    - Text: `Select the application which needs the password reset.`
    - Trigger: `Next button`
  - Callout 3:
    - Target: `How would you like to be contacted?` field
    - Placement: `Above`
    - Text: `Select how you would like to be contacted.`
    - Trigger: `Next button`
  - Callout 4:
    - Target: _Submit_ button
    - Placement: `Below`
    - Text: `Click to submit the request.`
    - Trigger: `Click`
  - Submit sample form data.
  - _Conclusion_:
    - Text: `You did it! Your Password reset request has been submitted.`

- **C. Test the Tour**

  - In Guided Tour Designer, click _Preview_.
  - Step through:
    - Begin Tour → Click Password Reset
    - Fill fields → Select SMS → Submit → Complete

- **D. Publish the Tour**

  - Navigate to `/cdsp` in a new tab, verify “You have no tours”.
  - Return to Guided Tour Designer and click _Publish_.
  - Confirm.

- **E. Execute the Tour**
  - Refresh `/cdsp`.
  - Red dot appears next to _Tours_ in header.
  - Select _Tours > How to Reset a Password_ to start the tour.

---

### Lab 7.2.1 - Clone the Landing Page

🎯 **Goal**: Clone and customize the baseline login page for the Cloud Dimensions portal.

- **A. Upload the Background Image**

  - Navigate to **System UI > Images**.
  - Select _New_.
  - Set `Category`: `Service Portal`
  - Set `Name`: `sp-landing-cd.svg`
  - Upload file: `sp-landing-cd.svg` from LabResources.zip
  - Select _Update_.

- **B. Clone the Baseline Landing Page**

  - Navigate to **/sp_config** > _Page Editor_.
  - Load the `landing` page.
  - Select the `landing` node.
  - Click _Clone Page_.
  - Type `copy` in the page list, select `copy_of_landing_1`.
  - Select the `copy_of_landing_1` node.
  - Set `Title`: `Cloud Dimensions Login Page`
  - Set `ID`: `landing_cd`
  - In _Page Specific CSS_:
    - Replace background image with `sp-landing-cd.svg`
    - Set `background-color`: `#7795B2`
    - In `section.page main.body:before`, set `background-color`: `#7795B2`
    - After last block, add:

```css
h3 {
  color: Black;
}
```

- Save.
- Navigate to **Service Portal > Portals**.
- Open `Cloud Dimensions`.
- Set `Login page`: `landing_cd`
- Save.

- **C. Preview the Page**

  - Open a second browser or log out.
  - Go to `<your_instance>.lab.service-now.com/cdsp`.

- **D. Update the Design of the Page**

  - In Page Designer, reload the page list.
  - Load `landing_cd`.
  - Select right-most column in container 1.
  - Delete the column.
  - Change remaining column `Size-md`: `12`.

- **E. Update the Style of the Page**

  - Edit the **HTML** widget instance.
  - Click _Source Code_ icon.
  - Update welcome message:
    - Text: `Welcome to the Cloud Dimensions Service Portal`
  - Remove `class="text-white"` from the `<h3>` tag.
  - Save and Save again.

- **F. Test Your Work**
  - Refresh `/cdsp`.
  - Confirm welcome message, styling, and layout updates.

---

### Lab 7.2.2 - Page Route Maps

🎯 **Goal**: Configure routing so the Service Catalog link redirects to the proper landing page.

- **A. Replace a Quick Link**

  - Load `cd_index` in Page Designer.
  - Edit **Quick Links** widget in container 2.
  - Remove: `Request Standing Desk`
  - Add: `Service Catalog`
  - Save.

- **B. Create a Page Route Map**

  - Refresh `/cdsp`, click `Service Catalog` link.
  - Confirm page loaded is `sc_home`.
  - Navigate to **Service Portal > Page Route Maps**.
  - Open `Catalog Landing`.
  - Select _lock icon_ beside **Service Portal(s)** to enable editing.
  - Add: `Cloud Dimensions`
  - Select _unlock icon_ to disable editing.
  - Ensure `Active` is checked.
  - Select _Update_.

- **C. Test Your Work**
  - Return to `/cdsp`, click `Service Catalog`.
  - Confirm display is `sc_landing` (even though URL is `?id=sc_home`).

---

### Lab 7.2.3 - Redirect Users to a Service Portal

🎯 **Goal**: Redirect base URL visitors to the Cloud Dimensions login page.

- **A. Review the SPEntryPage Script Include**

  - Navigate to **System Definition > Script Includes**.
  - Open `SPEntryPage`.
  - Review `getDefaultPortal()` and `getLoginURL()` logic.

- **B. Create a System Property**

  - Go to `sys_properties.list` via Filter Navigator.
  - Select _New_.
  - Set `Name`: `glide.entry.page.script`
  - Set `Type`: `string`
  - Set `Value`: `new SPEntryPage().getLoginURL()`
  - Select _Submit_.

- **C. Test the Redirect**
  - Log out or open a second browser.
  - Navigate to base URL (omit `/cdsp`).
  - Confirm redirect to `landing_cd`.
