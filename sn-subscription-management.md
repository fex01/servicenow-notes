# Subscription Management

## TODO

- [ ]

## Resources

### Further Courses

- [ ]

### Links

- [NpwLearning: Subscription Management Overview](https://nowlearning.servicenow.com/lxp/en/pages/learning-course?id=learning_course&course_id=a5ccc91e9387b11056aeb94c5cba106c&achievement_id=8b0e4b0c934575d0fb94b4886cba101c)

### Labs

- []

## Topics

### Subscription Management Overview

#### Key Features of Subscription Management

- **Purpose**: Application to manage ServiceNow subscription usage and optimize the number of subscriptions needed.
- **Capabilities**:
  - Allocate and monitor subscriptions.
  - Track usage and adjust allocations as needed.
  - Plan for subscription renewals.
  - Use dashboards to analyze subscription data.

#### Importance of Subscription Management

- SaaS applications like ServiceNow are licensed by subscription (e.g., ITSM, HR).
- Critical for understanding subscription usage and adoption.
- Provides visibility into ServiceNow licenses across the organization.
- **Identifies subscribed users based on group membership.**

#### Benefits of Subscription Management

- **Actionable UI**: Prioritizes key information for decision-making.
- **Accurate Entitlement Data**: Serves as a single source of truth.
- **Simplified Allocation**: Recommends groups for easier subscription management.

#### License Visibility in Non-Production Instances

- **Visibility**: Early access to subscriptions before deploying to production.
- **Transparency**: Enhanced clarity on subscription usage and entitlements.
- **Flexibility**:
  - Non-production instances remain sandbox environments.
  - Ability to activate unpurchased plugins with clear warnings.

### Installation and Usage Role Overview

- pre-installed from Washington release onwards

#### Assigning Usage Admins

- **Role Overview**:

  - Usage admins manage purchased subscription usage in production instances.
  - Responsibilities include:
    - Allocating subscriptions.
    - Monitoring usage of custom tables.
    - Updating subscriptions as needed.
  - **Receives all subscription-related notifications when enabled.**

- **Importance**:
  - Ensure at least one person in the organization has the `usage_admin` role.

### Subscription Types

1. **Capacity**:
   - **Description**: Monitors counts of transactions, records, or managed resources like devices or software.
   - **Meter Type**: Tracks measured units (e.g., transactions, devices, records, resources).
   - **Allocation Method**: Automatic; usage is calculated and displayed in the instance.
2. **Per-User**:
   - **Description**: Entitles users based on roles and access. Allocation recommendations provided.
   - **Meter Type**: Rights-based (Fulfiller, Business Stakeholder, or Application Users).
   - **Allocation Method**: Manual; allocate by assigning groups with measured roles or access rights.
3. **Unrestricted User**:
   - **Description**: Covers all active users in the **sys_user** table with `Active = true`.
   - **Meter Type**: Instance-wide active users.
   - **Allocation Method**: Automatic; all active users are included.
   - **Note**: Editing the Unrestricted Users list impacts the **sys_user** table and UU subscriptions.
   - **Reference**: [KB Article KB1116231](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1116231).
4. **Unlimited**:
   - **Description**: No user limit; all users are entitled.
   - **Meter Type**: Unlimited users (no measurement limit).
   - **Allocation Method**: Automatic.
5. **Display Only**:
   - **Description**: Displays subscription details without supporting allocation.
   - **Meter Type**: None.
   - **Allocation Method**: Not measured.

### Navigating the Subscription Management Application

- Use the **Subscription Overview dashboard** to monitor and manage subscription allocations.
- Navigate to **Subscription Management > Subscription Management** to access the Overview page.

#### Insights

- **Notifications**:
  - Highlight over-allocated subscriptions or available subscriptions to allocate.
- **Steps to Allocate a Subscription from Insights**:
  1. Go to **Subscription Management > Subscription Management**.
  2. Click the **Insights** tile.
  3. Select the subscription to allocate.
  4. Click **Allocate Subscription** or **Add group** (ServiceNow suggests relevant groups).
  5. Click **Confirm**.
- **Access Insights from a Subscription**:
  - Navigate to **Subscription Management > All Subscriptions**.
  - Select a subscription.
  - Click the **Insights** tile.

#### Issues with Custom Tables and Applications

- **Custom Applications**:
  - Non-ServiceNow applications created on the Now Platform.
  - Must be mapped to a product subscription to remain compliant.
- **Custom Tables**:
  - Non-ServiceNow tables created or installed by a customer.
  - Governed by contract terms and the [Custom Table Guide](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/legal/custom-table-guide.pdf).
  - **Exemptions**:
    - Tables extending specific ServiceNow tables (e.g., **cmdb_ci**) are exempt.
  - **Mapping Requirement**:
    - Unmapped tables are flagged as out of compliance.
    - Mapping ensures accurate tracking and avoids exceeding entitlements.
- **Steps to Map Custom Tables**:
  1. Click **Unmapped global custom tables** tile.
  2. Select tables to map (ServiceNow suggests the best subscription).
  3. Click **Map to product**.
  4. Click **Confirm**.
- **Steps to Map Custom Applications**:
  1. Click **Unmapped custom applications** tile.
  2. Select the application to map (ServiceNow suggests the best subscription).
  3. Click **Map to product**.
  4. Click **Confirm**.

#### Subscriptions Module

- Lists all purchased and allocated subscriptions.
- Accessible from:
  - **Navigation Menu**.
  - **Subscription Management Dashboard**.
- **Key Metrics**:
  - **Purchased**: Total resources available (users, transactions, subscription units, etc.).
  - **Allocated**: Subscribed users or allocated resources.
- **Color Coding**:
  - Indicates subscription allocation status.

### Subscription Management Settings

- The **Settings** module allows you to control the capacity threshold for subscription allocations in your instance.
- Accessible from:
  - **Navigation Menu**.
  - **Subscription Management Dashboard**.

#### Adjusting Subscription Thresholds

1. Navigate to **Subscription Management > Settings**.
2. Update the **Threshold for color codes** property (default is 90%).
3. Click **Save**.

- **Note**: Changing the threshold does not impact functionality. It provides usage admins a clear visual indicator of subscription allocation status.

#### Subscription Color Codes

- **Red (Over-allocated)**: Usage exceeds 100% of purchased subscriptions.
- **Green (Compliant)**: Usage is below the configured threshold.
- **Yellow (Near capacity)**: Usage is between the threshold and 100%.
- **Orange (Even)**: Allocated subscriptions equal purchased subscriptions.

### Allocating Per-User Subscriptions

- Subscriptions are allocated by assigning groups with relevant roles to subscriptions.
- Users with **admin** or **usage_admin** roles can perform this allocation.
- **Effect**: All users in the group receive a subscription, marked as **Group** under the subscribed user's source.

Steps:

1. Navigate to **All > Subscription Management > Subscription Overview**.
2. Select a **Per-User subscription** from the list.
3. Under **Subscribed groups** related list, click **Add groups**.
4. Choose the desired groups from the list.
5. Click **Save**.

Associated Roles and Role Types

- **Role Association**:
  - Subscriptions are allocated based on group roles.
  - Use the **Associated Roles** related list to view roles tied to a subscription and the applications they enable access to.
- **Role Details**:
  - A role may appear multiple times if it is associated with multiple applications (e.g., `itil` role as Fulfiller for Incident, Problem, and Change Management).
