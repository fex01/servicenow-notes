# Hardware Asset Management (HAM)

back to [Asset Management](./sn-asset.md)

## TODO

- [ ]

## Resources

### Courses

- [ ] [Hardware Asset Management (HAM) Fundamentals On Demand (Washington)](https://nowlearning.servicenow.com/lxp/en/it-asset-management/hardware-asset-management-ham-fundamentals-on-demand?id=learning_course_prev&course_id=944ea00847908654db63fb25126d4320)

### Links

-

### Labs

#### L1:Prepare the Asset Management Environment (W)

- [lab steps](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=4f92791b974a0e54524eb3cf9153af67)

##### L1: Objective

1. Validate that ITSM Asset Management and Hardware Asset Management (HAM) functionality are installed and activated.
2. Grant appropriate access to the asset manager for these applications.
3. Download supporting files for future labs.

##### L1-A: Validate Plugins

1. Log in as the System Administrator
2. Navigate to **System Definition > Plugins**. Switch to **Classic Application Manager** if prompted.
3. Verify the following plugins are installed:
   - Asset Management, Asset Management Workspace, Contract Management, Cost Management, Data Certification, Extended CMDB, Hardware Asset Management, Managed Documents, My Assets, Procurement.
   - Install and activate any missing plugins (optionally include demo data).

##### L1-B: Create a User Account

1. Navigate to **User Administration > Users** and create a new user with the following details:
   - User ID: hamm.dalorian
   - First Name: Hamm
   - Last Name: Dalorian
   - Title: Asset Manager
   - Email: `hamm.dalorian@example.com`
   - Time Zone: US/Pacific (optional).
2. Save the user record.

##### L1-C: Add User to a New Group

1. On Hamm’s user record, navigate to the **Groups** section and select **New**.
2. Create and save a group named **Asset Managers**.
3. Verify Hamm appears in the **Group Members** related list.

##### L1-D: Add Roles to the Group

1. Navigate to the **Roles** section of the **Asset Managers** group and select **Edit**.
2. Add the following roles to the group:
   - `asset`, `catalog_admin`, `discovery_admin`, `financial_mgmt_admin`, `flow_designer`, `ham_admin`, `inventory_admin`, `itil`, `procurement_user`.
3. Save the changes.

##### L1-E: Add User to Another Group

1. On Hamm’s user record, under the **Groups** section, select **Edit**.
2. Add **Field Services** to the group list.
3. Verify both **Asset Managers** and **Field Services** groups are listed.

##### L1-F: Verify Actions

1. Impersonate Hamm Dalorian through the **User Menu**.
2. Verify the following are available in the application navigator:
   - Asset Management
   - Hardware Asset Dashboard
   - Hardware Model Normalization.
3. End impersonation.

##### L1-G: Download Supporting Files

1. Navigate to **Self-Service > Knowledge** as the System Administrator.
2. Open the **Class knowledge base** and download the SupportingFiles.zip.
3. Save and unzip the file in an easily accessible location.

## Topics

### Introduction

- separately licensed Hardware Asset Management (HAM)
- differentiation
  - **Asset**:
    - tracked throughout its life for financial, contractual, and lifecycle data
    - procurement, receiving, maintenance, or retirement
    - track inventory
    - manage associated license, warranty, lease, or maintenance contracts
    - track monetary value or incurred costs
    - document the service status, end-of-life, and/or decommission
    - who is using it and/or how often it is being used
    - examples: HW, SW Licenses, Data, Buildings
  - **IT Asset**: technology component managed throughout its lifecycle for value, cost, contractual compliance, and usage
    - created or acquired, used to support business activities, managed financially and operationally, and then retired or expired at the end of their useful life
    - records stored in an asset repository and include all relevant data, such as asset tag, model category, model, depreciation
    - examples: SW Entitlement, router, server, switch
  - **CI**: track operational and relationship information
    - may have financial values assigned to it; however
    - does not have any depreciation linked to it
    - stored in the CMDB
    - purpose:
      - monitor and track its technical specifications
      - associated with an Incident, Problem, or Change record
      - relationship to other items
    - examples: servers, routers, switches, websites, storage devices
  - **Asset vs CI**:
    - overlap: Servers, Workstations / desktops, Enterprise network HW / appliances, SAN enterprise & local storage devices
    - organization may decide to track a component as just an asset, just a CI, or as both
- risks without HAM: wasted resources, limited visibility, inaccurate inventory, lack of accountability, and fulfillment or service delays
- HAM purpose: **mitigate risk** and **optimize cost**
  - What hardware assets do you have?
  - Where are they?
  - Who uses them?
  - How are they used?
  - How are they configured?
  - What do they cost?
  - What value to they deliver?
- HAM definition: stewardship of IT assets from planning through sunset
  - also:
    - set of business practices that joins financial, contractual, procurement, and inventory functions to support the lifecycle management and strategic decision-making for assets in an IT environment
    - Visibility to what you have, where it is, and how much it costs
- encompasses:
  - people:
    - Defined authority for controlling IT assets
    - Roadmap for growing and improving IT asset management
    - Dedicated resources responsible for managing IT assets
    - Stakeholders that champion IT asset management throughout the organization
  - process:
    - Well-defined and -adopted IT asset management processes
    - Clear and controlled integration with other processes, such as incident management, change management, contract management, procurement, and others as required
  - technology:
    - IT asset tracking and management software that brings together, inventory and installations, to provide a clear compliance and financial position
    - Automation applications for discovering, managing, inventorying, and retiring IT assets
    - An easy method, such as a service catalog, for the requesting of IT assets
    - Integrations with the applications used to support defined process integrations (e.g., integration with purchasing system)
- ITSM: configuration and delivery of IT services to users
- Goals of IT asset management (ITAM)
  - **improve productivity**: new hire process, asset requisition, share asset data, HW refresh
  - **financial reporting**: accurate and automated depreciation, accurate tax calculation, charge-back costs, project accounting
  - **cost optimization**: optimize contracts, standardize assets, employee separation, avoid penalities
  - **decision support**: asset reporting, asset dashboard, ad-hoc queries, data integration
- IT HW Asset Lifecycle
  - 1. Request: LC begins with a plan or a request - someone needs an asset to achieve a goal
  - 2. Procure: fulfillment by existing stock or through procurement from a vendor
  - 3. Receive: process
  - 4. Stock: process
  - operational phase:
    - 5. Deploy
    - 6. Monitor
    - 7. Support
    - 8. MAC: Move, add, and change
  - 9. Dispose
- Manage the Lifecycle
  - IT Financial Management
    - Fulfillment
    - Auditing
    - Active Asset Management
    - Disposition
  - Governance

![IT HW Asset Lifecycle](./attachments/sn-asset-ham-lifecycle.png)

### Requirements and Recommended Practices

- ISO 19770-1 IT Asset Management process standard: Capability Blueprint
  - Trustworthy Data: Know what you have so you can manage your assets.
  - Practical Management: Improve management controls and drive immediate benefits.
  - Operational Integration: Improve efficiency and effectiveness through integration with other areas, such as request, procurement, and IT Service Management.
  - Strategic Conformance: Achieve best in-class.
  - ![Capability Blueprint](./attachments/iso19770-1-capability-blueprint.png) ￼
- Phased Approach: **IT Asset Management Disciplines**
  - Inventory management
    - Access stock information
    - Create and manage stock information
    - Edit stock rules, stockrooms, and stockroom types
  - Financial management
    - Manage fixed assets, depreciation, and distribution costs
    - Work with expense lines and rate cards
    - Handle expense allocations
  - Contract management: Create, edit, renew/extend, and deactivate/delete contracts
  - Model management
    - Manage models and their critical processes that ensure good data for procurement and finance
    - Manage model categories
  - Vendor management
    - Manage vendor costs
    - Manage vendor SLAs
    - Manage related contracts
  - Hardware asset management
    - All of the items above, plus
    - Manage hardware and consumable assets

### Hardware Asset Management Implementation

#### ServiceNow IT Asset Management Products

1. **ITSM Asset Management Foundation Plugin**:
   - Provides the baseline for managing IT assets (hardware, software, and contracts).
   - Enables:
     - Inventory control.
     - Cost reduction for purchasing and managing assets.
     - Full asset lifecycle management from planning to disposal.
     - Compliance with standards and regulations.
     - Improved IT service delivery to end-users.
     - Establishing asset management standards and processes.
     - Mobile Asset Receiving & My Assets
2. **Hardware Asset Management (HAM)**:
   - Expands upon ITSM Asset Management with advanced automation and lifecycle insights.
   - Key Features:
     - **Hardware Model Normalization**: Normalizes asset models with a content library, lifecycle data, and HAM resource categories.
     - **Asset Lifecycle Automation**:
       - Automated flows: Asset order, disposal, stock orders, asset refresh, RMA, and more.
       - Tasks: Deploy, swap, retire assets.
     - **Asset Inventory Audit (Mobile)**: Supports mobile audits, disposal scanning, and remote receiving.
     - **Hardware Asset Manager Dashboard**: Centralized view for managing hardware assets.
   - Automates full asset lifecycle from procurement to disposal with enhanced CMDB integration.
   - Requires a separate license and activation by ServiceNow.
3. **Software Asset Management (SAM) Professional**:
   - Tracks and manages software licenses, compliance, and optimization.
   - Key Capabilities:
     - Reclaims unused software rights.
     - Manages allocations and purchases for software entitlements.
   - Requires a separate subscription
   - [SAM notes](./sn-asset-sam.md)

#### Differences Between HAM and ITSM Asset Management

- HAM enhances ITSM Asset Management in four key areas:
  1. **Hardware Model Normalization**.
  2. **Asset Lifecycle Automation**.
  3. **Asset Inventory Audit (Mobile)**.
  4. **Hardware Asset Manager Dashboard**.
- While ITSM Asset Management provides foundational capabilities, HAM focuses on automation, advanced workflows, and integration for hardware assets.

#### HAM Benefits

- **Comprehensive Lifecycle Management**:
  - Covers pre-production planning to post-production retirement.
  - Tracks financial, contractual, and inventory details.
- **Integrated with CMDB**:
  - Eliminates challenges like data integration and normalization.
  - Offers a unified platform for IT and asset management.

#### Required Plugins for Hardware Asset Management

**Active by Default**:

1. **ITSM Asset Management** (`com.snc.asset_management`)
   - Part of the ITSM Asset Application.
   - Active by default on ITSM and CSM instances upon activation.
2. **Contract Management**
3. **Depreciation**
4. **Expense Line**
5. **Fixed Asset**
6. **My Assets**

**Inactive by Default**:

1. **Hardware Asset Management** (sn_hamp)
   - Available via the ServiceNow Store.
   - Includes **Hardware Model Normalization** and **Normalization Data Services Client** plugins.
2. **Cost Management** (com.snc.cost_management)
3. **Data Certification**
   - plugin does not exist on Xanadu
   - exists on Vancouver
4. **Managed Documents** (com.snc.document_management)
5. **Procurement** (com.snc.procurement)

**Optional Plugins**:

Might require additional subscriptions:

1. **ITSM Software Asset Management Foundation**
2. **Software Asset Management (SAM) Professional**
3. **Governance, Risk, and Compliance (GRC)**
4. **Vendor Performance**
5. **Field Service Management**
6. **Performance Analytics**

### Hardware Asset Management (HAM) Plugin Installation

1. **Obtain License**:
   - Acquire a HAM license from the **ServiceNow Store**.
   - Ensure your instance is running **Paris or later**.
2. **Install HAM**:
   - Navigate to: **System Applications > All Available Applications > All**.
   - Search for **Hardware Asset Management** (`sn_hamp`).
3. **Role Requirement**:
   - Assign the **ham_admin** role for installation and configuration.

HAM updates are released on the **ServiceNow Store** independently of major product releases.
Check also [Lab 1](#l1-a-validate-plugins) for plugin validation.

#### Asset Management Modules

1. **Default ITSM Asset Management Modules**:
   - **Asset**:
     - Overview, Portfolios, All Assets, Consumables, Hardware Assets, License Assets, Other Assets, Software.
   - **Administration**:
     - Manage and configure asset-related settings.
   - **My Assets**:
     - Self-service module for end users.
2. **Additional HAM Modules (Activated with HAM Plugin)**:
   - **Asset**:
     - Hardware Asset Dashboard, Hardware Asset Workspace, Asset Tasks.
   - **Hardware Model Normalization**:
     - Overview.
   - **Loaner Management**:
     - All Loaner Asset Orders, Waitlisted Orders.
   - **Disposal Orders**:
     - Create Disposal Order, Disposal Orders.
   - **Return Merchandise Authorization (RMA)**:
     - All RMA Requests, RMA Line Items.
   - **Asset Audits**

#### Asset Management Process Relationships

- **Request/Catalog Management**:
  - Asset Output: Hardware and consumable models published in the Service Catalog.
- **Content Library Curation**:
  - Asset Output: Details from Discovery models and/or manufacturer lifecycle information that are not in the Central Software Library
- **Contract Management**:
  - Asset Input: Contract expiration dates, costs, terms, and conditions.
- **Procurement Management**:
  - Asset Input: Purchase order details from procurement systems.
- **Change Management**:
  - Asset Input: Hardware details for models or CIs supporting business services.
  - Asset Output: Cost allocation and assignment details.
- **Application Portfolio Management**:
  - Asset Input: Hardware lifecycle and model information tied to applications.
  - Asset Output: Hardware lifecycle data to support business applications.

#### Personas, Roles, and Groups

1. **Personas**:
   - **Process Owner**: Defines and oversees process.
   - **Asset Manager**: Handles operations, administration, and finances.
     - role: ham_admin - includes inventory_admin, asset, procurement_user
   - **Asset Administrator**: Performs procurement and inventory activities.
   - **System Administrator**: Maintains asset data and integrations.
   - **Configuration Manager**: Manages CI classes and health guidelines.
   - **Other Personas**: IT Finance Manager, IT Procurement Manager, IT Contract Manager, IT Vendor Manager.
2. **Roles**:
   - **asset**: Manages assets and records.
   - **catalog_admin**: Manages the service catalog.
   - **discovery_admin**: Configures and executes Discovery.
   - **flow_operator**: Views flow execution details and logs.
   - **ham_admin**: Manages HAM advanced features (requires HAM plugin).
   - **inventory_admin**: Manages stockrooms, rules, and stock information.
   - **itil**: Handles incident, problem, and change management tasks.
   - **procurement_user**: Manages purchase orders and transfer orders.

### Trustworthy Data

areas of interests:

- data dependability
- data consistency
- data accuracy
- data reliability
- data validation
- data credibility
- data believability
- data transferability
- data usefulness
