# Reports

## Resources

### 📘 Courses

- [ ] [Get Started with Reports](https://nowlearning.servicenow.com/lxp/en/now-intelligence/get-started-with-reports?id=learning_course_prev&course_id=8f92fd1d93763994fb94b4886cba10d9)

### 📄 ServiceNow Documentation

- [Reporting](https://docs.servicenow.com/csh?topicname=reporting-landing-page&version=latest)

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

## Report Types

### Summary Reports - Bars and Columns

- **Purpose:** Compare grouped records visually.
- **Use Cases:** Assignment load by assignee, incidents by priority.
- **Key features:**
  - **Group by:** Categorize records by primary attribute.
  - **Stack by:** Further categorizes data within each bar.
    - Using both Stack by and Group by categorizes data by two attributes simultaneously.
  - **Additional group by:** Enables dynamic data grouping with a dropdown to select alternative criteria.
  - **Aggregation:** Count (default), Average, Sum, Min, Max, Standard Deviation.
  - **Formatting:** Custom numerical/date labels on axes.
  - **Data table:** Optional detailed view below chart.
  - **Max number of groups:** Limits number of bars; excess data grouped as "Other" if "Show Other" is checked.
- **Quick creation methods:**
  - Analytics Q\&A: Queries like "incidents by Priority".
  - List view: Select field > Bar Chart option.

---

### Summary Reports - Pies and Scores

- **Purpose:** Visualize proportions relative to a whole.
- **Use Cases:** Incident priority distribution, changes by category.
- **Key features:**
  - **Group by / Additional group by:** Dynamic attribute comparisons.
  - **Aggregation:** Count (default), Average, Sum, Count Distinct.
  - **Single Score Reports:** Highlight critical metrics (e.g., open incidents).
    - Customizable conditions and aggregations.
- **Quick creation methods:**
  - Analytics Q\&A: Queries like "problems by Priority as pie".
  - List view: Select field > Pie Chart option.

---

### Trend Reports - Time Series

- **Purpose:** Historical trend visualization.
- **Use Cases:** Daily created incidents, monthly resolved incidents.
- **Key features:**
  - **Trend by:** Date attribute for timeline.
  - **Frequency (Per):** Daily, Weekly, Monthly.
  - **Group by:** Separate trends by additional attribute.
  - **Aggregation:** Count, Average, Sum, Standard Deviation.
  - **Visualization types:** Column, Line, Area, Spline, Step Line.
- **Quick creation methods:**
  - Analytics Q\&A: Queries like "incidents resolved monthly".

---

### Multidimensional Report Examples

- **Purpose:** Visualize data across multiple dimensions.
- **Types:**

  - **Bubble Charts:** Compare multiple dimensions visually.
  - **Heatmaps:** Matrix visualization to identify patterns quickly.
  - **Multilevel Pivot Tables:** Data breakdown by multiple attributes (e.g., incidents by impact and priority).

## Report Styling and Sharing

### Report Styling

- Styling options vary based on the selected report type (e.g., Bar, Pie, Heatmap).
- Navigate to **All > Reports > View/Run** and open a report; go to the _Style_ tab.
- **General settings**:
  - Select a color palette (e.g., range of blues, default theme).
  - Adjust chart size to better fit dashboards.
  - Enable or disable data labels to show values directly in chart elements.
- **Title settings**:
  - Title defaults to the report name; can be renamed independently.
  - Customize title font size, color, and horizontal alignment.
- **Legend settings**:
  - Configure vertical and horizontal alignment.
  - Enable legend border for visual separation.
- **Bar report styling (Configure tab)**:
  - _Stacked bars_ display multiple categories per group.
  - _Max number of groups_ limits visible categories.
  - _Show Other_ groups overflow categories into an “Other” bar.

### Distribute Reports

- Reports can be shared, scheduled, or exported for wider distribution or dashboard embedding.
- Navigate to **All > Reports > View/Run** and open a report; click the _Share_ icon to open the Sharing Panel.
- **Sharing Options:**
  - _Me_: Visible only to the creator.
  - _Everyone_: Available to all platform users.
  - _Groups and Users_: Restrict visibility to selected recipients.
- **Scheduling:**
  - Automates recurring email delivery.
  - Reports are sent as PDF or PNG snapshots.
  - Includes subject line and message body customization.
- **Add to Dashboard:**
  - Integrates a report widget into existing dashboards.
  - Users see real-time data if the report is shared with them.
- **Export to PDF:**
  - Generates a formatted PDF for offline or external use.
  - Allows orientation and delivery method configuration.
- **Publish:**
  - Generates a public shareable link.
  - ⚠️ Must enable `glide.report.published_reports.enabled` property.
  - _Unpublish_ revokes access.

### Working with Dashboards

- Dashboards consolidate multiple visual reports into a single shared view for performance monitoring.
- Navigate to **Self-Service > Dashboards** to view or create dashboards.
  - Users with any role can create dashboards using the _New_ button.
- **Adding Reports:**
  - Add existing reports from a widget selector.
  - Add from Report Designer via _Share > Add to Dashboard_.
  - Create new reports directly from dashboard widget configuration.
- **Styling and Layout:**
  - _Configuration tab_ provides layout templates.
  - Widgets can be resized and repositioned manually.
- **Sharing and Permissions:**
  - Dashboards can be shared with users, groups, or roles.
  - Permission levels:
    - **Viewer:** Can see shared dashboards; requires report access to see data.
    - **Editor:** Can edit dashboard layout; cannot share unless owner.
    - **Owner:** Full control over sharing, editing, and layout.

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

### Lab 2.1: Summary Reports – Bars and Columns

**Goal:** Create and configure a Bar report with grouping, stacking, aggregation, and formatting.

- **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: Open Incidents by Priority, Table: Incident).
  3. Type Tab: Select Bar visualization.
  4. Configure Tab: Group by Priority.
  5. Run and Save.
  6. Add Stack by Assignment Group, update title to `Open Incidents by priority and Assignment Group`
  7. Run, select Insert and Stay.
  8. Add Additional group by Impact, update title to `Open Incidents by Priority and Impact`
  9. Run, select Insert and Stay.
  10. Apply Aggregation (Average Business Duration), update title to `Avg Business duration of Incidents by Priority`
  11. Run, select Insert and Stay.
  12. Set Value Formatting to d/h/m/s and max duration to Hour.
  13. Display data table, Run and Save.

### Lab 2.2: Summary Reports – Pies and Scores

**Goal:** Create Pie and Single Score reports with enhanced grouping, aggregation, and filters.

- **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: All Problems by Priority as Pie, Table: Problem).
  3. Type Tab: Select Pie visualization.
  4. Configure Tab: Group by Priority, Run and Save.
  5. Add Additional group by Resolution Code, update title to `All Problems by Resolution code as Pie`
  6. Run, select Insert and Stay
  7. Navigate to Reports > Create New
  8. Create Single Score report (Name: Open Incidents, Table: Incident).
  9. Type Tab: Select Single Score visualization.
  10. Condition builder: Active=True, Priority=Critical.
  11. Configure Tab: Aggregate by Sum (Business Duration).
  12. Run and Save.

