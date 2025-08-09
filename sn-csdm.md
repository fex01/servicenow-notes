# Common Service Data Model CSDM

## TODO

- [ ]

## Resources

- [docs: Implementing the CSDM framework in stages](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implementation-stages.html)
  - [implementation notes](#implementing-the-csdm-framework)
- **CSDM** Getting Started with Services and Service Offerings
  - [NowCreate: CSDM Workshop - Getting Started](https://nowlearning.servicenow.com/nowcreate?id=nc_asset&asset_id=dde64c62875255d0f2f443f7dabb354b)
  - [CSDM workshop](https://nowlearning.servicenow.com/nowcreate?id=nc_asset&asset_id=5c4d48bfdb998d100c912b691396198e)
  - [CMDB workshop](https://nowlearning.servicenow.com/nowcreate?id=nc_asset&asset_id=3054c3838795d9d8af9f213acebb35c5)
  - [CSDM Data model examples](https://nowlearning.servicenow.com/nowcreate?id=nc_asset&asset_id=c0ddb115db6d0d900c912b6913961987)

### Further Courses

- [ ]

### Links

- [Docs](https://docs.servicenow.com/)
  - [CI relationships in the CMDB](https://docs.servicenow.com/csh?topicname=c_CIRelationships&version=latest)
- [Developer](http://developer.servicenow.com/)
- [CSC (Customer Success Center)](https://www.servicenow.com/success.html)
- [Community](https://www.servicenow.com/community/)
- [YouTube](https://www.youtube.com/user/servicenowinc)
- [Center of Excellence and Innovation (CoEI)](https://www.servicenow.com/success/playbook/center-excellence-innovation-coei.html)

### Labs

- []

## Implementing the CSDM framework

- [docs: Implementing the CSDM framework in stages](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implementation-stages.html)
  - [docs: Configure the CSDM Data Foundations dashboard](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/task/csdm-foundations-dashboard.html)
    - [docs: CSDM Data Foundations dashboard](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-data-foundations-dashboard.html)
    - 1. install free plugin `CSDM and the CMDB Data Foundations Dashboards`
    - 2. populate CSDM metrics by activating and executing the following scheduled jobs:
      - `CSDM Get Well Metric Collection` - collect metrics for compliant CIs, runs daily, stores results in table [sn_getwell_csdm_score]
      - `CSDM Data Foundations PA Metric Collection` - total count of non-compliance CIs
  - [docs: First activation step — Map existing life cycle data to CSDM standards](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/configuration-management/concept/csdm-life-cycle-standard-values.html)
    - Mapping table: `All > CSDM > Life Cycle Mapping` / [life_cycle_mapping]
      - OOB states should already be mapped to CSDM stage + status
      - incomplete records for custom states are automatically added, map appropriate LC stage + status to activate the records: [docs: Specify how to map legacy life-cycle states to CMDB states](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/create-life-cycle-migration.html)
        - If you map more than one legacy status value set to any single life-cycle value pair, then select the Reverse sync option
      - after checking the mappings, activate LC mapping with the `Activate` button on table level: [docs: Activate life cycle migration](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/activate-life-cycle-migration.html)
  - [docs: Second activation step — Activate the CSDM plugin](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/task/csdm-enable.html)
  - [docs: Third activation step — Migrate existing data to the CSDM framework](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/task/migrate.html)
    - [CSDM migration tools](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-migrate-tools.html)
    - manage custom attributes by deciding which are actually required:
      - Keep: The custom attribute doesn't have a related base-system attribute but it's required for a unique use case.
      - Refactor: The custom attribute does have a base-system attribute or a capability that can be migrated.
      - Do Not Need: The customization is no longer needed. Delete the attributes that you don’t use or use only rarely. Consider deleting attributes if there’s a better way to address a use case.
    - consider related dependencies: not automatically moved, identify with help of [identifying table dependencies script](https://www.servicenow.com/community/common-service-data-model/migrating-into-csdm-identifying-table-dependencies/ta-p/2308617)
      - use to estimate migration effort
  - CSDM implementation stages
    - [docs: Foundation](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implement-foundation-stage.html)
    - [docs: Crawl](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implement-crawl-stage.html)
    - [docs: Walk](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implement-walk-stage.html)
    - [docs: Run](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implement-run-stage.html)
    - [docs: Fly](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/concept/csdm-implement-fly-stage.html)
  - [docs: Auto-generate product models for logical CIs](https://www.servicenow.com/docs/bundle/washingtondc-servicenow-platform/page/product/csdm-implementation/task/csdm-auto-create-prod-model-for-ci.html)

## CSDM Basics

| Aspect                 | Business Application                                                                                                                                                                      | Application Service (subclass of Service Instance)                                                                                       | Application                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**        | Represents all software and infrastructure environments (Dev, Test, Prod) configured to provide business functionality; supports application rationalization, optimization, modernization | Logical representation of a deployed application stack; may include parent/child relationships for microservices or platform deployments | Any deployed program, module, or group of programs providing specific functionality on compute infrastructure; installed bits and bytes                       |
| **Scope**              | Connects IT to business outcomes; supports business capabilities                                                                                                                          | Operational delivery of a specific business application; connects technical layer with business layer                                    | Technical software components; foundation of application services                                                                                             |
| **CMDB Class**         | `cmdb_ci_business_app`                                                                                                                                                                    | `cmdb_ci_service_auto`                                                                                                                   | `cmdb_ci_appl`                                                                                                                                                |
| **Key Details**        | Not an operational CI; not used in Incident, Problem, Change; not version specific; contains metadata about the business application                                                      | Operational CI; used in Incident, Problem, Change for impact analysis; may be created per environment or geo                             | Operational CI; used in Incident, Problem, Change; unique deployment on specific host; discoverable installation of code communicating over a particular port |
| **Creation Method**    | Manual                                                                                                                                                                                    | Manual mapping; Service Mapping with entry point; Service Mapping with tags; Service Mapping with ML; Dynamic CI Group with query        | ServiceNow Discovery; Service Graph Connectors; Service Mapping                                                                                               |
| **Relationships**      | Business capabilities; application services; information objects                                                                                                                          | Supporting and connected applications; hosting infrastructure; other application services                                                | Hosting infrastructure                                                                                                                                        |
| **Examples**           | Payroll System                                                                                                                                                                            | Americas Payroll Application Service; APAC Payroll Application Service; Payroll Application Service (Dev)                                | MySQL; Apache Tomcat; Websphere                                                                                                                               |
| **Key Reference Data** | Business process; business criticality; support vendor; business owner; IT application owner; life cycle status                                                                           | Managed by group; support group; change group; owned by; life cycle status                                                               | Managed by group; support group; change group; owned by; life cycle status                                                                                    |
