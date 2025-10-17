next section: ## Client Scripts - remember to aim for condensed reference notes and not a recap of structure or content:

Client Scripts
Client Script Overview: What is a Client Script?
• Client Scripts manage the behavior of forms, fields, and lists in real time
- Make fields mandatory
- Set one field in response to another
- Modify choice list options
- Hide/Show form sections
- Display an alert
- Hide fields
- Prohibit list editing
• Client Scripts execute client-side (web browser)
- Browsers may present items in different ways
"Well-designed Client Scripts can reduce the amount of time it takes users to complete a form."
- Plato, c. 427-348 BC
Although modern browsers largely interpret JavaScript the same way, you may still observe browser-dependent behaviors in client-side scripts.
FAQ's
?
What exists Baseline?
x Hide
• More than 1,600 Client Scripts exist baseline.
• Not all Client Scripts are Active baseline
• Sample Client Scripts can be used as starting points.
• Sock monkeys can be Production Assistants at radio stations
?
Where can this be found?
* Hide
Navigate to the System Definition > Client Scripts module to create or modify Client
Scripts.


Client Script Overview: Client Script Execution
Trigger specifies when to execute
Script specifies what to execute
All scripts have a trigger specitying when a script's logic should execute. The trigger configuration fields depend on the script type.
• The Description field is for documenting the script. Include information like who wrote the script, what business requirement the script is for and any other pertinent information.
• The Messages field is used for internationalizing output to the user. For example, if the script creates an alert that says Hello World, the string "Hello World" would appear in the Messages field on its own line. If an entry exists in the sys_ui_message table with the same key but a localized language, the localized language version is presented to the user even though the script uses the version from the Messages field.
• The Script field is used to script what needs to happen when the conditions in the trigger are met.


Client Script Overview: Client Script Trigger
Client Scripts execute when their trigger condition is met
Additional info is required if the Client Script is triggered by a field value change...
or if it applies to a specific view of the form
While on the Client Scripts list, select New to create a new Client Script.
• Name - name of the Client Script. Use a standard naming scheme to identify custom scripts.
• Table - table the form or list is related to.
• Ul Type - select whether the script executes for Desktop only, Mobile/Service Portal only or All environments.
• Type - select when the script runs: onChange, onLoad, onsubmit, or onCellEdit.
• Field name - used only if the script responds to a field value change (onChange or onCellEdit); name of the field to which the script applies.
Application - identifies the scope of the Client Script.
• Active - if selected the script executes in the runtime environment.
• Inherited - execute the script for forms from any extending tables when selected.
• Global - if Global is selected the script applies to all Views. If the Global field is not selected, you must specify the View.
View - specifies the View to which the script applies. The View field is only visible when Global is not selected. A script can only act on the fields part of the selected form View. If the View field is blank the script applies to the Default view.


Client Script Overview: Client Script Trigger - Order
• Use the Order field when multiple Client Scripts for the same table have conflicting logic
• Executes in order from lowest to highest
• Does not appear on the Client Script form baseline
- Configure the form to add the field
Order is the sequence in which the Client Scripts are executed, from lowest to highest. By convention, Order numbers contain three digits. For example: 100, 200, 300, etc..



Client Script Overview: Client Script Type -
onLoad()
• Script runs when a form loads and before control is given to the user
• Typically used to manipulate a form's appearance or content on the screen
Users do not have the ability to modify form fields while an onLoad() Client Script executes.
Select onLoad as Client Script Type
the onLoad() function template Is automatically inserted into the Script (with no arguments passed to it)
For example, a baseline onLoad() Client Script on the Change form marks Standard Change fields as read-only before control is given to the user. Usually, onLoad() Client Scripts perform client-side-manipulation of the current form or set default record values.


