# MID Server

Back to [ServiceNow Discovery](./sn-discovery.md)

## Resources

- [KB0746702: How to Update a MID Server password](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746702)

## Overview

- MID: Management, Instrumentation, and Discovery
- lightweight Java application that runs as a Windows service or UNIX daemon
- does not retain any information, is a remote extension of an Instance in the enterprise network
- relevant for the following areas:
  - Discovery, Service Mapping
  - Cloud Provisioning and Governance, Cloud Insights
  - IntegrationHub, Event Management, Operational Intelligence
  - JDBC, LDAP, 3rd Party Integrations
- Outgoing (to SNow): https, port 443
- placement considerations:
  - Available bandwidth
  - Geographic location
  - IP access to targets (DMZs)
    - if port access from the internal network to the DMZ is limited, the DMZ might require an additional MID server
  - -> Always place the MID Server in a location that is not only close to the targets, but also has the most available bandwidth between it and the target.
- All > MID Server > Dashboard
  - MID Server status
  - MID Server Issues
  - Avg Percentage of CPU Used (Last 30 days)
  - Avg Percentage of Max Memory Used (Last 30 days)
- Installation
  - minimum requirements for 25 concurrent threads (base):
    - 2+ GHz Quad core processor
      - 64bit recommended
    - Windows Server 2012 R2
      - Linux possible, but Win recommended
    - PowerShell V3.0-5.1
      - `$PSVersionTable`
    - JRE min 11.0.8
      - `java -XshowSettings:properties -version`
    - connectivity to (only 443/80? or also any other ports required?):
      - servicenow.com
      - install.service-now.com
      - ocsp.entrust.net (or other OCSP CA)
      - External internet access to ServiceNow instance via port 443
  - Instance User
    - create MID server user
      - create a service account for each MID server
      - meaningful name to find in logs
    - create MID server group
    - assign role mid_server to group
    - assign users to group
  - MID server user - Windows
    - create service account
      - no local or domain admin
      - log on as a service permission
      - [step-by-step](#windows)
  - install MID server: elevated CMD Prompt `msiexec /i "Path\to\your\file.msi"`
    - SHIFT + Right-click > Copy as path
    - required information:
      - ServiceNow Instance URL, e.g. `https://instance.service-now.com`
      - ServiceNow MID Server Username
      - ServiceNow MID Server Password
      - MID Server Name - name for the MID server record in the SNow instance
      - Service Account Name - configured local service account with log on as a service permissions
      - Service Account Password
  - Validate: run validation before server is usable
  - Verify connectivity with Quick Discovery or scheduled Discovery
    - Quick Discovery
      - Discovery > Discovery Schedules > Quick Discovery
      - run immediate Discovery against a single IP

## ECC Queue

![ECC Queue](./attachments/sn-discovery-mid_server-ecc.png)

- External Communication Channel
- Instance places MID server instructions as output record on the queue
- MID server looks for work in the ECC queue via outbound port 443
- return results are placed by the MID server as input record into the queue
- Example: Discovery steps:
  1. instructions put into the ECC queue as outgoing probes
  2. MID Server monitors ECC Queue for jobs
  3. MID Server interrogates devices for information according to probe instructions
  4. MID Server reports responses as input record via the ECC queue
  5. XML payload of the input records is processed to update the CMDB
- default pull interval: 40 seconds
- process flow - Queue / State:
  - Output / Ready: new probe instructions in ECC Queue
  - Output / Processing: MID server is processing the probe instructions
  - Output / Processed: MID server has completed probe instructions
  - Input / Ready: MID server puts results in ECC Queue
  - Input / Processing: Instance is processing the input record
  - Input / Processed: Instance has processed the input record

### High Resource Deployments

- Standard MID server applications can share a MID server:
  - Discovery
  - Event Management
  - Integrations
  - Orchestration
  - Service Mapping
- selected applications are resource intensive and should be installed on dedicated hosts:
  - Cloud Management Platform (CMP)
  - alert aggregation and RCA
  - Operational Intelligence
- configuration:
- [MID server record] > Related Lists >
  - Supported Applications: disallow, for example, Cloud Management Platform, to avoid impacting Discovery
- MID Server Cluster
- cluster multiple MID server with same capabilities for load balancing and failover protection
- managed by business rule MID Server Cluster Management
  - checks to see if the MID Server assigned to a job in the ECC Queue belongs to a cluster
- two types: load balancing and failover protection cluster
  - but MID server can be simultaneous be part of both types of cluster
- creation
  - configure multiple MID server with same capabilities on an Instance
    - all are up and validated
  - All > MID Server > Clusters > New
    - configure name and type
    - Related Lists > Includes MID Servers
      - add MID Server to cluster
    - for failover configure MID server order

## Credential-less (NMap)

- [Install and uninstall Nmap on a MID Server](https://docs.servicenow.com/csh?topicname=install-nmap-on-mid-server.html&version=latest)
- [Credential-less Discovery with Nmap](https://docs.servicenow.com/csh?topicname=nmap-credential-less-discovery.html&version=latest)

## Installation

### Windows

- Step 1: Create the Service Account
  - Open Computer Management:
    - Press Windows + R, type compmgmt.msc, and press Enter.
    - In the Computer Management window, expand Local Users and Groups and then click Users.
  - Create a New User:
    - Right-click Users, and then click New User.
    - In the New User window, fill in the required details for the new account:
    - Username: Name the service account (e.g., ServiceAccount1).
    - Password: Set a strong password for this account.
    - Uncheck User must change password at next logon and check Password never expires.
    - Click Create.
- Step 2: Assign “Log on as a Service” Permission
  - The “Log on as a service” permission must be granted to this service account so that it can be used to run services. Here’s how you can do that:
    - Open Local Security Policy:
      - Press Windows + R, type secpol.msc, and press Enter to open the Local Security Policy editor.
      - Expand Local Policies and then click User Rights Assignment.
    - Grant Log on as a Service Permission:
      - In the right pane, find and double-click Log on as a service.
      - In the Log on as a service Properties window, click Add User or Group.
      - In the dialog box, enter the name of the service account you created (e.g., ServiceAccount1), then click OK.
      - Click OK again to close the properties window.
- Step 3: Configure the Service to Use the Service Account
  - Open Services:
    - Press Windows + R, type services.msc, and press Enter.
    - Locate the service you want to configure to run with the service account.
  - Modify Service Log On Settings:
    - Right-click the service and select Properties.
    - Go to the Log On tab.
    - Choose the option This account and enter the name of the service account (e.g., .\ServiceAccount1 for local accounts or DOMAIN\ServiceAccount1 for domain accounts).
    - Enter the password for the service account and confirm it.
    - Click OK.
  - Restart the Service:
    - After setting the account, restart the service to apply the changes. Right-click the service and choose Restart.

Configuration

- C:\ServiceNow MID Server mid-win22\agent\config.xml
  - `C:\` chosen installation path
  - `mid-win22` - MID server name
- XML parameter
  - url: instance url
  - mid.instance.username: instance mid server user
  - mid.instance.password: instance mid server user password hash
  - name: mid server name

## Troubleshooting

### MID Server FileNameComplianceInSync Error

- [community: MID Server FileNameComplianceInSync Error](https://www.servicenow.com/community/itom-forum/mid-server-filenamecomplianceinsync-error/td-p/3017630)
