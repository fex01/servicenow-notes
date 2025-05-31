# Reports

## TODO

-

## Resources

### 📘 Courses

- [ ] [Get Started with Reports](https://nowlearning.servicenow.com/lxp/en/now-intelligence/get-started-with-reports?id=learning_course_prev&course_id=8f92fd1d93763994fb94b4886cba10d9)

### 📄 ServiceNow Documentation

-

### 🧠 Community

-

### 📚 Standards

-

## Content

## Report Fundamentals

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

  - **Single Score** - Example: Total incidents overdue.
  - **Pie Chart** - Example: Incidents by state
  - **Time Series (Area Chart)** - Example: Incident volume over time.
  - **Heatmap** - Example: Incidents by priority and state.

- Dashboards can be viewed by any user if shared.

### Personas & Roles

- **Roles**
  - `report_user`
    - can use a Report Source
    - can create reports
  - `report_admin role`
    - everything report_user
    - can create Report Sources

---

### Report Designer

- Guided, step-by-step report creation tool.
- Navigation: _All > Reports > Create New_
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

  - **Dates**: Keywords (today, yesterday, last, this, next, day(s)**,** week(s)**,** quarter(s), or year(s))

    - e.g., "incidents updated last week"

  - **Specify Type**: Force visualization type ("as list", "as bar chart", "as pie chart")

    - e.g., "problems by priority as pie chart"

- Requires activation of Natural Language Query (NLQ) feature by System Administrator.

---

### Report Sources

- Defines data origin for reports (table + conditions).
- Three report source types:

- Table (Most Common)

- Select non-system tables directly.
- Users require table ACL permissions.

- Data Source

  - Predefined reusable filter conditions.
  - Created by Report Administrators (`report_admin` role).
  - Example steps:

    - Choose existing Data Source (e.g., Incidents.Open: Active=true).
    - Create new Data Source via UI Action:

      1. Define filter (e.g., Priority = High/Critical).
      2. Save as new Data Source.

    - Leverage existing Data Source directly in reports.

- External Data Import

  - Import Excel data into temporary ServiceNow table.
  - Import file requirements:

    - First row: Column names.
    - Max size: 2 MB; max columns: 25.
    - Expiration & visibility required.

  - Expiration options: 1-2 weeks, 1-3-6 months, 1 year.
  - Visibility options: Only me, Everyone, specific Users/Groups/Roles.
  - Reports automatically deleted post-expiration.

## Labs

### Lab 1.1: List Report

**Goal:** Create and verify a list report using Report Designer and Analytics Q\&A.

- **Section A:** Create List report using Report Designer:

  1. Navigate to **Reports > Create New**.
  2. Data Tab: Define report
     - Name: `Active Incidents by State`
     - Table: `Incident`
     - Condition: Active=True
  3. Type Tab: Choose List.
  4. Configure Tab: Group by State.
  5. Style Tab:
     - Show chart title: `Report only`
     - Chart title: `Active Incident by State`
     - Size of the chart title: `20` px
     - Chart title color: `Green`
     - Title horizontal alignment: `Left`
  6. Run and preview.
  7. Save

- **Section B:** Create List report using Analytics Q\&A:

  1. Navigate to **Reports > Create New**.
  2. Type natural query: `Active Incidents by State as list`
  3. click `Ask` to generate the report
  4. Run and confirm matching results.
  5. Save

### Lab 1.2: Report Sources

**Goal:** Create reports using existing and newly defined data sources.

- **Section A:** Use existing data source:

  1. Navigate to **Reports > Create New**.
  2. Data Tab: Define report

     - Name: `All Open Incidents`
     - Source type: `Data source`
     - Data source: `Incidents.Open (Incident)`

  3. Run and preview.
  4. Save

- **Section B:** Create new Data Source:

  1. Navigate to **Reports > Administration > Report Sources**.
  2. _New_
  3. Define properties:

     - Name: `Open Incidents–High and Critical Priority`
     - Table: `Incident [incident]`
     - Conditions: Active=True, Priority=`High/Critical`

  4. Submit

- **Section C:** Leverage new Data Source:

  1. Create report: `High and Critical Open Incidents`
  2. Select new Data Source (`Open incidents-Critical and High Priority`).
  3. Run, validate, and save.

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