Client Script Overview: Client Script Type -
onSubmit()
• Script runs when a form is saved, updated, or submitted
• Typically used for field validation
Users do not have the ability to modify form fields while an onSubmit () Client Script executes.
Note: onLoad client scripts only run if the page is reloaded after a Save. If the user does a Submit or Update, they would be taken to the previous location in the instance, the current page would not reload, and the onLoad script (s) would not execute.
The onSubmit () function template is automatically inserted into the Script (with no arguments passed to it)
Tip from the Field: Typically, onSubmit() Client Scripts validate data on the form and ensure the submission makes sense. If the inputs the user submits do not make sense, an onSubmit() Client Script can cancel form submission by returning a value of false.


Client Script Overview: Client Script Type -
onChange()
• Script runs when a particular field value changes
• Typically used to
- Respond to field values of interest
- Modify one field value in response to another
An onChange() Client Script watches one field. If two fields need to be watched, a second Client Script must be configured.
For example, one onChange() Client Script populates the 'Assignment group' field if the value in the Configuration item [cmdb_ci] field changes, while a second onChange(/ Client Script populates the Watch List if the value of the Priority field changes to 1.
Select onChange as Client Script Type
Select the field to watch for changes
The onChange() function template is automatically inserted into the Script (with 5 arguments passed to it)
An onChange() Client Script runs when a particular field value changes on the form.
The onChange() Client Script must specify these parameters:
• control - name of the object (field_name) whose value just changed. The object is identified in the Field name field on the Client Script form.
• oldValue - value of the control field when the form loaded and prior to the change. For example, if the value of Assigned to changes from Matt to Miranda the value of the parameter oldValue is Matt. oldValue will always be Matt (the value when the form loaded) no matter how many times the Assigned to value changes after the original form load.
• newValue - value of the control field after the change. For example, if the value of Assigned to changes from Matt to Miranda, the value of the parameter newValue is Miranda.
• isLoading - boolean value indicating whether the change is occurring as part of a form load.
Value is true if change is due to a form load. A form load means all the form's fields changed.
• isTemplate - boolean value indicating whether the change occurred due to population of the field by a template. Value is true if change is due to population from a template.


Client Script Overview: Client Script Type - onChange() Template 'if' Statement
ALL field values change when a form loads
if statement aborts script execution if field values change due to a form load or newValue has no value
Modify the script to change the behavior if necessary. For example, you might also check to see if the field value change was due to a template load.
function onchange (control, oldValue, newValue, isLoading, isTemplate) {
if (isLoading || newValue === '' || isTemplate) {
return;
}
//Type appropriate comment here, and begin script below
}



Client Script Overview: Client Script Type - onCellEdit()
Applies to all records selected
Script runs when a particular field on a list changes value
If you create a client-side script for fields on a form, an onCellEdit () Client Script can be used to ensure data in those fields is similarly controlled in a list.
Important: onCellEdit() scripts do not apply to List Widgets on homepages or dashboards.
Select onCellEdit as Client Script Type
Select the field to watch for changes
onCellEdit () function template automatically inserted in the Script (with 5 arguments passed to it)
Parameters automatically passed to an onCellEdit() Client Script:
• sysIDs - sys id of the edited item (s).
• table - the table name of the edited items).
• oldValues - the old value of the edited cells).
• newValue - the new value of the edited cells). Is the same for all edited items.
• callback - a callback continues the execution of other related cell edit scripts.
You must pass back either true or false in the callback function. If true is passed as a parameter, the other scripts are executed, or the change is committed if there are no more scripts. If false is passed as a parameter, any turther scripts are not executed, and the change is not committed.
Example:
function onCellEdit(sysIDs, table, oldvalues, newvalue, callback) {
var saveAndClose = true;
if(newValue == 6) {//Resolved
alert ('You cannot change the state to 'Resolved' from a list");
saveAndClose = false;
}
if (newValue == 7) {|/Closed
alert("You cannot change the state to 'Closed' from a list.");
saveAndClose = false;
}
callback (saveAndClose);
}


Catalog Client Script Overview
Trigger: When to execUTe
Script: What to execute
Name: Unique name for the Catalog Client Script.
• Applies to: Select the item type this Catalog Client Script applies to (A Catalog Item or A
Variable Set).
• Active: Select the check box to enable the Catalog Client Script. Clear the check box to disable the script.
• Ul Type: Identify where the Catalog Client Script executes (Desktop, Mobile/Service Portal, or All).
• Application: Identify the scope of the Catalog Client Script.
• Type: Identify when the Catalog Client Script executes (onChange, onLoad, or onsubmit).
• Catalog item or Variable set: Select a Catalog Item or Variable Set from the list.
• Variable name: Identify which field to watch for changes when onChange is selected as the Type.
• Applies on a Catalog Item view: Select the check box to apply the Catalog Client Script to Catalog Items displayed within the order screen on the Service Catalog. Available in the Requester view.
• Applies on Requested Items: Select the check box to apply the Catalog Client Script on a Requested Item form, after the item is requested. Available in the Fulfiller view.
• Applies on Catalog Tasks: Select the check box to apply the Catalog Client Script when a
Catalog Task form for the item is being displayed. Available in the Fulfiller view.
• Applies on the Target Record: Select the check box to support the Catalog Ul Policy on a record created for task-extended tables via Record Producers.
• Script: Script what needs to happen when the conditions in the trigger are met.



Client-side APIs
Client-side APIs: What Data Can You See in a Client
Script?
• Use predefined client-side classes and methods from ServiceNow to
Control how the platform looks and behaves in a web browser
- Enhance the end user experience
• This class reviews the most popular Client-side APIs
- g_form (GlideForm)
- g_user (GlideUser)
g_scratchpad (used with a Display Business Rule, Module 4)
ServiceNow provides client-side Javascript APIs:
•g_form - object whose properties are methods used to manage form and its fields in the record.
• g_user - object whose properties contain session information about the currently logged in user and their role (s).
• g_scratchpad - object passed to a Client Script from a server-side script known as a Display Business Rule. The object's properties and values are determined by the server-side script.
In addition to these predefined global variables, you also have any local variables you declare in a script. Visit developer.servicenow.com for the complete list of available client-side classes and methods.


Client-side APIs: g_form Object
The GlideForm API provides useful methods to
- Customize forms
- Manage form fields and their data
Object properties are the fields from the currently loaded record.
Object values are the field values when the record is initially loaded.


Client-side APIs: g_form Methods
• Access GlideForm methods using the g_form global object
9_form.<method
_name › (parameter information);‹
Syntax
• Examples
9_form. setValue ('impact', 1);
9_form.showFieldMsg|'state', 'Change is waiting approval' , 'info');
May also pass 'warning' or 'error' as an argument
• Commonly used g_form method examples
- Draw attention to an area on the form: flash (), showFieldMsg()
- Get field information: getValue()
- Change a field value: setValue), clearValue ()
- Change a choice list: addOption(), clearOptions)
- Get form information: getSections), isNewRecord()
GlideForm methods are only used client-side.
Examples:
g_form.addinfoMessage() - displays an informational message at the top of a form g_form.addOption() - adds an option to the end of a Choice list g_form.clearMessages() - removes messages previously added to the form g_form.clearOptions() - removes all options from a Choice list g_form.clearValue() - clears a field's value
g_form.flash() - flashes a field's label to draw attention to it g_form.getSections() - returns the elements of a form's section as an array
g_form.getValue () - retrieves a field's value
g_form.isNewRecord() - returns true if a record has never been saved
g_form.setValue() - sets a field's value
g_form.showFieldMsg() - displays a message under a form field




