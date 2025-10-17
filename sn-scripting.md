# Scripting on ServiceNow

## Resources

- [📜 ServiceNow Development Handbook by Tim Woodruff](./30-sn-dev-handbook.md)
- [Customization Best Practices (PDF)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/customization-best-practices.pdf)

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
