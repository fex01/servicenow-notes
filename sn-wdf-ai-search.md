# AI Search and External Content Connectors

## Courses

- [x] [Introduction to AI Search and External Content Connectors (Zurich)](https://learning.servicenow.com/lxp/en/now-platform/introduction-to-ai-search-and-external-content-connectors?id=learning_course_prev&course_id=fb805e3897843e54e7b47b70f053af0a)

## Related Documentation

- [AI Search](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/overview-ais.html)
- [Genius Result Cards](https://docs.servicenow.com/csh?topicname=genius-results-ais.html&version=latest)
- [Result improvement rules](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/result-improvement-rules-ais.html)
- [Semantic vector search in AI Search](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/semantic-search-ais.html)
- [Exploring External Content Connectors](https://www.servicenow.com/docs/r/platform-administration/ai-search/exploring-ext-cont-connectors.html)
  - [Configuring External Content Connectors](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/configuring-ext-cont-connectors.html)
  - [Using External Content Connectors](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/ai-search/concept/using-ext-cont-connectors.html)
  - [docs: Configure Microsoft SharePoint Online for external content indexing](https://www.servicenow.com/docs/r/platform-administration/ai-search/cfg-azure-spo-ext-cont-connector.html)
- [Knowledge Graph: Natural Languages queries](https://www.servicenow.com/docs/r/intelligent-experiences/knowledge-graph/knowledge-graph-landing.html)

## Overview

- find information across ServiceNow: Service Portal Search, Virtual Agent, Now Mobile App
- External Content Connectors:
  - Microsoft SharePoint Online
  - Atlassian Confluence Cloud
  - WebCrawler

## AI Search

### AI Search Overview

- replaces older Zing engine
- launched with Quebec
- AI Search index stores:
  - structured data: knowledge articles, catalog items, user records
  - application data: incidents, cases, problems, changes
  - external content: SharePoint, Confluence, WebCrawler, ...
    - do no longer rely on IntegrationHub Spokes, but on External Content Connectors (XCC)
- AI Search is intended to learn for improved search accuracy and ranking
  - auto-suggestions accepted
  - type-ahead usage
  - aggregated user interactions
- capabilities
  - context-aware search (user context)
  - [Knowledge Graph: Natural Languages queries](https://www.servicenow.com/docs/r/intelligent-experiences/knowledge-graph/knowledge-graph-landing.html)
  - Now Assist Integration
  - Content from External Content Connectors: SharePoint, Confluence, Google Drive, Jira, Slack, Box, OneDrive, and more

### AI Search Experience

- on Service Portal, Now Mobile and Virtual Agent
- Service Portal
  - lexical search + semantic vector search (LLM text understanding) = hybrid search
  - Result improvement rules: fine-tuning search results
    - boost sepcific results
    - block some results
    - highlight selected content
- Genius Result Cards
  - hybrid search
  - appears at the top of search results
  - can include links to internal and external sources
- Enhanced chat
  - Conversational Requests: complete SRQ via multi-turn conversation
  - Synthesizes Response: Virtual Agent uses a mix of Knowledge Articles, VA topics and Catalog Items
  - dynamic chat window can be repositioned

## External Content Connector

### XCC Overview

- list of available connectors: [Exploring External Content Connectors](https://www.servicenow.com/docs/r/platform-administration/ai-search/exploring-ext-cont-connectors.html)
- simplified setup: 5 streamlined steps
- enhanced monitoring tools and management dashboards: ensure security standards and performance expectations

### XCC Plugin Setup and Configuration

- downloads:
  - download `External Content Connectors Application Suite plugin` from ServiceNow Store
  - download specific connector for source system, for example SharePoint Online
- configuration
  - example: SharePoint Online
    - Step 1: Register an OAuth 2.0 application in the Microsoft Entra Admin Center: required to allow Microsoft SharePoint Online external content connector to access your SharePoint Online
      1. Register an application in Microsoft Entra Admin Center
      2. Add API permissions to generate a client ID and tenant ID
      3. Grant consent for the API to access necessary resources
      4. Generate a certificate file (Java Key Store (JKS)) for secure communication
      - more details see [docs: Configure Microsoft SharePoint Online for external content indexing](https://www.servicenow.com/docs/r/platform-administration/ai-search/cfg-azure-spo-ext-cont-connector.html)
    - Step 2: Configure External Content Connectors
      - navigate to `External Content Connectors Admin console` in Servicenow
      - Enter the Application (Client) ID, Directory (Tenant) ID, JKS certificate password, and JKS certificate thumbprint (Base 64)
      - attach JKS certificate
      - configure Crawl settings if you want to exclude some content / focus on specific content
        - include and exclude filters
      - schedule crawls: daily, weekly, specific times
        - available Crawl options:
          - full: index everything
          - partial: only index new or modified content since last crawl
          - user mapping: special crawl to retrieve user identity information for access control
        - at least one document crawl and one user mapping crawl per source
        - crawl history provides visibility into number of docs processed and efficiency
          - role `AIS_high_security_admin` required to see results of user mapping crawls
      - tenants for SharePoint Online
        - one connector per tenant
        - each tenant can include multiple SharePoint Online sites
          - as it is still the same tenant, only one connector is required
        - multiple connectors are possible if there are multiple tenants
      - document type check
        - text/html file content is ingested directly
        - binary files require processing using Apache Tika
          - Tika extracts text and metadata before ingestion
        - files them self are not copied to ServiceNow
    - Step 3: Configure AI Search
      - content is linked to a search profile, which allows for:
        - Results improvement rules
        - Stop words
        - Synonyms
        - Other search tuning parameters
    - Step 4: Preview and test:
      - Select the search profile you want to test against.
      - Run a test query and review the results.
      - A new tab (e.g., for SharePoint Online) will appear in the interface.
      - Select a returned document to preview it directly in the source system (e.g., SharePoint Online tenant).
