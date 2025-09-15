Scripting in ServiceNow - Course Notes

Revisit your instructions on how to format course notes. Deeply analyze the following content to provide  concise and helpful reference notes

Content:

## Scripting Overview
- Objectives
Answer the five W's (and one H) of Scripting
- What is Platform scripting?
- Why should you not script?
- When should you script?
- Where do scripts execute?
- Who can script?
- How do you script in ServiceNow?
Introduce Application Scope
Review ServiceNow APIs
Explore where to get Scripting help

What, why, when, where, who, and how?
What is platform scripting?
When making changes to your instance, use the Condition Builder whenever possible to configure simple conditions and actions.
However, use Platform Scripting for complex configurations and behaviors via JavaScript.
ServiceNow provides the ability to customize an instance using JavaScript (based on Mozilla Rhino).
JavaScript, popularized by Yahoo, is the most prevalent scripting language on the web. It is object-oriented, runs within a browser and does not need a license.
Rhino is an open-source implementation of JavaScript written entirely in Java. It is typically embedded into Java applications to provide scripting to end users.
The JavaScript engine in ServiceNow supports the ECMAScript5 and ECMAScript 2021 standards.

Why should you not script?
• ServiceNow is continually evolving; what you scripted in the past might not need to be scripted now.
• Easier to debug and fix configuration changes after an upgrade.
• Make sure a script is really needed
- How business-critical is the requirement?
- Will an Access Control List (ACL) rule perform what you need instead?
- Can you achieve at least 80% of your requirements via configuration changes instead of scripting?
• Consider ways of customizing without scripting
Remain current with ongoing development of ServiceNow:
• Check Product and Developer documentation of ServiceNow before developing anything new.
• Stay current on what has changed from release to release.
• Check the most recent version's release notes.
• Attend release meetings.

When should you script?
When to Script
Add new functionality
Extend existing functionality
Guide users through messaging
Automate processes
Interact with third-party applications
Examples of when you should script:
• Update related record (s) .
- Cascade a comment from a master incident to its children.
- Update the ownership of a Configuration Item (CI) after a Change Request.
• Approval Strategies
- One or all does not meet your business requirement.
- Approvers need to be set dynamically.
• Show/hide a form section.
• Scan a list of Cis to dynamically determine risk based on criticality.
• Query a database.
• Customize widgets.
• Change default behaviors.
The list of examples shown above is representative of typical uses for scripting. There are, of course, no limits as to what one can do with JavaScript in ServiceNow. It all comes down to your requirements!
Tip from the Field
ServiceNow is always enhancing the platform. For example, the Embedded Help has been updated and a new feature called Guided Tours has been added. Research these options before you script a solution to guide users. If you have already scripted a solution, revisit your code and see if new baseline options can replace the script.

Customization best practices
ServiceNow is always trying to make the upgrade process easier. Adopting this process helps with future upgrades to your instance.
Identify the record that needs updating
Determine whether a no-code (meets > 80% reqs.) -> Yes -> Implement the no-code or low-code approach
No
Determine whether a low-code approach would work  -> Yes -> Implement the no-code or low-code approach
No
Modify the baseline record
Review and revert the skipped record after an upgrade
If you are interested in learning more about customization best practices, go to the Now Community and search for "customization best practices - a resource" and/or download this pdf (https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/customization-best-practices.pdf).

Where do scripts execute?
Client side (browser)
• Auto-populate a field based on the value of another field
• Show/hide form sections
Server side
• Modify a database record
• Trigger a Flow
On a MID server
• Integrate to a third-party application
Where a script executes matters:
• Performance considerations
• Access to objects and methods:
- Client-side scripts have access to data on forms and in lists.
- Server-side scripts have access to database records.

Who can script?
System Administrator: Manages all the features, applications and data in the platform
System Definition Administrator: Manages a specific System Definition (for example, can only manage Business Rules)
Application Administrator: Manages all the features and data of an application
Baseline, the admin role has access to all platform features, functions, and data, regardless of security constraints. Grant this privilege carefully! If you have sensitive information, such as private HR records, ServiceNow recommends granting a custom admin role to an administrator who maintains that application.
More granular administrative roles, such as business_rule_admin, client.
_script_admin,
script include_admin and ui _policy_admin, grant specific access rights without granting the broader privileges of the admin role. For example, an administrator can grant a user rights to change Ul Policies, but not the rights to edit Client Scripts.
Important: Specific admin roles do not change the access level and behavior of the admin role, which grants general administrative privileges across the platform.


