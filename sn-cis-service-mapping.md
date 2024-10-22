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

##### L3: Map an Individual Service

- [lab pdf](https://nowlearning.servicenow.com/sys_attachment.do?sys_id=ff10a46f87020e54af9f213acebb3545)
- Create Credential
- Configure Service Mapping to Discover the EMEA Dispatch Scanning Service
- View the Service Mapping Discovery Log
- View the Results

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

#### Service Mapping Overview

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

#### Horizontal Discovery

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

#### Service Lifecycle

- Mapping Discovery Lifecycle Flow
  - **Start**: Readiness Checklist (All > Service Mapping > Home)
    - Mandatory
      - MID Server installation
      - Credentials configuration
      - Discover load balancers
      - Discover hosts
    - Optional
      - NetFlow
      - Cloud discovery
  - **Map**: Service Discovery
    - Bulk Discovery
      - Services suggested by discovering load balancers
      - CSV Import of candidate services
    - Single Creation
      - Manual creation
  - **Fix**: Error Handling
    - Bulk Error Handling
      - Category tiles
      - Fix one test all
    - Single Map Refinement
      - Group errors
      - Ignore errors
      - Next error
      - Skip and Resume
      - Create pattern from generic application
      - Pattern customization
  - **Review**: Review and Refine
    - Send for SME review
    - Interact with SME
    - Receive feedback from SME
    - Refine map
  - **Approve**: Activation of Service
    - Approval of service by application owner
    - Deployment of the service to production based on use case
    - Activation of the service on the Dashboard

#### Service mapping

- focus on **Start** (details see [Service Lifecycle](#service-lifecycle))
  - ensure `Service Mapping` plugin is purchased and activated
  - prepare credentials:
    - hosts: SSH, SNMP, Windows
    - application specific credentials: VMware Center, CIM, Applicative Credentials
  - prepare MID Server
  - review Readiness Checklist (All > Service Mapping > Home)
- roles
  - **sm_admin** / admin:
    - Maps, fixes, and maintains services
    - Performs advanced configuration
  - **sm_user**:
    - Views service maps to plan change or migration
    - Analyzes maps for continuity and availability
  - **sm_app_owner**:
    - Reviews, approves, and owns service
- Credentials
  - security:
    - credentials are AES128 encrypted in the instance
    - for transport to MID server decrypted and re-encrypted with MID server key
    - never stored in clear text on MID server storage, only in memory
    - third-party credential providers are possible
  - permission requirements:
    - Windows:
      - credentials:
        - domain user with local admin rights
        - SMB admin access to C$
      - connectivity:
        - WMI port open
        - SMB port open
    - Linux & Unix: selective sudo access, SSH port open (TCP, default 22)
    - Network Devices
      - credentials:
        - SNMP v1/2/3 read only community string
        - ACL on network device must include MID Server IP
      - connectivity: SNMP port open (UDP, default 161)
    - Applicative Credentials: used in Discovery Patterns, tied to specific CI Type
      - examples: basic auth., NTLM, Windows, SSH
- focus on **Map** (details see [Service Lifecycle](#service-lifecycle))
  - Service Mapping Application
    - requirements:
      - Credentials
      - Entry Point (individual or in bulk)
    - provides:
      - baseline CI Types & Discovery Patterns (common enterprise applications and connections)
      - continuous collection of traffic-based connection information (ADM probes)
  - Entry Points
    - define top level applications that comprise services (e.g. `http://cloud.cd.com:8081)`)
    - starting point for mapping process
    - created via import from CSV, manually entered, or suggested by Discovery of Load Balancers
      - All > Service Mapping > Home > Additional Options
  - use **Bulk Mapping** to scale mapping process: parallel, speed and quality over time
  - tools
    - Service Mapping Homepage: All > Service Mapping > Home
      - Map Candidates: _Map your Services_
      - Fix Service maps: _Fix your Services_
      - Approve Service maps: _Approve your Services_
      - Completed Service maps: _View your Services_
    - Service Map Views:
      - Application View vs. Host View
      - show dependent Services
      - visibility to changes of discovered CIs (bubbles on the Timeline)
    - Discovery Log: All > Discovery > Discovery Status > [specific record] Related List
      - Discovery Patterns tried and executed
      - Identification and Connection sections tried
      - Identification and Connection steps executed
  - Data Structure and Flow
    - Application Services are comprised by
      - an Entry Point
      - Host CIs
      - Application CIs
      - connections between CIs
    - Patterns have three sections:
      - Identification
      - Extension
      - Connection (only for Application Patterns)
    - ![Service Mapping Process Flow: With Connections](./attachments/sn-cis-service-mapping-process-flow.png)
- focus on **Fix** (details see [Service Lifecycle](#service-lifecycle))
  - Errors
    - are categorized and displayed in prioritized tiles
    - Each group of errors may be assigned to an owner for resolution
    - Assignment may be done based on platform task
    - Information is provided on suggested actions for common errors
  - Focus on the first 5 categories
    - Resolve errors in order of the categories from top left to bottom right
    - Resolving an error in a category may yield errors in subsequent categories
    - Work by selecting a sample error in each group and diagnose the problem
    - User can drill down into specific category and error group and try to resolve multiple errors at once
    - User task to delegate work to other teams (e.g. network, Unix)
    - Define SLAs on tasks if needed

#### Extending Patterns

#### Building Identification Sections

#### Building Connection Sections

#### CMDB Reconciliation

#### Other Service Mapping Approaches
