better
next: App Creation

```
Application development tools overview
Module 3.1
First, we will briefly explore various ServiceNow application development tools.



ServiceNow application developer tools
This course focuses on the entire application development lifecycle. ServiceNow offers various application development tools, depending on the complexity of the app and experience of the developer.
ServiceNow Studio is an integrated development tool for application developers to work on custom applications in one centralized location.
ServiceNow Studio offers a simple way to create, review, and update application files from a tabbed environment. The system opens ServiceNow Studio whenever you edit a custom application.
App Engine Studio (AES) is a guided low-code tool for application development.
(App Engine Studio requires an App Engine subscription or product packaged with one.)
In this class, we provide hands-on practice using ServiceNow Studio.
The fundamentals learned in this course will serve you well, whether you continue with traditional development approaches or make use of the more citizen developer-oriented tools.
For more information about your options for developing applications in ServiceNow, refer to this product document:
Build or modify applications in ServiceNow: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/custom-application/concept/developing-applications.html



Additional ServiceNow application development tools
Flow Designer
Enables process owners to automate work. Build multi-step flows from reusable components without having to code. Flow Designer enables process owners to use natural language to automate approvals, tasks, notifications, and record operations.
Integration Hub
Integration Hub is a Now Platform app for process automation and integrations. It enables you to build reusable integrations with third-party systems and call them from anywhere in the Now Platform.
Table Builder
Table Builder is a tool for creating, designing, and administering tables and forms in your application.
UI Builder
Ul Builder is a web user interface builder used to create or customize pages for workspace experiences.
Playbooks
Playbooks empower organizations to automate business processes. Playbooks leverage flows, adding a Ul layer to business logic. Agents and requesters can visualize and interact with a defined business process.
Creator Workflows
Creator Workflows allow you to build connected digital workflow apps fast with a low-code platform.
Check out the Developer Skills learning path on ServiceNow University, where you can learn about these development tools and much more!
Application Developer Skills learning path: https://learning.servicenow.com/lxp/en/app-engine/application-developer-skills?id=learning_path_prev&path_id=2a580f4447e96110ac2f89c2e36d4321



Create a custom application
Module 3.2
Next, we begin developing the Loaner Request application using ServiceNow Studio.
User story
As the Application Developer, I need a centralized development environment, so all the application files are organized and quickly accessible.


App creation process
Creating a custom application requires you define the application requirements.
Application configurations:
Name
Description
Scope
Define the application.
User roles:
Existing
Create new
When creating an application, ServiceNow Studio creates an Admin and User role by default. You may either use these or assign existing roles to the new application.
Tables:
Existing
Create new
- Create a table
- Extend a table
- Upload spreadsheet or PDF (specific licenses only)
Create one or more data tables by creating a table from scratch, extending an existing table, or uploading a spreadsheet or PDF.
Field inputs:
Continue defining the table with field inputs.
Table configurations:
Label
Auto-numbering
Manage access
Define the table.
Next steps:
ServiceNow Studio
Flow Designer
Set up another app
Once the application's basic content is created, the user can add additional application artifacts via ServiceNow Studio or Flow Designer, or the user can set up another application.
Note: The Scope value will appear as the prefix to the Name for many Application Artifacts. The Scope value is set automatically by ServiceNow. The Scope is constructed by concatenating:
x_+ <value from the glide.appcreator.company.code system property> + truncated Application Name. The glide.appcreator.company.code system property value is set by ServiceNow and is not user-changeable. It is typically 2-5 characters long. In class, the company code is calta.



ServiceNow Studio
Use ServiceNow Studio to build custom applications.
• Build, manage, and deploy applications all in one interface.
• Create and modify application files.
• Work in a tabbed environment.
To access ServiceNow Studio:
1. In the main ServiceNow window, navigate to App Engine > ServiceNow Studio.
To open an application for editing in ServiceNow Studio:
Option 1: In the main ServiceNow window, navigate to App Engine > ServiceNow Studio.
Select the application of interest.
Option 2: In the main ServiceNow window, navigate to System Applications > My Company Applications. Locate the application of interest, and select Edit in ServiceNow Studio.



ServiceNow Studio capabilities
In ServiceNow Studio, you can open and edit apps and app files in any scope, global or custom.
ServiceNow Studio has...
• Navigation and tabbed environment
• Cross-scope development environment
• Code search
• Quick creation of scripts and files
• Deployment capabilities through update sets or the internal application repository
• Global application files management
• Testing of the application (Opens Automated Test Framework in a ServiceNow Studio tab.)

ServiceNow Studio does NOT have, so...    So use this instead:
Ability to push to external source control    Update sets
Script Intellectual Property protection       Manage project access

Here's how I think about it. Generally speaking...
We BUILD the application in ServiceNow Studio.
We USE the application in ServiceNow.


Create a new custom application
Creating a new application in ServiceNow Studio is easy. Once you select Create, then select App. ServiceNow Studio guides you through the basic app setup.
Provide the name for the application you are creating, along with a description. Custom applications are typically scoped apps. If you wish, you can add an image to the app.
When a new application is created, ServiceNow Studio creates two roles by default: an Admin role and a User role. These roles can be deleted, and other roles can be added, as needed.



What's in a new application?
ServiceNow Studio provides the foundational elements of the new application. The app details include the app type, scope, date created, and sys_id.
Notice the application scope value is x_cdltd_loaner_r_0.
The system automatically truncated the name and appended a numeric value. If we had other scoped applications with the same truncated name, it would increment the numeric value.
A new application also contains:
• The two roles created by default: admin and user
• The Embedded Help Role Priority
As you can see, the application starts with just the basics. We will use ServiceNow Studio to develop additional app contents, such as adding a table, defining the type of user experience we wish to provide, setting up automation, and configuring app security.



3. Configure the app
Creating application files
Once the application record is created, it's time to build out more of the foundational elements, such as:
• Tables
• Access Controls
• Modules
• Forms
To create a new application file, select either one of the two Create buttons, then select File.
You will be presented with a pop-up window where you can select the file type you would like to create.



Designate data table options
As part of the Analysis and Design phases, a data model should have been documented. You may build a custom application that does not require any custom tables.
If you need custom tables to support your application, there are table creation methods available:
1. Extend a table: Create a custom table that copies an existing table and add additional fields to the child table.
2. Create a table: Create a custom table if there are no existing tables that match your needs or could be extended.
Note: If you create a custom table, review the Data table guidelines to ensure you are within the limits of your subscription and that your application performs as expected.
3. Upload a spreadsheet or PDF: Turn a spreadsheet or PDF into a custom table. (Note: This option is currently only available to customers with an App Engine Enterprise license.)
Follow these steps to:
Select an existing table without creating a custom table
1. In ServiceNow Studio, open the app file.
2. Select Create > File.
3. Search for and select Table Column, then select Continue.
4. Complete the remaining fields, then select Submit.
The result of these steps is that the existing table now has a scope-specific additional column.
Create a custom table by extending an existing table
1. Select Create > File > Table > Continue to create the app file.
2. In the Label field, enter the table name.
3. In the Extends table field, enter the name of the existing table to designate for your application.
4. On the list, select the table name.
5. Complete the remaining fields, then select Save (not Submit).
6. On the Columns tab, add additional fields as desired.
7. Select Update.
Create a custom table without selecting an existing table
1. Select Create > File > Table > Continue to create the app file.
2. In the Label field, enter the table name.
3. Leave the Extends table empty.
4. Complete the remaining fields, then select Submit.



Application tables
Deciding whether to base your application on an existing ServiceNow table or not is one of the most important decisions to make for an application.
If you extend an existing table, you inherit the functionality built into ServiceNow for the base table. If you start from a "blank slate" (brand new table), you have the opportunity to script and configure all behaviors of your application.
Applications can use multiple tables:
• Base table(s) that contains the primary application records.
• Reference/lookup tables.



What business logic exists for a table?
Use the Configure option to see the existing business logic for a table. Other business logic, such as Script includes, may also exist.
From any list view in ServiceNow or ServiceNow Studio:
1. Open the Column context menu (ellipses) and select the Configure option.
2. Select the All menu option.
From the filter navigator in ServiceNow or ServiceNow Studio:
1. Enter <table name>.config
2. View the options.



Default table fields
All new tables have a default set of fields.
Created by [sys_created_by], type = string: A string field automatically populated with the display
name of the user who inserted the record.
Created [sys_created_on], type = glide_date_time: A time-stamp field automatically populated by
the system at the moment of insert.
Sys_id [sys_id], type = GUID: The Unique Record Identifier for all records, automatically populated by
the system.
Updated [sys_updated_on], type = glide_date_time: A time-stamp field automatically populated by
the system every time the record is updated. Stores the most recent update date and time.
Updated by [sys_updated_by] type = string: A string field automatically populated with the display
name of the user who most recently updated the system.
Updates [sys_mod_count] type = numeric: A numeric field that counts the number of updates for this
record since record creation.

The six fields listed above are created by default when creating a table. If the extensible field is
selected, an additional field called Class is also created.
Class [sys_class_name] type = system class name:
If the table is extensible, a string field that indicates which child table contains the record.



Inherited table fields
Tables that extend a table inherit the parent's fields.
If the value in the table column is different than the table's Name, the field was inherited.
Note: The List Layout in the example shown is configured to display the Table column.



To extend or create new
A table exists with fields that are similar to what is needed: Extend
No similar table exists: Create New
Table will contain sample or seeded data that is used only for reference by the application: Create New
The scripts and workfiow for an existing table are useful for the application: Extend
You prefer to script the application behaviors yourself: Create New
You want to use the approval workflow activities: Extend
Tables must have the Extensible option selected in order to be extended. You can not extend a system or database view table.
The User Approval workflow activity works with all tables. All other Approval Activities work only with tables which extend Task.



Application access
Application Access provides runtime protection for application tables against read, write, create, and delete operations:
• Scripts
• Web service calls

Accessible: Select `This application scope only` to provide complete runtime protection. Select `All application scopes` to access all privately-scoped applications.
Caller Access: Caller access records are used to track cross-scope applications that request access to an application, application resource, or event. Options include: None, Caller Tracking, and Caller Restriction.
Can read/create/ update/delete: Select options to allow scripts from other application scopes to perform these database operations on the application's tables. These options never apply to the current application's scope.
Allow access to this table via web services: Allow scripts from other application scopes to make web services calls against the table. The user performing the query must have permissions to access the table.
Allow configuration: Allows application developers working from other application scopes to write scripts for this table.



Application menu and modules
The menu will be created once a table exists in the application scope. In this example, the module was created when the table was created.
The default module name is the plural of the table's name. You can change the name by editing the module configuration.
The default module always displays a list of all records from the table. There are no default records.
Important: Reload the ServiceNow browser window after adding application menus or modules to an application.



View and create modules
When a new application table is created, zero or one modules can be created. The
application developer must create additional modules.
If you created a module when you created a table, by default, the module's name will be the plural form of the table's name. For example, if the application is named Shipping, the default module name is Shippings.
View menu modules:
1. Open the application in ServiceNow Studio.
2. In the navigator panel, expand Module.
3. Select the module of interest.
Create a new module:
1. Open the application in ServiceNow Studio.
2. Select the Create button, then select File.
3. Make sure the Application field is set to your application.
4. Search for and select Module (sys_app_module) as the file type.
5. Select Continue.
6. Configure the module details.
7. Select Submit.



Configuring modules
Configuration options depend on the Link type.
Title     Defines the module name. Choose a title that clearly identifies the module.
Application Menu  Specifies the application (by name) under which the module appears. Defaults to the current application.
Order   Order in which Module appears in the Application Menu.
Hint    Defines the tool tip that appears when a user points to the module name.
Roles   Restricts module access to the specified roles. If this field is left blank, the application's roles are inherited, and the module is visible to all users.
Active  Defines whether the module appears in the application navigator.
Override application menu roles   Allows users to access this module even if they do not have permission to view the containing application menu. Users must still meet the role requirements for this module.
Link type   Specifies what type of link this module opens.
Table   The name of the table this Module is accessing.
View Name   Specifies the View in which the Module opens.
Filter      Used for lists. Specifies which records to display.
Note: Based on the link type, you may need to configure additional fields such as Filter, Content Page, or Arguments. See the ServiceNow documentation website (https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/reference/test-steps-app-navigator-category.html#title_r_ModuleLinkTypes) for more information.



Application records
As we have configured the application, additional records will be created in ServiceNow Studio.



Custom app table
There is a record for everything in the application on the custom app table. To view, select the App settings gear icon from the application details page in ServiceNow Studio.

Switch JavaScript Mode
This is where you can switch your JavaScript Mode. ECMAScript 2021 (ES12) is the default.

Bundle the app into an Update Set
From here, you can also bundle your entire app into an Update set.
Additional application details are located on the App details page.
Record for everything in the app
The application files related list shows you everything contained in the app.

Cross Scope Privileges
Cross scope privilege is a permission that allows one application to access resources in another application. This is useful for cases where an application needs to perform actions on data that is
owned by another application. For example, an incident management application may need to access customer data from the Customer Relationship Management (CRM) application.
In order for cross scope privilege to be activated, access needs to be allowed on both sides:
1. Application Access tab (referenced on previous page) - The app developer of App A needs to allow application access so other app developers can ask for permission.
AND
2. Cross scope privilege - The app developer for App B needs to ask for permission to access App A data.
Cross scope privileges are a powerful tool for integrating ServiceNow applications. However, it is important to use them carefully, as they can potentially create security risks. For example, if a cross scope privilege is not properly configured, it could allow an unauthorized application to access sensitive data.
During testing, application developers should run all of the application scripting logic to ensure the system creates any necessary cross scope privilege records. After application publication, the system only allows runtime requests to run that have a valid cross scope privilege record.



Application scope
The scope is visible in both ServiceNow Studio and the main ServiceNow window.
Scope in ServiceNow Studio
In ServiceNow Studio, the scope for each application file is visible in the bottom left corner of the screen. As you switch between files, the scope changes with you.
Caution: You can have multiple scopes open in ServiceNow Studio and switch between them.
Always double check when creating new records that you are in the correct scope.
To group tabs by scope, set the user preference to Organize tab groups by scope.
- Tabs that are color-coded and grouped are in the same scope.
• Tabs without colors indicate the file is in the global scope.
View the scope of a file by hovering over the tab.

Scope in ServiceNow
In the main ServiceNow browser, the scope selection menu icon (* globe) displays for users with roles that provide access to the application, update set, and domain scope pickers. Selecting an application sets the scope.
Application scope: Enables application developers to view and select the custom application where their changes apply. The Application Picker defaults to the newly created application. For more information, refer to Application scope: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/applications/concept/c_ApplicationScope.html
Update set: Enables admin users to choose an update set for making and tracking customizations. Development activity is captured as part of an application. For more information, see Update set administration: https://docs.servicenow.com/csh?topicname=update-set-administration.html&version=latest
Domain scope: Defines what users can access. Only users with access to domain separation see the domain scope picker. For more information, see Domain scope: https://docs.servicenow.com/csh?topicname=c_DomainScope.html&version=latest




3.4 Application Management
Application management
Module 3.4
User story
As the Application Developer, I manage the application development. I need tools to manage, install, and update applications on all company instances so users have access to the latest version in an efficient, timely manner.



Sharing applications
There are different methods to share an application.
Sharing method      Makes available to      Typical use case
Publish to the application repository     All instances assigned to the same company      Transfer an application to a test or production environment.
Publish to the ServiceNow Store       All ServiceNow customers      Share or sell applications to other companies.
Publish to an Update Set      Any instance with access to the Update Set file     Save a version of an application for compliance or backup reasons.

1. Publish to Update set
What is it?
for export.
Update sets are used to manage and store changes (versions) to an application and produce a file
How does it work?
When you publish an application to an update set, it creates an update set containing the current version of all application configuration records. It is basically a snapshot of your application.
When would it be used?
Use the update set as a backup file for auditing purposes or to transfer the application to another instance. Administrators can manually transfer versions between instances with update sets.
Where would it be available?
Any instance with access to the update set file.
2. Publish to the application repository
What is it?
The application repository is a central repository for all scoped applications. It enables ServiceNow customers to upload and distribute applications between their instances.
How does it work?
After you have designed, developed, and successfully tested a custom application, you can publish the application to the ServiceNow
application repository to share it with other instances in your company.
When would it be used?
Use the application repository to transter an application to a test or production environment.
Where would it be available?
It will be available to all instances assigned to the same company.
3. Publish to the ServiceNow Store
What is it?
Publishing an application to the ServiceNow Store makes it available to everyone.
How does it work?
To publish an application to the ServiceNow Store:
1. Create an application within a private application scope.
2. Join the Technology Partner Program.
3. Have the application certified.
When would it be used?
Use Publish to the ServiceNow Store when you wish to share or sell applications to other companies.
Where would it be available?
All ServiceNow customers.
Let's take a closer look at each. We'll begin with Publish to Update set.



How does Publish to Update set work?
An update set is a container for capturing customizations.
Publish to Update set
Create new, make changes, configure
"Sweep" it all into an Update set using Publish to Update set
Update sets can be used to deploy an application.
• Package all of the application files together.
• Export XML and add into any other instance (on the same family release).
• Move customizations between instances (dev-test-prod).
• Customizations and configurations are captured in an update set. By default, data is not included.

Update sets are a group of configuration changes that can be moved from one instance to another.
This feature allows administrators to group a series of changes into a named set and then move them as a unit to other systems for testing or deployment.
Update sets can produce a file for export. Administrators can manually transfer versions between instances with update sets.
Update sets let you apply changes in bulk, and help you force an instance to load the file versions you need.
For more information, select the links below:
System update sets: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/system-update-sets/concept/system-update-sets.html
Working with update sets in ServiceNow Studio: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/servicenow-studio/concept/working-with-update-sets-in-servicenow-studio.html



Deploy an update set
Developers must plan and fulfill a few steps manually.
Warning: Update sets allow moving changes between instances that may be running different family release versions and different features.
You can always load an update set created on an older family release on an instance running a newer family release. Loading an update set created on a newer family release on an instance running an older family release requires additional testing to determine compatibility.
Updates from newer family releases may not produce the same functionality when moved to older family releases. In extreme cases, newer family release updates may cause outages or data loss on an older family release instance. Where possible, avoid moving updates from newer family releases to older family releases. Similar constraints apply to moving updates between instances running different versions of ServiceNow Store apps.

The deployment process must be performed on both test and production.
The approach to deploying code and configuration changes in the ServiceNow environment involves using update sets along your instance chain. Once this is done, you clone back across the instances to match the environments.
It's important to note that using update sets can be a time-consuming process. There are manual steps involved, such as previewing update sets, working through collisions, and committing update sets. It can be challenging when working with a large development team generating multiple updates.


Publish, deploy, and retrieve an update set
The 'Publish to Update set' action creates a new update set and copies the latest version of each application file into the update set. The update set is then marked as Complete.
Publish an update set
1. In ServiceNow Studio, on the App details page, select the App settings and related links gear icon in the upper right.
2. Select "Publish to Update Set..." in the Related Links.
3. Select Publish.
4. Select Done.
5. View Customer Updates tab for a full list of contents.
Deploy an update set
Once an update set is complete, transfer it between instances to move customizations from development, through testing, and into production.
Deploy the update set
1. From the ServiceNow Studio home page, select the Deployment tab.
2. Expand the application of interest.
3. Select the update set of interest.
4. Change the State of the update set to Complete.
Setting the state of an update set to 'Complete' makes the update set "retrievable" in a connected instance (dev, test).
Retrieve the update set
1. On the target instance, (main ServiceNow window, not Studio) navigate to System Update Sets > Update Sources.
2. Select New.
3. Specify the connection settings, then select Test Connection.
4. Select Save (not Submit).
5. Select the Retrieve Completed Update Sets related link.
Any update sets marked as Completed are transferred from the source instance to the target instance. Update sets that already exist on the target instance are skipped.
The confirmation page provides detailed messages about how many update sets were transferred and how many were skipped.
To view retrieved update set, navigate to System Update Sets > Retrieved Update Sets.
If the system property glide.update_set.auto_preview is set to true, the system automatically starts the preview process after the update set is retrieved. If this property is false, you must start the process manually. For more information on the preview process, see Preview a remote update set.
Additional training resources
Retrieving Update Sets from Remote Instances: https://learning.servicenow.com/lxp/en/now-platform/retrieving-update-sets-from-remote-instances?id=learning_course_prev&course_id=68875453db77585030c91fdc1396197c



Deploy using the application repository
After you have designed, developed, and successfully dev-tested a custom application, you can publish your application to the application repository. Publishing an application to the app repo makes this version of the application available to all of an organization's ServiceNow instances.
The application repository allows development teams to deploy completed applications to other instances as a whole.
The application repository is a central repository for all scoped applications that are published. The application repository allows customers to upload and distribute applications between their instances. When you access the application repository, you can see and manage only the applications that are published by your own organization. You can not see or manage applications that are published by other organizations.
Important: Have a consistent process for development and deployment.
The ServiceNow application repository:
• Enables companies to store published applications for installation on any instance belonging to that company.
- glide.appcreator.company.code value must be the same on all instances (maint only property).
• Standardizes applications and versions installed on instances.
• Makes it easy to install/uninstall/update apps.
- Admin role required.
To use the application repository, an instance must have a valid subscription, matching application scope, and network access. As a result, personal developer instances cannot connect to the application repository.



Publish to the application repository
When publishing to an application repository, versions must be unique.
Publish an app to the application repository:
1. In ServiceNow Studio, open the App details page for the application.
2. Select Publish.
3. Note the New version number and edit as needed.
4. Update the Release notes as needed.
5. Select the Publish button.
6. Once complete, select Done.



Install and update an application
Install
• Applications in the Repository automatically appear on the All Apps tab.
• Do not do development work on instances where apps are installed; only develop on dev.
Update
• Badges indicate available updates.
• Administrators must update; no forced updates.
Install an application:
1. In the main ServiceNow window, open System Applications > My Company Applications.
2. Select the Not Installed tab.
3. Locate the application of interest and select the Install button.
Update an application:
1. In the main ServiceNow window, open System Applications > My Company Applications.
2. Select the Installed tab.
3. Locate the application of interest and select the Update button.



Uninstall or roll back an application
Roll back
• Roll back to the previous installation.
• Does not affect the global application record.
Uninstall
• Removes the application from an instance but not from the Repository.
• Can be re-installed at any time.
Roll back an installed application:
1. In the main ServiceNow window, open System Applications > My Company Applications.
2. Select the All Apps or Installed tab.
3. Locate the application of interest and select the Application Name (it is a link).
4. Select the Rollback Related Link.
5. Select the Rollback button to confirm the rollback.
6. Select the Done button.
Uninstall an application:
1. In the main ServiceNow window, open System Applications > My Company Applications.
2. Select the All Apps or Installed tab.
3. Locate the application of interest and select the Application Name (it is a link).
4. Select the Uninstall Related Link.
5. Select the OK button to confirm the uninstall.
6. Type the word uninstall in the confirmation box, then select the OK button.
7. Select the Done button.
Application repository resources
Publish app changes to the application repository from ServiceNow Studio: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/servicenow-studio/task/qs-publish-changes-to-app-using-app-repo.html
ServiceNow application repository: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/applications/concept/app-repo.html



What is the ServiceNow Store?
Applications can also be shared to the ServiceNow Store.
The ServiceNow Store is an online marketplace for downloading and installing ServiceNow applications.
• Some applications on the ServiceNow App Store are free, and some are fee-based.
• Applications are certified by ServiceNow for compliance with best practices.
• Applications published to the ServiceNow Store are sent for review and are not published directly to the store.
• After applications are reviewed and approved by ServiceNow, they are available for installation on any ServiceNow instance running a version supported by the application.
• The buyer is responsible for testing the App and assuming all risks.
Developers who want to build and distribute applications on the ServiceNow Store for the ServiceNow platform can join the ServiceNow Partner Program.
Learn more about the ServiceNow Partner Program: https://www.servicenow.com/partners.html
If you are already a ServiceNow Build partner, you can learn how to certify and publish joint solutions, integrations, and applications (apps) in the Partner Developer: Developing as a Build Partner learning path.
Partner Developer: Developing as a Build Partner: https://nowlearning.servicenow.com/lxp?id=learning_course_prev&course_id=0de03d0187526d94bfe94088dabb3554&autologin=yes
Note: You must be logged in to ServiceNow University to access the link.




3.5: Update sets during app development
User story
As the Application Developer, I need an efficient way to track file changes.
Update sets support version control and can be used to keep track of changes to applications and system platform features.



Update sets for app development
Update sets are flexible and can be used during both development and dep
Use update sets during the application development process to:
• Track customizations to application tables, fields, and records.
• Store customizations.
• Keep track of why a change was made.
• Export work in progress ahead of a clone.
Update sets are useful for:
• Customizing baseline applications.
• Customizing applications purchased from the store.
• Associating changes with SDLC artifacts.
- Stories, problems, bugs, enhancements, etc.



Update sets during app development
Update sets can be used to manage and store changes (versions) to an application during development.
Update sets can "record" changes you make to an application. Those changes can then be packaged and saved (version control) or deployed.
Creating a new Update set is like pressing "Record"
→
All changes are recorded in the Update set
→
Stop the Update set "recording"
→
Everything is contained in the Update set

We will practice using update sets in this class during the development of our application. Using update sets during development allows us to save versions of our new application as we build it.
Create a new update set:
1. In ServiceNow Studio, open the Update Set widget.
2. Select +New.
3. Name the new Update set.
4. Select Save.
5. Select Apply.
Complete an update set
Once an update set is complete, use these steps to stop the "recording" of changes to your application.
Complete the update set:
1. From the ServiceNow Studio home page, select the Deployment tab.
2. Expand the desired Application.
3. Select the desired update set.
4. Change the State of the update set to Complete.
Setting the state of an update set to 'Complete' closes the update set and makes it
"retrievable" in a connected instance (dev, test).



When to use each method
Update sets? Application repository?
ServiceNow Store?
How will I know which to use?
Here's an example of how we manage our app development and deployment. We follow an agile methodology and found this works best for our team:
1. After creating a new app, we use Publish to Update Set to capture everything in that new
app.
2. At the end of each day, we save our progress in an update set.
3. At the end of each sprint, we publish to the application repository.
4. Once the app is complete, if it is something we plan to sell to other companies, we use the ServiceNow Store.



ServiceNow recommendations
Design the Data Model before creating an application and tables in ServiceNow.
If possible, extend a ServiceNow table to gain functionality "for free".
Deploy the application using update sets, the application repository, or the ServiceNow Store.
Comment every step of the application development process you can!
```
