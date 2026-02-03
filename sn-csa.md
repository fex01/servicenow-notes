# System Administration

## TODO

- [ ]

## Resources

### Courses

- [ ]

### Links

- [Shared Responsibility Model](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-shared-responsibility-model.pdf)
- [Security Center](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/security-center/concept/sec-center.html)

### Labs

- []

## Delta Content

### Xanadu

- [Delta Exam Study Guide](https://nowlearning.servicenow.com/lxp/en/credentials/certified-system-administrator-delta-exam-study-guide-vancouver?id=kb_article_view&sysparm_article=KB0012121)
- **Shared Responsibility Model**
  - **Security Roles**: Divided among the **customer**, **ServiceNow**, and the **data center provider**.
  - **Instance Accessibility**: Designed for internet access; encryption in transit is strongly advised to protect data.
  - **Customer Responsibilities**:
    - **Data Compliance**: Adhere to privacy legislation in relevant jurisdictions.
    - **Secure Configuration**: Manage authentication, authorization, data classification, data retention, and encryption.
    - **Encryption**: Not enabled by default; various encryption solutions (application-centric, column-based, full volume) are offered.
    - **Logging**: The Now Platform supports extensive auditing; customers choose the depth of logs.
- **ServiceNow Security Center**
  - **Availability**: Included with the Now Platform at no additional cost. Accessible via _All > Security Center > Admin > Security Center_.
  - **Capabilities**:
    - **Best Practices**: Guides initial security configuration and tracks Instance Security Maturity.
    - **Hardening**: Ensures security properties align with recommended values; provides compliance scoring and trends.
    - **Scanner**: Checks the instance for misconfigurations or insecure settings.
    - **Customer Actions**: Highlights areas requiring attention (e.g., deprecations) and provides workflows for changes.
    - **Learning**: Central resource hub for documentation and compliance materials.
    - **Metrics**: Monitors security KPIs to detect threats and risky behaviors.
    - **Notifications**: Configurable alerts for threshold-based security events.
- **Named Security Contacts**
  - **Importance**: Primary channel for ServiceNow to communicate critical security-related information.
  - **Recommendations**: Keep contact details current, including an individual and a distribution list.
  - **Reference**: Search “Company Key Contacts and Notifications List Overview” on Now Support to update contacts.

### Zurich

- **Delta Exam Study Guide**
  - [CSA Delta Exam Study Guide – Zurich](https://learning.servicenow.com/lxp/en/certified-system-administrator-csa-delta-exam-study-guide?id=kb_article_view&sysparm_article=KB0012121)
- **System Update Sets**
  - **Purpose**
    - Move configuration changes extending `sys_metadata` between instances
    - XML-based container of configuration deltas
  - **Captured**
    - Business Rules, Client Scripts, UI Policies/Actions
    - Script Includes, ACLs, Data Policies
    - Dictionary entries, form/layout changes
    - `sys_properties`, app menus/modules
  - **Not Captured**
    - Data records (Incidents, Tasks, CMDB)
    - Users, Groups, Roles
    - Attachments, MID Server config, runtime integration state
  - **Use Cases**
    - Feature delivery, patches, hotfixes
    - Backup, audit, rollback planning
- **Update Set Management**
  - One requirement per update set
  - One application scope per update set
  - Small, logical, cohesive sets preferred
  - Verify _Application Scope_ and _Current Update Set_ before changes
  - Do not delete update sets
  - Do not back out `Default` update set
  - Do not manually edit `update_set` field
- **Packaging & Promotion**
  - **Batching (Preferred)**: parent update set with scoped child sets
  - **Merging**: consolidate sets; higher risk if done late
  - Export → Retrieve → Preview → Commit
  - Always Preview before Commit
  - Set to `Ignore` after production commit
- **Validation & Conflict Handling**
  - Compare local vs remote update sets
  - Resolve collisions record-by-record
  - Run **Instance Scan** before _Complete_ and before Commit
- **Best Practices**
  - Short, ticket-based naming (e.g., `STRY1001-IncidentFix`)
  - Prefer fix-forward via properties/feature toggles
  - Avoid using `Default` for planned work
  - Extra review for ACLs, scripts, integrations