How do you script in ServiceNow?
The Syntax Editor is the built-in text editor of ServiceNow.
• Allows you to write scripts in ECMAScript 2021 (ES12) mode.
• Offers the following features as you script
- Automatic Javascript syntax coloring, auto-indentation, line numbers and creation of closing braces and quotes
- Context-sensitive help
- Code editing functions
- Editor macros for typing commonly used code
- Syntax error checking
- Minimap
The Syntax Editor is enabled baseline for new instances. For upgraded instances, a System Administrator must activate the Syntax Editor [com.glide.syntax_editor] plugin.

Locate Scripts: navigate directly to table configurations
• Use commands in the Application Navigator's Filter Navigator field to navigate directly to table elements.
• Append .config after the table name to display all the configuration changes made to that table (for example, incident.config).

Application scope
• Every application has a scope.
• Determines which of its resources are available to other applications.
• Once scope is assigned to an application, it cannot be changed.
Baseline applications provided by ServiceNow (for example, Incident, Service Catalog, Service Portal, etc.), as well as any custom application created before application scope was implemented are also in the global scope. It is difficult to protect/isolate application data in the Global scope.
There is no migration path to a custom or different scope.
Tip from the Field
Select the
update sets using drop-down menus.
icon on the Header bar so that you can switch between application scopes and
• Scope protects an application and its artifacts from damage to or from other applications
• Must be configured to grant other applications the ability to act on its records
Explicit permission must be granted for applications to share their resources with other applications
Artifacts are the application files in an application. Examples include, but are not limited to, Tables, Access Controls, Email Notifications, Data Policies, Client Scripts, Business Rules, Script Includes, etc.
Application developers specify an application scope when they create a new application. They can also specify what parts of an application are accessible to other applications from:
• The Custom application record.
• Each application Table record.
For example, suppose you create a Travel & Expense Management application. By default, the application can access and change its own tables and business logic, but other applications in the platform cannot unless you grant them explicit permission to do so.
Application scope ensures:
• The application does not interrupt core business services.
• Other applications do not interfere with its normal functioning.

Application scope: updating scripts in another scope
Out-of-scope scripts are read-only.
Built-in limitations prevent developers from updating artifacts while in a different scope. This protects the application from inadvertent modifications.

Application scope: scope namespace identifier
• The system automatically prefixes a namespace identifier to scoped application artifacts (including scripts).
• Cannot be changed or removed to ensure they are always associated with the proper application.
Syntax          Description                                           Cloud Dimensions Example
                scoped application artifacts always begin with x_     x_
Vendor Prefix   Unique ServiceNow generated prefix for each customer  cld
Application ID  Set when the application is first created             travel
Script name     Unique script name                                    ExpensesReqBy
This example generates the namespace identifier:
x_cld_travel_ExpensesReqBy
The application scope prevents naming conflicts and allows the contextual development environment to determine what changes, if any, are permitted. Applications in the Global scope do not append a unique namespace identifier to the application name.

JavaScript in ServiceNow
JavaScript in ServiceNow: JavaScript APls
Provide classes and methods that can be used in scripts to define the functionality of the platform
Client-side Classes
GlideAjax
GlideForm
GlideList
GlideRecord
GlideUser
spModal
Server-side Classes
GlideAggregate
GlideDateTime
GlideElement
GlideRecord
Glide Query
GlideSystem
JSON
Workflow
Classes are grouped by those used for client-side scripts, REST APls, global server scripts, and scoped server scripts.
More classes are available for use in scripts and new ones are constantly being developed. It is important to stay current on what has changed from release to release.
• Visit the official Developer site of ServiceNow to see the list of available API classes and methods, definitions on what they do, instructions on how to use them, as well as sample scripts written by ServiceNow developers.
• Visit the official Documentation site of ServiceNow to review API release notes.

