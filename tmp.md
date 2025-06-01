# ServiceNow Reports - Report Types

## TODO

* [ ] Add content for hands-on exercises
* [ ] Add specific links and cross-references

---

## Summary Reports - Bars and Columns

* **Purpose:** Compare grouped records visually.
* **Use Cases:** Assignment load by assignee, incidents by priority.
* **Key features:**

  * **Group by:** Categorize records by primary attribute.
  * **Stack by:** Further categorizes data within each bar.

    * Using both Stack by and Group by categorizes data by two attributes simultaneously.
  * **Additional group by:** Enables dynamic data grouping with a dropdown to select alternative criteria.
  * **Aggregation:** Count (default), Average, Sum, Min, Max, Standard Deviation.
  * **Formatting:** Custom numerical/date labels on axes.
  * **Data table:** Optional detailed view below chart.
  * **Max number of groups:** Limits number of bars; excess data grouped as "Other" if "Show Other" is checked.
* **Quick creation methods:**

  * Analytics Q\&A: Queries like "incidents by Priority".
  * List view: Select field > Bar Chart option.

---

## Summary Reports - Pies and Scores

* **Purpose:** Visualize proportions relative to a whole.
* **Use Cases:** Incident priority distribution, changes by category.
* **Key features:**

  * **Group by / Additional group by:** Dynamic attribute comparisons.
  * **Aggregation:** Count (default), Average, Sum, Count Distinct.
  * **Single Score Reports:** Highlight critical metrics (e.g., open incidents).

    * Customizable conditions and aggregations.
* **Quick creation methods:**

  * Analytics Q\&A: Queries like "problems by Priority as pie".
  * List view: Select field > Pie Chart option.

---

## Trend Reports - Time Series

* **Purpose:** Historical trend visualization.
* **Use Cases:** Daily created incidents, monthly resolved incidents.
* **Key features:**

  * **Trend by:** Date attribute for timeline.
  * **Frequency (Per):** Daily, Weekly, Monthly.
  * **Group by:** Separate trends by additional attribute.
  * **Aggregation:** Count, Average, Sum, Standard Deviation.
  * **Visualization types:** Column, Line, Area, Spline, Step Line.
* **Quick creation methods:**

  * Analytics Q\&A: Queries like "incidents resolved monthly".

---

## Multidimensional Report Examples

* **Purpose:** Visualize data across multiple dimensions.
* **Types:**

  * **Bubble Charts:** Compare multiple dimensions visually.
  * **Heatmaps:** Matrix visualization to identify patterns quickly.
  * **Multilevel Pivot Tables:** Data breakdown by multiple attributes (e.g., incidents by impact and priority).

---

## Labs

### Lab 2.1: Summary Reports – Bars and Columns

**Goal:** Create and configure a Bar report with grouping, stacking, aggregation, and formatting.

* **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: Open Incidents by Priority, Table: Incident).
  3. Type Tab: Select Bar visualization.
  4. Configure Tab: Group by Priority.
  5. Run and Save.
  6. Add Stack by Assignment Group, update title.
  7. Run, Insert, and Stay.
  8. Add Additional group by Impact, update title.
  9. Apply Aggregation (Average Business Duration), update title.
  10. Set Value Formatting to d/h/m/s and max duration to Hour.
  11. Display data table, Run and Save.

### Lab 2.2: Summary Reports – Pies and Scores

**Goal:** Create Pie and Single Score reports with enhanced grouping, aggregation, and filters.

* **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: All Problems by Priority as Pie, Table: Problem).
  3. Type Tab: Select Pie visualization.
  4. Configure Tab: Group by Priority, Run and Save.
  5. Add Additional group by Resolution Code, update title.
  6. Run, Insert, and Stay.
  7. Create Single Score report (Name: Open Incidents, Table: Incident).
  8. Type Tab: Select Single Score visualization.
  9. Condition builder: Active=True, Priority=Critical.
  10. Configure Tab: Aggregate by Sum (Business Duration).
  11. Run and Save.

### Lab 2.3: Trend Reports – Time Series

**Goal:** Create various Time Series reports to analyze trends in incident creation, closure, resolution, and business duration.

* **Steps:**

  1. Navigate to Reports > Create New.
  2. Data Tab: Define report (Name: Incidents Created Daily, Table: Incident).
  3. Type Tab: Select Column visualization (Time Series).
  4. Configure Tab: Trend by Created date, frequency Date.
  5. Run and Save.
  6. Modify report: Trend by Closed date, frequency Week, update title.
  7. Run, Insert, and Stay.
  8. Modify report: Trend by Resolved date, frequency Month, update title.
  9. Run, Insert.
  10. New report: Business Duration of Closed Incidents, Avg aggregation, Trend by Closed date, frequency Date.
  11. Run and Save.
  12. Modify report: Max aggregation, update title.
  13. Run, Insert.

---
