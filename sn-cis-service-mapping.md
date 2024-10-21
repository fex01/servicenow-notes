# SNow CIS Service Mapping

Back to [SNow ITOM](./sn-itom.md)

[[toc]]

## TODO

- [ ]

## Resources

### Requirements CIS Voucher

- [ ] Service Mapping Fundamentals
- [ ] [Service Mapping Advanced Simulator](https://nowlearning.servicenow.com/lxp/en/it-operations-management/service-mapping-advanced-simulator-washington?id=learning_course_prev&course_id=e3db6a8487760a1024e0bb39dabb35b7)
- [ ] [Service Mapping Advanced](https://nowlearning.servicenow.com/lxp/en/it-operations-management/service-mapping-advanced?id=learning_course_prev&course_id=72774609c3b77d905922751ce00131d2)
  - [eBook](https://servicenow.read.inkling.com/a/b/19c4613ca7d841ee9b3cc5f1bd05302d/p/18356415fd69484b9dd3100dfd444379)
- Recommended:
  - [x] [Discovery Fundamentals](./sn-cis-discovery.md#discovery-fundamentals)
  - [ ] Event Management Fundamentals
  - [ ] ServiceNow Learning Library courses (CMDB Reconciliation, Event Management)

### Further Courses

- [ ]

### Links

- [Link Shortcut](shortcuts://run-shortcut?name=SNow%20Docs%20URL)
- [Docs](https://docs.servicenow.com/)
- [Developer](http://developer.servicenow.com/)
- [CSC (Customer Success Center)](https://www.servicenow.com/success.html)
- [Community](https://www.servicenow.com/community/)
- [YouTube](https://www.youtube.com/user/servicenowinc)
- [Center of Excellence and Innovation (CoEI)](https://www.servicenow.com/success/playbook/center-excellence-innovation-coei.html)
- Additional Resources
  - [Mainline Exam Blueprint: Certified Implementation Specialist - Service Mapping (CIS-SM)](https://nowlearning.servicenow.com/lxp/en/credentials/certified-implementation-specialist-service-mapping-mainline?id=kb_article_view&sysparm_article=KB0011558)
  - [eBook: Service Mapping Advanced](https://servicenow.read.inkling.com/a/b/19c4613ca7d841ee9b3cc5f1bd05302d/p/18356415fd69484b9dd3100dfd444379)

### Labs

#### Service Mapping Fundamentals

##### L1: Navigate Service Mapping

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=db96f12b87828e54af9f213acebb3546)
- Service Mapping and Discovery Applications
  - All > Service Mapping > Home
    - Start point for Service Mapping Discovery
    - Access Service Mapping workflow tasks
    - Progress statistics: services with errors, waiting for approval, completed
    - -> Additional Options link (below statistics, left)
    - -> Readiness Checklist (cogwheel, top right)
  - All > Service Mapping > Administration > Discovery Dashboard
  - All > Pattern Designer > Discovery Patterns
    - Pattern is responsible for identifying a specific CI Type
  - All > Service Mapping > Administration > Credentials
  - All > Service Mapping > Administration > MID Servers
  - All > Discovery > Discovery Schedules
    - Quick Discovery
  - All > Service Mapping > Administration > Discovery Schedules

##### L2.1: MID Server Validation

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=7f5f8cc9878642d052417445dabb3536)
- collect information
  - **ServiceNow Instance URL:**
    - `https://nowlearning-nlinst02158679-001.lab.service-now.com/`
  - **ServiceNow Instance Username/Password:**
    - `lab.midserver`
    - `?`
  - **Windows Server Public IP and FQDN (for RDP):**
    - `nowlearning-nlinst02158679-mid-001.lab.service-now.com`
  - **Windows Server Private IP**
    - `198.51.159.51`
  - **Windows Server Administrative Username/Password:**
    - `administrator`
    - `2MwFCKnxc6Qw`
- validate MID Server

##### L2.2: Run Horizontal Discovery

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=5920100187c642d052417445dabb3593)
- Quick Discovery
  - All > Discovery > Discovery Schedules
  - _Quick Discovery_ button
    - Target IP
    - MID Server
  - check results via _Discovery Status_ record
- Discovery Status Details
  - All > Discovery > Discovery Status
  - _Discovery Status_ record
    - _Discovery Log_ related list
    - _Devices_ related list
      - Discovered CIs with links to CI records
    - _ECC Queue_ related list
    - _Show Discovery timeline_ related link
      - select probes and sensors to see individual runtimes
- Create Credentials
  - All > Discovery > Credentials
  - create Windows Credentials matching `Windows Server Administrative Username/Password`

##### L3

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=ff10a46f87020e54af9f213acebb3545)

##### L5.1

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=908a11d2874a8e1452417445dabb3505)

##### L5.2

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=ccbfd0c5874e42d052417445dabb3582)

##### L7

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=81bb24c1878282d052417445dabb355b)

##### L9.1

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=34da985d87c6c6d052417445dabb354b)

##### L9.2

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=696f281b878e8654af9f213acebb3599)
  - [cmdb key value import file](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=9efbdc55870ac6d052417445dabb3552)

## Courses

### Service Mapping Fundamentals On Demand

- [course](https://nowlearning.servicenow.com/lxp/en/pages/learning-course?id=learning_course&course_id=8a3364af87bf71505aa9ca2d0ebb35a5&group_id=1b43ecefc33fbd14acc871f9d0013136&child_id=6f43ecefc33fbd14acc871f9d0013195&spa=1)
- Services Mapping
  - does: Map all software and hardware components associated with a service.
  - is:
    - agentless
      - service centric
      - configuration based (does not rely on network traffic)
  - top-down instead of bottom-up
  - does not map the whole inventory, but only the specific CIs supporting a given entry point
- service examples
  - Email Service - relies on: Unix Server, AD/LDAP, Storage/SAN, Network devices, ESX server
  - Internal Web Service - relies on: IIS, Windows Server, Load Balancer, MSSQL, Storage and Network
  - Database Service - relies on: Unix, ESX, Storage
  - Stock Trader Service - relies on: IIS, Windows Server, MSSQL
- ITOM Solutions
  - ITOM Visibility
    - [Discovery](./sn-cis-discovery.md)
    - [Service Mapping](./sn-cis-service-mapping.md)
  - ITOM Health
    - Event Management
    - Agent Client Collector
    - Predictive AIOps
  - ITOM Optimization
    - Cloud Provisioning & Governance
    - Site Reliability Operations
- business problem to be addressed: bridging The Gap between IT Operations managing Technology Silos and Business Users consuming software services
  - Which IT components deliver this service?
  - The fund transfer service is down. Which IT component caused it?
  - Which services are affected by this failure?
  - Will my change have a business impact? On which services?
- architecture
  - requires MID server (see [SNow MID Server](./sn-mid-server.md))
- Application Dependency Mapping (ADM)
  - Dependency View / Unified Map displays relevant dependency relationships:
    - App to Host
    - App to App
      - based on which app listens to which port on which host
      - not service aware
  - utilizes the _Application Dependency Mapping_ probe
  - Process Classifier
    - Locate unique process that reveals a specific application is running on a host
    - Determine unique conditions for process
    - Configure new or update process classifier and discovery pattern
