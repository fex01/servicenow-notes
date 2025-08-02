# Platform Analytics

Former: Performance Analytics

## Resources

### 📘 Courses

- [x] [Platform Analytics (PA) Overview](https://learning.servicenow.com/lxp/en/now-intelligence/platform-analytics-pa-overview?id=learning_course_prev&course_id=fb9decf8932f06905402393d6cba10f6)
- [ ] [KPI Composer Overview](https://learning.servicenow.com/lxp/en/now-intelligence/kpi-composer-overview?id=learning_course_prev&course_id=1f2469534722d6d03c6f6013e16d433c)

### 📄 ServiceNow Documentation

- [KPI Composer](https://docs.servicenow.com/csh?topicname=designing-pa-solution.html&version=latest)
- [Out-of-the-box Analytics Solutions](https://docs.servicenow.com/csh?topicname=content-packs-in-form-analytics.html&version=latest)

### Apps and Plugins

- [KPI Composer Store App](https://store.servicenow.com/sn_appstore_store.do#!/store/application/62a50aba0f800010ad8350feb6767e4f/4.1.2)

## Introduction to Platform Analytics

- **Purpose & Benefits:**

  - Anticipate operational trends
  - Prioritize resources effectively
  - Drive automation and self-service
  - Support continual service improvement
  - Make confident decisions using data

- **Common Pitfalls:**

  - Measuring too many metrics without clear relevance
  - Visualizations lacking context (timeframes, targets)
  - Reliance on static metrics (PowerPoint decks, Excel sheets)
  - Overloaded dashboards without clear decision-making guidance

- **Characteristics of Effective Analytics:**

  - Clear connection between metrics and stakeholder goals
  - Action-oriented indicators prompting immediate improvement
  - Analytics embedded directly in workflows/processes
  - Dashboards tailored specifically to target audience needs

- **Examples of Provided Dashboards:**
  - **Incident Analytics:** Incident volume, resolution rates, state, priority
  - **Virtual Agent Analytics:** Conversation statuses, topics, durations, users
  - **Vulnerability Analytics:** Executive summary of vulnerabilities for quick identification
  - **HR Case Analytics:** Performance metrics, accountability, progress of HR cases

### Stakeholders and Personas

- **Executives:** High-level governance metrics, strategic overviews
- **Service Owners:** Insights on service quality and costs
- **Front-line Workers:** Immediate, targeted data for quick operational decisions
- **End Users:** Request and service status updates

> **Reminder:** Always design KPIs and dashboards with your specific stakeholders in mind.

See [Visualize](#visualize) to align dashboards to stakeholder personas.

### Indicator vs. Direct Table Query

- **Analytics Trend (Indicator-based):**

  - Tracks process evolution over time
  - Enables performance visualization against defined targets
  - Provides actionable notifications and trend forecasting
  - Supports correlation of multiple processes for deeper insights
  - _Example_: Percentage of critical incidents not worked in the last 24 hours

- **Direct Table Queries:**
  - Provide snapshots of data at a single point in time
  - Useful when historical trends aren't required
  - Deliver immediate, real-time summaries
  - _Example_: Current open incidents or incidents resolved in the past week

> **Insight:** Choose analytics type based on whether you require immediate snapshots (table queries) or historical insights (indicators).

### Architecture and Components

- **Platform Analytics Data Flow:**

  1. **Generate Business Process Data:** Daily activities populate process tables (e.g., new incident records).
  2. **Scheduled Data Collection:** Jobs regularly capture snapshots from tables.
  3. **Store Data in Scores Tables:**
     - `[pa_scores_l1]`: Indicator scores
     - `[pa_scores_l2]`: Breakdown indicator scores
     - `[pa_snapshots]`: References to actual records
  4. **Explore KPI & Visualizations:** Scores become available post-collection; visualized as charts or single scores.
  5. **Visualize in Dashboards:** Multiple visualizations consolidated into dashboards.

- **Key Analytics Components:**
  - **Indicators (KPIs):** Measurable data points used to assess performance.
    - Example: Number of open incidents.
  - **KPI Details:** Exploratory view offering deep insights into indicators (trends, predictions, breakdowns).
    - Example: Percentage of incidents resolved by the first assigned group.
  - **Breakdowns:** Group indicators by qualitative attributes (priority, category).
    - Example: Incident priority trends displayed separately (Low, Moderate, High, Critical).
  - **Data Collector:** Runs scheduled collections and stores snapshots.
    - Example: `[PA Incident] Daily Data Collection` job.
  - **Data Visualization:** Reusable representations of indicators (single values, trends).
    - Example: Time series trend for Number of Open Incidents.
  - **Next Experience Dashboards:** Collections of visualizations targeting specific audiences and processes.
    - Example: Incident Management dashboard summarizing overall process health.

## Implementation Plan

### Plan

- Define organizational objectives clearly and ensure stakeholder alignment.
- Identify critical processes impacting desired business outcomes.
- Determine key metrics representing process performance; focus on actionable metrics.
- **Key insight:** Ensure stakeholder alignment early to support your strategy.
- Document and distinguish:
  - **Leading indicators** (inputs; behavior-focused, easier to influence)
  - **Lagging indicators** (outputs; outcome-focused, easier to measure but harder to influence)
- Example KPIs:
  - _Leading_: Exercise (calories burnt), Diet (calories consumed)
  - _Lagging_: Weight
- Use KPI Composer (free store app) to visually map objectives and outcomes to KPIs:
  - [KPI Composer Store App](https://store.servicenow.com/sn_appstore_store.do#!/store/application/62a50aba0f800010ad8350feb6767e4f/4.1.2)
  - Course: [KPI Composer Overview](https://learning.servicenow.com/lxp/en/now-intelligence/kpi-composer-overview?id=learning_course_prev&course_id=1f2469534722d6d03c6f6013e16d433c)
  - Docs: [KPI Composer](https://docs.servicenow.com/csh?topicname=designing-pa-solution.html&version=latest)

### Leverage

- Utilize pre-packaged Analytics Solutions (Content Packs) to quickly start analytics.
- Content Packs include KPIs, Data Visualizations, Dashboards, and related objects.
- Steps to leverage best practice content:
  1. **Find Solution**
     - Browse available Content Packs via: `https://<instance>.service-now.com/nav_to.do?uri=%2F$allappsmgmt.do`
     - Search for "Content Pack".
  2. **Review Solution**
     - Evaluate descriptions and subscription details within selected Content Pack.
  3. **Install Solution**
     - Activate appropriate Performance Analytics Content Pack plugin (e.g., Incident SLA Management).
- Documentation: [Out-of-the-box Analytics Solutions](https://docs.servicenow.com/csh?topicname=content-packs-in-form-analytics.html&version=latest)

### Configure

- Ensure proper execution of **Data Collection jobs** to populate dashboards.
- Key components:
  - **Indicator Sources**: Define subsets of data (e.g., Changes with State = Open).
  - **Indicators**: Calculate specific metrics (e.g., % of Urgent Changes).
  - **Collection Jobs**: Scheduled jobs capturing process data regularly.
  - **Data Visualizations**: Reusable indicator views placed onto dashboards.
- Configuration steps:
  1. **Verify Sources**
     - Confirm Indicator Sources reference correct fields.
     - Validate fields for `<Application>.New`, `<Application>.Open`, and `<Application>.Closed` Indicator Sources.
  2. **Run Historic Collection**
     - Execute once initially to populate historical metrics (default: last 60 days).
     - Adjust timeframe if more historical data is needed.
     - Note: Historic collections might not accurately reflect Breakdown trends.
  3. **Activate Daily Collection**
     - Schedule daily collection for accurate, ongoing trend data.
- Verify collection job completion via: _All > Platform Analytics Administration > Data Collector > Job Logs_

### Visualize

- Display metrics effectively using [Next Experience Dashboards](#next-experience-dashboards) tailored to stakeholders.
- Dashboard best practices:
  - Begin with out-of-the-box dashboards, then customize incrementally.
  - Collaborate with stakeholders (Executives, Service Owners, Workers) to build role-specific dashboards.
  - Regularly review dashboard usage; ensure stakeholder needs are continuously met.
- Dashboard examples tailored by stakeholder roles:
  - **Executive**: Overview of critical business KPIs aligned with corporate objectives.
  - **Manager/Service Owner**: Status of managed services and team direction insights.
  - **Front-line Worker/Agent**: Clarity on workloads and immediate tasks.
  - **End User/Customer**: Status of requests, approvals, incidents, and HR cases.
- Continuously refine and optimize dashboards for continual service improvement.
- **Key insight:** Dashboards should clearly tell the story and prompt action.

## Performance Analysis

### KPI Details

- Provides detailed insights into indicator performance data through:
  - **Score Trend:** Historical view of indicator performance.
  - **Target:** Defines desired performance goals.
  - **Thresholds:** Generates alerts upon reaching defined points.
  - **Forecast:** Anticipates future trends based on past data.
- Use **Compare tab** to analyze differences between scores and associated records across two dates.
- For configuration details, see [Configure](#configure) under **Implementation Plan**.

### Next Experience Dashboards

- Reusable canvas containing visualizations, filters, and UI components.
- Access and permissions:
  - **All platform users:** Can view dashboards shared with them.
  - **Users with any role:**
    - Create dashboards, add content, share owned dashboards, delete own dashboards.
  - **Users without roles:**
    - Can only view dashboards shared with them; no create/edit permissions.
  - **pa_admin and pa_power_user roles:**
    - Edit content, manage dashboard access, update properties on dashboards they can edit.
    - Only delete dashboards they own.
  - **dashboard_admin role:**
    - Edit and manage content, users, groups, and roles for any dashboard.
- Dashboards can include filters by configuring a **Breakdown Source**, applying the selected element as a filter across all dashboard visualizations.
