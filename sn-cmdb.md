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
