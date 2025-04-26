# ServiceNow Development Handbook

[Tim Woodruff](https://www.linkedin.com/in/sn-timw/)

## Resources

- [books](http://books.snc.guru/)
- [blog](http://snprotips.com/)
- [code examples](https://github.com/thisnameissoclever/sn_dev_handbook_3/tree/a31e35c9f09a61dd021bf4883159307222b00f58)

## Code & Coding Guidelines

- use _pure functions_: functions without side effects
  - avoid pass-by-reference (PBR) problems:
    - primitive types (string, number, boolean) are passed by value <- no side effects as the original reference is not changed
    - objects are passed by reference <- side effects as the original reference points to the same object
  - declare variables used in the function

```js
function sayHello(myName) {
  alert("Hello, " + myName + "!");
}
```

- Don't Repeat Yourself: **DRY**
  - use objects or arrays to loop over data
- use _Constructors_ to create objects
  - capital function name: `function Person(name, age) {...}`
  - use `new` keyword to create object: `var myPerson = new Person("John", 30);`
  - find object constructor name: `myPerson.constructor.name`

```js
var i, grRecord, stateChange, stateChangeDetails;

//constructor
function StageChangeDetail(table, query, state) {
  this.table_name = table;
  this.encoded_query = query;
  this.state_value = state;
}

stateChangeDetails = [
  //An array of StateChangeDetail objects
  new StageChangeDetail("incident", "some_query", 3),
  new StageChangeDetail("problem", "some_other_query", 4),
  new StageChangeDetail("change_request", "yet_a_third_query", 5),
];

for (i = 0; i < stateChangeDetails.length; i++) {
  stateChange = stateChangeDetails[i];
  grRecord = new GlideRecord(stateChange.table_name);
  grRecord.addEncodedQuery(stateChange.encoded_query);
  grRecord.query();
  while (grRecord.next()) {
    //set state to work in progress
    grRecord.setValue("state", stateChange.state_value);
    grRecord.update();
  }
}
```

- or use functions

```js
changeState("incident", 3, "some_query");
changeState("problem", 4, "some_other_query");
changeState("change_request", 5, "third_query");

/**
 * Update the state of all records in the provided table, which match the provided encoded query.
 * @param {string} tableName - The name of the table to run this operation against
 * @param {string|number} newState - The new value for the state field. This may be an integer or string, depending on the value expected by the table provided.
 * @param {string} [encodedQuery] - A string containing the encoded query to filter the records on which to perform this operation. If no query is provided, ALL records in the table will be modified.
 * @return {number} - The number of records on which this operation was performed.
 */
function changeState(tableName, newState, encodedQuery) {
  var grRecord = new GlideRecord(tableName);
  if (encodedQuery) {
    grRecord.addEncodedQuery(encodedQuery);
  }

  grRecord.setValue("state", newState); //set state to work in progress
  grRecord.updateMultiple();

  return grRecord.getRowCount();
}
```

- getter and setter
  - use `.getValue()` and `.setValue()` to get and set field values and avoid pass-by-reference problems
    - exceptions:
      - Journal fields - write directly: `grRecord.work_notes = "some text";`
        - use `grRecord.work_notes.getJournalEntry(1)` to read the latest work note
        - use `grRecord.work_notes.getJournalEntry(-1)` to get all work notes (delimiter: `\n\n`)
      - Catalog variables - get values with `.toString()` and avoid PBR issues
      - Dot-walking
        - also use `.toString()` to avoid PBR issues
        - do not dot-walk for more than three layers - if necessary use `grRecord.getRefRecord()` to get the server-side GlideElement object
- be consistent
  - string declaration: single `'` or double quotes `"`
  - curly-brace placement - see [One True Brace Style (1TBS)](<https://en.wikipedia.org/wiki/Indentation_style#Variant:_1TBS_(OTBS)>)
  - indentation - use a Code Editor with (auto) formatting to avoid manual errors
- field security vs. field obscurity
  - client-side measure (UI Policy, Client Script) can be bypassed and are only to be used for user convenience
  - use server-side measures (ACL, Business Rule, Data Policy) to enforce security
  - combine client-side and server-side measures for best results

### UI Policies vs. Client Scripts

- UI Policies are simpler and do not allow for complex logic
  - use UI Policies for simple field visibility, mandatory, and read-only settings
- only use Client Scripts when complex scenarios make it necessary
  - document why you habe to use a Client Script
  - include logic to:
    - handle the reverse-if-false scenario or when the condition is no longer true
    - consider first-time load (if `isLoading` is true)
    - consider triggering field of an `onChange` Client Script
- setVisible() vs. setDisplay() (Client Script)
  - `g_form.setVisible()` hides the field and its label, but leaves a blank space
  - `g_form.setDisplay()` hides the field and its label, and collapses the blank space

### Business Rules

- Business Rule Order: `current.update()`
- ![Business Rule Order](./attachments/sn-dev-hb-business-rule-trigger.png)
- always triggered by database operations: `insert`, `update`, `delete`, `query`
- when - in relation to db operations:
  - `before`
    - alter the record before it is written to the db, do not use to alter other records
    - `current.setAbortAction(true)` - stop the operation
      - or use the _Abort action_ checkbox in the Business Rule
    - no need for `current.update()`, as the operation is already on the way to the db
    - avoid long scripts - user has to **wait** for execution!
  - `after`
    - after db operation but before the record is displayed
    - very good to update related records that should be displayed in the current view - for example related list records
      - use async for related records that are currently not displayed
    - be careful with `current.update()`, as it triggers the Business Rule again (infinite loop potential!)
    - avoid long scripts - user has to **wait** for execution!
  - `async`
    - will be executed in a few seconds - but the user does not have to wait
    - for related records that are currently not displayed
    - caveat: previous state of `current` record is not available
    - be careful not to run into race conditions
  - `display`
    - triggered after the record is _retrieved_ from the db
    - modify displayed data **without** altering the record (as long as `current.update()` is not used - do not!)
    - often used to populate the _scratchpad_ for client scripts

### Client-Side Performance: Use Asynchronous Calls

- Problem: Synchronous server calls (`GlideRecord`, `GlideAjax`) executed in client-side scripts freeze the browser and negatively impact user experience.
- Solution: Always prefer asynchronous client-server interactions to maintain responsive user interfaces.
- approaches:
  - **Display Business Rules** (Server-side)
    - Ideal if:
      - Required data and retrieval conditions are known at page load.
    - Usage:
      - Populate `g_scratchpad` with server data accessible to Client Scripts, UI Policies, and UI Actions.
      - Modify the `current` object directly if form data adjustments are needed.
    - Limitations:
      - Does NOT apply to Catalog Client Scripts — use AJAX (`GlideAjax`) instead.
  - **GlideAjax** (Asynchronous, Client-side initiated)
    - Ideal if:
      - Conditions for retrieving data are dynamic or unknown at form load.
      - Complex logic or larger data sets are involved.
  - **Asynchronous GlideRecord** (Client-side)
    - Acceptable for:
      - Small, infrequent queries (retrieving single or limited records).
      - Reference field lookups using `g_form.getReference()` with callbacks.
  - Further Examples & Details: [GlideRecord & GlideAjax: Client-Side Vs. Server-Side](https://snprotips.com/blog/2016/2/6/gliderecord-client-side-vs-server-side)
- this can be a challenge for **onSubmit** Client Scripts:
  - challenge: async callbacks cannot stop form submission once initiated
  - async calls are a GlideAjax script, a GlideRecord query, or a getRefRecord() query
  - solution: Use a combination of client data variables (setClientData, getClientData) and a self-submitting callback
    - The general workflow is:
      - Initial form submission triggers validation (onSubmit).
      - Validation result stored via setClientData.
      - If validation passes (getClientData is true), form submits normally.
      - If validation fails, form submission is halted, and an error message is displayed.
  - more incl. code example: [Asynchronous onSubmit Catalog/Client Scripts in ServiceNow](https://snprotips.com/blog/2018/10/19/synchronous-lite-onsubmit-catalogclient-scripts)

### DOM Manipulation

- Concept: Direct DOM manipulation is strongly discouraged in ServiceNow, particularly in the Service Portal.
- Problem: Manipulating the DOM directly leads to compatibility and maintainability issues.
- Recommended Approach:
  - Avoid direct DOM manipulation entirely, using out-of-box methods and APIs whenever possible.
  - For functionality previously reliant on DOM manipulation (e.g., validating attachments in Service Portal), custom APIs or scripts are required.
    - Example workaround: Implement a custom API (`sp_form.getAttachments()`) via Script Include and JS Include.
    - Implementation details: [portalattachments.snc.guru](http://portalattachments.snc.guru/)
- Client Scripts:
  - To ensure functionality in Service Portal, set Catalog Client Script type to either:
    - **All** (recommended for universal functionality)
    - **Mobile / Service Portal** (specifically for portal-only scenarios)
  - Clearly document exceptions where scripts differ between classic UI and Service Portal to maintain clarity

## Debugging

- _All > System Diagnostics > Session Debug_

### Server-Side Debugging

- Concept: The **Script Debugger** pauses synchronous server-side scripts, enabling step-by-step inspection of variable states and logic flow.
- Problem: Identifying issues in complex server-side scripts can be challenging without visibility into real-time execution and variable states.
- Recommended Approach:
  - **Set Breakpoints** in the script editor (click line numbers) to indicate where execution should pause.
  - **Use Script Debugger** (`System Diagnostics > Script Debugger`) to inspect variables and execution paths.
    - Debugger provides controls for navigating through paused scripts:
      - **Stop Debugging** (pause icon): Ends debugging entirely.
      - **Resume Execution** (play icon): Continues execution until next breakpoint.
      - **Step Over**: Executes current line without entering function calls.
      - **Step Into**: Executes current line and enters function calls, allowing detailed debugging within the called function (if accessible).
        - Limitations: Cannot step into black-box system APIs (e.g., `gs.nowDateTime()`).
      - **Step Out**: Exits current function and resumes debugging in the calling script.
    - View **Local Variables** in real-time; use Console for complex object inspection.
- Limitations:
  - Only synchronous operations can be debugged (e.g., Business Rules, Script Includes).
  - Asynchronous operations and certain inbound API calls cannot be debugged directly.
    - REST APIs can be debugged synchronously via **REST API Explorer** (_System Web Services > REST > REST API Explorer_).
- **Debugger Console**: Evaluate real-time values of variables, including those not clearly displayed in the Local panel.
  - Execute arbitrary code snippets mid-debugging to inspect or alter script behavior temporarily.
  - Type JavaScript code directly into the Console; the result of the last line executed is displayed immediately.
    - Example: Typing `grIncident.isNewRecord();` returns `true` or `false`.
  - Dynamically modify variable values mid-execution to test conditional logic or script paths interactively.
    - Changes made via Console are temporary, affecting only the current debugging session.
  - Limitations: Does NOT persist changes beyond the current debugging instance.
  - Recommendation: Leverage this console for rapid experimentation, validating logic, or inspecting complex data structures

### Client-Side Debugging

- Concept: Client-side scripts (Client Scripts, UI Scripts, Catalog Client Scripts) run in the browser, not on the server, thus requiring browser developer tools for debugging.
- Recommended Approach:
  - Use built-in browser developer tools (e.g., Chrome DevTools) for client-side debugging:
    - Add the statement `debugger;` directly into your client-side scripts where you want execution to pause.
    - Open browser developer tools (F12 in Chrome) and trigger your script.
    - Execution pauses at the `debugger;` statement, enabling inspection of variables, step-by-step execution, and call stack visibility.
  - Browser debugger UI includes familiar controls: Resume Execution, Step Over, Step Into, Step Out
    - **Scope/Local** Panel (below Call Stack, right side): Inspect real-time values of local script variables.
- Additional Tips:
  - **Client-side Script Executor**:
    - Press `CTRL+SHIFT+]` on a record form to open a client-side script executor for quick script testing.
  - **Asynchronous Debugging**:
    - Place `debugger;` statements within callback functions to debug asynchronous code.
    - To retain context during asynchronous debugging, add a second `debugger;` statement in synchronous code and click "Resume Execution" in between

### Common Bugs

- **`.update()` in Business Rules**
  - **Never** use `current.update()` within a Business Rule.
    - Causes unintended double updates, potentially creating infinite loops and serious performance issues.
  - **Recommended approach**:
    - Modify the `current` record directly within **before** Business Rules (no `update()` call needed).
    - If peripheral (related) records need updating, perform in an **after** or **async** Business Rule.
- **`.update()` Can Also Insert**
  - GlideRecord `.update()` method can unexpectedly insert new records if the GlideRecord object does not reference an existing record.
- **`.setWorkflow(false)` vs. `.autoSysFields(false)`**
  - `.setWorkflow(false)` prevents Business Rules, workflows, and cascade operations (including cascade deletes). Be cautious, as this might cause orphaned records.
  - `.autoSysFields(false)` prevents automatic updates to system fields (`sys_updated_on`, `sys_updated_by`).
    - Important when performing mass updates to avoid altering timestamps and user fields unintentionally.
- **Limiting Query Results**
  - Explicitly enforce single-record queries using `.setLimit(1)` for efficiency.
  - Use `if (grTask.next())` instead of `while (grTask.next())` when expecting exactly one record.
  - Validate single-record assumptions using `.setLimit(2)` and `.hasNext()`

## Naming Conventions

### Tables

- **Singular Table Names**
  - Always use **singular names and labels** for tables.
    - Correct examples: `incident`, `problem`, `change`
    - Incorrect: `incidents`, `problems`
  - Plural labels can be set explicitly in the table dictionary if needed (e.g., "Logbook Entries").
- **Specialized Table Prefixes**
  - Use clear prefixes for specialized utility tables:
    - **Data Lookup tables**: prefix with `u_dl_`  
      Example: `u_dl_incident_priority`
      - Must extend the Data Lookup Matcher Rules (`dl_matcher`) table.
    - **Many-to-many tables**: prefix with `u_m2m_`  
      Example: `u_m2m_user_group`
- **Capitalization**
  - Table labels should use **Title Case** (capitalize the first letter of each word).
  - Acronyms should be fully capitalized.

### Field Names and Labels

- **Consistency in Names and Labels**
  - Field **names** should clearly reflect their labels, using `snake_case`.
    - Example: Label "Business justification" → Name: `u_business_justification`
  - Do **NOT** include table names within field labels or names unless referencing a different table explicitly.
- **Reference Fields**
  - For fields referencing other tables, indicate clearly:
    - Label: "Related problem" | Name: `u_related_problem`
  - If a reference might change to another table in the future, consider using a more generic name (e.g., `u_related_task`) and a specific label.
- **Avoid Unnecessary Words**
  - Do **NOT** add redundant terms like "ID" or "number" in labels for reference fields.
    - Example: Reference field to Incident table → simply labeled "Incident", not "Incident ID" or "Incident number".
- **Capitalization**
  - Field labels: **Sentence case** (capitalize only the first word, except acronyms).
  - Table labels: **Title Case** (capitalize first letter of each word).
- **Catalog Variables**
  - Use clear, concise "Question" fields to prompt users (e.g., "What is the business justification?").
  - Variable **names** use `snake_case`, no spaces, and **no** "u\_" prefix required.
- **Duplicate Variables**
  - General rule:
    - Avoid having multiple variables or fields with similar names and purposes (e.g., `u_name_1`, `u_name_2`).
  - Best Practices:
    - Use distinct, meaningful names whenever possible.
    - Only introduce numbered variables if absolutely necessary and no better solution exists.
    - Apply the same standard to both **names** and **labels** for database fields and catalog variables.

### JavaScript Variables

- **Naming conventions**:
  - Variables: use **camelCase** (e.g., `assigneeSysId`)
  - Classes (Script Includes): use **TitleCase** (e.g., `AssigneeUtils`)
  - Constants: use **UPPERCASE_WITH_UNDERSCORES** (e.g., `DEFAULT_QUERY_LIMIT`)
  - Variable names must start with a letter (lowercase for non-class variables).
- **Best Practices**:
  - Declare variables at the top of their scope or function.
  - **Do NOT** declare variables within loops (`while`, `for`) or conditional (`if`) blocks.
    - Avoids re-initialization, scope-related errors, or undefined variables.
  - Initialize variables with default values to prevent undefined errors (e.g., integers to `-1` or `0`).

#### Object Properties (Keys)

- **Naming conventions**:
  - Property names (keys) may use either **camelCase** (`propertyOne`) or **snake_case** (`property_one`).
  - Choose one style consistently throughout each object or related set of functionality.
  - Avoid mixing styles within the same context or object.

#### GlideRecords

- **Naming conventions**:
  - GlideRecord variables should start with `gr` (e.g., `grIncident`, `grOpenIncident`).
  - Use **singular** names, reflecting that a GlideRecord holds only one record at a time.
  - Arrays should use **plural** names (e.g., `sectionNames`, `openIncidents`).
- **Best Practices**:
  - Name GlideRecord variables descriptively to reflect their query context.
  - Update variable names if the associated query logic changes.
  - Prefer indicating object type prefixes for Glide objects (e.g., `gdtNoonYesterday` for a GlideDateTime object).

#### Iterators

- **Naming conventions**:
  - Use meaningful names if possible (e.g., `snInstance`, `food`).
  - Simple names like `i`, `p`, or `index` are acceptable for general-purpose loops.
  - Always differentiate iterator names in nested loops to avoid overwriting outer loop variables.
- **Best Practices**:
  - Iterators should be **block-scoped** — only used within the loop they control.
  - When iterating over object properties, always check `.hasOwnProperty()` to avoid inherited properties.
  - Prefer avoiding heavy nested loops (e.g., nested GlideRecord queries); instead, gather necessary data first (e.g., array of sys_ids) and query once.
  - For arrays, iterators usually represent integers — use simple names like `i` or descriptive names related to the content type if helpful.

### NC: Database Views

- **Naming conventions**:
  - Prefix all database view names with `dv_`.
  - Follow with a description of the joined tables (e.g., `dv_incident_problem`).

## Tables and Columns

### Custom Fields

- **Considerations before creating a custom field**:
  - **Necessity**:
    - Only add fields if the data genuinely adds value and no better solution exists.
  - **Existing Data**:
    - If the data already exists elsewhere, use a reference, derived field, or calculated field instead of creating a duplicate field.
- **Best Practices**:
  - If the value is always scripted or computed, use the **Calculated** option on the field's dictionary record and make the field read-only on the client.
  - Carefully decide whether the field should appear on forms or lists, and manage its visibility across views.
  - Follow established **naming conventions** for field names and labels (see: [Tables](#tables)).
- **Field Access and Security**:
  - Set fields to read-only or mandatory as appropriate.
  - Use server-side controls (ACLs, Data Policies, or Business Rules) to enforce access and edit rules, rather than relying only on client-side controls.
  - If blocking actions with `current.setAbortAction(true)`, consider checking `gs.getSession().isInteractive()` to allow background processes to proceed without interruption.

### Reference Fields

- **Concept**:
  - Reference fields (foreign keys) link records between tables but can impact performance when referencing large tables.
- **Best Practices**:
  - Use **Reference Qualifiers** to pre-filter available options and reduce search scope.
    - Improves client-side performance by limiting the number of queried records.
    - Makes auto-complete and search functionality faster and more responsive.
- **Further Optimization**:
  - Apply query efficiency principles (see: Performance > Query Efficiency) when defining reference qualifiers.

### Extending Tables

- **Concept**:
  - Table extensions inherit all fields from the parent table and store only additional differences in the child table.
- **Best Practices**:
  - Only extend a table if you need **most** of its fields.
  - Be aware that records from extending tables are also visible in the parent table (e.g., Incidents, Changes, and Problems all appear under Task).

### The Task Table

- **Concept**:
  - The `Task` table is a critical, heavily extended base table, represented as a large flat structure in the backend database.
- **Best Practices**:
  - **Protect the Task table**:
    - Avoid adding unnecessary fields, especially large fields (long strings, large max lengths).
    - Changes to Task directly affect all extended tables (Incident, Problem, Change, etc.).
  - **Use Overrides**:
    - Use **Label Overrides** and **Dictionary Overrides** to make changes specific to a child table without impacting all task-based tables.
- **Considerations**:
  - Only add new fields to `Task` if they are universally needed across all extending tables.
  - Be mindful of database performance impacts when modifying or extending the `Task` table structure.

#### The State Field

- **Concept**:
  - The `state` field on the `Task` table is an **integer** field that drives important ticket lifecycle logic across the platform.
- **Best Practices**:
  - **Do not** arbitrarily modify or remove existing state values or labels.
  - When adding new state values:
    - **Active states**: use integers **< 7** (positive or negative numbers like `-1`, `-2` if needed).
    - **Inactive states**: use integers **≥ 7** (aligned with "Resolved", "Closed", "Cancelled").
- **System Behavior**:
  - State values ≥ 7 are assumed inactive.
  - State values < 7 are assumed active.
  - Platform logic (e.g., `TaskStateUtil` Script Include) relies on dictionary attributes like `close_states` and `default_close_state` to manage state behavior.
- **Helpful Techniques**:
  - Use a **helper Script Include** to define and maintain state models for custom Task-based tables (e.g., `MyTaskStates` class).
  - When needed on the client side, pass state models using a **Display Business Rule** with `g_scratchpad`.
- **Additional Notes**:
  - **Value** defines the system meaning; **Sequence** controls the dropdown order.

### TaC: Database Views

- **Concept**:
  - Database Views combine data from multiple tables for reporting or simplified querying but must be used carefully due to performance impacts.
- **Best Practices**:
  - Prefer **dot-walking** over database views if using proper reference fields.
    - Example: Use `ordered_for.department` instead of creating a view to join Orders and Users tables.
  - Only use a database view if dot-walking is insufficient.
- **Creation Guidelines**:
  - The **first (left) table** should be the table with **fewer records** to optimize performance.
  - **Coalesce** only on fields with **existing database indexes**.
  - Avoid using [SQL reserved words](https://dev.mysql.com/doc/refman/5.7/en/keywords.html) for table names or aliases.
  - **Access Control**:
    - Non-admins cannot access new views by default; **explicit ACLs** must be created.
- **Additional Notes**:
  - Database views are resource-intensive—always consult your team or architect before creating one.

### Default vs. Calculated Fields

- **Default Fields**:
  - Apply default values when a form loads or when a record is inserted **only if the field is blank**.
  - Default values can be static or scripted using `javascript:`.
    - example: `javascript:'Record created by ' + gs.getUser().getDisplayName() + ' on ' + current.getValue('sys_created_on')+'.';`
  - Default value is **not re-evaluated** after the initial insertion.
  - On form load, the default script may not have full `current` object data.
  - To restrict default execution only at insert, check if `current.sys_created_on.nil()`.
    - example: `javascript:if (!current.sys_created_on.nil()) { ... }`
- **Calculated Fields**:
  - Always scripted and **re-evaluated on every record update and read**.
  - Useful for dynamic values that must reflect the current state of the record.
  - Impact on performance: every read operation recalculates the field—even when the field is not displayed.
  - Prefer **Insert/Update Business Rules** over calculated fields if recalculation is not strictly necessary.
- **Key Differences**:
  - **Default** = static or first-time-only value (insert time or form load).
  - **Calculated** = dynamic value updated every time the record is read or modified.
- **Performance Tip**:
  - Only use calculated fields when necessary; otherwise, use Business Rules for better scalability.

## List and Form Design

### Form Layouts

- **General Structure**:
  - Forms should be organized into logical sections to improve usability and clarity:
    1. **Top Section**: Two-column layout with critical "at-a-glance" details (e.g., Number, Priority, Assigned to).
    2. **Middle Section**: Additional data fields and optional form sections (grouped logically to avoid excessive tab flipping).
    3. **Bottom Section**: Long text fields, journal inputs, and activity formatters before related lists.
- **Best Practices**:
  - Keep journal inputs directly above journal lists to avoid confusion.
  - Maintain rough **symmetry** between columns for visual balance (real-world use takes precedence over Form Designer appearance).
  - **Do not duplicate** fields within the same form view.
  - For modifications on **admin-only forms** (e.g., ACLs), be cautious about whether changes are captured in an Update Set.
- **UX Considerations**:
  - Avoid putting frequently updated or long fields in the middle of the form.
  - Design forms to minimize unnecessary scrolling, especially for users without the tabbed interface enabled.

### List Layouts

- **General Structure**:
  - Always configure the **default list view** when creating a new table.
  - Prioritize fields that users need to see at a glance:
    - Start with a **unique identifying field** (not `sys_id`, e.g., Number).
    - Follow with important context fields (e.g., Assigned to).
    - Date fields are often positioned toward the **right** of the list.
- **Best Practices**:
  - Avoid clutter: limit the number of fields to those essential for quick reference.
  - Exclude large, non-wrapped text fields unless they add meaningful list-view value.
  - Keep the layout clean to fit within a reasonably sized browser window.
- **Pro-tip**:
  - To make a String field appear as a **multi-line input** on forms, set its Max Length to **256 characters or more**.

## OOB Records

### General Guidelines

- **Do not modify OOB records** directly if avoidable.
  - Prefer adding conditions to **disable** unwanted behavior without altering the script.
  - Use **Insert and Stay** to duplicate and customize functionality separately.
  - Minimizes upgrade issues and makes reviewing skipped updates easier.
- **Why it matters**:
  - Modified OOB records complicate upgrades and can trigger unpredictable cascading bugs.
  - Skipped updates during upgrades require manual intervention if OOB scripts were changed.
- **Deprecated practice**:
  - Deactivating OOB records and cloning them with changes is generally discouraged due to hidden dependencies.
- **Best Practices**:
  - Review system warnings and error logs regularly after changes.
  - Catch and log predictable errors proactively for easier debugging.

### Extending OOB Script Includes

- **Extending is preferred** over modifying:
  - Create a new Script Include extending the original via `Object.extendsObject()`.
  - Override or add new methods/properties as needed.
  - Inherits functionality without breaking or modifying the original OOB logic.
- **Example Figures**:
  - [Fig. 6.01 - ExampleScriptInclude.js](https://github.com/thisnameissoclever/sn_dev_handbook_3/blob/a31e35c9f09a61dd021bf4883159307222b00f58/Chapter%2006%20-%20OOB%20Records/Fig%206.01.js)
  - [Fig. 6.02 - ExampleExtendedScript.js](https://github.com/thisnameissoclever/sn_dev_handbook_3/blob/a31e35c9f09a61dd021bf4883159307222b00f58/Chapter%2006%20-%20OOB%20Records/Fig%206.02.js)