Client-side APls: Referencing Field Names
• 9_form object methods refer to fields by their field name, not their label
• Easy way to locate a field name
- Right-click a field's label
- The field name appears on the Context menu
For example, the first parameter required by the addDecoration() method is a field name.
9_form. addDecoration('String field_name'‚'String icon'‚'String title');
Provide the field name caller_id vs. the field label Caller.
9_form. addDecoration('caller_id', 'icon-star' ,'preferred member');
Tip from the Field: Show - 'field_name' option on the Context menu works great to display the name of a field. A pop-up with a few of the field's properties are displayed. Copy the field name for your script. Additional properties include Table, Type, Max Length, and Attributes.


Client-side APls: g_form Method Syntax
• Method use documented on the Developers portal
• Two ways to search for methods
1. Use the Search field to search for a specific string
2. Manually locate the method of interest on the page
To locate a g_form method manually:
1. Select API > Client.
2. Expand the GlideForm class.
3. Locate and select the method of interest.
• The method's syntax is documented in the middle-column of the page. Most methods have their parameters and return value documented.
• If an example is included, it is located to the right of the method's documentation.


Client-side APls: g_form.getValue ()
• g_form.getValue() is a very commonly used g_form method
• Retrieves a field value from the form (not the database)
• Pay close attention to the tield's data type when using this method
var ‹varName› = 9_form.getValue('<field_name›') ; Syntax
var incPriority = g_form.getValue ('priority'); Example
Since JavaScript is weakly typed, it is not always necessary to verify the data type when scripting. In the case of the g_form.getValue() method however, you must pay attention to the data type, or your script may have unexpected results.
The g_form.getValue() method always returns a string despite the data type of the field. If returning a number is important, use the g_form.getlntValue() or g_form.getDecimalValue() methods instead.
Important: This method cannot retrieve values from the database, it retrieves values from forms even if the field is not visible in the current view or to the logged in user.


