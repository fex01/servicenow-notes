# CMDB

## Tag Governance

- [docs: Tag Governance](https://docs.servicenow.com/bundle/washingtondc-it-operations-management/page/product/it-operations-management/concept/tag-governance.html)
- summary (ChatGPT):
  - Tag Governance App: Identifies non-compliant cloud/on-premises resources against organizational tag policies.
  - Tags: Key-value pairs used to categorize assets for better visibility into cloud usage and costs.
  - Discovery Features:
    - Collects cloud tags for VMs and saves them in the Key Value table.
    - Supports major cloud providers (AWS, Azure, GCP) and container ecosystems.
  - Tagging Policies:
    - Establish policies based on organizational needs (e.g., finance, IT security).
    - Consider user access levels and real-time checks for effective management.
  - Dashboard Functions:
    - Monitor compliance with tag policies.
    - Identify non-compliant CIs and use remediation flows for bulk updates.
  - Policy Types for Auditing:
    - Tag Count: Checks specified tag key counts.
    - Tag Presence: Verifies presence of specified tag key values.
    - Tag Key & Value: Confirms presence of specific key-value pairs.
  - Auto-Remediation: Automates tagging of cloud resources using AWS permissions.
  - Requirements: ITOM Visibility entitlements needed for remediation tasks.

## Change Management

- [CMDB - Process Guide](https://nowlearning.servicenow.com/nowcreate/en/pages/assets?id=nc_asset&nc_ai_search=true&sys_id=8efe3ca0db289c1077c0ce46b99619ef&table=x_snc_accel_asset&asset_id=31ac790b474112504f97dc84f16d438b&searchTerm=CMDB%20-%20Process%20Guide)
  - chapter Data Maintenance/Update and Maintenance
    - Configuration Control: ensures only authorized and identifiable CIs are added to the CMDB
      - governs updates to the CMDB
      - forward unauthorized changes to Change Management
      - discrepancies and errors are to be forwarded to the CI Owner for resolution
    - change management for any CI updates
      - configuration manager receives change request to update existing CI
      - authorized changes are prioritized and forwarded to CMDB Admin
      - rejected changes are returned to requestor with an explanation
      - for changes to CIs / new CIs discovered with Discovery and other tools, verify that an authorized change request exists
        - alternative: trigger discovery for associated CI during change implementation / review to update the CMDB in accordance with the change
    - managing proposed changes
      - feature to pre-configure changes to configuration items and their associated relationships
      - do not happen until applied
      - can be displayed on the CI record
      - use to approve changes:
        - if approved, all proposals can be applied with a quick command
        - if rejected, no changes have to be rolled back
      - options:
        - modify any field on the CI form
        - add or delete CI relationships
      - [docs: Managing proposed changes](https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/configuration-management/concept/c_ProposedChanges.html)
- [Maintain a healthy CMDB](https://nowlearning.servicenow.com/nowcreate/en/pages/assets?id=nc_asset&nc_ai_search=true&sys_id=4450f8c0c32746501ac0f60f05013152&table=x_snc_accel_asset&asset_id=70e2839cc3601ed05922751ce001313e&searchTerm=Configuration%20Control)
  - chapter Manage and control change
    - Use ServiceNow Change Management to handle change requests – And use the Proposed Change function for updates of non-discoverable, manually-entered data.
    - Make sure that changes are reviewed and approved before they’re made
    - Use the Identification and Reconciliation Engine (IRE) to import new data in your CMDB –IRE
    processes help maintain data integrity in the CMDB, preventing duplicate CIs by uniquely
    identifying CIs and CI attributes by allowing only authoritative data sources to write to CMDB.
    - Configure permissions so that only authorized users can make changes to your CMDB
    - Communicate changes to stakeholders

## Access Control Options

- alternative: activate auditing for CMDB tables
  - [community: How to Enable Audit History for CI and Asset Tables](https://www.servicenow.com/community/cmdb-forum/how-to-enable-audit-history-for-ci-and-asset-tables/m-p/2842781)
    - All > System Definition -> Dictionary
      - open table record and set Audit to true
      - can have performance impact, configure data cleanups
- check: have ITIL user CMDB write permissions
  - yes: [sn_cmdb_editor]
  - [itil_admin] contains [sn_cmdb_admin]
- not in scope: admin, security_admin
- light restrictions:
  - ensure that roles [sn_cmdb_editor] and [sn_cmdb_admin] are only assigned to Configuration Manager, CMDB Admin, and Class Owners
  - ensure that no other roles have write access to the CMDB
    - if [itil] loses [sn_cmdb_editor], it has to be assigned on Class Owner level
  - no further restrictions
- heavy restrictions:
  - write
    - Configuration Manager, CMDB Admin with role [sn_cmdb_admin]: full access
    - Class Owners: restrict to respective CI Classes / CI Groups
    - Technical Service Offerings for Application Services Managed by Group: down to Application level
    - Technical Service Offerings for Infrastructure (Dynamic CI Groups) Managed by Groups: all CIs in Dynamic CI Group
    - discovery source service accounts: restrict to CI Classes according to Reconciliation Rules
  - Services CIs restricted according to service roles: [service_author], [service_admin], [service_editor]
  - erweitert: Schreibschutz auf spezifischen Feldern möglich
  - sensitive tables:
    - [cmdb_ci_config_file_tracked]

## Workshop Topics

### Themenliste

- Business goals and Use Cases
  - ITOM Starter Package_SN_v003.pptx, s13,
  - CMDB - PreWorkshop Readiness Kickoff.pptx, s12-14
- Begriffsklärung
  - Configuration Management
    - CMDB - PreWorkshop Readiness Kickoff.pptx, s13
  - CMDB
    - CMDB - PreWorkshop Readiness Kickoff.pptx, s14
    - ITOM Starter Package_SN_v003.pptx, s17
      - inkl. Ziele Configuration Management
  - Discovery
    - ITOM Starter Package_SN_v003.pptx, s32
  - CI
    - CMDB - Project Workshop.pptx, s40
  - Asset vs CI
    - ITOM Starter Package_SN_v003.pptx, s18, s76
    - CMDB - Project Workshop.pptx, s41-42
    - Starterpaket ITOM/01 Input/CMDB v0.1.pptx, s37-40, s67
  - Key Concepts
    - ITOM Starter Package_SN_v003.pptx, s73
    - CMDB - Project Workshop.pptx, s44
- ServiceNow Application Interactions
  - CMDB - PreWorkshop Readiness Kickoff.pptx, s15
  - ITOM Starter Package_SN_v003.pptx, s19
    - Interaktionen ITSM Prozesse
- Design CMDB Data Model
  - CMDB - PreWorkshop Readiness Kickoff.pptx, s19
  - CMDB - Project Workshop.pptx, s30-35
    - incl. CSDM
  - ITOM Starter Package_SN_v003.pptx, s20-21
    - only CSDM
- Configuration Management Prozess
  - ITOM Starter Package_SN_v003.pptx, s22-23
  - Operationalize CMDB
    - CMDB - PreWorkshop Readiness Kickoff.pptx, s20
    - CMDB - Project Workshop.pptx, s36
- Personas and Roles
  - ITOM Starter Package_SN_v003.pptx, s26, s60
  - CMDB - PreWorkshop Readiness Kickoff.pptx, s24-29
  - CMDB - Project Workshop.pptx, s25-29
- Populating the CMDB
  - ITOM Starter Package_SN_v003.pptx, s34
    - Typical CIs for Crawl Phase Discovery s41
  - CMDB - PreWorkshop Readiness Kickoff.pptx, s29-30
- Implementation and Maintenance Plan – High Level
  - ITOM Starter Package_SN_v003.pptx, s33
- MID server implementation
  - ITOM Starter Package_SN_v003.pptx, s52-58
    Starterpaket ITOM/ITOM_MID_Server Konfig.pptx, 29 slides
- Final Slides
  - Links to Resources
    - CMDB - PreWorkshop Readiness Kickoff.pptx, s32

### Steps

- according to `CMDB - Project Workshop.pptx`
  - 1. Set your direction - s12ff, Business goals and use cases
    - Plan your successful CMDB deployment.pdf, p5-6
  - 2. Build a team - s25ff, Personas and Roles
  - 3. Design Data Model - s30ff
  - 4. Operationalize and Maintain the CMDB - s36
- further slidedeck structure
  - 5. CMDB definitions and concepts - s37ff
  - 6. ServiceNow CMDB Basics
    - s44 Key Concepts
    - s45-46 Data Tables
      - ITOM Starter Package_SN_v003.pptx, s72
    - s47-52 Class Structure
      - Crawl CIs also in ITOM...: s24, s41
    - s53-58 CI Attributes
      - CI Groups also in ITOM...: s74
      - CI Record Form also in ITOM...: s44
    - s59-68 Product Models and CSDM
    - s69-76 Lifecycle Stage/Status
    - s77-80 CI Groups
      - CI Groups also in ITOM...: s74
    - s81-87 Dynamic CI Groups
      - Verantwortlichkeiten CI Klassen (TS, TSO), Starterpaket ITOM/01 Input/CMDB v0.1.pptx, s55
  - 7. Populating the CMDB - s88-94
    - s95-112 Identification and Reconciliation
      - Discovery and IRE Engine Process Flow also in ITOM...: s104
    - s113-120 CMDB 360
  - 8. Manage - Data Management and CMDB Health - s120ff
    - s121-136 Data Manager
    - s137-157 CMDB Health
    - s158-174 CMDB Management
  - 9. Decisions - s175
    - also Itom...: s45-48
    - s179-180 CMDB Story Themes
  - 10. Additional Resources - s181
    - s182 links
    - s183 plugins
      - ITOM..., s6
    - 185 Next steps


- Agenda
  - first draft:
    - 1 CMDB
      - 1.1 CMDB Einführung
      - 1.2 Strategie
        - Ziele 
        - CMDB Team 
        - Data Model
        - Operation & Management
      - 1.3 CMDB Konzepte
      - 1.4 CMDB Grundlagen
      - 1.5 CMDB Datenimport
      - 1.6 CMDB Pflege
      - 1.7 Entscheidungen
    - 2 Discovery
    - 3 Asset Management
  - second try
    - Ziele
    - Einführung und Begriffsklärung
    - Grundlagen CSDM
    - Grundlagen CMDB Health
    - CMDB Use Cases, Datenmodell und CI-Quellen
    - CMDB Discovery - Grundlagen und Zulieferleistungen
    - CMDB Rollen und Verantwortlichkeiten
    - Config Management Prozess / Pflegeprozesse
