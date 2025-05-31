# ServiceNow Reports Reference Notes

## TODO

- [ ] Add content for Lesson 5
- [ ] Add specific links and resources
- [ ] Cross-reference related sections

---

## Table of Contents

- [Report Fundamentals](#report-fundamentals)

  - [Overview](#overview)
  - [Report Designer](#report-designer)
  - [Analytics Q\&A](#analytics-qa)
  - [Report Sources](#report-sources)

- [Labs](#labs)

  - [Lab 1.1: List Report](#lab-11-list-report)
  - [Lab 1.2: Report Sources](#lab-12-report-sources)
  - [Lab 1.3: External Data Import](#lab-13-external-data-import)

---

## Report Fundamentals

### Overview

- Reports visualize real-time business metrics.
- Report types based on purpose:

  - Comparison
  - Distribution
  - Relationship
  - Composition
  - Current State

- Navigate to **Reports > View/Run** to explore report types.
- Reports tabs:

  - **My Reports**: Created by the user.
  - **Group, Global, All**: Authorized reports.

- **report_user** role required to access Reports application.
- Reports can be combined onto dashboards for faster decisions.
- Dashboard widgets examples:

  - **Single Score**: Total incidents overdue.
  - **Pie Chart**: Incidents by state.
  - **Time Series (Area Chart)**: Incident volume over time.
  - **Heatmap**: Incidents by priority and state.

- Dashboards can be viewed by any user if shared.

---

### Report Designer

- Guided, step-by-step report creation tool.
- Report creation stages:

  1. **Data Phase**: Select table containing data.
  2. **Type Phase**: Choose visualization type:

     - Pie/Bar charts: Comparisons
     - Time Series: Historical trends
     - Single Score: KPIs
     - List: Spreadsheet-like view

  3. **Configure Phase**: Select attributes to group or aggregate data.
  4. **Style Phase**: Customize visual appearance (size, colors, fonts).

- **Condition Builder** filters data during report creation.
- Example: Creating List Report

  1. Select table (Incident).
  2. Filter data (e.g., Active=true).
  3. Choose type (List).
  4. Group by attributes (State).
  5. Style report (title, alignment, font).
  6. Save and share reports.

- Preview reports anytime with **Run** button.

---

### Analytics Q\&A

- Converts natural language queries into report definitions.
- Accessible from any list or Data tab in Report Designer.
- Automatically suggests recent queries and table/column matches.
- Example Queries:

  - **Single Score**: Keywords (Total, Count, Avg., Min., Max.)

    - e.g., "count of incidents assigned to Eduardo"

  - **Historical Trend**: Keywords (daily, monthly, quarterly, yearly)

    - e.g., "monthly average of business duration for incidents"

  - **Bar Chart**: Keyword (By)

    - e.g., "number of open incidents by category"

  - **Dates/List**: Keywords (today, last week, etc.)

    - e.g., "incidents updated last week"

  - **Specify Type**: Force visualization type ("as list", "as bar chart", "as pie chart")

    - e.g., "problems by priority as pie chart"

- Requires activation of Natural Language Query (NLQ) feature by System Administrator.

---

### Report Sources

- Defines data origin for reports (table + conditions).
- Three report source types:

#### Table (Most Common)

- Select non-system tables directly.
- Users require table ACL permissions.

#### Data Source

- Predefined reusable filter conditions.
- Created by Report Administrators (`report_admin` role).
- Example steps:

  - Choose existing Data Source (e.g., Incidents.Open: Active=true).
  - Create new Data Source via UI Action:

    1. Define filter (e.g., Priority = High/Critical).
    2. Save as new Data Source.

  - Leverage existing Data Source directly in reports.

#### External Data Import

- Import Excel data into temporary ServiceNow table.
- Import file requirements:

  - First row: Column names.
  - Max size: 2 MB; max columns: 25.
  - Expiration & visibility required.

- Expiration options: 1-2 weeks, 1-3-6 months, 1 year.
- Visibility options: Only me, Everyone, specific Users/Groups/Roles.
- Reports automatically deleted post-expiration.

---

## Labs

### Lab 1.1: List Report

**Goal:** Create and verify a list report using Report Designer and Analytics Q\&A.

### Lab 1.2: Report Sources

**Goal:** Create reports using existing and newly defined data sources.

### Lab 1.3: External Data Import

**Goal:** Use external data (Excel file) to create a ServiceNow report.

**Detailed Steps:**

- **Section A:** Validate Excel file requirements:

  - Extension: `.xlsx`
  - First worksheet only
  - First row: Column names
  - File size: < 2 MB
  - Rows: < 10,000
  - Columns: < 25

- **Section B:** Create report from external data:

  1. Navigate to **Reports > Create New**.
  2. Data Tab:

     - Name: `Outages by Root Cause`
     - Source type: `External import`
     - Upload external file
     - External source properties:

       - Name: `System Outages`
       - Expire: `1 Month (30 days)`
       - Visible to: `Everyone`

  3. Select visualization type: `Bar`
  4. Configure report:

     - Group by: `Root Cause`
     - Aggregation: `Count`

  5. Run, preview, analyze results.
  6. Save report.