### Lab 2.3: Trend Reports – Time Series

**Goal:** Create various Time Series reports to analyze trends in incident creation, closure, resolution, and business duration.

- **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: Incidents Created Daily, Table: Incident).
  3. Type Tab: Select Column visualization (Time Series).
  4. Configure Tab: Trend by `Created`, frequency `date`.
  5. Run and Save.
  6. Modify report: Trend by Closed date, frequency Week, update title to `Closed Incidents Weekly`
  7. Run, select Insert and Stay
  8. Modify report: Trend by Resolved date, frequency Month, update title to `Resolved Incidents Monthly`
  9. Run, Insert.
  10. New report: Business Duration of Closed Incident, Column visualization (Time Series), Avg aggregation, Trend by Closed date, frequency Date.
  11. Run and Save.
  12. Modify report: Max aggregation, update title to `Maximum Business Duration of Closed Incidents`
  13. Run, Insert.

---

### Lab 3.1 - Report Styling

🎯 **Goal**: Use styling configurations to visually enhance reports like Pie, Heatmap, and Bar charts.

- **A. Style a Pie Chart**

  - Navigate to **All > Reports > View/Run**
  - Search for `Active Incidents by State` and open the report
  - Go to the _Type_ tab, search `Pie`, and select the Pie chart type
  - Go to the _Style_ tab
  - In the General section:
    - Set `Chart color`: Use color palette
    - Set palette: `Blues dark to light (3)`
    - Enable `Display data labels`
    - Set `Chart size`: Medium
    - Set `Decimal precision`: `2`
  - In the Title section:
    - `Show chart title`: `Report only`
    - `Chart title`: `Active Incidents by State`
    - `Size`: `26 px`
    - `Color`: `LimeGreen`
    - `Horizontal alignment`: `Center`
    - `Vertical alignment`: `Top`
  - In the Legend section:
    - Enable `Show legend`
    - Set `Horizontal alignment`: `Center`
    - Set `Vertical alignment`: `Bottom`
    - Enable `Show legend border`
    - Enable `Left align legend text`
  - Click _Run_
  - Save the report

