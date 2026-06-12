In the Technical domain, CSDM uses Application Service (cmdb_ci_service) to represent the technical delivery of an application. The business application is connected to its application service via a Provided by::Provided for relationship.

The digital product concept appears in some community discussions, but official CSDM 5 documentation still refers to business applications. ServiceNow’s product leaders have stated that future versions may generalize digital products, but as of May 2026 the formal CMDB class remains cmdb_ci_business_app.

Newer sources on LeanIX–ServiceNow integration (2025–2026)

ServiceNow Store – LeanIX Integration (version 1.1.5, May 2026)

The most up‑to‑date information about the integration comes from the LeanIX Integration application on the ServiceNow Store (version 1.1.5 released 18 May 2026).  The store description notes that the integration provides bi‑directional synchronization between LeanIX and ServiceNow and describes several key features:

* Applications created in LeanIX are synchronised as Business Applications in ServiceNow.  The integration “automatically synchronizes Applications of the LeanIX Enterprise Architecture tool to Business Applications in ServiceNow” .
* Hardware and software discovered by ServiceNow are linked back to LeanIX.  The same description states that it “creates linkage of underlying Software and Hardware (discovered) in ServiceNow to LeanIX” .
* Initial load from ServiceNow to LeanIX.  It “supports the creation of an initial load of the LeanIX inventory from ServiceNow” .
* The integration requires a ServiceNow CMDB and an integration user with ACLs to access tables such as cmdb_ci_business_app .  Documentation is provided at the SAP Help portal.
* Release notes for version 1.1.5 mention improvements to error handling and metadata retrieval and confirm support for Zurich (ServiceNow Tokyo) through Xanadu family releases .

LeanIX help portal (2026)

The official LeanIX help portal (May 2026) includes a detailed ServiceNow integration guide.  Key points from the documentation (paraphrased, not verbatim) include:

* Master data in LeanIX: LeanIX should remain the system of record for the application portfolio.  Enterprise architects model applications and IT components in LeanIX; business applications in ServiceNow are derived from LeanIX applications via the integration.
* Mapping: LeanIX Application fact sheets map to ServiceNow Business Application (cmdb_ci_business_app) CIs.  LeanIX IT Component fact sheets map to ServiceNow Software Model or Product Model classes, depending on whether the component is software or hardware.  A matching correlation ID ensures that updates remain synchronised.
* Lifecycle and ownership: The integration allows LeanIX to remain responsible for planning and governance (e.g., lifecycle status, owners) while ServiceNow handles operational incidents and change management.  Planned applications in LeanIX are imported as Business Services to maintain the CSDM link to technical services.
* Configuration options: Administrators can configure which attributes are synchronised, define filters to include only relevant applications (e.g., exclude trivial desktop tools), and control how relationships (e.g., “provided by” between business application and application service) are created.

LeanIX Community discussion (Sept 2025)

A LeanIX community thread from September 2025 shows that organisations moving from ServiceNow‑centric application mastering to LeanIX want LeanIX to be the source of truth.  Contributors noted they synchronise the app ID to the correlation_id field and use a clean one‑way sync to avoid conflicts; they plan to automate creation of application‑to‑application service relationships .  This discussion underscores the trend that new implementations master the application in LeanIX and export only selected data to ServiceNow.

ServiceNow Community post (June 2025)

A ServiceNow community post from June 2025 discusses mapping LeanIX IT components to ServiceNow’s CMDB.  A solution by a ServiceNow architect explains that:

* Business Applications: LeanIX Business Applications are imported into cmdb_ci_business_app and relate to business capabilities.
* IT Components: These map to Software Models (cmdb_ci_appl or cmdb_ci_product_model) rather than directly to cmdb_ci because product models are templates; for impact analysis, one should create CIs and relate them to the application service.
* Service relations: Application services depend on applications or software models through a Depends on::Used by relationship.  This ensures dependencies appear in the Digital Product Model (DPM) and Service Operations Workspace .

This post confirms the mapping approach for LeanIX components and emphasises using the CSDM relationships rather than inventing new ones.

Verified best practices for CSDM 5 and LeanIX integration

