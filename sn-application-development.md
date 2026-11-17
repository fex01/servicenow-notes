# Application Development

## TODO

- [ ] Lab 9.1.1: verify the record producer's stored `Other` choice value and align its script comparison; the course script uses `Other`, while the table choice uses `other`.
- [ ] Lab 6.1.1: confirm the training instance's effective `When` setting for `Set Reserved State`; the notes make the before-save behavior explicit because the guide's basic view does not show it.
- [ ] Validate the labs on the target instance and release; UI labels, availability, plugins, and instance data can vary. Lab 7.2.1 uses an adapted dummy-data example and still needs end-to-end testing.

## Application Development Checklist

- **1. Analyze and design business logic** — [Design and requirements](#design-and-requirements), [server-side logic](#server-side-logic)
  - [ ] Define the business problem and desired outcomes.
  - [ ] Identify user personas and stakeholders.
  - [ ] Identify inputs and outputs.
  - [ ] Map process steps and exceptions.
- **2. Design and build the data model** — [Tables and inheritance](#tables-and-inheritance), [field design](#field-design)
  - [ ] Identify and configure tables.
  - [ ] Define columns and their types.
  - [ ] Define relationships between records.
- **3. Design and create the user interface** — [Form and view design](#form-and-view-design), [UI Policies and Client Scripts](#ui-policies-and-client-scripts)
  - [ ] Design and build the desktop and tablet interface for the intended users.
- **4. Apply security** — [ACL decisions and matching](#acl-decisions-and-matching), [cross-scope application access](#cross-scope-application-access)
  - [ ] Define and assign roles.
  - [ ] Configure and test access controls.
- **5. Automate** — [Flow Designer](#flow-designer-and-integration-hub), [scheduled scripts, events, and notifications](#scheduled-scripts-events-and-notifications)
  - [ ] Configure flows where appropriate.
  - [ ] Configure Scheduled Script Executions where appropriate.
  - [ ] Configure email notifications where needed.
- **6. Integrate** — [Import sets](#import-sets), [REST and web services](#rest-and-web-services)
  - [ ] Plan and test data imports where needed.
  - [ ] Configure and test web services where needed.
- **7. Test** — [Automated Test Framework](#automated-test-framework), [diagnostic paths](#diagnostic-paths)
  - [ ] Test requirements, user access, automation, integrations, and failure cases.
- **8. Enhance the user interface** — [Record producer design](#record-producer-design)
  - [ ] Add a Service Catalog experience where appropriate.
- **Deploy and maintain** — [Source control and deployment](#source-control-and-deployment), [application properties](#application-properties)
  - [ ] Package and deploy the application; establish ownership and operational support.

## Resources

### 📘 Courses

- [Application Development Fundamentals On Demand](https://learning.servicenow.com/lxp/en/now-platform/application-development-fundamentals-on-demand?id=learning_course_prev&course_id=35eefed887bb52d03a3a84c7cebb35f8)
- [Application Development Fundamentals participant guide - Australia](https://servicenow.read.inkling.com/a/b/39150f3ad6644504ae8d102a643a728a/p/6cd650d8bd71445fa5686fcb013c438a) · [local PDF](./course-ebooks/application-development-fundamentals-australia.pdf)
- [Application Developer Skills learning path](https://learning.servicenow.com/lxp/en/app-engine/application-developer-skills?id=learning_path_prev&path_id=2a580f4447e96110ac2f89c2e36d4321)
- [Introduction to Access Controls](https://nowlearning.servicenow.com/lxp/en/now-platform/introduction-to-access-controls?id=learning_course_prev&course_id=3c13324dc3de7d541ac0f60f05013187)
- [Retrieving Update Sets from Remote Instances](https://learning.servicenow.com/lxp/en/now-platform/retrieving-update-sets-from-remote-instances?id=learning_course_prev&course_id=68875453db77585030c91fdc1396197c)
- [Introduction to Access Analyzer](https://nowlearning.servicenow.com/lxp/en/platform-security/introduction-to-access-analyzer?id=learning_course_prev&course_id=f20cef1347c10e582a090dcbd36d43fd)

### 📄 Documentation

- [Application scope](https://www.servicenow.com/docs/r/application-development/c_ApplicationScope.html) · [Namespace identifier](https://www.servicenow.com/docs/r/application-development/c_NamespaceIdentifier.html)
- [NowCreate: Create your own app](https://mynow.servicenow.com/now/best-practices/success-packs/create-your-own-app) · [Delegated development](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/applications/concept/c_DelegatedDevelopment.html)
- [ServiceNow Studio source control](https://www.servicenow.com/docs/r/application-development/servicenow-studio-classic/source-control-integration.html) · [Update sets in Studio](https://www.servicenow.com/docs/r/application-development/servicenow-studio-classic/working-with-update-sets-in-servicenow-studio.html)
- [JavaScript engine](https://www.servicenow.com/docs/r/api-reference/scripts/c_JS_engine_upgrade.html) · [ES12 for individual scripts](https://www.servicenow.com/docs/r/api-reference/scripts/set-es12-mode-scripts.html)
- [ACL overview](https://www.servicenow.com/docs/r/platform-security/access-control/exploring-access-control-list.html) · [Deny-Unless ACL](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html)
- [Application access settings](https://www.servicenow.com/docs/r/application-development/c_ApplicationAccessSettings.html) · [Script Includes](https://www.servicenow.com/docs/r/api-reference/scripts/c_ScriptIncludes.html)
- [Access Analyzer](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/integrate/identity/concept/access-analyzer.html) · [Flow execution details](https://www.servicenow.com/docs/bundle/yokohama-build-workflows/page/administer/flow-designer/concept/flow-execution-details.html) · [Notification variables](https://docs.servicenow.com/csh?topicname=notification-variables.html&version=latest)
- [REST authentication](https://www.servicenow.com/docs/r/api-reference/web-services/c_OutboundRESTAuth.html) · [Basic authentication profile](https://www.servicenow.com/docs/r/api-reference/web-services/t_ConfigureRESTMsgBasicAuth.html)
- [Property cache-flush troubleshooting](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0822644) · [When to Use Ignore Cache](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1000746)

### Related notes

- [Scripting](./sn-scripting.md) · [Flow Designer](./sn-flow-designer.md) · [Automated Test Framework](./sn-atf.md) · [App Engine Studio](./sn-app-engine-studio.md)

## Foundations and Application Scope

### Development lifecycle and fit

- Work in increments: analyze → design → build → test → deploy; identify owners and operational support before release.
- A typical platform fit has relational records, a request/fulfill process, forms, access controls, automation, and reporting. Validate business value and platform/licensing constraints before building.
- Use the [application development checklist](#application-development-checklist) to plan work and find related notes.
- Design for personas and measurable outcomes rather than matching a solution to a preconceived feature.

### Application scope and namespace

- Scope associates an application's artifacts with a namespace and controls access from other applications. Private scope is the normal choice for new custom applications; Global remains relevant for existing global artifacts and dependencies.
- Namespace pattern: `x_<company_code>_<application_id>`; the generated name can be truncated. The instance company prefix is held in `glide.appcreator.company.code`.
- Scope selection matters at creation time; select the correct application before creating files. The namespace of existing application artifacts cannot simply be renamed in place; plan any transition/rebuild separately.
- Out-of-scope warnings indicate the artifact belongs to another application. Switching scope for a specific change is different from moving the artifact.
- Delegated development grants non-admins application-specific file, scripting, security, and deployment permissions. Grant only the file types and actions required.

## Application Design and Data Model

### Design and requirements

- Define the business problem, desired outcomes, stakeholders, and personas. For each process, capture inputs and source, outputs and recipients, frequency, state changes, exceptions, and owner.
- Document entities, fields, relationships, retention, integration ownership, and expected data volume. Design UI and access around personas.
- Use acceptance criteria and test cases to verify both expected behavior and denied access. See [ATF notes](./sn-atf.md).

### Tables and inheritance

- **Extend** an extensible table when its data and behavior fit; child tables inherit fields and applicable parent behavior. Use dictionary overrides where needed and verify inherited automation and reference qualifiers.
- **Create a new table** when no suitable parent exists or independent behavior is needed; review custom-table entitlement and performance limits.
- Default fields include `sys_id`, `sys_created_on`, `sys_created_by`, `sys_updated_on`, `sys_updated_by`, and `sys_mod_count`; extensible tables also use `sys_class_name`.
- Inspect existing logic from a list's column menu → _Configure_ → _All_, or navigate to `<table_name>.config`. Use `Columns` and the table column to distinguish inherited fields.
- Table `Controls` can configure auto-numbering, extensibility, modules, and generated ACLs. Application Access is separate from user authorization; see [Cross-scope application access](#cross-scope-application-access).

### Field design

- Choose appropriate types early: `Reference` for related records, `Choice` for constrained values, `Date/Time` for timestamps, and numeric types for numbers. Type changes and field deletion can affect data.
- Prefer reuse where semantics fit. Relabeling can clarify a form but leaves the underlying column name unchanged; avoid changing parent behavior unintentionally.
- Removing a field from a form changes layout; deleting a column is a data-model change and can remove its stored values. Inherited fields cannot be deleted from the child as if locally defined.
- Form Builder: Studio → _Create_ → `File` → `Data` → `Form` → select table → _Open_; add or arrange fields, sections, and formatters → _Save_.

## Studio and Application Files

### Studio workflow

- ServiceNow Studio organizes application files, app details, scope, source control, and deployment; use the main instance UI to work with application data.
- Create a scoped app: **All > ServiceNow Studio** → _Create_ → `App` → `On your own` → _Continue_ → name, description, and `Scoped` → review generated roles → _Continue_.
- Create an artifact: Studio → _Create_ → `File` → choose application/scope, category, and file type → _Continue_ → configure → _Submit_.
- Studio interfaces and available features vary by release and installed Store app; check the instance before applying a release-specific path.

### Application menus and modules

- Menu roles control access to the application menu; module roles add navigation restrictions. Hiding navigation does not secure records; use ACLs.
- Common link types: `New Record`, `List of Records` (optional filter), `URL (from Arguments)`, `Separator`, and `Map Page`.
- `Override application menu roles` changes menu/module visibility behavior; test as the intended user. Module ordering is controlled by `Order`.

## Forms, Views, and Client Logic

### Form and view design

- Keep forms short, use descriptive labels and contextual help, place primary identifiers near the top, group related fields, and use full-width rows for longer text.
- A view is a saved layout for the same underlying records; it is not a security boundary. Use views for personas and devices, and enforce data access with ACLs.
- In Form Builder, select a view → _Add_, _Duplicate this form view_, or edit its layout → _Save_. A View Rule can select a view using conditions or server-side script.
- Typical feedback APIs: `g_form.showFieldMsg()`, `g_form.hideFieldMsg()`, `g_form.addInfoMessage()`, and `g_form.addErrorMessage()`.

### UI Policies and Client Scripts

- **UI Policies** apply conditional client-side behavior to fields. UI Policy Actions set `Mandatory`, `Visible`, and `Read only`; `Leave alone` preserves a property and `Reverse if false` reverses configured actions.
- Configure table, view applicability, condition, `On load`, order, and optional true/false scripts; test both transitions and initial form load.
- **Client Scripts** handle `onLoad`, `onChange`, `onSubmit`, or `onCellEdit` behavior. Configure UI type, table, and field/view as applicable; keep client logic responsive.
- `g_form` controls the form; `g_user` provides user information. Never rely on client-side role checks to enforce security.
- A display Business Rule can pass server values through `g_scratchpad` to an onLoad Client Script. `g_form.getReference(field, callback)` is asynchronous; use sparingly and consider GlideAjax for tailored server data.
- Detailed APIs and patterns: [Scripting notes](./sn-scripting.md).

## Server-side Logic

### JavaScript modes

- Modes: ECMAScript 2021 (`ES12`), ES5 Standards, and Compatibility. Check the application **and individual script** settings and the supported-feature table; the platform supports a subset of each standard.
- Since Xanadu, ES12 is enabled by default for newly created scripts regardless of the application's configured mode; global applications can enable ES12 for individual scripts. Existing scripts and applications may retain older modes.
- Test behavior before changing the mode of existing scripts; do not assume all Global scripts run in Compatibility mode.

### Business Rules and reusable logic

- Business Rules run server-side on configured table operations: `before` for validation/current-record changes; `after` for reactions after save; `async` for deferred work; `display` to prepare `g_scratchpad`.
- Configure operations, conditions, order, and advanced script as required. In a before rule, `current.setAbortAction(true)` rejects the database action.
- Avoid `current.update()` in Business Rules: it can trigger recursion. Changes to `current` in before rules are saved with the transaction.
- Script Includes centralize reusable server-side logic; the class/function name must match the record name. Configure `Accessible from`, active state, and protection policy deliberately.
- Protection policy affects installed/downloaded application files: `None`, `Read-only`, or `Protected`; it does not replace source-instance authorization.
- More examples: [Business Rules and Script Includes](./sn-scripting.md).

## Security and Cross-Scope Access

### ACL decisions and matching

- ACLs secure an object and operation with roles, security attributes, data conditions, and/or script. All configured requirements of an individual rule must pass.
- `Deny-Unless` is evaluated before `Allow-If`; a failing applicable Deny-Unless denies access. A passing Deny-Unless is not the same as a general grant; evaluate applicable Allow-If rules and the documented fallback behavior.
- Record access is evaluated before field access. `<table>.--None--` targets the record, `<table>.<field>` a field, and `<table>.*` a wildcard field rule; matching rules follow table inheritance and specificity; a successful field evaluation stops further field matching.
- Example field search for `incident.number`: `incident.number` → `task.number` → `*.number` → `incident.*` → `task.*` → `*.*`; verify actual evaluation with the platform's security debugger.
- Role requirements within one ACL are alternatives; other configured requirements on that rule must also pass. Multiple matching rules and decision types require their own evaluation—do not infer denial from one Allow-If failure alone.
- Menu/module roles govern navigation, not direct table or field access. Test records and fields using users with each relevant role, including a user who should be denied.

### ACL administration and troubleshooting

- Elevate `security_admin` before creating/editing ACLs; remove elevation after use. In Studio, save an application file to refresh permissions if the file type is not yet visible after elevation.
- On a list, _Configure_ → _Security Rules_ to inspect relevant rules. Use **System Security > Debugging > Debug Security Rules** and _Stop Debugging_ when finished.
- [Access Analyzer](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/integrate/identity/concept/access-analyzer.html) helps investigate effective access; check release and Store-app availability.
- Server-side checks such as `gs.hasRole()` and GlideRecord `canCreate()`, `canRead()`, `canWrite()`, and `canDelete()` support authorized server logic; client checks are not enforcement.

### Cross-scope application access

- ACLs restrict **users**; Application Access restricts **other application scopes**. Both can matter for an operation.
- Table `Application Access`: `Accessible from` is `This application scope only` or `All application scopes`; `Can read/create/update/delete` govern cross-scope operations, not the application's own scope.
- `Allow access to this table via web services` controls service access in conjunction with caller permissions; `Allow configuration` governs cross-scope configuration.
- `Caller Access`: `None`, `Caller Tracking`, or `Caller Restriction`; inspect Restricted Caller Access records and approve requests only when appropriate.

## Automation and Notifications

### Flow Designer and Integration Hub

- Flows combine a trigger, actions, flow logic, data pills, and optional subflows. Triggers can be record-based, scheduled, or application-based.
- Test with representative records → inspect execution details and action inputs/outputs → activate. Flow tests can create or update records; use a non-production instance.
- `Wait for Condition` pauses until record criteria match; `Create Task` can wait for completion; `Update Record` modifies the selected record.
- Integration Hub provides reusable integration actions packaged in spokes; availability and licensing vary. See [Flow Designer notes](./sn-flow-designer.md).

### Application properties

- Use properties for relatively stable configuration, not high-frequency state. Read a property with `gs.getProperty('<scope>.<name>', '<default>')`; control read/write roles.
- Property category → add and order System Properties → expose with a role-protected module. URL pattern: `system_properties_ui.do?sysparm_title=<title>&sysparm_category=<category>`.
- `Ignore cache` changes cache-flush behavior when a property is updated; it is not simply a stale-value switch. Frequent changes can still affect performance. Consult the linked support guidance and test operational impact.

### Scheduled scripts, events, and notifications

- Scheduled Script Executions run server-side on a schedule or on demand, without an automatic record `current` context. Save before _Execute Now_; inspect **System Scheduler > Scheduled Jobs**.
- Register an event → queue it using `gs.eventQueue('<event_name>', record, parm1, parm2)` → respond through a notification and/or Script Action. Inspect **System Logs > Events**.
- Notification configuration: `When to send`, `Who will receive`, and `What it will contain`. Common substitutions: `${field}`, `${event.parm1}`, `${URI}`, and `${URI_REF}`.
- Check the recipient's notification preferences, preview a representative record, and inspect **System Logs > Emails**. A Script Action receives the event and record and runs server-side.

## Integration and Data Import

### Import sets

- Load source data into a staging table → create a Transform Map → map source fields to target fields → set coalesce for record matching → transform → inspect import-set rows, errors, and target records.
- Confirm target access, data types, duplicates, business-rule behavior, and rollback/repair strategy before a production import.

### REST and web services

- Outbound REST: create a REST Message and HTTP method; configure endpoint, authentication profile, headers, query parameters, and variable substitutions; test status **and response body** before using a script.
- Methods: `GET` read, `POST` create, `PUT` replace, `PATCH` modify, `DELETE` remove. Parse JSON/XML according to the actual response; handle empty results and failures.
- REST API Explorer: **System Web Services > REST > REST API Explorer**. Choose operation, table/path, query, fields, and headers → _Send_. Use non-production for any operation that can alter records.
- Build complex filters on a list and copy the breadcrumb query to `sysparm_query`; use `sysparm_fields` to limit returned fields.
- Use an appropriate Basic Auth or OAuth profile rather than embedding credentials in scripts. Avoid logging or emailing passwords; the course's credential example is an isolated training exercise only.

## Testing and Troubleshooting

### Automated Test Framework

- ATF tests consist of ordered test steps and can create users, impersonate, open forms, set values, submit, and assert results. ATF rolls back tracked test changes, including changes made in the same session; excluded tables (including `sys_email` and ECC queue tables and their extensions) and external effects persist. See [ATF rollback exclusions](https://www.servicenow.com/docs/r/application-development/automated-test-framework-atf/atf-excluded-from-rollback.html).
- Enable execution only on an appropriate non-production instance: **Automated Test Framework > Administration > Properties**. Run tests and inspect step results, client errors, and screenshots.
- Test Management supports manual test plans and execution. Detailed ATF administration and patterns: [ATF notes](./sn-atf.md).

### Diagnostic paths

- Access: **System Security > Debugging > Debug Security Rules**, Access Analyzer, and impersonation.
- Automation: Flow Designer execution details and action outputs; **System Logs > Events** for queued events; **System Logs > Emails** for notifications.
- Imports: import-set row states and transform results; integrations: response status/body and permitted outbound logs; avoid sensitive values in logs.

## Source Control and Deployment

### Choosing a mechanism

- **Git source control**: track application metadata, branch, commit, and collaborate during development. Current Studio supports source-control operations for scoped/global applications on non-production instances; capabilities and UI vary by release.
- **Update sets**: group and migrate captured configuration changes; check contents, dependencies, preview, resolve collisions, then commit on the target. Ordinary business data is generally not captured by default.
- **Application repository**: publish versioned application packages for installation/update across an organization's instances. **ServiceNow Store** is for approved broader distribution.
- A branch isolates work; a stash temporarily shelves local changes. Source control is not itself a production deployment mechanism.

### Publishing and retrieving

- Publish an app to an update set: Studio → app details → _More Options_ → _Settings_ → _Publish to Update Set_ → version and description → _Publish_; inspect `Customer Updates`.
- Publish to repository: Studio → app details → _More Options_ → _Publish_ → review version and release notes → _Publish_. On the target, **System Applications > My Company Applications** → `Not Installed` → _Install_; for upgrades use `Installed` and select the version → _Update_ → _Install_.
- Retrieve a completed update set on the target using **System Update Sets > Update Sources** → configured source → _Retrieve Completed Update Sets_; inspect **Retrieved Update Sets**, preview, resolve issues, and commit.
- Selected demo records can be packaged as application files from a list's column options → _Create Application Files_ → choose `Load When`; validate data and dependencies on the target.
- Avoid assuming update sets, repository packages, and Git contain identical data or dependencies. Test version compatibility and rollback in non-production.

## Service Catalog and Record Producers

### Record producer design

- A record producer is a catalog item that creates a target-table record from questions; a standard catalog item typically produces requested items. Choose a producer for a guided submission experience and a form/list when users need record editing or list behavior.
- Create from the target table's _Add to Service Catalog_ related link → configure selected fields; use Catalog Builder to adjust questions, help, layout, and destination.
- Catalog UI Policies and Catalog Client Scripts operate on **variables**. A producer script runs server-side before insert: `producer` contains submitted variables and `current` is the new target record. Do not call `current.update()`.
- A module can open the producer with link type `URL (from Arguments)` and `com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=<producer_sys_id>`.

## Labs

- **Baseline**: Application Development Fundamentals **Australia** participant guide; lab numbers below refer to this edition. Older notes used different numbering and update-set checkpoints—do not combine steps by number alone.
- Labs are sequential and use a non-production training instance. UI names and external service screens can vary by release; full scripts are included where the course uses macros.

- Lab scripts below use the course instance's scope `x_cdltd_loaner_r_0`; if your instance generates a different scope or table name, substitute it consistently in scripts, event names, roles, REST-message names, and property names.

### Lab 2.2.1 - The Loaner Request application

🎯 **Goal**: Examine the requirements, process, data model, and interface design for the application built in later labs.

- **A. Review the design**
  - Business problem: requests for laptops, phones, and projectors are managed through email and spreadsheets, are difficult to track, and can be missed.
  - Outcomes: one request location, timely fulfillment, retired spreadsheets, higher requester satisfaction, and automation wherever possible.
  - Personas: `Employee Self-Service` can submit through an available producer or catalog item; `User/Requester` creates requests, sees `Create New` and `Open`, reads records where `Requested for` is the user, and uses Self Service view; `Administrator/Fulfiller` sees all modules and views and can create, read, edit, and delete requests.
  - Inputs: form and catalog submissions as needed, unique by platform-assigned number; a one-time `.xls` import, unique by request ticket number.
  - Outputs: pickup, return, and overdue email to `Requested for`; weekly statistics to the CTO; on-demand statistics for authorized users.
  - Process: create pre-deployment and post-deployment tasks; check for pickup, return, and overdue items; notify the requester and repeat overdue reminders until return.
  - Data model: `Loaner Request` has `Number`, `Requested for` (reference to User), `Configuration item` (reference to CMDB), `Assignment Group` (reference to Group), `Assigned to` (reference to User), `State`, `Start date`, `End date`, `Item type`, `Location to be used`, `Depot`, `Short description`, and `Description`.
  - `Loaner Task` includes `Number`, `Assigned to` (User reference), `State`, `Priority`, `Short description`, `Description`, `Work notes`, `Additional Comments`, and `Parent` (Loaner Request reference). The requested-for User data includes `User name`, `Email`, `Manager` (User reference), and `Notifications`.

### Lab 3.2.1 - Create an application

🎯 **Goal**: Create a scoped Loaner Request application and inspect its generated files.

- **A. Create the application**
  - Open **All > ServiceNow Studio** → _Create_ → `App` → `On your own` → _Continue_.
  - Set `Name = Loaner Request`, `Description = App that enables users to check out loaner equipment.`, and `Scope = Scoped`; select _Continue_.
  - Leave the generated admin and user roles in place → _Continue_ → _View app details_.
  - Refresh the Apps list, select `Loaner Request`, and review its application details and generated files.

### Lab 3.3.1 - Create application files

🎯 **Goal**: Create the Loaner Request table, navigation modules, and a user group.

- **A. Create the table**
  - In Studio, _Create_ → `File` → select application `Loaner Request` → `Data` → `Table` → _Continue_.
  - Set `Label = Loaner Request`, `Extends table = Task`, and clear `Create mobile module`; leave the generated name.
  - On `Controls`, select `Auto-number`; set `Prefix = LNR`, `Number = 2000`, `Number of digits = 6`, and `User role = x_cdltd_loaner_r_0.user`; retain `Create access controls` → _Submit_.
  - Close the welcome dialog → _More Options_ → `Advanced view` → `Application Access`; verify `Accessible from = All application scopes`, `Can read = selected`, and `Allow access to this table via web services = selected`.
  - Review `Columns` for inherited Task fields and automatically created fields; refresh the Studio navigator to view the generated artifacts.
- **B. Inspect scope**
  - In the main instance, refresh the browser → open the scope selector → inspect the `Loaner Request` scope record.
  - In Studio, open **Apps > Loaner Request > App details** → _More Options_ → _Settings_ to inspect the application record.
- **C. Create navigation modules**
  - In Studio, _Create_ → `File` → application `Loaner Request` → `User Interface` → `Module [sys_app_module]` → _Continue_.
  - Create `Create New`: `Application menu = Loaner Request`, `Order = 200`, `Link type = New Record`, `Table = Loaner Request` → _Submit_.
  - Repeat with `Link type = List of Records`, `Table = Loaner Request`, and `Application menu = Loaner Request`:
    - `Open`: `Order = 400`; filter `Active is true`.
    - `Open - Unassigned`: `Order = 500`; filter `Active is true AND Assigned to is empty`.
    - `Closed`: `Order = 600`; filter `Active is false`.
  - Open **User Interface > Module > Loaner Requests**, change `Title` to `All`, and position it after `Open`.
  - Refresh the main navigator; search `Loaner Request`. If missing, refresh menus or switch to `Global` scope and back.
- **D. Test and create the group**
  - Open **Loaner Request > Create New**; create open and `Closed Complete` records, then test the `All`, `Open`, and `Closed` modules.
  - Open **User Administration > Groups** → _New_; set `Name = Loaner Request Users` and a description → _Save_.
  - On `Roles`, _Edit_ → move `x_cdltd_loaner_r_0.user` to the selected list → _Save_. On `Group Members`, _Edit_ → add `Beth Anglin` → _Save_ → _Update_.

### Lab 3.4.1 - Link the application to source control (optional)

🎯 **Goal**: Link the scoped application to a private GitHub repository.

- **A. Create a repository and token**
  - In GitHub, select _New repository_: `Repository name = adf_loaner_request`, `Visibility = Private`; leave README, `.gitignore`, and license initialization unchecked → _Create repository_.
  - Copy the HTTPS repository URL: `https://github.com/<github-username>/adf_loaner_request.git`.
  - Open **Profile > Settings > Developer settings > Personal access tokens > Fine-grained tokens** → _Generate new token_.
  - Set a descriptive token name and expiration; under `Repository access`, choose `Only select repositories` → `adf_loaner_request`. Under `Repository permissions`, set `Contents = Read and write` → _Generate token_ → copy the token for the next step.
- **B. Link the app**
  - In ServiceNow, open **Connections & Credentials > Credentials** → _New_ → `Basic Auth Credentials`; set `Name = GitHub`, `User name = <github-username>`, `Password = <personal-access-token>`, and `Active = selected` → _Submit_.
  - In ServiceNow Studio, open **Apps > Loaner Request > App details > Source control** → _Link to source control_; enter the HTTPS URL, `Branch = main`, and `Credential = GitHub` → _Link to source control_ → _Close_.
  - Refresh the GitHub repository; select `main` and verify its initial commit and application files. The course instance sets its Git default-branch properties to `main`.
  - The [course-linked Studio walkthrough](https://www.servicenow.com/community/developer-advocate-blog/source-control-in-servicenow-studio-complete-walkthrough/ba-p/3356303) also shows a repository initialized with a README and an instance-specific branch. If using that branch instead of `main`, select it in GitHub to inspect the application files.

### Lab 4.1.1 - Working with fields and views

🎯 **Goal**: Configure the Loaner Request form and a Self Service view.

- **A. Configure the Default form**
  - In Studio, _Create_ → `File` → `Data` → `Form` → select `Loaner Request` → _Open_ → complete the Table Builder introduction.
  - Remove `Parent`, `Priority`, and `Active` from the form; _Save_.
  - Add `Requested for`: `requested_for`, type `Reference`, reference `User [sys_user]`, `Mandatory = selected`.
  - Add `Start date` (`start_date`) and `End date` (`end_date`): type `Date/Time`, `Mandatory = selected`; place them on the form and _Save_.
  - Add `Item type` (`item_type`, `Choice`); configure `Laptop = cmdb_ci_computer`, `Mobile Phone = cmdb_ci_mobile_device`, `Projector = cmdb_ci_projector`; `Show choices as = Dropdown` → _Apply_ → _Save_. Refresh Studio and set default `cmdb_ci_computer`.
  - Add `Depot` (`depot`, `Choice`) with `New York = ny`, `London = london`, `Buenos Aires = ba`, `Santa Clara = sc`, `Singapore = singapore`, `Sydney = sydney`, and `Other = other`; use `Dropdown` and default `sc` → _Save_.
  - Switch scope to `Global`; edit inherited `State` choices to `Requested = 13`, `Reserved = 14`, `Deployment Prep = 15`, `Ready for Pickup = 16`, `Checked Out = 17`, `Post Deployment = 18`, and `Closed Complete = 3`. Use `Dropdown`, confirm the override, and _Save_. Switch back to `Loaner Request`; set default `13` → _Save_.
    - mark other choices as inactive
  - Add `Location to be used` (`location_to_be_used`, `String`); place above `Depot`. Arrange the top section as left column `Number`, `Requested for`, `Configuration item`, `Assigned to`; right column `State`, `Start date`, `End date`, `Item type`, `Location to be used`, `Depot`; place `Short description` and `Description` full-width below.
  - Add `Log` section: `Additional comments`, `Work notes`, and `Activities (filtered)` formatter. Add a two-column `Statistics` section: left `Opened`, `Updated`, `Closed`; right `Opened by`, `Updated by`, `Closed by`, `Active` → _Save_.
- **B. Create and test the Self Service view**
  - Next to `Default view`, _More actions_ → _Duplicate this form view_; enter `ESS` → _Create_. The existing view's title displays as `Self Service`.
  - Configure two columns: left `Number`, `Requested for`, `Start date`, `End date`; right `State`, `Item type`, `Location to be used`. Retain a merged section with `Short description`, `Description`, and `Activity formatter`; remove the remaining fields and sections → _Save_.
  - Open an existing Loaner Request → Form Header context menu → **View > Self Service**; verify the layout. If existing records show numeric state `1`, select a valid state and save each affected record.

### Lab 4.2.1 - Create a UI Policy

🎯 **Goal**: Show and require the Other field only when Depot is Other, with a single explanatory message.

- **A. Add the field and policy**
  - Open the Loaner Request Default form in Studio → add `Other` (`other`, `String`) below `Depot` → _Save_.
  - Select `Other` → `UI Policies` → _Add a UI Policy_. Set `Short Description = Make ‘Other’ field visible and mandatory – Loaner Request`, `Order = 100`, and `Active = selected`.
  - In `Advanced settings`, select `Apply to all views`, `On load`, and `Reverse if false`; clear `Inherit`. Set condition `Depot is Other`.
  - Add action `Field name = Other`, `Mandatory = True`, `Visible = True`, `Read only = Leave alone` → _Add UI Policy_ → _Save_.
- **B. Add and test scripts**
  - Open **Client Development > UI Policy > Make 'Other' field visible and mandatory** → `Advanced view` → `Script`; select `Run scripts`, `Run scripts in UI type = All`.
  - Set true script to `function onCondition() { g_form.showFieldMsg('other', 'Where will you pick up the loaner?', 'info'); }`.
  - Set false script to `function onCondition() { g_form.hideFieldMsg('other'); }` → _Update_.
  - In a Loaner Request Default view, switch `Depot` to `Other`, away, and back; verify visibility, mandatory state, and exactly one message.

### Lab 4.2.2 - Scripting

🎯 **Goal**: Set client fields, pass display data to the client, and validate dates on the server.

- **A. Set item type on change**
  - Studio → _Create_ → `File` → `Client Development` → `Client Script`; set `Name = Set Loaner Item Type`, `Table = Loaner Request`, `UI Type = Desktop`, `Type = onChange`, `Field name = Configuration item`, and `Description = Set Item type field automatically for mobiles.`
  - Replace the default script with the following course example → _Submit_. It uses an asynchronous `g_form.getReference` callback and case-insensitive matching:
    ```javascript
    function onChange(control, oldValue, newValue, isLoading, isTemplate) {
      if (isLoading) return;
      g_form.getReference("cmdb_ci", checkName);
      /* This grabs the record for the configuration item, 
    then performs the below function using that record. 
    See additional note below for usage tips. */
      function checkName(ci) {
        var name = ci.name + "";
        // Check the name of the CI using regular expressions;
        // Set and lock Item type field based on the CI name.
        if (
          name.match(/.*blackberry.*/i) ||
          name.match(/.*iphone.*/i) ||
          name.match(/.*android.*/i)
        ) {
          g_form.setValue("item_type", "cmdb_ci_mobile_device", "Mobile Phone");
          g_form.setReadOnly("item_type", true);
        } else if (name.match(/.*macbook.*/i)) {
          g_form.setValue("item_type", "cmdb_ci_computer", "Laptop");
          g_form.setReadOnly("item_type", true);
        } else {
          g_form.setReadOnly("item_type", false);
        }
      }
      /***** 
    Yes, g_form.getReference() fell from grace as a recommended practice some releases ago. 
    However, it is still broadly used in a pinch to fetch a single record without using the rigors of 
    GlideAJAX; a quick code search will confirm hundreds of occurrences. 
    Use with caution! For more information: 
    https://developer.servicenow.com/dev.do#!/reference/api/vancouver/client/c_GlideFormAPI#r_GlideForm-GetReference_S_F?navFilter=getR
    *****/
    }
    ```
  - Test a matching configuration item in a Loaner Request and verify the item type and read-only state.
- **B. Pass location using a display rule**
  - Create `Business Rule`: `Name = Set Scratchpad Values`, `Table = Loaner Request`, `Active = selected`, `Advanced = selected`, `When = display`, `Order = 100`.
  - Set the Business Rule `Script` to the following → _Submit_:
    ```javascript
    (function executeRule(current, previous /*null when async*/) {
      g_scratchpad.city = current.requested_for.city;
      g_scratchpad.country = current.requested_for.country;
      // Hooray for dotwalking!
      // By writing these values to the scratchpad, a client script can easily fetch them.
    })(current, previous);
    ```
  - Create `Client Script`: `Name = Set Loaner Location`, `Table = Loaner Request`, `UI Type = All`, `Type = onLoad`, `Description = Automatically set 'Location to be used' field value based on user location.` Set `Script` to the following → _Submit_:
    ```javascript
    function onLoad() {
      // This uses the dotwalking superpowers of the Scratchpad to use the requestor's city & state as the default location to be used. Make sure whomever you use for testing has values in their user record for this!
      if (g_form.getValue("location_to_be_used") != "") {
        return;
      }
      var city = g_scratchpad.city;
      var country = g_scratchpad.country;
      if (city && country) {
        g_form.setValue("location_to_be_used", city + ", " + country);
      } else if (city) {
        g_form.setValue("location_to_be_used", city);
      } else if (country) {
        g_form.setValue("location_to_be_used", country);
      }
      if (city || country) {
        g_form.showFieldMsg(
          "location_to_be_used",
          "Value set automatically - you may override by editing",
          "info",
        );
      }
    }
    ```
  - In `sys_user.list`, add and populate `City` and `Country code` for a test user. In **Loaner Request > All**, add `Requested for` and `Location to be used` through column controls → _Configure_ → _List Layout_. Set a blank-location record's `Requested for` in the list, save, and open the record to verify the location.
- **C. Validate dates**
  - Create `Business Rule`: `Name = Validate Start and End Dates`, `Table = Loaner Request`, `Active = selected`, `Advanced = selected`, `When = before`, `Insert = selected`, `Update = selected`.
  - Set `Script` to the following → _Submit_. For `end_date < start_date`, it displays an error and aborts the transaction:
    ```javascript
    (function executeRule(current, previous /*null when async*/) {
      if (current.end_date < current.start_date) {
        gs.addErrorMessage("End date must be on or after start date!");
        current.end_date = "";
        current.setAbortAction(true);
        // This rejects the submission of the record if you set the end date before the start date
        // Food for thought: why was script used here rather than a scriptless business rule?
      }
    })(current, previous);
    ```
  - Create a record with end before start; verify that submission is rejected. Test equal start and end timestamps and verify that they are accepted. Open the Default form's `Policies and rules` to inspect related logic.

### Lab 4.3.1 - Publish to Update set

🎯 **Goal**: Package the current Loaner Request application into an update set.

- **A. Publish and inspect**
  - Studio → **Apps > Loaner Request > App details** → _More Options_ → _Settings_ → _Publish to Update Set_.
  - Verify `Version = 1.0.0`; set `Description = Loaner Request app - module 4.` → _Publish_ → _Done_.
  - Review the `Customer Updates` related list for captured files.

### Lab 4.3.2 - Publish to the application repository

🎯 **Goal**: Publish the scoped application and review installation on another instance.

- **A. Commit and publish**
  - Optional: Studio app details → **Source control > Commit changes** → select changed files → _Continue_ → `Commit comment = Loaner Request application with module 4 labs completed.` → _Commit files_ → _Close_.
  - App details → _More Options_ → _Publish_ → review version and release notes → _Publish_ → _Done_.
- **B. Install on a second instance**
  - The training instance has no full Dev/Test/Prod stack; review rather than execute this part there.
  - On a destination instance, open **System Applications > My Company Applications > Not Installed** → locate `Loaner Request` → _Install_ → _Install_ → _Close_; verify under `Installed`.

### Lab 5.1.1 - Configure application security

🎯 **Goal**: Restrict navigation, records, and views for administrator, requester, and non-user personas.

- **A. Configure roles and groups**
  - In Studio, **Loaner Request > Security > Role > x_cdltd_loaner_r_0.admin** → `Contains Roles` → _Edit_ → add `x_cdltd_loaner_r_0.user` → _Save_ → _Update_.
  - In **User Administration > Groups**, create `Loaner Request Admins` with description `Loaner Request application users with the Loaner Request Admin role.` → _Save_; add the application admin role on `Roles` → _Save_ → _Update_.
  - In **User Administration > Users**, add `System Administrator` and `Fred Luddy` to `Loaner Request Admins`; remove Fred's platform `admin` role. The prior lab placed `Beth Anglin` in `Loaner Request Users`.
- **B. Restrict modules**
  - In Studio, open **User Interface > Module > All**; under `Visibility`, replace the application user role with `x_cdltd_loaner_r_0.admin`. Repeat for `Closed` and `Open - Unassigned`; the module form autosaves.
- **C. Configure ACLs**
  - In Studio's user menu, _Elevate role_ → select `security_admin` → _Update_.
  - Open **Security > Access Control > x_cdltd_loaner_r_0_loaner_request**; locate the `read` ACL and replace the required user role with `x_cdltd_loaner_r_0.admin` → _Update_. Repeat for `delete`.
  - _Create_ → `File` → `Access Control` → _Continue_; create `Type = record`, `Operation = read`, `Decision type = Allow if`, `Name = Loaner Request / --None--`, `Active = selected`, `Admin overrides = selected`, required role `x_cdltd_loaner_r_0.user`, condition `Requested for is (dynamic) Me` → _Submit_ → verify → _Continue_.
  - Create another record/read `Allow if` ACL for `Loaner Request / --None--`, with `Active`, `Admin overrides`, and `Advanced` selected; require `x_cdltd_loaner_r_0.user`; set `Advanced Condition` to `current.isNewRecord();` → _Submit_ → verify → _Continue_.
  - Confirm the original `create` and `write` ACLs still require the user role. Remove `security_admin` elevation through the user menu.
- **D. Force a view and test**
  - _Create_ → `File` → `View Rule [sysrule_view]`; set `Name = Users see only ESS view`, `Table = Loaner Request`, `Device type = Browser`, `Active = selected`, `Advanced = selected`.
  - Inside `overrideView()`, use `if (!gs.hasRole('x_cdltd_loaner_r_0.admin')) { answer = 'ess'; }` → _Submit_.
  - Impersonate `Fred Luddy`: verify all modules, all records, create/edit/delete, and all views. Impersonate `Beth Anglin`: verify `Create New` and `Open`, creation, own requested-for records, and Self Service view. Impersonate `Abel Tuter`: verify no application access. End impersonation.
  - Optional: commit changed files with `Loaner Request application with Lab 5.1.1 completed.`

### Lab 5.2.1 - Set application access (optional)

🎯 **Goal**: Test cross-scope read and update permissions with a Global scheduled script.

- **A. Prepare access and records**
  - End impersonation and elevation. In Studio, **Data > Table > Loaner Request** → _Additional actions_ → `Advanced view` → `Application Access`.
  - Set `Accessible from = All application scopes`, `Caller Access = Caller Tracking`, `Can read = selected`, `Can create/update/delete = cleared`, and `Allow access to this table via web services = selected` → _Update_.
  - In **Loaner Request > All**, ensure at least four active requests exist.
- **B. Test Global caller access**
  - Studio → _Create_ → `File` → application/scope `Global` → `Scheduled Script Execution`; set `Name = Update LNRs from Global`, `Run = On Demand`.
  - Set `Script` to the following → _Submit_. The query limits the exercise to three non-closed records:
    ```javascript
    /*  
    Run this script from Global scope both BEFORE _and_ AFTER 
    checking "Can update" from the Loaner Request Table's Application Access section.
    */
    // This method _should_ address occasional instance "bad behavior" during this demo.
    gs.invalidateCache();
    // Look up open LNR records
    var loanerRecs = new GlideRecord("x_cdltd_loaner_r_0_loaner_request");
    loanerRecs.addQuery("state", "!=", 3); // not Closed Complete
    loanerRecs.setLimit(3); // let's not get carried away...
    loanerRecs.query();
    // We're in Global scope — in other words, "out of scope." Can we close the LNR records?
    while (loanerRecs.next()) {
      loanerRecs.setValue("state", 3); // mark Closed Complete
      loanerRecs.update(); // save the records
    }
    // No dice closing them out? Try checking the "Can update" box on the Loaner Table, then try again!
    ```
  - Open Loaner Request app details → _More Options_ → _Settings_ → `Restricted Caller Access Privileges`; execute the scheduled script using _Execute Now_. Refresh the privilege list and **Loaner Request > All**; verify records were not closed while `Can update` was cleared.
  - Return to the table's `Application Access`, select `Can update` → _Update_; _Execute Now_ again. Verify the records change and a write privilege appears.
  - Clear `Can update` → _Update_ to restore the prior setting.

### Lab 6.1.1 - Flow Designer to manage deployment states

🎯 **Goal**: Automate laptop preparation and post-deployment tasks for a Loaner Request.

- **A. Create the task table**
  - End impersonation and elevation; select `Loaner Request` scope. In Studio, _Create_ → `File` → `Data` → `Table`.
  - Set `Label = Loaner Task`, `Extends table = Task`, `Create module = selected`, `Create mobile module = cleared`, `Add module to menu = Loaner Request`; on `Controls`, select `Auto-number` and `Create access controls`, and set `User role = x_cdltd_loaner_r_0.admin` → _Submit_. Do not add fields.
- **B. Create the flow and trigger**
  - _Create_ → `File` → `Automation` → `Flow`; set `Flow name = Loaner Laptop`, `Application = Loaner Request`, `Description = Basic flow for assigning work on a loaner laptop.`, `Protection = --None--`, `Run As = User who initiates session`, and leave `Run with roles` empty → _Build flow_.
  - _Add a trigger_ → `Record > Created or Updated`; set `Table = Loaner Request`, condition `Item Type is Laptop AND State is Reserved`, `Run Trigger = Once` → _Add Filter_ → _Done_.
- **C. Add actions**
  - Add `ServiceNow Core > Wait For Condition`: `Record = Trigger > Loaner Request Record`, `Condition = State is Deployment Prep`.
  - Add `Create Task`: `Table = Loaner Task`, `Parent = Loaner Request Record`, `Priority = 3 - Moderate`, `Short description = Prepare the laptop for deployment.`, `Wait = selected`, annotation `Deployment Prep`.
  - Add `Update Record`: `Record = Loaner Request Record`, `State = Ready for Pickup`, annotation `Ready for Pickup`.
  - Add another `Wait For Condition` for the same record, `State is Post Deployment`; add a second `Create Task` with the same table, parent, priority, and wait setting, `Short description = Perform the post deployment tasks.`, annotation `Post Deployment`.
  - Add `Update Record` for the request, `State = Closed Complete`, annotation `Closed Complete`. Arrange the six actions in the stated sequence; the guide's illustration confirms this order.
- **D. Configure task states**
  - Studio → _Create_ → `File` → `Form` → select `Loaner Task` → _Open_. Switch scope to `Global`; select inherited `State` → `Choices` → _Edit_. Keep `Open = 1`, `Work in Progress = 2`, and `Closed Complete = 3` → _Apply_ → confirm override → _Save_.
  - Switch back to `Loaner Request`; verify the default is `Open` (`1`) → _Save_.
- **E. Test and activate**
  - On a Loaner Request form, Form Header → **Configure > Related Lists** → add `Loaner Task --> Parent` → _Save_.
  - In the flow, _Test_ → create a request with `Requested for = <user>`, `State = Reserved`, valid start/end dates, and `Item type = Laptop` → _Submit_ → select the record → _Run Test_.
  - In execution details, open the request and set `State = Deployment Prep`; close the generated task as `Closed Complete`; set request state to `Post Deployment`; close the second task; refresh execution details and confirm the request reaches `Closed Complete`.
  - After a successful test, _Activate_ → confirm _Activate_.
- **F. Set Reserved automatically**
  - Create `Business Rule`: `Name = Set Reserved State`, `Table = Loaner Request`, `Active = selected`, `Insert = selected`, `Update = selected`; filter `State is Requested AND Configuration item changes AND Configuration item is not empty`. For explicit timing, select `Advanced` and set `When = before`: this is an implementation choice for changing the current record before saving, since the course's basic-view screenshot does not expose `When`.
  - On `Actions`, set `State = Reserved` → _Submit_. Test by changing an empty configuration item to a populated value on a `Requested` record; a laptop can then trigger the flow.

### Lab 6.2.1 - Create application properties

🎯 **Goal**: Create and secure configurable reminder intervals and a properties module.

- **A. Create category and properties**
  - Studio → _Create_ → `File` → application `Loaner Request` → `Properties > System Property Category`; set `Name = Loaner Request`, `Title = Loaner Request Properties` → _Submit_.
  - Create three `Properties > System Property` files; each has `Type = integer`, `Value = 24`, and read/write roles `x_cdltd_loaner_r_0.admin`:
    - `Suffix = pickup.leadtime`; description `Number of hours before a reservation starts to send a reminder to the requester.`
    - `Suffix = return.remindtime`; description `Number of hours before a reservation ends to send a reminder to the requester.`
    - `Suffix = overdue.remindtime`; description `Number of hours to wait between overdue reminders.`
  - In the category's `Properties` related list, _Edit_ → add the three properties → _Save_; set orders `pickup.leadtime = 100`, `return.remindtime = 200`, `overdue.remindtime = 300` → _Update_.
- **B. Create modules and test**
  - Create a `Module` with `Title = Properties`, `Application Menu = Loaner Request`, `Order = 800`, `Roles = x_cdltd_loaner_r_0.admin`, `Active = selected`, `Link type = URL (from Arguments)`, and `Arguments = system_properties_ui.do?sysparm_title=Loaner Request Properties&sysparm_category=Loaner Request` → _Submit_.
  - Create a separator module: `Title = Admin tools`, same application menu and admin role, `Order = 700`, `Active = selected`, `Link type = Separator` → _Submit_.
  - Refresh the main browser, open **Loaner Request > Properties**, verify order and save/reopen a changed value. Impersonate Beth and verify neither admin-only module is visible; end impersonation.

### Lab 6.3.1 - Scheduled Script Execution and email

🎯 **Goal**: Detect requests ready for pickup, queue an event, and notify the requester.

- **A. Add a reminder field and register the event**
  - Studio → **Data > Form > Loaner Request** → Default view; add `Pick up reminder` (`pick_up_reminder`, `Date/Time`) below `Other` → _Save_.
  - _Create_ → `File` → `Server Development > Event Registration`; set `Suffix = pickUp`, `Table = Loaner Request`, `Fired by = Scheduled Script Execution: Loaner Item Pick Up`, `Description = Used to trigger an email to remind a user to pick up their loaner item.` → _Submit_.
- **B. Create and test the scheduled script**
  - Create `Server Development > Scheduled Script Execution`: `Name = Loaner Item Pick Up`, `Active = selected`, `Run = Periodically`, `Repeat Interval = 1 hour`; set `Script` to the following → _Submit_:
    ```javascript
    var pickUpLeadTime =
      gs.getProperty("x_cdltd_loaner_r_0.pickup.leadtime", 24) * 60 * 60 * 1000;
    var noticeTime = new GlideDateTime();
    noticeTime.add(pickUpLeadTime);
    // The above block ensures the GlideRecord query finds the records that are due up in the span specified by the leadtime property
    var readyRec = new GlideRecord("x_cdltd_loaner_r_0_loaner_request");
    readyRec.addQuery("state", 16);
    readyRec.addQuery("pick_up_reminder", "");
    readyRec.addQuery("start_date", "<=", noticeTime);
    readyRec.query();
    // the above GR query looks for LNR records which:
    // (1) are in state "Ready for Pickup"
    // (2) haven't already generated a reminder
    // (3) are within the acceptable span for pickup
    var rightNow = new GlideDateTime();
    while (readyRec.next()) {
      readyRec.pick_up_reminder = rightNow;
      // update each LNR so we don't spam the requesters (see line 9, above)
      readyRec.update();
      gs.eventQueue(
        "x_cdltd_loaner_r_0.pickUp",
        readyRec,
        readyRec.number,
        gs.getUserName(),
      );
      // fire the event to trigger the email notification!
    }
    ```
  - The script reads `x_cdltd_loaner_r_0.pickup.leadtime` (default `24` hours), finds `state = 16`, empty `pick_up_reminder`, and `start_date` within the lead time; it stamps the reminder and queues `x_cdltd_loaner_r_0.pickUp`.
  - Create or update qualifying records → _Execute Now_ → **System Logs > Events**; filter `Name contains loaner` and verify the events.
- **C. Create and test the notification**
  - Create `Notification [sysevent_email_action]`: `Name = Loaner Item Pick Up`, `Table = Loaner Request`, `Category = Targeted Communication`, `Active = selected`.
  - `When to send`: `Send when = Event is fired`, `Event name = x_cdltd_loaner_r_0.pickUp`. In `Advanced view`, `Who will receive`: move `Requested for` to `Users/Groups in fields`.
  - `What it will contain`: `Subject = Your loaner ${item_type} is ready for pick up`; enter the following in `Message HTML` → _Update_ → _Preview Notification_:
    - `Dear ${requested_for},`
    - `The ${item_type} (${cmdb_ci}) is available for pick up at ${depot}.`
    - `Your reservation is scheduled to begin ${start_date}. Please return the item to the same location you picked it up by ${end_date}.`
    - `You will receive a return reminder notification.`
  - Test with `Requested for = George Washington` or another user with notifications enabled, `State = Ready for Pickup`, `Start date` within the lead time, and empty `Pick up reminder`; _Execute Now_. Open **System Logs > Emails**, select the created email → _Preview Email_ and verify substitutions.

### Lab 6.4.1 - Script include

🎯 **Goal**: Move reminder logic into reusable functions and call them from a scheduled script.

- **A. Create the Script Include**
  - Studio → _Create_ → `File` → `Server Development > Script Include`; set `Name = LoanerUtils`, `Accessible from = This application scope only`, `Active = selected`; leave the generated API name.
  - Replace the default script with this course example → _Submit_. It contains the pickup, return, and overdue helper methods:

    ```javascript
    var LoanerUtils = Class.create();
    LoanerUtils.prototype = {
      initialize: function () {
        this.appScopeName = gs.getCurrentScopeName();
        this.loanerTableName = this.appScopeName + "_loaner_request";
        this.pickupLeadTime =
          gs.getProperty(this.appScopeName + ".pickup.leadtime", 24) *
          60 *
          60 *
          1000;
        this.returnRemindTime =
          gs.getProperty(this.appScopeName + ".return.remindtime", 24) *
          60 *
          60 *
          1000;
        this.overdueRemindTime =
          gs.getProperty(this.appScopeName + ".overdue.remindtime", 24) *
          60 *
          60 *
          1000;
        this.pickupEvent = this.appScopeName + ".pickUp";
        this.returnEvent = this.appScopeName + ".return";
        this.overdueEvent = this.appScopeName + ".overdue";
      },
      getNullPickupReminders: function () {
        var a = [];
        var noticeTime = new GlideDateTime();
        noticeTime.add(this.pickupLeadTime);
        var pLoaners = new GlideRecord(this.loanerTableName);
        pLoaners.addQuery("state", 16); // i.e., "Ready for Pickup"
        pLoaners.addQuery("pick_up_reminder", "");
        pLoaners.addQuery("start_date", "<=", noticeTime); // Basically, Start Date in the past
        pLoaners.query();
        while (pLoaners.next()) {
          a.push(pLoaners.getUniqueValue()); // pump these records into an array, then use sendPickupReminder() to fire the events
        }
        return a;
      },
      sendPickupReminder: function (id) {
        var spLoaner = new GlideRecord(this.loanerTableName);
        if (!spLoaner.get(id)) {
          gs.error(
            ">>>ERROR: LoanerUtils: sendPickupReminder(): FAILED TO RETRIEVE RECORD",
          );
          return;
        }
        spLoaner.pick_up_reminder = new GlideDateTime().getDisplayValue();
        spLoaner.update();
        gs.eventQueue(
          this.pickupEvent,
          spLoaner,
          spLoaner.start_date,
          spLoaner.end_date,
        );
        return;
      },
      getNullReturnReminders: function () {
        var a = [];
        var noticeTime = new GlideDateTime();
        noticeTime.add(this.returnRemindTime);
        var rLoaners = new GlideRecord(this.loanerTableName);
        rLoaners.addQuery("state", 17); // State "Checked Out"
        rLoaners.addQuery("return_reminder", "");
        rLoaners.addQuery("end_date", "<=", noticeTime);
        rLoaners.query();
        while (rLoaners.next()) {
          a.push(rLoaners.getUniqueValue());
        }
        return a;
      },
      sendReturnReminder: function (id) {
        var srLoaner = new GlideRecord(this.loanerTableName);
        if (!srLoaner.get(id)) {
          gs.error(
            ">>>ERROR: LoanerUtils: sendReturnReminder(): FAILED TO RETRIEVE RECORD",
          );
          return;
        }
        srLoaner.return_reminder = new GlideDateTime().getDisplayValue();
        srLoaner.update();
        gs.eventQueue(
          this.returnEvent,
          srLoaner,
          srLoaner.start_date,
          srLoaner.end_date,
        );
        return;
      },
      getOverdueRequests: function () {
        var a = [];
        var rightNow = new GlideDateTime().getDisplayValue();
        var oLoaners = new GlideRecord(this.loanerTableName);
        oLoaners.addQuery("end_date", "<=", rightNow);
        oLoaners.addQuery("state", 17);
        oLoaners.query();
        while (oLoaners.next()) {
          a.push(oLoaners.getUniqueValue());
        }
        return a;
      },
      timeToRemindOverdue: function (id) {
        var remindLoaner = new GlideRecord(this.loanerTableName);
        if (!remindLoaner.get(id)) {
          gs.error(
            ">>>ERROR: LoanerUtils: timeToRemindOverdue(): FAILED TO RETRIEVE RECORD",
          );
          return false;
        }
        var noticeTime = new GlideDateTime();
        noticeTime.subtract(this.overdueRemindTime);
        var baseDate =
          remindLoaner.last_overdue_reminder == ""
            ? remindLoaner.end_date
            : remindLoaner.last_overdue_reminder;
        return baseDate <= noticeTime;
      },
      sendOverdueReminder: function (id) {
        var soLoaner = new GlideRecord(this.loanerTableName);

        if (!soLoaner.get(id)) {
          gs.error(
            ">>>ERROR: LoanerUtils: setLastOverdueReminder(): FAILED TO RETRIEVE RECORD",
          );
          return;
        }
        ++soLoaner.overdue_count;
        soLoaner.last_overdue_reminder = new GlideDateTime().getDisplayValue();
        soLoaner.update();
        gs.eventQueue(
          this.overdueEvent,
          soLoaner,
          soLoaner.start_date,
          soLoaner.end_date,
        );
        return;
      },
      type: "LoanerUtils",
    };
    ```

  - The initializer reads the scoped pickup, return, and overdue properties; pickup methods find ready records without a reminder, stamp the record, and queue the pickup event.
- **B. Call and test**
  - Open `Loaner Item Pick Up` Scheduled Script Execution; replace its script with `var lutil = new LoanerUtils(); var plist = lutil.getNullPickupReminders(); for (var i = 0; i < plist.length; i++) { lutil.sendPickupReminder(plist[i]); }` → _Update_.
  - Create or modify a qualifying pickup request for a notification-enabled user → _Execute Now_; verify **System Logs > Events**, **System Logs > Emails**, and the populated `Pick up reminder` field.
  - Optional: commit changes with `Loaner Request application with module 6 labs completed.`
- **C. Return and overdue challenge (optional)**
  - On the Default Loaner Request form, create a two-column `Reminders` section. Add `Return reminder` (`return_reminder`, `Date/Time`), `Last overdue reminder` (`last_overdue_reminder`, `Date/Time`), and `Overdue count` (`overdue_count`, `Integer`); move `Pick up reminder` there → _Save_.
  - Studio → _Create_ → `File` → `Server Development > Event Registration`; create each suffix `return` and `overdue` on `Table = Loaner Request`, using a description and `Fired by` value identifying the corresponding scheduled job. Their fully qualified event names use the application scope.
  - Create an active `Scheduled Script Execution` named `Loaner Return Reminder`, `Run = Periodically`, `Repeat Interval = 1 hour`; use the following example → _Submit_:
    ```javascript
    var utils = new LoanerUtils();
    var ids = utils.getNullReturnReminders();
    for (var i = 0; i < ids.length; i++) {
      utils.sendReturnReminder(ids[i]);
    }
    ```
  - Create another active hourly `Scheduled Script Execution` named `Loaner Overdue Reminder`; use the following example → _Submit_. The helper checks the configured repeat interval before queuing an overdue reminder:
    ```javascript
    var utils = new LoanerUtils();
    var ids = utils.getOverdueRequests();
    for (var i = 0; i < ids.length; i++) {
      if (utils.timeToRemindOverdue(ids[i])) {
        utils.sendOverdueReminder(ids[i]);
      }
    }
    ```
  - Create an active `Notification` for each event on `Table = Loaner Request`; select `Send when = Event is fired`, choose the matching scoped `return` or `overdue` event, and add `Requested for` under `Users/Groups in fields`. Supply subjects and messages identifying `${number}`, `${item_type}`, and `${end_date}`; _Submit_. These names and hourly schedules are a concrete example for the guide's open-ended challenge.
  - Test a notification-enabled requester with `State = Checked Out`, an end date within `return.remindtime`, and an empty `Return reminder`; _Execute Now_ on `Loaner Return Reminder` and verify the record, **System Logs > Events**, and **System Logs > Emails**. For overdue, use a past end date and a blank or sufficiently old `Last overdue reminder`; execute the overdue job and verify the timestamp, count, event, and email. Re-run before the interval expires and confirm no additional overdue reminder is queued.

### Lab 7.1.1 - Importing records from a spreadsheet

🎯 **Goal**: Load spreadsheet rows into a new Password Vault table through an import set.

- **A. Prepare source and table**
  - Switch to `Global` scope. Open **Configuration > Base Items > Computers**; choose a disposable test computer, prefix its name with `LNR`, and record its unique `Asset tag`. If needed, create a test computer with `Name = LNR Test Laptop` and `Asset tag = LNR-TEST-001`.
  - Create `passwords.xlsx` with column headers `Asset` and `Password`; add one row containing the test computer’s exact asset tag and `TRAINING-ONLY-NOT-A-SECRET`. Save locally. Use fictitious values only.
  - Open **System Definition > Tables** → _New_; set `Label = Password Vault`, `Name = u_password_vault`, `Create module = selected`, `Create mobile module = cleared`, `Add module to menu = -- Create New --`, `New menu name = Password Vault`.
  - `Controls`: `Create access controls = selected`, `User role = admin`. `Application Access`: `Accessible from = All application scopes`, `Can read = selected`, `Allow access to this table via web services = selected` → _Save_.
  - On `Columns`, add `Password` (`String`) and `Asset` (`String`) → _Update_.
- **B. Load and transform**
  - Open **System Import Sets > Load Data**; `Import set table = Create table`, `Label = Password Import File`, `Table Name = u_password_import_file`, `Source of the import = File`, `File = passwords.xlsx` → _Submit_.
  - _Create transform map_: `Name = Password Transform Map`, `Source Table = Password Import File [u_password_import_file]`, `Target Table = Password Vault [u_password_vault]`, `Active = selected`, `Run business rules = cleared` → _Save_.
  - _Auto Map Matching Fields_ → verify `Field Maps` → _Transform_ → _Transform_. Open the resulting `ISET...` import set and inspect `Import Set Rows`; verify target records under **Password Vault > Password Vaults**.

### Lab 7.2.1 - Web service consumer

🎯 **Goal**: Exercise a REST consumer and provider using the training instance and retrieve a matching vault record.

- **A. Explore the provider**
  - Complete Lab 7.1.1 using only the fictitious value `TRAINING-ONLY-NOT-A-SECRET`. In `Global` scope, open **System Web Services > REST > REST API Explorer** → _Explore_ if prompted → `Retrieve records from a table (GET)`.
  - Set `tableName = Password Vault (u_password_vault)`, `sysparm_query = u_asset=<test asset tag>`, `sysparm_fields = u_password`, and response format `application/json` → _Send_. Verify status `200` and the dummy value.
- **B. Configure authentication**
  - With `web_service_admin`, open **System Web Services > REST > REST Message** → _New_. Set `Name = Training vault lookup`, `Endpoint = https://<YOUR_TRAINING_INSTANCE_HOST>/api/now/table/u_password_vault`, and `Authentication type = Basic`.
  - At `Basic auth profile`, use the reference lookup → _New_. Set `Name = Training vault profile`, and enter a disposable training account and password authorized to read the admin-protected vault → _Submit_. Select the profile on the REST message and _Submit_. Open the profile and use Form Header → _Copy sys_id_. This exercise uses an admin-protected sample table; use a least-privilege integration account and appropriate ACLs in real integrations.
- **C. Create and test a consumer**
  - In `Loaner Request` scope, Studio → _Create_ → `File` → `Server Development > Business Rule`. Set `Name = Retrieved Credentials`, `Table = Loaner Request`, `Active = selected`, `Advanced = selected`, `When = async`, `Insert = selected`, `Update = selected`.
  - Set `Script` below, replacing the host and profile sys*id → \_Submit*. This adaptation uses the authentication profile rather than embedding a password and logs only the presence of the fictitious record:
    ```javascript
    (function executeRule(current, previous) {
      if (current.getValue("item_type") != "cmdb_ci_computer") return;
      var ci = current.cmdb_ci.getRefRecord();
      if (!ci.isValidRecord() || !ci.getValue("asset_tag")) return;
      var request = new sn_ws.RESTMessageV2();
      request.setEndpoint(
        "https://<YOUR_TRAINING_INSTANCE_HOST>/api/now/table/u_password_vault?sysparm_query=" +
          encodeURIComponent("u_asset=" + ci.getValue("asset_tag")) +
          "&sysparm_fields=u_password&sysparm_limit=1",
      );
      request.setHttpMethod("GET");
      request.setAuthenticationProfile("basic", "<BASIC_AUTH_PROFILE_SYS_ID>");
      request.setRequestHeader("Accept", "application/json");
      var response = request.execute();
      if (response.getStatusCode() != 200) {
        gs.error(
          "Training vault lookup failed: HTTP " + response.getStatusCode(),
        );
        return;
      }
      var result = JSON.parse(response.getBody()).result;
      gs.info("Training vault record found: " + (result.length > 0));
    })(current, previous);
    ```
  - In **Loaner Request > Open**, select `State = Ready for Pickup`, `Item type = Laptop`, and the `LNR` test computer from Lab 7.1.1 → _Update_. Inspect **System Logs > System Log > Application Logs** for `Training vault record found: true`.
- **D. Test email integration and clean up**
  - Open notification `Loaner Item Pick Up` → `What it will contain > Message HTML`; append the following, replacing the host and profile sys*id → \_Save*. If prompted, allow conversion to a Notification Email Script. It prints the fictitious value from Lab 7.1.1; never use a real secret here:
    ```html
    <mail_script>
    var ci = current.cmdb_ci.getRefRecord();
    if (current.getValue('item_type') == 'cmdb_ci_computer' && ci.isValidRecord()) {
        var request = new sn_ws.RESTMessageV2();
        request.setEndpoint('https://<YOUR_TRAINING_INSTANCE_HOST>/api/now/table/u_password_vault?sysparm_query=' +
            encodeURIComponent('u_asset=' + ci.getValue('asset_tag')) + '&sysparm_fields=u_password&sysparm_limit=1');
        request.setHttpMethod('GET');
        request.setAuthenticationProfile('basic', '<BASIC_AUTH_PROFILE_SYS_ID>');
        request.setRequestHeader('Accept', 'application/json');
        var response = request.execute();
        if (response.getStatusCode() == 200) {
            var result = JSON.parse(response.getBody()).result;
            if (result.length && result[0].u_password == 'TRAINING-ONLY-NOT-A-SECRET')
                template.print('Training value: ' + result[0].u_password);
        }
    }
    </mail_script>
    ```
  - Use a qualifying pickup record with the test laptop, empty reminder, and start date within 24 hours; run the `Loaner Item Pick Up` scheduled job with _Execute Now_. Inspect **System Mailboxes > Outbound > Outbox** → _Preview Email_ and verify `Training value: TRAINING-ONLY-NOT-A-SECRET`.
  - Deactivate the `Retrieved Credentials` Business Rule, remove the added mail script or reference from the notification and delete its generated Notification Email Script, and remove the temporary REST message and authentication profile when no longer needed. Remove test output according to instance policy; rotate any credentials inadvertently exposed in logs, email, or script.

### Lab 7.2.2 - Publish the updated application

🎯 **Goal**: Package application changes and selected demo data for installation or upgrade.

- **A. Capture data and publish**
  - Optional: Studio app details → **Source control > Commit changes** → select files → _Continue_ → comment `Loaner Request application with module 7 labs completed.` → _Commit files_ → _Close_.
  - In the main instance, select `Loaner Request` scope → **Loaner Request > All** → Number column options → _Create Application Files_ → `Load When = New Install and Upgrades` → _OK_.
  - In Studio app details, _More Options_ → _Publish_ → review → _Publish_ → _Done_.
- **B. Update a destination instance**
  - On the second instance, open **System Applications > My Company Applications > Installed**; refresh, choose the published version → _Update_ → _Install_ → _Close_. If prompted to map applications with custom tables, select _Install_ → _Close_.
  - Verify the version and demo records in **Loaner Request > All**. This step is reference-only in the single training instance.

### Lab 8.1.1 - Automated Test Framework

🎯 **Goal**: Test form access and the start/end date Business Rule using ATF.

- **A. Enable and create the test**
  - Verify `Validate Start and End Dates` is active. In `Global` scope, open **Automated Test Framework > Administration > Properties**, enable test/test-suite execution → _Save_; return to `Loaner Request` scope.
  - In Studio, create `Test`: `Name = My First Loaner Request ATF Test`, `Application = Loaner Request`, `Active = selected` → _Save_.
- **B. Add ordered test steps**
  - `1`: _Add Test Step_ → `Create a User`; `Active = selected`, `Groups = Loaner Request Admins`, `Impersonate this user = selected` → _Submit_.
  - `2`: `Form > Open a New Form`; `Active = selected`, `Form UI = Standard UI`, `Table = Loaner Request` → _Submit_.
  - `3`: `Form > Set Field Values`; same UI and table; `Requested for = Abel Tuter`, `Start date = today`, `End date = before today` → _Submit_.
  - `4`: `Form > Submit a Form`; `Form UI = Standard UI`, `Assert type = Form submitted to server` → _Submit_.
- **C. Run failing and passing cases**
  - _Run Test_ → _Run Test_; observe the Client Test Runner, then _Go to Result_ → _Manage Attachments_ to inspect the failure screenshot. The invalid date should prevent submission.
  - If an unrelated client error blocks the exercise, the guide provides `Actions on selected rows > Add all client errors to ignored list`; use only after reviewing the errors and understanding the impact.
  - Edit step `3`: `Requested for = Abraham Lincoln`, `Start date = today`, `End date = after today` → _Update_; run again and verify all steps pass.
  - Optional: commit changes with `Loaner Request application with module 8 labs completed.`

### Lab 9.1.1 - Service Catalog user interface

🎯 **Goal**: Replace the new-request form entry point with a Service Catalog record producer.

- **A. Create the producer**
  - In Studio, **Data > Table > Loaner Request** → _Additional Actions_ → `Advanced view` → _Add to Service Catalog_.
  - Set `Name = Loaner Request`, `Short description = Submit a New Loaner Request`, `Category = Can We Help You?`; select `Requested for`, `Item type`, `Start date`, `End date`, `Depot`, `Other`, `Location to be used`, and `Description` → _Save and Open_.
  - In the main instance, open **Self-Service > Service Catalog > Can We Help You? > Loaner Request** and inspect the initial form.
- **B. Configure Catalog Builder**
  - In Studio, **User Interface > Record Producer > Loaner Request** → _Edit in Catalog Builder_. Set item name and short description as above; set description to `Please enter your reservation request. When your item has been requested, someone from the Service Desk will contact you to discuss special requirements, options or conflicts, and to schedule a pick-up time and location.`
  - `Destination`: `Record submission table = Loaner Request`; `Location`: `Catalogs = Service Catalog`, `Categories = Can We Help You?`, `Topics = empty`.
  - Under `Questions`, edit and save labels: `Requested for` → `Who is this reservation for?`; `Item type` → `What would you like to reserve?`; `Start date` → `When will you start using the equipment?`; `End date` → `When will you return the equipment?`; `Depot` → `Where would you like to pick up this item?`; `Other` → `Specify other location.`; `Location to be used` → `Where will you use this equipment (country)?`; `Description` → `Please provide any special needs or comments here:`.
  - Insert `Two column container`: `Title = Request details`, `Display title = cleared` → _Submit_. Move it above the questions. Arrange left column `Requested for`, `Start date`, `Depot`, `Location to be used`; right column `Item type`, `End date`, `Other`; leave `Description` outside.
  - Edit `Start date` → `Annotation` → select `Show instructions`; enter `The start date for the request must be after today.` → _Save_ → _Review and submit_ → _Submit_. Preview and verify the help text.
- **C. Script, link, and test**
  - In the main instance, submit the producer and inspect the created Loaner Request. In Studio, open the producer → _Edit in Catalog Builder_ → `Questions` → edit the `Depot` question → inspect the stored value of its `Other` choice. Use that exact value in the comparison below; the example uses `other`.
  - Return to the producer → `What it will contain > Script`; append the following adapted example below the default script → _Update_:
    ```javascript
    current.item_type = producer.item_type;
    current.depot = producer.depot;
    if (String(producer.depot) == "other") {
      current.other = producer.other;
    }
    current.short_description =
      "Reservation: " +
      current.item_type.getDisplayValue() +
      " from " +
      current.depot.getDisplayValue();
    current.state = 13;
    ```
  - Submit another producer request; verify the short description and `Requested` state.
  - In **User Interface > Module > Create New**, set `Link type = URL (from Arguments)` and `Arguments = com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=<record producer sys_id>`; obtain the ID from the producer Form Header → _Copy sys_id_.
  - Refresh the main browser → **Loaner Request > Create New**; verify the producer opens. Test from the `All` menu, since an older favorite may retain its prior target.

### Lab 9.1.2 - Enhancing the Service Catalog user interface

🎯 **Goal**: Show and require the Other catalog variable only when the selected depot is Other.

- **A. Create behavior and test**
  - Studio → **User Interface > Record Producer > Loaner Request** → _Edit in Catalog Builder_ → `UI Policy` → _Add new behavior_.
  - `Details`: `Active = selected`, `Applies to = Loaner Request`, `Short description = Only show ‘Other’ field if Depot value is ‘Other’`. `Conditions`: `depot is Other`.
  - `Actions` → _Add new action_: `Variable name = other`, `Mandatory = True`, `Read only = Leave alone`, `Visible = True`, `Value action = Leave alone`, `Field message type = None` → _Save_ → _Add behavior_ → _Review and submit_ → _Submit_.
  - Open **Self-Service > Service Catalog > Can We Help You? > Loaner Request**; set the depot question to `Other` and verify `Specify other location` is visible and mandatory. Select a different depot and verify the variable becomes hidden and is no longer mandatory; switch back and verify both settings return.

### Lab 9.1.3 - Publish the Loaner Request app to an update set (optional)

🎯 **Goal**: Commit and package the completed catalog-enhanced application.

- **A. Commit and publish**
  - If the application was connected to Git in Lab 3.4.1, optionally open Studio app details → **Source control > Commit changes** → review files → _Continue_ → `Commit comment = Loaner Request application with module 9.1 labs completed.` → _Commit files_ → _Close_.
  - App details → _More Options_ → _Settings_ → _Publish to Update Set_; update the version and set `Description = Loaner Request application` → _Publish_ → _Done_. Review `Customer Updates`.
  - Optional: use the update set's _Export to XML_ related link to retain a package for a personal developer instance.

### Lab 9.2.1 - Outbound REST message (optional)

🎯 **Goal**: Geocode requestor locations through an outbound REST message and display them on a map.

- **A. Obtain the service key**
  - Open `https://www.geoapify.com/pricing`, create a free account and project `Map page`; select `Geocoding API`, review the request parameters, and copy the project's API key.
- **B. Configure the REST message**
  - Studio → _Create_ → `File` → `Integrations (Outbound) > REST Message`; set `Name = Get Lat Long`, `Accessible from = This application scope only`, `Description = Retrieve Latitude and Longitude from Geoapify.`, `Endpoint = https://api.geoapify.com/v1/geocode/search` → _Submit_.
  - Open `Default GET` → `HTTP Request > HTTP Query Parameters`: add `apiKey = <Geoapify API key>`, `Order = 100`; add `text = ${text}`, `Order = 200` → _Update_.
  - On `Variable Substitutions`, _New_: `Name = text`, `Test value = Solana Beach, CA`, `Method = Default GET` → _Submit_; refresh the list → _Test_. Verify HTTP `200`, returned latitude/longitude, and expected accuracy.
- **C. Create the map and module**
  - Studio → _Create_ → `File` → `User Interface > Map Page`; set `Suffix = Requested for Locations`, `Type = Terrain`. Paste this adaptation of the course example, changing the scoped REST Message name and table name if needed → _Submit_. The checks skip records without a matching country or usable geocoding result:
    ```javascript
    // Let's go get all the active Loaner Requests where the requestor has a _city and country_ in their user record
    var loaners = new GlideRecord("x_cdltd_loaner_r_0_loaner_request");
    loaners.addEncodedQuery(
      "active=true^requested_for.cityISNOTEMPTY^requested_for.countryISNOTEMPTY",
    );
    loaners.orderBy("number");
    loaners.query();
    // Now, loop through these results...
    while (loaners.next()) {
      // ...but, within THESE results, let's get the LABEL of the country field (via the sys_choice table), since our REST provider prefers that.
      var countrygr = new GlideRecord("sys_choice");
      countrygr.addQuery("name", "sys_user");
      countrygr.addQuery("element", "country");
      countrygr.addQuery("language", "en");
      countrygr.addQuery("value", loaners.requested_for.country);
      countrygr.query();
      if (!countrygr.next()) continue;
      var query = loaners.requested_for.city + "," + countrygr.label;
      var r = new sn_ws.RESTMessageV2(
        "x_cdltd_loaner_r_0.Get Lat Long",
        "Default GET",
      );
      r.setStringParameterNoEscape("text", query);
      var response = r.execute();
      if (response.getStatusCode() != 200) continue;
      var responseBody = response.getBody();
      // Extract latitude and longitude values from REST Message response in JSON format
      var responseJSON = JSON.parse(responseBody);
      if (!responseJSON.features || !responseJSON.features.length) continue;
      var myLat = responseJSON.features[0].properties.lat;
      var myLong = responseJSON.features[0].properties.lon;
      // Plot each 'Requested for' location on a Google map
      var item = map.addItem(loaners);
      item.latitude = String(myLat);
      item.longitude = String(myLong);
      item.dialog_title = loaners.getDisplayValue();
      item.icon = "https://maps.google.com/mapfiles/ms/micons/yellow.png";
      item.icon_width = "32";
      item.icon_height = "32";
    }
    ```
  - The code parses `features[0].properties.lat` and `.lon` and adds a yellow marker linked to each request.
  - **Source inconsistency resolved from illustration**: the prose later says `addr`, but both the configured query parameter and completed-script screenshot use `text`; verify your HTTP method uses the same name.
  - Create `Module`: `Title = Requestor Locations`, `Application Menu = Loaner Request`, `Order = 900`, `Roles = x_cdltd_loaner_r_0.admin`, `Link Type = Map Page`, `Map page = Requested for Locations` → _Submit_.
- **D. Test**
  - Ensure at least three active Loaner Requests have a `Requested for` user with city and country code; open **Loaner Request > Admin tools > Requestor Locations**. Verify yellow markers and select one to open its associated request.
  - Optional: commit with `Loaner Request application with Lab 9.2.1 completed.` and use Lab 9.1.3 to package changes.
