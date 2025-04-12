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