Client-side APls: g_form.getValue() - Text Field
g_form.getValue('number')
- Returns the field's content exactly as it appears on the form
- The Number [number] field is a string (text) field
g_form.getValue('number') returns INC8675309
Right-click a field's label and select Show - '<field_name>' from the Context menu to confirm a field's
data type.


Client-side APIs: g_form.getValue() - Choice List
g_form.getValue ('impact)
- Returns the value of the selection, not the user-friendly label
- The Impact impact] field is a choice list
g_form.getValue('impact') returns 1
To see a choice list's values, right-click the field's label and select Show Choice List.


Client-side APls: g_form.getValue() - Reference
Field
g_form.getValue|'caller_id')
- Returns the sys_id of the referenced record
- The Caller [caller_id] field is a reference field
g_form.getValue(caller_id') returns 5493fd1787f3b0107703a6483cbb35a0
A sys_id is the database's unique key for a record.
Tip from the Field: The examples shown have used the GlideModal() method in a Client Script to show the value of a single field. You can see several field values at once without a Client Script. If you have the 'admin' role, select Show XML on the form's Context menu. This displays the record's data in XML format.
Right-click on the Caller label and select Show - 'caller_id' to see its data type (reference, in this example) and its reference (to sys_user).



Client-side APls: g_user Object
• The GlideUser API provides useful methods to access information about the currently logged in
User
• Access GlideUser methods using the g_user global object
For the form shown, the g_user object contains the following properties and values for Asaak Monkey:
9_user = fuserName: "asaak. monkey",
userID: "46d44a23a9fe19810012d100cca80666"
firstName: "Asaak", lastName: "Monkey"
}
Script used for the alert shown:
function onSubmit () {
if (9_form. isNewRecord ()) {
alert "Thank you for submitting this Incident, " +
g_user. firstName);
}


Client-side APls: g_user Object Properties and
Methods
g_User Properties:
• firstName
• lastName
userID
• username
g_user Methods:
• getClientData()
• getFulName ()
• hasRole()
• hasRoleExactly)
• hasRoleFromList ()
• hasRoles()
Syntax: g_user.<property>
Example:
alert "Logged in user: " + g_user.userName);
Syntax: g_user.<method_name>(parameter information);
Example:
if (g_user.hasRole ('itil'{
alert"Logged in user is a Fulfiller");
}
• getClientData() - returns the session client value previously set with the putClientData() method
• getFullName() - returns the logged in user's first name and last name separated by a space
• hasRole() - returns true if the logged in user has the specified role or has the admin role
• hasRoleExactly) - returns true only if the logged in user has the specified role
• hasRoleFromList) - returns true if the logged in user has at least one role from the passed in list or has the admin role
• hasRoles) - returns true if the logged in user has any role
Important: Do not rely on g_user methods to apply security. Client-side security is easily defeated using developer tools built into browsers. Access Control or another server-side security strategy is recommended.



