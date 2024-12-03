# Asset Management

## TODO

- [ ]

## Resources

- [Software Asset Management](./sn-asset-sam.md)
- [Hardware Asset Management](./sn-asset-ham.md)

### Courses

- [x] [Discovery Extras (Course) Asset and CI Relationships (Content)](https://nowlearning.servicenow.com/lxp?id=learning_course_prev&course_id=9ac281de1b95c050d540b912cd4bcbca)

### Links

- [community: Assets, Configuration Items, and Model Categories: understanding how they work together](https://www.servicenow.com/community/in-other-news/assets-configuration-items-and-model-categories-understanding/ba-p/2279633)
- [docs: Model categories](https://docs.servicenow.com/bundle/xanadu-it-asset-management/page/product/product-catalog/concept/c_ModelCategories.html)

### Labs

- []

## Topics

### Asset and CI Relationships

![Asset and CI Relationships](./attachments/sn-asset-relationships.png)

- [course: Discovery Extras (Course) Asset and CI Relationships (Content)](https://nowlearning.servicenow.com/lxp?id=learning_course_prev&course_id=9ac281de1b95c050d540b912cd4bcbca)
- business rules to sync CI <> Assets
  - Update CI fields on change (on the Asset [alm_asset] table)
  - Update Asset fields on change (on the Configuration Item [cmdb_ci] table)
- main Asset classes:
  - Hardware
  - Software License
  - Consumable
  - Facility
- create additional Asset classes if required, for example Vehicle
- terms:
  - **Asset**: assist with tracking through financial, contractual and leasing lifecycles
    - relevant:
      - Cost
      - Serial number
      - Asset tag
      - Warranty
      - Contracts
      - Who uses it?
      - Where is it?
    - creation - most common: imports & procurement process
      - prerequisites: Model and Model Category
      - when a Catalog Item is associated with a Model, the Asset can be created during procurement
  - **Consumable Assets**: store that you have purchased a quantity and total cost of lower-value Assets
    - wouldn’t track via serial number
    - no CI sync
  - **CI**: track operational and relationship information
    - relevant:
      - Operation details:
        - Operating system
        - Memory
        - CPU
        - Network information
        - File system
        - Installed software
      - Who uses it?
      - Where is it?
  - **Model Category**: drive the automatic creation of assets and CIs
    - **Model Category and Model must be defined before creating an Asset record**
    - references both an Asset class and a CI class
    - if one is created, the other will be created automatically
    - business rules to automatic insert and update of changed attributes on either Asset or CI
      - insert functionality contained in script “AssetandCI”
      - sync functionality contained in script “AssetAndCISynchronizer”
    - sync attributes are mapped in Asset CI Field Mapping [alm_asset_ci_field_mapping]
  - **Model**:
    - template for specific versions or various configurations of an Asset
    - is the common link between Asset (Model) und CI (Model ID)
    - Used for managing and tracking assets through ServiceNow Asset applications, such as:
      - Product Catalogs
      - Asset Management
      - Procurement
    - can be associated to one or more model categories
      - example: Dell Alienware M17 can be part of both Computer and Server model categories and associated CIs would be classified based on the OS they are running
    - required to enable the automated Asset or CI creation via Model Category
  - **Product model class**: Class table where the models are stored. The default values are
    - Application
    - Consumable
    - Contract
    - Facility
    - Hardware
    - Service
    - Software
- automatic record creation exceptions
  - no CI creation for:
    - Consumable Asset
    - License Asset
    - filled value in its Configuration Item field
    - Substatus of Pre-allocated
    - Model Category without CI class field
  - no Asset creation for
    - filled value in its Asset field
    - CI Class returned for SNC.CMDBUtil.isExcludedFromBR(current.getTableName())
    - if Enforce CI Verification is selected on the Model Category
- example:
  - **Model Category**: Computer
    - **Model**: Apple MacBook Pro 15”
  - **Asset Class**: Hardware [alm_hardware]
    - **Asset**: P1000479 - Apple MacBook Pro 15”
  - **CI Class**: Computer [cmdb_ci_computer]
    - **CI**: MaxMustermann-Mac

### Example Asset Import: Mobile Devices - Preparation Notes

- prerequisites
  - Intune - Mobile Devices
    - filter to only create CIs for Phones and Tablets, not Computers
      - how?
        - by Model? how to identify which models are phones and which not? Keep an hardcoded List?
          - normalize Model, check if Model exists, check if Model Category != Mobile Device?
          - how to handle not-preexisting models?
    - Assigned to
      - map against [sys_user], otherwise stays empty?
      - source: email, User Name
    - Carrier
      - normalize (how?)
      - map against [core_company]
      - if not exist, create new record
      - source: Carrier
    - Manufacturer
      - normalize (how?)
      - map against [core_company]
      - if not exist, create new record and set checkmark “Manufacturer”
      - source: Manufacturer
    - identify CI Class: Handheld Computing Device
      - (CI Class Manager or System Definition > Tables)
    - identify Asset class: Hardware
      - [ ] (System Definition > Tables > search “name=*asset || name=*alm”)
    - identify or create Model Category
      - Product model class: Hardware
      - no match for a Model Category with CI Class=Handheld Computing Device
      - candidates:
        - Mobile Device - no mapped CI Class
          - update to map CI Class=Handheld Computing Device?
          - update not possible - delete and recreate?
        - Communication Device (no mapped Asset class)
        - Communication Hardware (no mapped CI class)
        - Computer
          - maps to cmdb_ci_computer, not Handheld Computing Devices
          - Asset class=alm_hardware
    - Model ID
      - normalize (how?)
      - map against Model Category > Product Model Class ([cmdb_hardware_product_model])
        - prerequisite:
          - Manufacturer
          - Model Category
          - anything else?
    - CI Class (Handheld Computing Device)
      - Asset: auto-creation due to Model Category
      - additional reference fields - any additional prerequisites?
        - Change Group
        - Attested By
        - Business Unit
        - Approval group
        - OT asset details
        - Company
        - Cost center
        - CPU manufacturer
        - Department
        - Duplicate Of
        - Life Cycle Stage
        - Life Cycle Stage Status
        - Location
        - Maintenance schedule
        - Managed by
        - Managed By Group
        - Most frequent logged in user
        - Owned by
        - Schedule
        - Supported by
        - Support group
        - Vendor
  - Excel - Mobile Contracts
    - Vendor (Contract)
      - hardcoded: Vodafone (Excel is a Vodafone Export)
    - Rahmenvertrag
      - ast_contract
      - prerequisites?
        - Contract Model?
        - Customer? Hardcoded? Or model?
      - source: unique values for “Rahmenvertrag”
    - Contract
      - ast_contract
      - Parent=Contract where Name=“Column Rahmenvertrag”
    - SIM Cards
      - identify CI Class: cmdb_ci_sim_card
        - (CI Class Manager or System Definition > Tables)
      - identify or create Asset class: Hardware
        - [ ] (System Definition > Tables > search “name=*asset || name=*alm”)
      - identify or create Model Category
        - Product model class: None
          - [ ] no model differentiation required?
        - created Model Category SIM Card, matching CI/Asset Class as defined before
      - Asset Sim Card
        - prerequisites:
          - Assigned to
            - map against [sys_user], otherwise stays empty?
            - source: Teilnehmername?
          - Vendor=Vodafone?
          - Model: required? -> yes for Asset <> CI sync
          - Asset/CI have no field Carrier
        - additional reference fields - any additional prerequisites? - Approval group - Attested By - Business Unit - Change Group - Company - Cost center - Department - Duplicate Of - Life Cycle Stage - Life Cycle Stage Status - Location - Maintenance schedule - Managed by - Managed By Group - OT asset details - Owned by - Schedule - Support group - Supported by - Vendor
      - CI SIM Card to add data, for example SIM Type
