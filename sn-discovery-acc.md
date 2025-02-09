# Agent Client Collector

## TODO

- [ ]

## Resources

### Courses

- [ ]

### Links

- [docs: Agent Client Collector data collection properties](https://www.servicenow.com/docs/bundle/washingtondc-it-operations-management/page/product/agent-client-collector/reference/acc-data-collection-properties.html)
- [community: Step by Step Configuration](https://www.servicenow.com/community/itom-articles/discovery-with-agent-client-collector-step-by-step-configuration/ta-p/2324008)
  - on MID server allow inbound port 8433 (This is the default port for Agent Client Collector)
- [docs: Incorporating the Agent Client Collector into a custom base image for mass deployment](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/agent-client-collector/task/acc-virtual-deployment.html)
- [KB: Agent Client Collector Visibility](https://noderegister.service-now.com/kb?id=kb_article_view&sysparm_article=KB0966481)
- [Agent Client Collector for Visibility](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/agent-client-collector/concept/acc-visibility-landing-page.html)

### Labs

- []

## Topics

### To Sort

- Empfehlung: als System laufen lassen
  - nur in der Paketierten Version einstellbar
  - in der Konfig IQuery = true nach Installation setzen
- ACC Mid Server Empfehlung: Linux - kann mit deutlich mehr ACC Agents umgehen
  - wenn per Internet erreichbar: in der Cloud autark ohne Verbindung zum Kernnetz laufen

### Assigned To Discovery

- resources
  - [docs: Populating Assigned To attribute in Computer CI for ACC-V](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/agent-client-collector/task/fetching-logged-in-user-information-for-acc-v.html)
- automatically populate Assigned to for Windows endpoint devices and macOS devices by setting the following system properties
  - `sn_acc_vis_content.set_assigned_to`
  - `sn_acc_vis_content.assigned_to_user_order`
- requires:
  - local credentials with "Log on As Local System User" instead of default ServiceNow service user
    - executed commands on Windows:
      - `wmic COMPUTERSYSTEM GET USERNAME`
      - `From osquery: SELECT l.user FROM logged_in_users l JOIN users u ON l.sid = u.uuid WHERE u.type != 'special'`
    - executed commands on macOS: `SELECT distinct(l.user) FROM logged_in_users l JOIN users u ON l.user = u.username`
- identified user name is matched against sys_user table
  - identified user names can be prioritized with sys property `sn_acc_vis_content.assigned_to_user_order`
    - default: `computer_system_username,logged_in_users`
- priority:
  - by default, if Assigned To is not empty, it will not be overwritten
  - sys property `sn_acc_vis_content.set_assigned_to` can be set to `true` to overwrite the Assigned To field
    - define reconciliation rules to set priorities

### DF: Agent Client Collector for Visibility (ACC-V)

- installation
  - required license: ITOM Discovery v2, ITOM Visibility or any bundle that includes ITOM Visibility
  - required plugins
    - _Discovery_ plugin (com.snc.discovery) must be installed and activated
    - _Agent Client Collector Framework_ (ACC-F)
    - ITOM-Discovery or ITOM-Visibility SKUs (SU-based licensing) is required
    - _Discovery and Service Mapping Patterns_ plugin
    - _Visibility Content_ plugin
    - _Agent Client Collector for Visibility_ (ACC-V) application is downloaded from the ServiceNow Store or from the instance (sn_acc_visibility)
  - MID properties to be enabled
    - mid.sa.ssh.use_sncssh set to true
    - mid.ssh.use_snc set to true
  - ACC: check allow list at the responsibility of the user Activation:
    - sn_agent.appl_classification_behavior set to `full` (enable pattern execution)
    - sn_agent.disco_disable_ci_clobber_of_agentless_disco set to false (for horizontal discovery)
  - full prerequisites for patterns with ACC: [Pattern Execution with Agent Client Collector](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1323623)
- Overview ACC-V
  - installed on Windows, Mac and Linux to collect host data
  - multiple capabilities based on installed plugins:
    - Agent Client Collector Framework (ACC-F)
    - Agent Client Collector Monitoring (ACC-M)
    - Agent Client Collector For Visibility (ACC-V)
      - Discovery & SAM
  - Deploys Ruby scripts that execute OS Query and OS-specific commands to gather information such as:
    - Basic Inventory
    - Serial Numbers
    - Storage Devices
    - File Systems
    - Network Adapters
    - TCP Connections
    - Running Processes
    - Installed Software
    - Local User
  - Powershell is not being used in any of the ACC-V modules
- Process: applies Checks and Policies to schedule and collect host data which is triggered during the following cases:
  - Periodic scheduling: A policy-based approach where Discovery is triggered on a periodic basis
  - On CI delete: When the computer or server CI record is deleted
  - MID Server cycle: When the MID Server goes down and comes back up
  - Target host cycle: When the target host goes down and comes back up
  - Network break: When there is a break in the network link to the target
- MID server
  - ACC Listener needs to be installed
    - All > MID Server > Servers > {mid server} > Related Link > Setup ACC Listener
    - Enter the MID web server port (8800) in the displayed field - or choose a custom port
    - confirm:
      - Agent Client Collector > Deployment > MID Web Server
      - Agent Client Collector > Deployment > Websocket Endpoint
      - get API key name from Agent Client Collector > Deployment > MID Web Server API Key > Related Link > View API Key
        - validate via `curl -Lk -H "Authorization: Key <API_KEY>" https://<mid_server_address>:<port>/api/mid/mon`
  - Agents use the MID server to send data to the ServiceNow Instance
  - Agent send first data > CI is created > CI Class policies are send back to the MID server > policies are pushed to the agent devices
  - Policies include:
    - checks
    - check parameter
    - plugins
    - frequency
- Agent Installation
  - [docs: Install the Agent Client Collector on a Windows machine manually](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/agent-client-collector/task/acc-install-windows.html)
    - download via All > Agent Client Collector > Deployment > Agent Downloads
    - Windows: start Installer via CLI with Admin Permissions: `msiexec /i <path to msi file>`
    - required information: MID server address, API key, and the MID server port
  - [docs: View the Agent Client Collector logs](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/agent-client-collector/task/acc-view-log.html)
    - Windows: `C:/ProgramData/ServiceNow/agent-client-collector/log/acc.log`
    - Linux: `/var/log/servicenow/agent-client-collector/acc.log`
    - macOS: `/Library/Application Support/servicenow/agent-client-collector`
- Check Definitions
  - All > Agent Client Collector > Configuration > Check Definitions
    - checks are stored, created and updated on the instance
  - executes the osquery command on agents
  - osquery commands are used to gather specific attribute details from a CI such as serial number, file systems, running processes, etc
  - four Check Definitions are used by four ACC-V Policies
- Policies
  - four policies for ACC-V
    - Enhanced Discovery Policy
    - Software Installed Policy
    - SAM discovery
    - SAM background policy
  - define which CI type to monitor
  - defines interval-based scheduling
  - default interval is 86400 seconds, which is every 24
- Discovery Source: ACC-Visibility
- Pattern Execution from the ACC
  - [community post](https://www.servicenow.com/community/itom-blog/running-patterns-with-the-agent-client-collector-check-out-what/ba-p/2568742)
  - Execute discovery patterns on environments that are not typically accessible for agentless discovery
  - Leverage existing connection from the ACC instead of trying SSH and WinRM/ PowerShell to connect to the system
  - Flexibility to execute discovery patterns for both agentless & agent-based discovery
  - Allow discovery admins to run Service Mapping in Hybrid mode (Agentless + Agent-based)
  - Supported from Washington release onwards with Service Mapping Plus application