Client-side Debugging: Debugging Client Scripts -
Desktop
• Many times, your scripts do not work as expected
• You can debug them using the following strategies:
- ServiceNow built-in client-side debugging tools
• Script debug messages
• Response Time Indicator
- JavaScript debugging tools
• alert ()
• try/catch
- Browser tools (for example, JavaScript console, Web Console)
- Third-party tools
In some cases, more than one debugging strategy may need to be used. The built-in and Javascript debugging tools will be reviewed.


Client-side Debugging: Script Debug Messages
Include addinfoMessage() and addErrorMessage() methods in your script
Pros:
• Convenient strategy as messages appear on the form being tested
• Write any debugging information you want since messages are not restricted to field
values
Cons:
• Statements must be removed before moving scripts to other instances
• Other users see the message(s)
The showFieldMsg) method can also be used to display debugging output next to a specific field.
All users are affected when the addinfoMessage), addErrorMessage), and show FieldMsg() methods are used as everyone sees the output on the form. In a multiple administrator/developer environment, this approach has the potential to be confusing. Consider including code in your debugging scripts to include your name in the output or to hide the output from other users.
• Include a g_user property in the script to identify yourself in the message. Example:
9_form. addInfoMessage (g_user firstName + ", the value of caller_id is: " +
9_form.getValue('caller_id'));
• Include a g_user property in combination with an IF statement to display the message only to you. Example:
if (g_user.userName == 'admin'){
9_form. addInfoMessage("The value of caller_id is: " +
9_form.getValuel'caller_id'));
}
Tip from the Field: Create a Debug Syntax Editor Macro to quickly insert commonly used debugging code.


Client-side Debugging: Response Time Indicator
• Useful for locating the cause of slow page loads
• Times are in milliseconds
- Network
- Server
Browser
Select the clock icon link to see a detailed breakdown of the browser processing times on forms
Use this strategy to look for Client Script issues causing long load times. Administrators can disable the Response Time Indicator by setting the glide.ui.response_time property to false.


Client-side Debugging: JavaScript Debugging
Tool-Try/Catch
Javascript debugging strategy used to trap runtime errors
Try/Catch syntax:
try{
/code to execute goes here
}
catch (err){
//code to deal with error here
}
err is a Javascript object with properties description, message, name, and number.
You can throw your own error messages for the catch function using the JavaScript throw0 function.
Try/catch only traps runtime errors. Using throw|) you can also catch user errors such as entering an invalid data value in a field.


Reference Objects
• Reference Object records exist on a table other than a form's currently loaded table
• Reference Object data is not loaded into forms
• Client-side scripts only have access to data on forms
"Since Accounts Payable printer issues rarely occur, I always have to look up the correct Assignment group. It would be great if the
'Assigned to' field would automatically populate when I select the CI."
When writing client-side scripts, you have access to all form fields and their values. Reference Object fields exist on forms, but the Reference Object record itself is not loaded into the form.


Reference Objects: Scripting with Reference
Objects
• Forms only store a Reference Object's sys_id
• Reference Object fields cannot be directly referenced from a Client Script
Retrieving Reference Object fields requires a trip to the server and back
- Server trips take time
- Make as few trips as possible!
A reference field stores a sys_id for the record it references in the database, but the sys_id is not shown. The reference field shows the record's display value on the form.


Script Versions
• Track changes to the record
• Created automatically every time a script is saved, submitted or updated
• Can compare versions to see differences
• Can revert to a previous version of a script
Located at the bottom of the form:
Script versions are available for other script types and are not unique to Client Scripts.
Update Sets do not include every version. If you migrate a script from one instance to another, only the most recent version of the script is included in an Update Set.


Script Versions: Two Ways to Compare Script
Versions
Compare to the current version:
1. Right-click the version record and select Compare to Current on the Context menu
Compare any two versions: 
1. Select checkboxes beside two versions
2. Select Compare on the Actions on selected rows...menu
The Versions Related List is visible baseline.
In the event it is not, open the record's Context menu and select Configure > Form Layout. Add Versions to the Selected column and save the change.