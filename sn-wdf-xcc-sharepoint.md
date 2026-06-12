# Microsoft SharePoint Online external content connector

## 20260408 XCC Setup

- 

## Resources

### Courses

- [ ]

### Links

- ServiceNow docs:
  - [Install External Content Connectors](https://docs.servicenow.com/csh?version=latest&topicname=install-ext-cont-connectors)
  - [Microsoft SharePoint Online external content connector](https://docs.servicenow.com/csh?version=latest&topicname=microsoft-sharepoint-online-external-content-connector)
    - [Estimate document volume](https://docs.servicenow.com/csh?version=latest&topicname=estimate-doc-volume-mspo)
    - [Create a public/private key pair](https://docs.servicenow.com/csh?version=latest&topicname=gen-cert-spo-ext-cont-connector)
    - [Configure MS SharePoint](https://docs.servicenow.com/csh?version=latest&topicname=cfg-azure-spo-ext-cont-connector)
    - [Configure site and site collection access](https://docs.servicenow.com/csh?version=latest&topicname=configure-site-collection-access-spo-external-content-connector)
    - [Create connector](https://docs.servicenow.com/csh?version=latest&topicname=create-ext-cont-connector-mspo)
    - [Configure crawl settings for MS SharePoint](https://docs.servicenow.com/csh?version=latest&topicname=configure-crawl-settings-spo-ext-cont-connector)
      - [docs: Create a content crawl for an external content connector](https://docs.servicenow.com/csh?version=latest&topicname=create-content-crawl-external-content-connector)
      - [docs: Create a user permission crawl for an external content connector](https://docs.servicenow.com/csh?version=latest&topicname=create-user-mapping-crawl-external-content-connector)
    - [View retrievable page content](https://docs.servicenow.com/csh?version=latest&topicname=view-retrievable-page-content-mspo-rest-api)
- Microsoft docs:
  - [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide)

### Plugins

- [External Content Connectors Application Suite plugin](https://store.servicenow.com/store/app/dd69bc781bd9a650396216db234bcb0b)
- `External Content Connectors Sharepoint Online`(sn_ext_conn_spo)

## Overview

The Microsoft SharePoint Online external content connector enables retrieval of pages from your SharePoint Online source system, making content and metadata searchable within AI Search applications.
It allows administrators to schedule content and user permission crawls for updated content and security principals, respectively, feeding this data into AI Search for indexing.

### Key Features

- Crawling Capabilities: The connector supports content crawls for updated content and user permission crawls for security principals, which are essential for maintaining accurate search indexing.
- Search Indexing: Indexed content is stored in a connector-specific indexed source, which can be linked to search profiles to enhance searchability in AI Search applications.
- Dynamic and Static Content Handling: The connector retrieves static content effectively but may struggle with dynamic web parts, which may result in incomplete content retrieval.
- API Integration: Utilizes the SharePoint REST API to access content from the underlying list items, fetching metadata like title, author, and modification date.

### Key Outcomes

By implementing the Microsoft SharePoint Online external content connector, customers can:

- Improve the searchability of SharePoint content in AI Search applications.
- Ensure accurate indexing of content through scheduled crawls.
- Understand the scope of documents in their SharePoint environment to set appropriate crawl settings.
- Manage permissions and access for a more secure and efficient content retrieval process.

## Estimate document volume

[Estimate document volume](https://docs.servicenow.com/csh?version=latest&topicname=estimate-doc-volume-mspo)
Estimate the total number of documents included in your Microsoft SharePoint Online source system and the document counts for individual sites. Use this information to determine crawl scope settings needed for your Microsoft SharePoint Online external content connector.

- required prerequisites: Microsoft 365 admin center instance
  - login credentials
  - Permission to configure and export the Microsoft SharePoint Online active site listing
  - for details see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide)
- limits:
  - each content connector can crawl up to 10 million documents
  - each user permission crawl can retrieve up to 500.000 unique security principals (users, groups, etc.)
  - mitigation: filter settings or customer support call to increase limits
- steps:
  - Log in to the [Microsoft 365 admin center](https://admin.microsoft.com/)
  - Navigate to Admin centers > All admin centers, then select SharePoint in the list of admin centers.
  - Navigate to Sites > Active sites.
  - In the Active sites list, select the Customize columns header, ensure that the following columns are selected for display, then select Apply.
    - Site name
    - URL
    - Storage used (GB)
    - Files
  - Export and analyze the document counts for active sites.
    - Select Export.
    - When prompted, save the active sites CSV list to a convenient location.
    - Open the exported active sites CSV list in a tool of your choice.
    - For each site entry in the active sites list, find the number of available documents in the Files field.
      - Use the Site name and URL field values to identify your sites.
    - Find the total number of available documents in your Microsoft SharePoint Online source system by adding up the Files field values for all the sites in the active sites CSV list.

## Create a public/private key pair

[Create a public/private key pair](https://docs.servicenow.com/csh?version=latest&topicname=gen-cert-spo-ext-cont-connector)
Generate a public/private key pair for the Microsoft SharePoint Online external content connector. Extract the public key as a DER-encoded binary X.509 format certificate for use in configuring API access for the connector in the Microsoft Entra admin center.

## Configure Microsoft SharePoint Online for external content indexing

[Configure MS SharePoint](https://docs.servicenow.com/csh?version=latest&topicname=cfg-azure-spo-ext-cont-connector)
Register an OAuth 2.0 application in the Microsoft Entra admin center to allow the Microsoft SharePoint Online external content connector to access your Microsoft SharePoint Online source system.

## Configure site and site collection access

[Configure site and site collection access](https://docs.servicenow.com/csh?version=latest&topicname=configure-site-collection-access-spo-external-content-connector)
Allow the Microsoft SharePoint Online connector to crawl your sites and site collections by granting site-specific SharePoint API FullControl permissions to the OAuth 2.0 app registered in Microsoft Entra for the connector.

## Create connector

[Create connector](https://docs.servicenow.com/csh?version=latest&topicname=create-ext-cont-connector-mspo)
Create an external content connector to retrieve searchable content and security principals from your Microsoft SharePoint Online source system.

## Configure crawl settings

[Configure crawl settings for MS SharePoint](https://docs.servicenow.com/csh?version=latest&topicname=configure-crawl-settings-spo-ext-cont-connector)

- [docs: Create a content crawl for an external content connector](https://docs.servicenow.com/csh?version=latest&topicname=create-content-crawl-external-content-connector)
- [docs: Create a user permission crawl for an external content connector](https://docs.servicenow.com/csh?version=latest&topicname=create-user-mapping-crawl-external-content-connector)

Specify the sites you want your Microsoft SharePoint Online external content connector to crawl. Define inclusion or exclusion filters for file extensions to dictate the types of documents the crawl retrieves and feeds to AI Search for indexing.

## View retrievable page content

[View retrievable page content](https://docs.servicenow.com/csh?version=latest&topicname=view-retrievable-page-content-mspo-rest-api)
Review the elements of of a Microsoft SharePoint Online page's content that can be retrieved by the Microsoft SharePoint Online external content connector.