- **B. Style a Heatmap**

  - Navigate to **All > Reports > View/Run**
  - Search for `Incident by Priority and State` and open the report
  - Go to the _Style_ tab
  - In the General section:
    - Enable `Use heatmap colors`
    - `Color for high scores`: `LimeGreen`
    - `Color for low scores`: `MidnightBlue`
    - Enable `Display data labels`
    - Set `Chart size`: `Large`
    - Set `Decimal precision`: `2`
  - In the Title section:
    - `Show chart title`: `Report only`
    - `Chart title`: `Incident Counts by Priority and State`
    - `Size`: `20 px`
    - `Color`: `DarkBlue`
    - `Horizontal alignment`: `Center`
    - `Vertical alignment`: `Top`
  - In the Legend section:
    - Enable `Show legend`
    - Set `Horizontal alignment`: `Right`
    - Set `Vertical alignment`: `Middle`
    - Enable `Show legend border`
    - Enable `Left align legend text`
  - Click _Run_
  - Save the report

- **C. Style a Bar Chart**
  - Navigate to **All > Reports > View/Run**
  - Search for `Open Incidents by Priority` and open the report
  - In the _Configure_ tab:
    - Set `Stack by`: `Category`
    - Enable `Grouped bars`
    - Disable `Display data table`
    - Disable `Show other`
  - In the _Style_ tab, General section:
    - `Chart color`: Use color palette
    - `Set palette`: `Default UI14`
    - Enable `Display data labels`
    - `Chart size`: Medium
    - `Decimal precision`: `2`
  - In the Title section:
    - `Chart title`: `Open Incidents by Priority`
    - `Size`: `20 px`
    - `Color`: `Green`
    - `Horizontal alignment`: `Center`
    - `Vertical alignment`: `Top`
  - In the Legend section:
    - Enable `Show legend`
    - `Horizontal alignment`: `Center`
    - `Vertical alignment`: `Bottom`
    - Enable `Show legend border`
    - Enable `Left align legend text`
  - In the Axis section:
    - X-axis:
      - `Title`: `Priority`
      - `Title size`: `12 px`
      - Enable `Title bold`
      - `X axis label size`: `11 px`
    - Y-axis:
      - `Title`: `Incident Count`
      - `Title size`: `12 px`
      - Enable `Title bold`
      - Enable `Display Grid`
      - `Y axis label size`: `11 px`
  - Click _Run_
  - In _Configure_ tab again:
    - Set `Stacked bars`: Enable
    - Ensure `Stack by`: `Category`
  - Click _Run_
  - Save the report

### Lab 3.2 - Distribute the Reports

🎯 **Goal**: Practice multiple options to share and distribute reports including sharing, scheduling, exporting, and publishing.

