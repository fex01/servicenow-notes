# Hardware Asset Management (HAM)

## TODO

- [ ]

## Resources

### Courses

- [ ] [Hardware Asset Management (HAM) Fundamentals On Demand (Washington)](https://nowlearning.servicenow.com/lxp/en/it-asset-management/hardware-asset-management-ham-fundamentals-on-demand?id=learning_course_prev&course_id=944ea00847908654db63fb25126d4320)

### Links

-

### Labs

- []

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
  - improve productivity: new hire process, asset requisition, share asset data, HW refresh
  - financial reporting: accurate and automated depreciation, accurate tax calculation, charge-back costs, project accounting
  - cost optimization: optimize contracts, standardize assets, employee separation, avoid penalities
  - decision support: asset reporting, asset dashboard, ad-hoc queries, data integration
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
