# Scripting on ServiceNow

## Resources

- [📜 ServiceNow Development Handbook by Tim Woodruff](./30-sn-dev-handbook.md)
- [Customization Best Practices (PDF)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/customization-best-practices.pdf)
- Developer API Documentation
  - [Server-side APIs](https://developer.servicenow.com/dev.do#!/reference/api/latest/server_legacy/c_GlideRecordAPI)
  - [Client-side APIs](https://developer.servicenow.com/dev.do#!/reference/api/latest/client/c_GlideFormAPI)

### 📘 Courses

- [x] [Learning JavaScript on the Now Platform](https://learning.servicenow.com/lxp/en/now-platform/learning-javascript-on-the-now-platform?id=learning_course_prev&course_id=8cdb2ad5975de9505b0b7ec11153af34)
- [ ] [Scripting Course on NowLearning](https://nowlearning.servicenow.com/lxp?id=learning_course_prev&course_id=15cbcb7adbfec590421266f748961923)
  - [Course book](https://servicenow.read.inkling.com/a/b/28698044fcc848a8a88c2ddee196533a/p/bbeaec5ab9504cf39c54c80936c01494)

### 🧠 Community

- _(Add specific forums, discussions, or expert posts as encountered)_

### Other Links

- [Course Repository – All Code Snippets](https://github.com/chucktomasi/sn-learn-javascript)
- [YouTube Series: Learn JavaScript on the Now Platform](https://www.youtube.com/watch?v=62Nabpb94Jw&list=PL3rNcyAiDYK2_87aRvXEmAyD8M9DARVGK&index=3)
- [Now Platform Scripting Best Practices – Developer Portal (Tokyo)](https://developer.servicenow.com/dev.do#!/guides/tokyo/now-platform/tpb-guide/scripting_technical_best_practices)
- [Pluralsight](https://www.pluralsight.com/browse?=&q=javascript)
- [Codecademy](https://www.codecademy.com/search?query=javascript)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/javascript)

## Scripting Overview

- **What**:
  - Use Condition Builder for simple logic, script for complex behavior
  - JavaScript via Rhino engine, supports ES5 + ES2021 (ES12)
- **Why not**:
  - Upgrades often obsolete scripts
  - Configurations easier to debug/maintain
  - Validate need: business critical, ACLs, ≥80% config possible
  - Stay current: docs, release notes, release meetings
- **When**:
  - Add/extend functionality, guide users, automate, integrate with third-party apps
  - Examples: cascade comments, update CI ownership, dynamic approvals, hide/show form sections, query DB, widgets, default behavior changes
  - Prefer baseline options (e.g., Guided Tours) before custom scripts
- **Where**:
  - Client: form/list data (auto-populate, show/hide)
  - Server: DB updates, trigger Flows
  - MID Server: integrations
  - Location impacts performance and object access
- **Who**:
  - `admin`: full control, overrides security
  - Scoped roles: `business_rule_admin`, `client_script_admin`, `script_include_admin`, `ui_policy_admin`
  - Application/System Definition Admin: manage specific app/features
- **How**:
  - Syntax Editor: syntax coloring, auto-indent, macros, error checking, ES2021 mode
  - Enabled baseline; activate plugin `com.glide.syntax_editor` on upgrades
  - Navigate scripts: use filter or `tablename.config`

### Best Practices

- Prefer no-code (≥80% reqs) → low-code → last resort scripting
- Modify baseline only when necessary; review skipped records after upgrade
- [Customization Best Practices (PDF)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/customization-best-practices.pdf)
- Use Condition Builder first
- Create Syntax Editor macros for reusable snippets
- Expand Script Editor for large scripts
- Verify scope impact
- Use official docs, Now Community, join SNUG

### Application Scope

- Each app has scope; once set cannot change; no migration path
- Global scope = baseline apps + older custom apps; harder to isolate data
- Scope protects artifacts (Tables, ACLs, Notifications, Scripts, etc.); explicit permission required to share
- Out-of-scope scripts are read-only
- Namespace prefix format: `x_<vendor>_<app_id>_<artifact>` (e.g., `x_cld_travel_ExpensesReqBy`)

### JavaScript APIs

- **Client-side**: `GlideAjax`, `GlideForm`, `GlideList`, `GlideRecord`, `GlideUser`, `spModal`
- **Server-side**: `GlideAggregate`, `GlideDateTime`, `GlideElement`, `GlideRecord`, Glide Query, `GlideSystem`, `JSON`, Workflow
- APIs differ by scope: _Server Scoped_ vs _Server Global_
- Always match API docs to instance version and scope

### JavaScript Modes

- **Compatibility Mode**: legacy pre-Helsinki + global scripts; limited, no third-party libraries
- **ES5 Mode** (default scoped): `'use strict'`, JSON, Array/Date methods, object property controls
- **ES2021 Mode (ES12)**: `let`, `const`, default params, `for-of`, newer features
- Global scope toggle:
  - ES2021 on → `var` + `const` both valid
  - ES2021 off → ES2021 syntax errors, `var` only

## Client Scripts

- **Purpose**

  - Real-time form/list behavior in browser: mandatory/hide/show, set values, modify choices, alerts, prohibit list edit
  - Execute client-side; expect minor browser differences

- **Location**

  - Create/modify: **System Definition > Client Scripts**

- **Core Fields (Client Script form)**

  - `Name` • `Table` • `Application` (scope) • `Active` • `Inherited`
  - `UI Type`: Desktop | Mobile/Service Portal | All
  - `Type`: `onLoad` | `onSubmit` | `onChange` | `onCellEdit`
  - `Field name`: required for `onChange`/`onCellEdit`
  - `Global` checkbox → if unchecked, set `View`; script only sees fields in that view
  - `Description`: business context
  - `Messages`: i18n keys shown as strings in code; resolved via `sys_ui_message`
  - `Script`: main logic
  - `Order` (hidden baseline; add via form layout): lower runs first; use 3-digit steps (100, 200)

- **Trigger Types**

  - `onLoad()`
    - Runs before user can edit; manipulate UI or defaults
  - `onSubmit()`
    - Runs on Save/Update/Submit; validate; cancel with `return false`
    - Note: `onLoad` runs only on full reload after Save, not after Submit/Update navigation
  - `onChange(control, oldValue, newValue, isLoading, isTemplate)`

    - Runs when watched field changes
    - Template:

      ```js
      function onChange(c, oldV, newV, isLoading, isTemplate) {
        if (isLoading || newV === "" || isTemplate) return;
        // logic
      }
      ```

    - One field per script; watch another field → separate script

  - `onCellEdit(sysIDs, table, oldValues, newValue, callback)`
    - Runs on list edit of watched field; affects all selected rows
    - Must call `callback(true|false)` to continue/abort remaining handlers and commit
    - Not for homepage/dashboard List Widgets

- **Catalog Client Scripts** _(Service Catalog)_

  - Fields: `Name` • `Applies to`: Catalog Item | Variable Set • `Active` • `UI Type` • `Application` • `Type`: `onLoad` | `onChange` | `onSubmit`
  - Targets: `Catalog item` or `Variable set` selector • `Variable name` (for `onChange`)
  - Scope of application:
    - `Applies on a Catalog Item view` (Requester)
    - `Applies on Requested Items` (RITM, Fulfiller)
    - `Applies on Catalog Tasks` (SCTASK, Fulfiller)
    - `Applies on the Target Record` (Record Producers for task-extended tables)

- **Client-side APIs**

  - **Globals**
    - `g_form` (GlideForm): form and field control
    - `g_user` (GlideUser): current user session info
    - `g_scratchpad`: data from Display Business Rule
  - **Field name vs label**
    - Use field **name** (e.g., `caller_id`), not label; get via field label context menu: _Show – 'field_name'_
  - **Common `g_form` methods**
    - Read: `getValue()`, `getIntValue()`, `getDecimalValue()`, `isNewRecord()`, `getSections()`
    - Write: `setValue()`, `clearValue()`, `addOption()`, `clearOptions()`
    - UX: `addInfoMessage()`, `addErrorMessage()`, `showFieldMsg()`, `flash()`, `clearMessages()`
  - **Data type nuances**
    - `getValue()` returns **string** for all types
      - Choice: returns **value** (e.g., `'1'`), not label
      - Reference: returns **sys_id**
      - Need numbers → use `getIntValue()` / `getDecimalValue()`
  - **`g_user` quick refs**
    - Props: `firstName`, `lastName`, `userID`, `userName`
    - Methods: `getFullName()`, `hasRole()`, `hasRoleExactly()`, `hasRoleFromList()`, `hasRoles()`
    - difference between `hasRole()` and `hasRoleExactly()`:
      - `hasRole()` is also true if the user is admin
      - `hasRoleExactly()` checks only for the specified role and would not be true for admin
    - Security note: do **not** enforce security in client; use ACLs/server-side

- **Reference Objects**

  - Reference fields store only `sys_id` on form; referenced record data not on form
  - To read referenced fields → server roundtrip (minimize trips); use Display BR + `g_scratchpad` or GlideAjax pattern

- **Debugging**

  - UI messages: `g_form.addInfoMessage()`, `addErrorMessage()`, `showFieldMsg()`
    - Limit visibility in team environments, e.g., guard with `if (g_user.userName === 'admin') { … }`
  - Response Time Indicator: diagnose slow loads; disable via `glide.ui.response_time=false` if needed
  - JS try/catch for runtime errors; `throw` for custom error flow
  - Browser dev tools console

- **Baseline & Samples**

  - Platform includes many baseline Client Scripts; not all active; use as patterns

- **Versioning**
  - Script Versions created on save/submit/update; compare and revert
  - Compare methods:
    - _Compare to Current_ via version row menu
    - Select two versions → _Compare_ via _Actions on selected rows…_
  - Revert from Version form: _Revert to this version_
  - Update Sets carry only the **latest** version

## UI Policies

- **Purpose**

  - Client-side form control: `Mandatory`, `Visible`, `Read-only`
  - Runs after [Client Scripts](#client-scripts)
  - Prefer over Client Scripts for performance and maintainability

- **Location**

  - Create/modify: **System UI > UI Policies**
  - Baseline: ~2,100+ policies available

- **Core Fields (UI Policy form)**

  - `Table` • `Application` • `Active`
  - `Short description` (use as name) • `Description` (add via form layout)
  - `Order` (lower runs first; add field via form layout if hidden)
  - **When to apply**
    - `Conditions` (Condition Builder; blank = always)
    - `Global` or `View` (if not Global)
    - `Reverse if false` (invert actions + run “if false” script)
    - `On load` (on load and on change)
    - `Inherit` (apply to extending tables)

- **Actions (UI Policy Actions)**

  - Per `Field name`: set `Mandatory`, `Visible`, `Read only`
  - Target field must exist on the form/view (Next Experience)
  - Policy can evaluate any record field even if not visible

- **Scripting (optional)**

  - Enable `Run scripts`
  - `Run scripts in UI type`: Desktop | Mobile/Service Portal | All
  - `Execute if true` / `Execute if false` → `onCondition()` runs automatically
  - Same client globals as Client Scripts: `g_form`, `g_user`, `g_scratchpad`
  - Use scripts for complex logic: section show/hide, advanced validation, dynamic data ops

- **Conditions behavior**

  - Re-evaluated only on **user** field changes
  - System-driven changes do not recheck; use **Data Policies** for non-form updates

- **Catalog UI Policies**

  - Fields: `Applies to` (Catalog Item | Variable Set) • `Catalog item/Variable set` • `Short description` • `Application` • `Active` • `Order`
  - When to apply:
    - `Catalog Conditions` (variables)
    - Scopes: `Applies on a Catalog Item view` | `Applies on Requested Items` | `Applies on Catalog Tasks` | `Applies on the Target Record`
    - `On load` • `Reverse if false`
  - Scripting: `Run scripts` • `Run scripts in UI Type` • `Execute if true/false`

- **Debugging**

  - **Debug UI Policies** (platform toggle) + browser console logs show actions and evaluation
  - For user-facing messages use `g_form.addInfoMessage()` / `addErrorMessage()` (avoid in shared testing)

- **When to choose**

  - Form load/change effects: **UI Policy** or **Client Script**
  - Save/submit validation: **Client Script** only
  - Prior field value needed: **Client Script**
  - List edits: **Client Script (onCellEdit)**
  - Need minimal code and fast load: **UI Policy** first

- **Good practices**
  - Minimize number of policies; tune `Order`
  - Prefer Condition Builder over scripts
  - Disable `On load` if not needed
  - Document with `Short description` + `Description`

## Business Rules

- **Purpose**

  - Server-side logic on record access: display, insert, update, delete, query
  - Change field values, enforce rules, pass data to client
  - Runs for all access methods: forms, lists, web services

- **Location**

  - Create/modify: **System Definition > Business Rules**
  - Baseline: 2,000+ rules

- **Form essentials**

  - `Name` • `Application` (scope) • `Table` • `Active` • `Advanced` (to expose scripting)
  - Add `Description` via form layout for documentation

- **When to run**

  - Triggers: `Insert` • `Update` • `Delete` • `Query`
  - Conditions: `Filter Conditions` (must be true) • `Role conditions`
  - Advanced options:
    - `When`: `before query` | `display` | `before` | `after` | `async`
    - `Order`: lower runs first

- **Execution timeline**

  - User/System action → **Before Query** → DB Query → **Display** → Form submit → **Before** → DB Update → **After** → **Async**

- **Types**

  - **Before Query**: pre-filter results like ACL; silent removal of rows
  - **Display**: after read, before render; populate `g_scratchpad` for [Client Scripts](#client-scripts)
  - **Before**: validate/mutate before write (e.g., set `closed_by`)
  - **After**: post-write side effects (e.g., cascade updates)
  - **Async**: queued job after commit; no `previous`; prefer when user need not wait
    - `Priority` visible when `async`; 3-digit convention (100, 300, …)
    - Queue visibility: **System Scheduler > Scheduled Jobs** (names prefixed `ASYNC`)

- **Actions (basic trigger tab)**: what the BR will do

  - `Set field values` • `Add message` • `Abort action` (ends transaction; message still allowed)

- **Advanced tab**

  - `Condition` (JS; blank = true)
  - `Script` (server JS)
  - Note: **Both** When-to-run conditions and Advanced `Condition` must be true for `Script` to execute
  - Use functions only for single-context needs; multi-context logic → Script Include

- **Server globals & data access**

  - `current`: latest in-transaction values
  - `previous`: values at load; **not available in `async`**
  - `g_scratchpad`: from **Display** rules for client use; read via [Client Scripts](#client-scripts)
  - Dot-walking: `<object>.<reference>.<field>` e.g., `current.caller_id.department.name`
  - Script Tree: expands fields and inserts dot-walk path automatically

- **Debugging**

  - Logs: `gs.info()`, `gs.warn()`, `gs.error()`, `gs.debug()`; prefer over legacy `gs.log()`
    - View: **System Logs > System Log**
  - Form messages: `gs.addInfoMessage()`, `gs.addErrorMessage()` (avoid in multi-admin environments)
  - **Script Debugger** (role: `admin` or `script_debugger`)
    - Step, breakpoints, call stack, variables, session-specific
    - Limits: cannot step async jobs; respects read access; timeouts stop session
    - Console Debugger: evaluate expressions; object printing limited; `gs.*` not supported
  - **Script Tracer**
    - Path: **System Diagnostics > Script Tracer**
    - Filter by file type/table; see changed lines; open in Debugger

- **Good practices**
  - Prefer **Async** over **After** when immediate response not required
  - Use **Display** rules + `g_scratchpad` to avoid client roundtrips
  - Put simple checks in `Filter Conditions`; keep scripts from running unnecessarily
  - Document via `Description`; structure `Order` in 3-digit steps
  - Comment code; select appropriate debug method for context

## GlideSystem

- **Purpose**

  - Server-side API (`gs.`) providing system-level data and utilities
  - Access user, system, logging, and date/time information
  - Scoped vs Global APIs: scoped apps must use **Scoped GlideSystem**

- **Access**

  - Global: available in any server-side script (`gs.methodName()`)
  - Scoped: limited method set; cannot call Global APIs
  - Docs: [developer.servicenow.com → Chevron -> Reference -> APIs → Server Scoped/Global → GlideSystem](https://developer.servicenow.com/dev.do#!/reference/api/latest/server_legacy/c_GlideSystemAPI?navFilter=glidesystem)

- **Key Categories**

  - **User methods**

    - `getUser()`: returns current user object reference
    - `getUserID()`: returns sys_id
    - `getUserName()`: returns username (e.g., `admin`)
    - `getUserDisplayName()`: returns display name (e.g., `System Administrator`)
    - `hasRole(role)`: true if user has role
    - `hasRoleInGroup(role, group)`: true if user has role in group
    - Example:

      ```js
      if (gs.hasRole("itil")) {
        gs.addInfoMessage(gs.getUserDisplayName());
      }
      ```

  - **System methods**

    - `getProperty(name)`: system property value
    - `getPreference(name)`: user preference
    - `getDisplayColumn(table)`: table display column
    - `tableExists(table)`: true if table exists
    - `nil(value)`: true if null/empty
    - `eventQueue(event, record)`: send event to Event Manager
    - `print(msg)`, `logError(msg)`, `getMessage(key)`: log utilities
    - `addInfoMessage(msg)` / `addErrorMessage(msg)`: show messages in UI

  - **Date & time methods**

    - `now()`, `nowDateTime()`: current date/time
    - `dateDiff(date1, date2, format)`: difference between dates
    - `beginningOfLastWeek()`, `endOfLastWeek()`
    - `beginningOfNextMonth()`, `endOfNextMonth()`
    - `minutesAgo(n)`, `daysAgo(n)`, `monthsAgo(n)`, `yearsAgo(n)`
    - Use **GlideDate** / **GlideDateTime** for manipulation and time zone-safe ops

      ```js
      var gdt = new GlideDateTime();
      gs.info(gdt.getDisplayValue());
      ```

- **GlideDate / GlideDateTime**

  - Manipulate date/time values safely (local + UTC)
  - Create object via field reference:

    ```js
    var gdt = gr.my_datetime_field.getGlideObject();
    ```

  - Use `GlideDateTime` instead of raw JavaScript `Date` for platform consistency

- **Scoped GlideSystem**

  - Use in private app scopes; methods limited to:
    - User: `getUser()`, `getUserName()`, etc.
    - General: `getProperty()`, `nil()`, etc.
    - Logging: `debug()`, `info()`, `warn()`, `error()`, `isDebugging()`
  - Error shown if global-only methods are used:  
    _“Function log() not allowed in scope x_app. Use gs.debug() or gs.info() instead.”_

- **Scoped logging**

  - `gs.debug()`, `gs.info()`, `gs.warn()`, `gs.error()`
  - `gs.isDebugging()`: check if debugging is enabled
  - Logs visible in **System Logs > System Log > All** and bottom of form with Session Debug on

- **Good practices**
  - Use GlideDate/GlideDateTime instead of native JS date
  - Use correct API set for scope (Scoped or Global)
  - Prefer `gs.info()` over legacy `gs.log()`
  - Check developer site for current API changes and deprecations
  - Validate date fields using GlideDateTime where possible

## Labs

### Lab 1.3.1 - Using the Syntax Editor

🎯 **Goal**: Practice using the Syntax Editor and create a custom Syntax Editor Macro

- **A. Preparation**

  - Answer knowledge questions throughout the lab as prompted
  - Use the provided script levels (Beginner, Intermediate, Expert) to guide scripting effort

- **B. Use the Syntax Editor**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
    - Note: New scripts run in strict mode by default; to disable globally, set system property `glide.script.block.client.globals = false`
  - In the form:
    - Set `Name` = `Lab 1.3.1 Using the Syntax Editor`
    - De-select `Active`
  - In the Script field, enter plain text:

    ```txt
    Code to test the Syntax Editor features
    • Syntax coloring
    • Special character highlighting
    • Layout
    • And more!
    ```

  - Convert to comment:
    - Select all text
    - Click _Toggle Comment_ in the Syntax Editor toolbar
  - Below the comment, enter:

    ```javascript
    var myString = "Hello World";
    var myNum = 32;
    var myArray = ["Smartphone", "Tablet", "Laptop"];
    var myObj = {
      property1: "first",
      property2: "second",
      property3: "Third",
    };

    for (var i = 0; i < myArray.length; i++) {
      alert("The current value of myArray is: " + myArray[i]);
    }
    ```

  - Select _Save_ in the Syntax Editor toolbar
  - Turn off syntax highlighting:
    - Click _Toggle Syntax Editor_ icon
    - Observe: syntax highlighting and editing features are disabled
  - Click same icon again to re-enable highlighting
  - Use _Replace_ to change `property2` → `propertyTwo`
    - Click _Replace_
    - `Find`: `2`
    - `Replace`: `Two`
    - Use _Next Match_ to skip other occurrences
    - Use _Replace_ to update only the relevant instance
  - Use _Replace All_ to change `"Third"` → `"third"`
    - Click _Replace All_
    - `Find`: `Third`
    - `Replace`: `third`
    - Click _Replace All_
  - Click _Update_ to save and exit

- **C. Create a Syntax Editor Macro**

  - Navigate to **System Definition > Syntax Editor Macros**
  - Create a new macro:

    - `Name`: `try`
    - `Comments`: `Client-side try/catch`
    - `Text`:

      ```javascript
      try {
        //comment added here to prevent empty block statement alert
      } catch (err) {
        g_form.addErrorMessage("A runtime error occurred: " + err);
      }
      ```

  - Return to the previously created Client Script via **History** or Favorites
  - Place cursor on new line, type `help` and press `<Tab>`
    - Observe the try macro expands with description from `Comments`
    - Observe the `info` macro has no description due to empty Comments field
  - Delete `help` macro text
  - Click _Update_ to save and exit

### Lab 1.3.2 - Syntax Checking

🎯 **Goal**: Practice using the Syntax Editor's built-in Syntax Checker to identify and resolve scripting errors

- **A. Syntax Checking in the Syntax Editor**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
  - Configure the trigger:
    - `Name`: `Lab 1.3.2 Syntax Checking`
    - `Active`: _unchecked_
  - In the Script field, enter the following (with intentional errors):

    ```javascript
    //Script used to practice Syntax Checking.
    var peripherals = [keyboard, mouse, printer, speakers, ];
    var myNum = .5;
    for (var i=0, i < peripherals.length, i++) {
     alert("Current peripheral is " + peripherals[i]);
    }
    if (myNum) {
      myNum++;
      alert("myNum" + myNum) ;
    }
    ```

  - Select _Save_
    - Observe that the record saves, but syntax errors are still shown
  - Hover over red underlined areas to view error messages from the Syntax Checker
  - Correct the script to resolve all detected errors:

    ```javascript
    //Script used to practice Syntax Checking.
    var peripherals = ["keyboard", "mouse", "printer", "speakers"];
    var myNum = 0.5;
    for (var i = 0; i < peripherals.length; i++) {
      alert("Current peripheral is " + peripherals[i]);
    }
    if (myNum) {
      myNum++;
      alert("myNum: " + myNum);
    }
    ```

  - Select _Update_ to save the corrected script

- **Notes**
  - Some syntax issues not flagged by the editor:
    - Missing quotes in array values
    - Extra comma in array declaration
    - Wrong variable reference: `peripheral[i]` instead of `peripherals[i]`

### Lab 2.1.1 - Two Simple Client Scripts

🎯 **Goal**: Create and test `onLoad` and `onCellEdit` Client Scripts to observe script behavior and form/list interaction

- **A. Create an onLoad() Client Script**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
  - Configure the form:
    - `Name`: `Lab 2.1.1 onLoad Alert`
    - `Table`: `Incident [incident]`
    - `UI Type`: `Desktop`
    - `Type`: `onLoad`
    - `Active`: _checked_
    - `Inherited`: _unchecked_
    - `Global`: _checked_
    - `Description`: `Lab 2.1.1 onLoad Client Script`
  - In the script editor:

    ```javascript
    function onLoad() {
      alert("The form has finished loading and is ready for user input.");
    }
    ```

  - Select _Format Code_
  - Select _Submit_

- **B. Test Your Work**

  - Open any Incident record
    - Observe: Alert message appears
  - Select _OK_
  - Modify any field value
  - Use the _Context menu > Save_ to remain on form
    - Alert appears again (onLoad triggered)
  - Create a new Incident
    - Observe: Alert displays on form load
  - Deactivate the Client Script:
    - Reopen `Lab 2.1.1 onLoad Alert`
    - Uncheck `Active`
    - Select _Update_

- **C. Create an onCellEdit() Client Script**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
  - Configure the form:
    - `Name`: `Lab 2.1.1 onCellEdit Alert`
    - `Table`: `Incident [incident]`
    - `UI Type`: `Desktop`
    - `Type`: `onCellEdit`
    - `Field Name`: `State`
    - `Active`: _checked_
    - `Inherited`: _unchecked_
    - `Global`: _checked_
    - `Description`: `Lab 2.1.1 onCellEdit Alert`
  - In the script editor:

    ```txt
    Your pseudo-code:

    Create the saveAndClose variable with the value of true.

    If the newValue of State is Resolved, alert the user that they cannot change State to Resolved from a list and set the value of the saveAndClose variable to false.
    If the newValue of State is Closed, alert the user that they cannot change State to Closed from a list and set the value of the saveAndClose variable to false.
    Execute the callback function returning the value of saveAndClose.

    If true is returned, the new value of the State field is committed.
    If false is returned, the new value of the State field is not committed.
    ```

  - Solution:

    ```javascript
    function onCellEdit(sysIDs, table, oldValues, newValue, callback) {
      var saveAndClose = true;

      if (newValue == 6) {
        // Resolved
        alert("you cannot change the state to 'Resolved' from a list");
        saveAndClose = false;
      }

      if (newValue == 7) {
        //Closed
        alert("you cannot change the state to 'Closed' from a list");
        saveAndClose = false;
      }

      callback(saveAndClose);
    }
    ```

  - Select _Submit_

- **D. Test Your Work**
  - Navigate to **Incident > Open**
  - Record the current value of any Incident's `State` field
  - Attempt to change `State` to `Resolved` from the list:
    - Double-click the `State` field
    - Select `Resolved` and click the checkmark
    - Alert appears: “You cannot change the state to 'Resolved' from a list”
    - Value does **not** update (callback returned `false`)
  - Use multi-select:
    - Hold _Shift_, select multiple `State` fields (background turns purple)
    - Double-click one selected field, change to `Closed`, then _Save_
    - Alert appears: “You cannot change the state to 'Closed' from a list”
    - No fields update (callback returned `false`)
  - Deactivate the Client Script:
    - Reopen `Lab 2.1.1 onCellEdit Alert`
    - Uncheck `Active`
    - Select _Update_

### Lab 2.2.1 - g_form and g_user

🎯 **Goal**: Use `g_form` and `g_user` methods in a Client Script to enforce P1 incident detail confirmation for non-Major Incident Managers

- **A. Preparation**

  - Create a new role:
    - Navigate to **User Administration > Roles**
    - Select _New_
    - `Name`: `major_inc_mgr`
    - `Description`: `Role required for Major Incident Managers`
    - Select _Submit_
  - Create a new group and assign the role:
    - Navigate to **User Administration > Groups**
    - Select _New_
    - `Name`: `Major Incident Managers`
    - `Description`: `Major Incident Managers`
    - Select _Save_ to remain on form
    - Under _Roles_ related list:
      - Click _Edit_, search for `major_inc_mgr`, add to list
      - Select _Save_
    - Under _Group Members_ related list:
      - Click _Edit_, add:
        - `Beth Anglin`
        - `Christen Mitchell`
        - `Don Goodliffe`
      - Select _Save_, then _Update_

- **B. Use Both g_form and g_user Methods in a Client Script**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
  - Configure the form:
    - `Name`: `Lab 2.2.1 Confirm Major Incident Details`
    - `Table`: `Incident [incident]`
    - `UI Type`: `Desktop`
    - `Type`: `onSubmit`
    - `Active`: _checked_
    - `Inherited`: _unchecked_
    - `Global`: _checked_
    - `Description`: `Confirm initial P1 details are included if the Incident creator is not a Major Incident Manager`
  - Implement script logic based on this pseudo-code:

    ```txt
    When the form is submitted, saved, or updated...

    If Impact and Urgency are both high and the user does not have the major_inc_mgr role...

    Create the ans variable to store the user's response in a confirmation box asking them to ensure base information is included in the record before submitting a Priority-1 incident.
    If the user cancels the submission...

    Generate an alert stating the incident was not submitted and provide instructions to use the Additional comments field if Major Incident base information is missing.
    Add a field message below the Category, Configuration item, Assignment group and Short description fields identifying them as Major Incident base fields.
    Return true or false based on the confirmation box response.
    ```

  - Solution:

    ```js
    function onSubmit() {
      if (
        g_form.getValue("impact") == 1 &&
        g_form.getValue("urgency") == 1 &&
        !g_user.hasRoleExactly("major_inc_mgr")
      ) {
        var ans = confirm(
          "Hallo " +
            g_user.firstName +
            ",\nThe customer is notified of all Priority-1 Incidents. Confirm basic information is included before submitting this P1 incident.\n\nSelect Ok to submit, or Cancel to return to the record."
        );

        if (!ans) {
          g_form.addInfoMessage("Incident is not submitted");
          g_form.addInfoMessage(
            "If base information is unavailable, use the 'Additional comments' field to document why it is missing."
          );

          g_form.showFieldMsg("category", "Major Incident base field");
          g_form.showFieldMsg("cmdb_ci", "Major Incident base field");
          g_form.showFieldMsg("assignment_group", "Major Incident base field");
          g_form.showFieldMsg("short_description", "Major Incident base field");
        }
        return ans;
      }
    }
    ```

  - Select _Submit_

- **C. Test Your Work**
  - Create a new Incident
    - Populate mandatory fields
    - Set `Impact` = `1 - High`, `Urgency` = `1 - High`
  - Select _Save_
    - Cancel the confirmation dialog
    - Observe:
      - Two info messages at top of form
      - Four field messages below:
        - `Category`
        - `Configuration item`
        - `Assignment group`
        - `Short description`
      - Incident is **not** submitted
  - Modify script to include `g_user.firstName` in confirmation message
    - Retest and confirm user's first name is displayed
  - Impersonate a Major Incident Manager:
    - Select avatar > _Impersonate User_
    - Choose:
      - `Beth Anglin`
      - `Christen Mitchell`
      - `Don Goodliffe`
    - Create new P1 Incident
      - No confirmation message appears (user has required role)
  - End impersonation:
    - Select avatar > _End Impersonation_
  - Deactivate Client Script:
    - Reopen `Lab 2.2.1 Confirm Major Incident Details`
    - Uncheck `Active`
    - Select _Update_

### Lab 2.3.1 - Debugging Client Scripts

🎯 **Goal**: Debug a Client Script using ServiceNow messages and `alert()` to validate variable values and script flow

- **A. Preparation**

  - Open the Client Script: `Lab 2.3.1 Client Script Debugging Client Script`
  - Check the `Active` checkbox to enable it
  - Review the pseudo-code for logic structure:

    ```txt
    - On Impact change:
      - Store current State in variable incState
      - If incState == 1:
        - Add decoration and flash label aqua
      - If Impact is High or Medium:
        - Remove State choices: On Hold, Resolved, Closed, Canceled
        - Add info message about removal
      - Else (not High or Medium and not loading):
        - Clear State choice list
        - Add options back
        - Reset State field to incState
    ```

  - Add the script to the Syntax Editor
  - Select _Create Favorite_ on form’s context menu for easy access
  - Select _Update_

- **B. Observe the Current Execution of the Script**

  - Create a new Incident
  - Without changing `State`, open its choice list and note all values
  - Set `Impact` = `1 - High`
  - Confirm the following:
    - Decoration on `State` field: ❌ No
    - State label flashes aqua: ❌ No
    - State options reduced to `New` and `In Progress`: ✅ Yes
    - Info message at top: ✅ Yes

- **C. Use the alert() Method to Confirm Variable Values and Script Execution**

  - Open the Client Script again
  - Add debugging `alert()` messages:

    ```javascript
    function onChange(control, oldValue, newValue, isLoading, isTemplate) {
      if (isLoading || newValue == "") {
        return;
      }

      var incState = g_form.getValue("incident");
      alert("Debug - The value of incState is: " + incState);

      if (incState == 1) {
        alert("Debug - LINE 11 EXECUTED!");
        g_form.addDecoration("state", "icon-edit", "Gathering initial details");
        g_form.flash("state", "aqua", 4);
      }

      if (newValue == "1" || newValue == "2") {
        g_form.removeOption("state", "3");
        g_form.removeOption("state", "6");
        g_form.removeOption("state", "7");
        g_form.removeOption("state", "8");
        g_form.addInfoMessage("The State options have been removed");
      } else if (!isLoading && newValue != "1" && newValue != "2") {
        g_form.clearOptions("state");
        g_form.addOption("state", "1", "New");
        g_form.addOption("state", "2", "In Progress");
        g_form.addOption("state", "3", "On Hold");
        g_form.addOption("state", "6", "Resolved");
        g_form.addOption("state", "7", "Closed");
        g_form.addOption("state", "8", "Canceled");
        g_form.setValue("state", incState);
      }
    }
    ```

  - Select _Update_

- **D. Force the Updated Script to Execute**

  - Create a new Incident and save the record
  - Set `Impact` = `1 - High`
  - Confirm:
    - `incState` value (via alert): ❌ Empty
    - `LINE 11 EXECUTED` alert: ❌ Not shown
  - Right-click the `State` field label to confirm field name: `state`
  - Fix variable reference:

    ```javascript
    var incState = g_form.getValue("state");
    ```

  - Select _Update_
  - Create new Incident again, set `Impact` = `1 - High`
  - Confirm:
    - `incState` alert shows `1`
    - `LINE 11 EXECUTED!` alert shows
    - Decoration and flash applied to `State`
    - State options reduced
    - Info message shown

- **E. Final Debugging and Validation**
  - Confirm you are not the only one seeing the InfoMessage: ❌ Everyone can see it
  - Debugging via form messages and `alert()` is best suited for: ✅ Development
  - Update `Impact` to `3 - Low`
  - Fix error in `else if` block if needed (check for syntax, casing, logic)
  - Retest until no errors remain

### Lab 3.1.1 - Incident Resolved/Closed UI Policy

🎯 **Goal**: Create a UI Policy that triggers on `Resolved` or `Closed` states to adjust field behaviors and provide user guidance

- **A. Create a UI Policy**

  - Navigate to **System UI > UI Policies**
  - Select _New_
  - Configure the UI Policy:
    - `Table`: `Incident [incident]`
    - `Active`: _checked_
    - `Short Description`: `Lab 3.1.1 Incident Resolved or Closed`
    - `Order`: `100` (If not visible, use _Configure > Form Layout_ to add)
    - `Condition`: `State` **is one of** `Resolved`, `Closed` (use _Shift_ to select both)
    - `Global`: _checked_
    - `On Load`: _unchecked_
    - `Reverse if false`: _checked_
    - `Inherit`: _unchecked_
  - Select _Save_ to remain on form

- **Add UI Policy Action: Urgency (Read-only)**

  - Scroll to **UI Policy Actions** and select _New_
    - `Field name`: `Urgency`
    - `Read Only`: _True_
    - Leave `Mandatory` and `Visible` unchanged
  - Select _Submit_
  - If red error icon appears next to Urgency:
    - Open the Urgency action
    - Select link to conflicting UI Policy (e.g., _Make fields read-only on close_)
    - Record its `Order` value (e.g., `100`)
    - Return to `Lab 3.1.1 Incident Resolved or Closed`
      - Switch to _Advanced view_ if needed
      - Set `Order` to a value higher than the conflicting policy (e.g., `200`)
      - Select _Save_
    - Confirm the error icon disappears

- **Add Additional UI Policy Actions**

  - _Resolved by_: `Mandatory` = _True_
  - _Impact_: `Read Only` = _True_

- **Add Execute if True Script**

  - On the _Script_ tab, check _Run scripts_
  - Expand _Show Script_ and copy into `Execute if true`:

    ```javascript
    if (
      g_form.getValue("close_code") == "" ||
      g_form.getValue("close_notes") == "" ||
      g_form.getValue("resolved_by") == ""
    ) {
      g_form.addInfoMessage(
        "REMINDER: Populate the Resolution Information fields before saving an Incident in a Resolved or Closed State."
      );
    }
    ```

  - Select _Format Code_
  - Select _Update_

- **B. Test Your Work**

  - Open any Incident record
  - Set `State` = `Resolved` or `Closed`
    - Confirm:
      - `Impact` and `Urgency` fields are read-only
      - `Resolved by` is mandatory
      - Info message appears:  
        _“REMINDER: Populate the Resolution Information fields before saving an Incident in a Resolved or Closed State.”_
  - Set `State` = `In Progress`
    - Info message should disappear

- **Add Execute if False Script**

  - Reopen `Lab 3.1.1 Incident Resolved or Closed` UI Policy
  - On _Script_ tab, add to `Execute if false`:

    ```javascript
    function onCondition() {
      g_form.clearMessages();
    }
    ```

  - Select _Update_
  - Test again:
    - Set `State` = `Resolved` or `Closed`, confirm info message appears
    - Change `State` back to `In Progress`, confirm message disappears

- **Confirm Behavior**
  - `Reverse if false` **must** be selected for `Execute if false` to run
  - If `Execute if false` is empty, nothing will happen—even if `Reverse if false` is checked

### Lab 4.1.1 - Debugging Business Rules

🎯 **Goal**: Debug a Business Rule using multiple server-side debugging strategies, including Script Debugger, logs, Script Tracer, and the Debug Business Rule feature

- **A. Preparation**

  - Navigate to **System Definition > Business Rules**
  - Open `Lab 4.1.1 Business Rule Debugging`
  - Check `Active`
  - In the Script, replace `<your_initials>` with your initials in the error message:

    ```javascript
    catch (err) {
      gs.error("abc: a JavaScript runtime error occurred - " + err);
    }
    ```

  - Select _Save_
  - Review when the script triggers and what it does
  - Select _Create Favorite_ for quick access

- **B. Use Script Debugger – Breakpoints and Variables**

  - Set breakpoints in the Script at:
    - `var myNum = current.state;`
    - `var priorityValue = current.priority;`
    - `var createdValue = current.sys_created_on;`
    - `SlaTargetNotification(priorityValue, createdValue);`
  - Select _Open Script Debugger_ (Editor actions) and keep it open
  - Trigger Business Rule:
    - Open an active Incident
    - Change `State` ≠ `Closed`
    - Select _Save_
  - In Script Debugger:
    - Select _Start Debugging_
    - Script pauses at first breakpoint (line highlighted red)
    - Expand _Local variables_ and note if `myNum` is shown
    - Select _Next Breakpoint_ and re-check `myNum` (value now visible)
    - Repeat for `priorityValue` and `createdValue`
    - On last breakpoint, allow script to complete

- **C. Use Script Debugger – Current vs Previous Values**

  - Keep Script Debugger open
  - Open an Incident with a non-matching `Short description`
  - Trigger the rule:
    - Change `State` ≠ `Closed`, select _Save_
  - Start Debugging
  - Expand:
    - `previous.short_description` → record this value
    - `current.short_description` → record this value
  - ✅ Conclusion: `current` contains updated values, `previous` contains original values

- **D. Use Script Debugger – Call Stack**

  - Navigate to **System Definition > Script Includes**
  - Open `SlaTargetNotification`
  - Set breakpoint on `gs.info` line
  - Open Script Debugger
  - Confirm breakpoints include Script Include line
  - In Debugger, load `Lab 4.1.1 Business Rule`
  - Set only these breakpoints:
    - `var createdValue = ...`
    - `try { ...`
  - Trigger rule:
    - Open active Incident, change `State`, select _Save_
  - Start Debugging:
    - Confirm current script in Code Pane Header
    - Select _Next Breakpoint_ → debugger jumps into `SlaTargetNotification`
    - Confirm script name in header is `Script Include`
    - Select _Next Breakpoint_ → debugger returns to Business Rule
    - Header confirms context shift

- **E. Debug Using GlideSystem Logging**

  - Open `Lab 4.1.1 Business Rule Debugging Business Rule`
  - Remove all breakpoints
  - Review script:

    ```javascript
    try {
      thisFunctionDoesNotExist();
    } catch (err) {
      gs.error("abc: a JavaScript runtime error occurred - " + err);
    }

    thisFunctionAlsoDoesNotExist();
    ```

  - Trigger rule:
    - Open Incident, change `State`, select _Update_
  - Navigate to **System Logs > System Log > Script Log Statements**
    - Search `Message` for `thisFunction`
    - ✅ Only `thisFunctionDoesNotExist()` logs an error (in try/catch)
    - ❌ `thisFunctionAlsoDoesNotExist()` does not log (not caught)

- **F. Debug Using Script Tracer**

  - Navigate to **System Diagnostics > Script Tracer**
  - Select _Start Tracer_
  - Trigger rule:
    - Create Incident:
      - `Caller`: Joe Employee
      - `Category`: Hardware
      - `Short Description`: Cassette player is broken
    - Select _Save_
  - In Script Tracer:
    - Select second _Save - UI Action_
    - Confirm Incident fields match inputs
    - Select `Lab 4.1.1 Business Rule Debugging`
    - Confirm `short_description` updated per rule
    - Review both error entries
    - ✅ Conclusion: Script Tracer logs **both** errors (even outside try/catch), unlike GlideSystem logs

- **G. Debug Using Debug Business Rule Feature**

  - Navigate to **System Diagnostics > Session Debug > Debug Business Rule**
  - In another tab:
    - Open a **Closed** Incident
    - Modify any field and select _Save_
  - In Session Log tab, search for: `4.1.1 Business Rule Debugging`
    - Confirm rule was **skipped** due to condition `current.state != 7` not being met
  - Navigate to **System Security > Debugging > Stop Debugging**
  - Deactivate `Lab 4.1.1 Business Rule Debugging Business Rule`

### Lab 4.1.2 - Current and Previous

🎯 **Goal**: Create a Business Rule using `current` and `previous` objects to automatically manage RCA tracking fields on the Incident form

- **A. Preparation**

  - Open an Incident form
  - Right-click header → _Configure > Form Builder_
  - Select _+ Add a field_
    - Field 1:
      - `Column label`: `RCA included`
      - `Column name`: `u_rca_included`
      - `Type`: `True/False`
    - Click _Add_
  - Select _Add another one_
    - Field 2:
      - `Column label`: `RCA`
      - `Column name`: `u_rca`
      - `Type`: `String`
    - Click _Add_, then _Done_
  - In Form Builder layout:
    - Drag `RCA included` below `Description`
    - Drag `RCA` below `RCA included`
  - Select _Save_
  - Close Form Builder and reload Incident form

- **B. Create the Business Rule**

  - Navigate to **System Definition > Business Rules**
  - Select _New_
  - Configure:
    - `Name`: `Lab 4.1.2 RCA Included`
    - `Table`: `Incident [incident]`
    - `Active`: _checked_
    - `Advanced`: _checked_
    - `When`: `before`
    - `Order`: `125`
    - `Insert`: _checked_
    - `Update`: _checked_
  - In _Script_ field, start with:
    - Type `try` and press `<Tab>` to insert macro
  - Format the code, and replace error handling line:

    ```javascript
    (function executeRule(current, previous /*null when async*/) {
      try {
        if (current.u_rca.nil() && current.u_rca_included) {
          current.u_rca_included = false;
        } else if (!current.u_rca.nil() && !current.u_rca_included) {
          current.u_rca_included = true;
        }
      } catch (err) {
        gs.error("A runtime error occurred: " + err);
      }
    })(current, previous);
    ```

  - Select _Submit_

- **C. Test Your Work**
  - Open any Incident record
  - Step 1: Check `RCA included` and _Save_
    - Field should become unchecked (if `RCA` is empty)
  - Step 2: Enter any value in `RCA` and _Save_
    - Field `RCA included` should become checked
  - ✅ Confirm:
    - RCA included updates automatically based on RCA content
  - 🔒 `RCA included` field does **not** need to remain visible on the form
    - Field can be used for reporting or querying only
  - Deactivate the Business Rule:
    - Reopen `Lab 4.1.2 RCA Included`
    - Uncheck `Active`
    - Select _Update_

### Lab 4.1.3 - Display Business Rules and Dot-Walking

🎯 **Goal**: Use the `g_scratchpad` object to pass server-side data (via Display Business Rule) to a Client Script using dot-walking and conditionally prompt the user when reopening an Incident

- **A. Create a Display Business Rule**

  - Navigate to **System Definition > Business Rules**
  - Select _New_
  - Configure:
    - `Name`: `Lab 4.1.3 Display Business Rule`
    - `Table`: `Incident [incident]`
    - `Active`: _checked_
    - `Advanced`: _checked_
    - `When`: `display`
    - `Order`: `150`
  - Script:

    ```javascript
    (function executeRule(current, previous /*null when async*/) {
      g_scratchpad.resolvedByFirstName = current.resolved_by.first_name;
      g_scratchpad.resolvedByLastName = current.resolved_by.last_name;

      if (current.reopen_count.nil()) {
        g_scratchpad.reopenCount = "0";
      } else {
        g_scratchpad.reopenCount = current.reopen_count;
      }
    })(current, previous);
    ```

  - Select _Submit_

- **B. Create a Client Script**

  - Navigate to **System Definition > Client Scripts**
  - Select _New_
  - Configure:
    - `Name`: `Lab 4.1.3 ResolvedBy Client Script`
    - `Table`: `Incident [incident]`
    - `UI Type`: `Desktop`
    - `Type`: `onChange`
    - `Field Name`: `State`
    - `Active`: _checked_
    - `Inherited`: _unchecked_
    - `Global`: _checked_
  - Script:

    ```javascript
    function onChange(control, oldValue, newValue, isLoading, isTemplate) {
      if (isLoading || newValue === "") {
        return;
      }

      // 6 = Resolved, 7 = Closed, 8 = Canceled
      if (
        (oldValue == "6" || oldValue == "7" || oldValue == "8") &&
        newValue != "6" &&
        newValue != "7" &&
        newValue != "8"
      ) {
        var answer = confirm(
          "This incident was resolved by " +
            g_scratchpad.resolvedByFirstName +
            " " +
            g_scratchpad.resolvedByLastName +
            " and has been reopened " +
            g_scratchpad.reopenCount +
            " times.\n\nAre you sure you want to reopen it?"
        );

        if (!answer) {
          g_form.setValue("state", oldValue);
        }
      }
    }
    ```

  - Select _Submit_

- **C. Test Your Work**
  - Open an Incident in `Resolved` state (or create and resolve one)
  - Fill Resolution Information fields and _Save_
  - Change `State` to `In Progress`
    - ✅ Confirmation dialog should appear
    - ✅ Names and reopen count from `g_scratchpad` should display
  - Click _Cancel_ in confirmation
    - ✅ State should revert to original (`Resolved`)
  - Repeat change to `In Progress` and click _OK_
    - _Save_ the record to remain on form
  - Set State back to `Resolved`, repopulate Resolution fields, and _Save_
  - Set State to `In Progress` again
    - ✅ Reopen count should increment
  - Deactivate both scripts:
    - `Lab 4.1.3 Display Business Rule` → _Inactive_
    - `Lab 4.1.3 ResolvedBy Client Script` → _Inactive_

### Lab 5.1.1 - Set the CAB Date

🎯 **Goal**: Automatically set the CAB date for new Change Requests to the next Wednesday using `GlideSystem` and `GlideDateTime`

- **A. Create a Business Rule**

  - Navigate to **System Definition > Business Rules**
  - Select _New_
  - Configure:
    - `Name`: `Lab 5.1.1 Set CAB Date`
    - `Table`: `Change Request [change_request]`
    - `Active`: _checked_
    - `Advanced`: _checked_
    - `When`: `before`
    - `Order`: `300`
    - `Insert`: _checked_
  - In the _Script_ tab:

    - Type `try` and press `<Tab>` to insert macro (from Lab 1.3.1)
    - Replace the script content with:

      ```javascript
      (function executeRule(current, previous /*null when async*/) {
        try {
          var gdt = new GlideDateTime(gs.beginningOfNextWeek());
          gdt.addDaysLocalTime(2); // Adds 2 days = Wednesday
          current.setValue("cab_date_time", gdt);
        } catch (err) {
          gs.error("A runtime error occurred: " + err);
        }
      })(current, previous);
      ```

    - Select _Format Code_

  - Select _Submit_

- **B. Test Your Work**
  - Create a new Change Request:
    - Select **Models > Normal: ITIL Mode 1 Normal Change**
    - Set `Short description`: `Testing Lab 5.1.1`
  - Save the record
  - Navigate to the _Schedule_ tab
    - ✅ Verify `CAB Date/Time` is set to the upcoming Wednesday
  - If value is incorrect, debug and re-test logic
  - Deactivate the Business Rule:
    - Reopen `Lab 5.1.1 Set CAB Date`
    - Uncheck `Active`
    - Select _Update_

### Lab 5.1.2 - Re-Open Problem Date Validation

🎯 **Goal**: Enforce a policy that prevents Problem records from being reopened if they were closed more than 30 days ago using GlideDateTime logic in a UI Action

- **A. Update a UI Action**

  - Navigate to **Problem > All**
  - Open any Problem record
  - Right-click header → _Configure > UI Actions_
  - Locate and open **UI Action: Re-Analyze**
    - (Tip: Alternatively, right-click the _Re-Analyze_ link on the form and select _Edit UI Action_)
  - Update the script with the following:

    ```javascript
    action.setRedirectURL(current);

    try {
      var today = new GlideDateTime();
      var closed = new GlideDateTime(current.closed_at);

      if (closed) {
        var dateDiff = GlideDateTime.subtract(closed, today);
        var dateDiffNum = dateDiff.getDayPart();

        if (dateDiffNum > 30) {
          gs.addErrorMessage(
            "A problem cannot be reopened after it has been closed for more than 30 days. Please open a new Problem."
          );
        } else {
          new ProblemStateUtils().onReAnalyze(current);
        }
      }
    } catch (err) {
      gs.error("A runtime error occurred: " + err);
    }
    ```

  - Select _Update_

- **B. Test Your Work**

  - Navigate to **Problem > All**
  - Open a Problem record with:
    - `State`: `Closed`
    - `Resolution code`: `Risk Accepted`
    - `Closed date`: more than 30 days ago
    - (Adjust list view if necessary to display these fields)
  - Select the **Re-Analyze** UI Action
    - ✅ Confirm error message appears:
      _"A problem cannot be reopened after it has been closed for more than 30 days. Please open a new Problem."_
    - ❌ If not, debug the date comparison logic and re-test

- **C. Revert to the Original Version**
  - Reopen the **UI Action: Re-Analyze**
  - In the _Versions_ related list:
    - Select both the _Current_ and a _Previous_ version
    - From _Actions on selected rows..._, select **Compare**
  - In the _Compare to Current_ view:
    - Select the `Script` field
    - Compare and determine if the selected version is the original
  - If so:
    - Click _Revert to Selected Version_
    - Select _OK_ when prompted
  - Confirm the script has been restored in the Re-Analyze UI Action
