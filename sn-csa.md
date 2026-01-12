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