- **A. Share a Report**

  - Navigate to **All > Reports > Create New**
  - In the Data tab:
    - `Name`: `All Incidents by Location`
    - `Source type`: `Table`
    - `Table`: `Incident`
  - Go to the _Type_ tab, select `Bar` chart
  - Go to the _Configure_ tab, set `Group by`: `Location`
  - Click the _Share_ icon to open the sharing panel
  - Click _Share_ and confirm with _Save and Continue_
  - Select `Groups and Users`
  - Click _Add User_ icon
  - Add user `Don Goodliffe`
  - Click _OK_
  - Save the report
  - Impersonate `Don Goodliffe`
    - Navigate to **All > Reports > View/Run**
    - Select _Group_ section and verify report appears
  - End impersonation

- **B. Schedule a Report**

  - Navigate to **All > Reports > View/Run**
  - Open the `All Incidents by Location` report
  - From the sharing panel, click _Schedule_
  - Configure:
    - `Email`: `don.goodliffe@example.com`
    - `Subject`: `All Incidents by Location Report`
    - `Message`: `Hello Don, Here are the incident counts categorized as per different locations.`
  - Click _Submit_

- **C. Add a Report to the Dashboard**

  - Open the report and click the _Share_ icon
  - Click _Add to Dashboard_
  - Set:
    - `Dashboard`: `Incident Management`
    - `Tab`: `Incident Open`
  - Click _Add_ (not _Add here_)
  - Confirm report appears on the selected dashboard tab

- **D. Export a Report to PDF**

  - Navigate to **All > Reports > View/Run**
  - Open the `All Incidents by Location` report
  - From the sharing panel, click _Export to PDF_
  - Set:
    - `Orientation`: `Landscape`
    - `Delivery`: `Generate now`
  - Click _Export_
  - When complete, click _Download_

- **E. Publish a Report**
  - Navigate to **sys_properties.list**
  - Search for `glide.report.published_reports.enabled`
  - Set `Value`: `true`, click _Update_
  - Go to **All > Reports > View/Run**
  - Open the report
  - Click the _Share_ icon
  - Click _Publish_
  - Copy the link using _Copy report link_ icon

### Lab 3.3 - Working with Dashboards

🎯 **Goal**: Create a personal dashboard and add both existing and new reports to it for centralized visualization.

- Steps:

  - **A. Create Personal Dashboard**

    - Navigate to **Self-Service > Dashboards**
    - Click _Create a dashboard_
    - Enter `Personal Report Dashboard` in the Name field
    - Click _Submit_

  - **B. Add Existing Report from Dashboard**

    - Open `Personal Report Dashboard`
    - Click the _Edit_ icon (pencil)
    - Click _Add Widget (+)_
    - Set Widget Category to `Reports`
    - Type `Incidents by Priority` in the Filter field
    - Select the report and click _Add_
    - Verify the report appears in the dashboard layout

  - **C. Add Existing Report from Report Designer**

    - Navigate to **All > Reports > View/Run**
    - Open `Open Incidents by Priority and Impact`
    - Click _Sharing_, then click _Add to Dashboard_
    - Choose `Personal Report Dashboard` in the Dashboard field
    - Click _Add_
    - Verify the report appears in the dashboard layout

  - **D. Create and Add New Report from Dashboard**

    - Open `Personal Report Dashboard`
    - Click _Add Widget (+)_
    - Set Widget Category to `Reports`
    - Click _#New Report_, then click _Add_
    - Click _Click here to configure this reusable widget_
    - In the Report Designer:
      - Set Name: `Open Incidents by Category`
      - Table: `Incident`
      - Type: `Bar`
      - Group by: `Category`
      - Aggregation: `Count`
    - Click _Run_, then _Save_

  - **E. Share the Dashboard**

    - Click _Sharing_
    - Add yourself to the Users list
    - Select permission as `Can edit`
    - Click _Share_

  - **F. Adjust Dashboard Layout**
    - Click _Configuration_
    - Choose desired layout (e.g., Two column, equal width)
    - Drag widgets to reposition as desired