1. Model only business‑impacting applications as Business Applications.  CSDM 5 still uses the Business Application class.  It explicitly advises organisations to avoid modelling every software product or desktop tool as a business application; only systems that provide a business capability and have financial or organisational impact belong in cmdb_ci_business_app.  Commodity software (desktop tools, utilities) should be recorded in lower‑level CI classes (Software Model or Product Model).
2. Use LeanIX as the master for the application portfolio.  A current trend in 2025/2026 implementations is to master the application portfolio in LeanIX.  LeanIX’s integration automatically synchronises applications to ServiceNow as Business Applications  and sends back discovered hardware/software.  The help portal emphasises keeping LeanIX as the source of truth and controlling which applications are exported to ServiceNow.
3. Maintain relationships using CSDM patterns.  For each business application, create an Application Service (cmdb_ci_service) and connect them with a Provided by::Provided for relationship.  Link underlying software and hardware CIs to the application service via Depends on::Used by relations .  The integration can automate this mapping if configured correctly.
4. Keep a full application inventory outside the CMDB if necessary.  If a customer insists on having visibility into every application (home‑grown, third‑party, desktop, SaaS), LeanIX (or another APM tool) is a better location than the ServiceNow CMDB.  LeanIX allows you to model trivial or “IT component” applications without overloading the Business Application table.  You can still perform risk or data‑protection analysis on those items using fields in their respective CI tables without promoting them to cmdb_ci_business_app.
5. Alternate approach within ServiceNow (if LeanIX is not used).  If a client insists on keeping all applications in ServiceNow, create a separate “Application Inventory” table (extending cmdb_ci or using cmdb_ci_appl) to store non‑business‑impacting applications.  Use a field or a tag to mark whether an application is a business application.  Only those flagged are promoted to cmdb_ci_business_app and related to business capabilities.  This approach preserves governance and risk visibility without polluting the Business Application class.
6. Integration configuration:
    * Filtering: Configure the LeanIX integration to sync only applications that meet criteria such as lifecycle phase, criticality, or classification.  Exclude trivial tools from the sync to avoid cluttering ServiceNow.
    * Correlation IDs: Use correlation_id to uniquely match LeanIX entries with ServiceNow CIs, avoiding duplicates.  Community posts confirm this practice .
    * Initial data load: Use the integration’s initial load feature to import existing ServiceNow data into LeanIX.  Clean up duplicates and assign correlation IDs as needed.
    * Permissions: Ensure the integration user has ACLs to create and update cmdb_ci_business_app records .

Answer to the user’s specific questions

* Is there more current guidance than the 2019 LeanIX source?  Yes.  The ServiceNow Store entry for the LeanIX Integration (version 1.1.5, May 2026) confirms that the integration synchronises LeanIX applications into Business Applications in ServiceNow and links underlying software and hardware .  The LeanIX help portal (2026) further explains mapping and configuration options.  These sources supersede the 2019 article and confirm the continued use of business application in CSDM 5.
* Is the “digital product” concept part of CSDM 5?  No.  The “digital product” term appears in some blogs, but official CSDM 5 documentation still models applications using cmdb_ci_business_app.  Business applications remain the focal point for linking business capabilities to technical services.
* Should every software product be treated as a business application?  No.  Only applications that support business capabilities and have material business impact should be captured as business applications.  Desktop software and trivial tools should be stored as software models or IT components.  You can still perform risk or data‑protection analysis on those items using fields in their respective CI tables without promoting them to cmdb_ci_business_app.
* If the client insists on an overview of all applications in ServiceNow, what approach should be taken?  Either:
    1. Use LeanIX as the master inventory and synchronise to ServiceNow only business applications.  Keep the full inventory in LeanIX and create reports or dashboards there for governance.  Use the integration to import risk ratings and compliance flags back to ServiceNow at the product model or CI level.
    2. Within ServiceNow, create a dedicated Application Inventory table for all software.  Use a boolean or classification field to designate critical applications.  Use transform maps or integration flows to populate the Business Application table only for critical applications.  This keeps the CMDB aligned with CSDM best practice while still providing a single location in the platform for governance processes.
* Integrating with LeanIX under CSDM 5:  Continue to map LeanIX Applications to ServiceNow Business Applications and LeanIX IT Components to ServiceNow Product Models or Software Models.  The integration’s 2026 release notes and help documentation provide configuration controls to filter which applications are synchronised, ensuring only relevant business applications are created in the CMDB.  For trivial web applications or desktop software, create CIs in cmdb_ci_appl or cmdb_ci_product_model and disable their synchronisation as business applications.

Conclusion

Recent (2025–2026) guidance confirms that CSDM 5 still uses the Business Application class and that LeanIX’s ServiceNow integration continues to map applications to Business Applications .  Organisations are encouraged to keep LeanIX as the master application inventory and synchronise only applications with business impact to ServiceNow.  For full visibility of all software, maintain a separate inventory (either in LeanIX or a custom table) and avoid cluttering the Business Application table.  Following these practices ensures a clean CMDB, preserves CSDM relationships, and supports risk and compliance analysis across the entire application landscape.