JavaScript in ServiceNow: API documentation
The APls section of the developer site (developer.servicenow.com) is the place to go for official API documentation.
Server Scoped: support for scoped applications. These APls may behave differently in the Global scope
Server Global: support for legacy applications in the Global scope
API Documentation is presented as Server Scoped or Server Global. Understand what scope you are using, because you cannot call a global Glide APl in a scoped application.
Another thing you want to consider is the version of your instance. Make sure the documentation you are looking at is for the version of your instance.
In the API documentation, there are links to REST, Server Scoped, Server Global, Now Experience Ul Framework, Client and Client Mobile APls.
From the drop-down list, you can select one of the following APl Type options. By default, the link you clicked in the Apis menu is the selected AP Type.
Client
Client Mobile
REST
Server Scoped
Server Global

JavaScript in ServiceNow: JavaScript mode - scoped apps
To support existing scripts and new scripts developed to the ECMAScript 2021 standard, the Javascript engine has three modes:
• Compatibility Mode.
• ES5 Standards Mode.
• ECMAScript 2021 (ES12).
ECMAScript 2021 (ES12) mode is an option that allows server-side scripts for scoped applications and the global scope to use the ECMAScript 2021 (ES12) standard. This mode does not preserve the legacy behaviors in the pre-Tokyo JavaScript engine. This mode supports a subset of ECMAScript syntax and features such as:
• let declaration
• Default function parameters
• For-of loops
• const declaration
• Additional ECMAScript 2021 (Es12) syntax and features can be found at docs.servicenow.com.
ES5 Standards Mode is the default mode when creating new scoped scripts. It supports ECMAScript5 syntax, extensions and features including:
• The 'use strict' declaration.
• Control over extensibility of objects.
• Get and set properties on objects.
• Control overwrite-ability, configurability, and innumerability of object properties.
• New Array and Date methods.
• Native JSON support.
Compatibility mode is used for all scripts developed prior to the Helsinki release and all global scripts.
Compatibility mode has some differences from the old Javascript engine.
JSON support changes:
• JSON.stringify() and JSON.parse() are now implemented using the ES5 Native JSON object.
• The new JSON().encode () and JSON().decode () are still supported but should only be used when the legacy behavior is required.
• The use of third-party JavaScript libraries is not supported in Compatibility mode.

JavaScript in ServiceNow: JavaScript mode - global scope
Turned on: when creating server-side scripts you have the option to take advantage of ECMAscript
2021 syntax and features or use the other modes.
Turned on - var and const both work
Turned off: using ECMAScript 2021 syntax or features causes errors.
Turned off - var works, const doesn't

Scripting resources
Scripting resources: where to get help
JavaScript Resources
W3schools https://www.w3schools.com/js/default.asp
codecademy https://www.codecademy.com/search?query=javascript
Pluralsight https://www.pluralsight.com/browse?=&q=javascript
mozilla https://developer.mozilla.org/en-US/JavaScript
stackoverflow https://stackoverflow.com/questions/tagged/javascript

Scripting overview
Good Practices
• Use a Condition Builder whenever possible to configure your instance.
• Create a Syntax Editor Macro to quickly insert commonly used syntax.
• Expand the Script Editor when editing large scripts.
• Identify the Scope of your script to ensure it only affects the resources in the same scope.
• Use the Now Community and ServiceNow websites.
• Join at least one SNUG.
Make good use of the Now Community; ServiceNow websites are more than just product documentation!

Module recap: scripting overview
Core Concept #1
Scripts can create new or extend the existing functionality of ServiceNow
Core Concept #2
The answer is not always to create a new script
Core Concept #3
Scripts execute in different locations:
Client-side - Server-side - On a MID server
Core Concept #4
The built-in Syntax Editor offers industry standard scripting capabilities
Real-World Cases
Why would you use these capabilities?
When would you use these capabilities?
How often would you use these capabilities?
Other Core Concepts:
• Debug with the Syntax Checker
• Globally scoped scripts are shared resources
• Privately scoped scripts only affect resources in the same scope
• Know where to get scripting help
Discuss: Why, when, and how often would you use the capabilities shown in this module.




## Client Scripts
[content will follow]




## Ul Policies 
[content will follow]





## Business Rules
[content will follow]





## GlideSystem
[content will follow]





## GlideRecord
[content will follow]





## Script Includes
[content will follow]





## Flow Designer Scripting
[content will follow]