# Automation Center

## Courses

- [x] [Automation Center Overview](https://learning.servicenow.com/lxp/en/pages/learning-course?id=learning_course&course_id=d37d9922c3802610a1b37473e4013137&child_id=b28d5de68708a21086dc8598cebb3505&spa=1)

## Related Documentation

- [Automation Engine on the ServiceNow Community](https://www.servicenow.com/community/automation-engine/ct-p/automation-engine)
- [Automation Center on the ServiceNow Website](https://www.servicenow.com/products/automation-center.html)
- [Automation Center in the Product Documentation Website](https://docs.servicenow.com/csh?version=latest&topicname=automation-center-landing-page.html)
  - [docs: Create an automation request from Automation Center](https://docs.servicenow.com/csh?version=latest&topicname=create-automation-request-autocenter.html)

## Overview

- centralized hub for automation activities
  - monitor automations across vendors and platforms in one location
  - letting Business Users request automations for connected systems / platforms
- Workspace
  - Overview dashboard: current and future automations
  - Executions dashboard: health of automation activities, displaying robot executions, bot processes, and job execution details
  - Business value dashboard
  - Automation CIs

### Plugins

- Automation Center (sn_ac)

### CMDB

- automation requests are mapped to Automation CIs: Flows, RPA Bot Processes, third-party automations
- relate automation CIs to Business Applications
  - improved reporting
  - reference in INC and CHG Mgmt

### Components

- Integration Hub
- RPA Hub
- Document Intelligence
- Stream Connect for Apache Kafka
- Process Mining
- API Management

### Personas and Roles

- Personas
  - Executive Sponsor
  - Business Owner
  - Developer/Administrator
  - Platform Owner
  - Process Owner
  - Solution Architect
- Roles
  - Automation Admin: `sn_ac.automation_admin`
  - Automation Technical User: `sn_ac.automation_technical_user`
  - Automation Business User: `sn_ac.automation_business_user`

### Automation Request

- Business Owner (sn_ac.automation_business_user) submits request `Submit Automation Request`
  - separate task table: ATR0001001
  - Automation Center Workspace > Lists > Build > All Automation Requests
  - more information: [docs: Create an automation request from Automation Center](https://docs.servicenow.com/csh?version=latest&topicname=create-automation-request-autocenter.html)

### Tracking Automation Value

- insert financial information directly on the request: cost per run, expected savings per year (time + money), numbers of users benefitted
- add automation goals to connect multiple related automation requests

### Visual Task Board (Kanban)

- view and update automation requests and tasks

### Publishing an Automation

- map Automation CI's to your request
- automation CIs perform the work, the request is just a container
- one request can require multiple automations