# Foundation Data

## IRE support for non-CMDB tables

- [docs: IRE support for non-CMDB tables](https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/configuration-management/concept/ire-support-non-cmdb-tables.html)
- only for specific non-CMDB tables:
  - application-specific scope tables
  - foundation tables:
    - Location [cmn_location]
    - Department [cmn_department]
    - Cost Center [cmn_cost_center]
    - Building [cmn_building]
    - User [sys_user]
    - Group [sys_user_group]
- not possible to use CI Class Manager for non-CMDB tables. Work directly on the respective tables

  - [docs: Create an identification rule for a non-CMDB table](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/create-non-cmdb-id-rule.html)

    - All > Identification/Reconciliation > CI Identifiers
      - New
        - Name | Name of CI identifier.
        - Applies to | Supported non-CMDB table.
        - Independent | Must be checked to indicate that the identifier can identify a record independently of other records.
      - _Save_
        - Tab _Identifier Entries_ > New
        - Tab _Related Entries_ > New
    - for _Hybrid Entry CI Criterion Attributes_, background scripts have to be used

      - sample script:

        ```js
        var gr = new GlideRecord("cmdb_identifier_entry");
        // get the identifier entry you want to update
        gr.get("<identifier_entry_sys_id>");
        // set the attributes you want in the hybrid rule in a comma separated list
        // for example: 'name,serial_number'
        gr.hybrid_entry_ci_criterion_attributes =
          "<column_name_1>,<column_name_2>,<etc.>";
        gr.update();
        ```

  - [docs: Create a reconciliation rule for a non-CMDB table](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/concept/create-reconciliation-rule-non-cmdb.html)
  - [docs: Create an IRE data source rule for non-CMDB tables](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/create-non-cmdb-ire-data-src-rule.html)
  - [docs: Create a data refresh rule for a non-CMDB table](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/create-non-cmdb-data-refresh-rule.html)
  - [docs: Create an identification inclusion rule for a non-CMDB table](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/task/create-non-cmdb-id-inclusion-rule.html)
  - [docs: Simulate payload execution using identification simulation](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/concept/identification-simulation.html)
  - [docs: Use partial payloads](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/concept/ire.html)
  - [docs: Review and remediate de-duplication tasks](https://docs.servicenow.com/bundle/washingtondc-servicenow-platform/page/product/configuration-management/concept/de-duplication-tasks.html)

## Normalization Foundation Data
