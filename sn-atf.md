# Automated Test Framework (ATF)

## TODO

- [ ]

## Resources

### Courses

- [ ][ATF Learning Path](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-essentials?id=learning_path_prev&path_id=e7c6e2e2876b19946a0bedbd0ebb3592)
  - [ ][ATF Introduction](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-introduction?id=learning_course_prev&course_id=2eebce6687a319946a0bedbd0ebb35db)
  - [ ][ATF Run Tests and Test Suites](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-run-tests-and-test-suites?id=learning_course_prev&course_id=0ff09ea2872719946a0bedbd0ebb35d9)
  - [ ][ATF Create and Schedule Tests and Test Suites](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-create-and-schedule-tests-and?id=learning_course_prev&course_id=ff945eae872719946a0bedbd0ebb3584)
  - [ ][ATF Additional Tips, Techniques, and Resources](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-additional-tips-techniques-and?id=learning_course_prev&course_id=5cf816ae876719946a0bedbd0ebb3539)
  - [ ][ATF Administration](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-administration?id=learning_course_prev&course_id=0f5e1a6687e719946a0bedbd0ebb351a)

### Plugins

- [ServiceNow Store – ATF Test Generator and Cloud Runner](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)
  - automatically creates ATF tests by analyzing instance behaviors and workflows: for regression testing and instance validation after changes or upgrades
  - Cloud Runner: run client-side tests in the cloud instead of a users browser

### Links

- [ATF Documentation](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/concept/atf-landing-page.html)
  - [Available quick start tests by application or feature](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/reference/available-quick-start-tests.html?state=seamless)
  - [View the progress of automated tests](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-view-progress.html)
  - [Compare results and execution times for different automated test and suite results](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-compare-runs.html)
  - [Exploring ATF Test Generator and Cloud Runner](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/administer/atf-test-generator-cloud-runner/concept/atf-tg-cr-landing.html)
  - [Available quick start tests by application or feature](https://docs.servicenow.com/csh?topicname=available-quick-start-tests.html&version=latest)
  - [Available Test Steps and Categories](https://docs.servicenow.com/csh?topicname=test-step-categories.html&version=latest)
- create testing plans and track the remaining manual testing: [Strategic Portfolio Management/Test Management application](https://www.servicenow.com/docs/bundle/yokohama-it-business-management/page/product/test-management2/concept/test-management-overview.html)

### Labs

#### Activity 1 - Run a test and review results (ATF Run Tests and Test Suites)

- **Goal**: Run the prebuilt "Multi-Batch Test" and analyze its results to understand test execution batches and result review.
- Steps:
  - **A. Run the Test**
    - Navigate to **Automated Test Framework > Tests**
    - Search for and open **Multi-Batch Test**
    - Review the test steps and their descriptions
    - Click **Run Test** in the form header
    - Select a client test runner (or use current browser if none listed)
    - Observe test execution in the separate test runner window
    - Once complete, return to the main window and note the test ran in 4 batches
  - **B. Review the Test Results**
    - In the Run Test window, click **Go to Result**
    - Check the **Step Results** list — all steps should show **Success**
    - Open **Test Log** to view browser console output
    - Open **Test Transactions** to view server-side logs
    - Click **Manage Attachments** to view screenshots
      - Only UI steps generate screenshots — 7 of 9 steps in this case
      - Find the screenshot for step 4 **Set Field Values**, showing value "Emily"

#### Activity 2 - Run a test suite and review results (ATF Run Tests and Test Suites)

- **Goal**: Run the "Suite That Continues on Member Failure" test suite, identify and fix a failed test, then re-run only the failed test to confirm the fix.
- Steps:
  - **A. Run the Test Suite**
    - Navigate to **Automated Test Framework > Suites**
    - Search for and open **Suite That Continues on Member Failure**
    - Review the 3 included tests — all set to **continue on failure**
    - Click **Run Test Suite** in the form header
    - Select a client test runner (or use current browser if none listed)
    - Observe UI steps running in a separate browser window
    - Return to the main window after execution and confirm failure in test 2: **Fails Because an Assert Fails**
  - **B. Review the Test Suite Results**
    - In the Run Test Suite window, click **Go to Result**
    - Locate the failed test and open its timestamped result
    - On the **Step Results** tab, identify failure in step 4 — **Field Values Validation**
    - Review the summary — failure due to mismatch between set value and expected value
  - **C. Fix the Test**
    - Navigate to **Automated Test Framework > Tests**
    - Open the test **Fails Because an Assert Fails**
    - Compare the **Set Field Values** and **Field Values Validation** steps
    - Update the expected Description value in the validation step to:
      - _About all the tasks that need to be discussed_
    - Click **Update** to save
  - **D. Re-run Failed Test**
    - Navigate to **Automated Test Framework > Suite Results**
    - Open the previous result for the suite using its timestamp
    - Click **Re-run Failed Tests**
    - Select a client test runner (or use current browser if none listed)
    - Observe the execution and verify the corrected test passes

#### Activity 1 - Copy and configure a quick start test (ATF Create Tests)

- **Goal**: Copy a ServiceNow-delivered quick start test ("CHG: Convert Normal to Emergency type") and configure it to impersonate a specific user, then verify it runs successfully on your instance.

- **Steps**:

  - **A. Copy and Configure the Test**

    - Navigate to **Automated Test Framework > Tests**
    - Find and open the **CHG: Convert Normal to Emergency type** quick start test (inactive/read-only)
    - Set **application scope** to **Change Management - ATF**
    - Click **Copy Test** and confirm demo data installation
    - In the copied test, open the **Impersonate** step:
      - Set **User** to **Fred Luddy**, then save
    - Open the **Set Field Values** step:
      - Change field from **Type** to **Model**; set value to **Emergency**, then save

  - **B. Run Test and Verify Results**
    - Click **Run Test** on the test form
    - Select or start a **client test runner**
    - Watch the test execute client-side steps in the runner window
    - After completion, return to main window; verify test succeeded
    - Click **Go to Result** to review detailed results; confirm all steps have **Status: Success**
    - Screenshots available for UI steps

## Topics

### Introduction

- **Goals & Benefits**
  - Reduces validation time for instance upgrades
  - Ensures consistent, repeatable testing to maintain quality
  - Upgrade-safe and UI-independent without extra licensing costs
  - Mitigates risk by enabling frequent and confident upgrades
- **Core Functionalities**
  - **Functional Business Logic Testing**
    - Validates processes meet defined acceptance criteria
    - Supports out-of-box, scoped/custom apps, Service Portal, and custom data/forms
    - Performs tests via UI or directly on server-side data
  - **Regression Testing**
    - Confirms existing processes function correctly after upgrades or changes
    - Provides consistent pre/post-change validation
  - **Browser Compatibility Testing**
    - Single test covers multiple browsers and operating systems
  - **Server-side Jasmine Integration**
    - Enhances server-side validation using Jasmine JavaScript tests
- **Limitations** (Use manual testing or third-party tools like Selenium for these)
  - Performance testing
  - Load testing
  - Report validation
  - Email formatting tests

#### ATF Architecture

- **Test Suites**
  - Collections of related tests or child test suites, run sequentially with one click
  - Useful for organizing regression tests and complex test scenarios
  - Supports nested hierarchies with one parent per suite; tests can belong to multiple suites
- **Tests**
  - Sets of actions (steps) and assertions verifying specific functionality
  - Should focus on smaller, clearly-defined objectives rather than broad scenarios
  - Can include both client-side (UI-based) and server-side actions/assertions
  - Ideal for Agile environments, can be linked to Stories as acceptance criteria
  - Recommended practice: create and impersonate test users dynamically within tests for accurate authorization checks
- **Test Steps**
  - Individual actions or assertions within a test (e.g., creating users, opening forms, validating fields)
  - OOB test steps provided for a no-code approach
  - Additional custom test steps can be created by an ATF Test Admin as needed

#### ATF Roles

- **Test Designer**
  - `atf_test_designer`
  - Primary ATF role; typically assigned to application developers
  - Responsibilities:
    - Create, edit, delete tests and test suites
    - Add existing test steps (cannot create new configurations)
    - Run tests and suites; view results
    - View ATF system properties
  - Skills Required: Low-code or No-code; advanced debugging experience beneficial
- **Test Administrator**
  - `atf_test_admin`
  - Manages ATF environment and creates reusable test step configurations
  - Responsibilities include all Test Designer capabilities plus:
    - Create and edit ATF system properties
    - Develop custom test step configurations through scripting
    - Assist Test Designers with advanced debugging
  - Skills Required: Advanced scripting/programming experience
- **Web Service Tester**
  - Specializes in building and maintaining web service integration tests (REST, SOAP)
  - Responsibilities include all Test Designer capabilities plus:
    - Build web service tests involving integrations
    - Assist Test Designers in complex debugging tasks involving scripting
  - Skills Required: Advanced scripting/programming, with expertise in web services

#### ATF Process

- **1. Identify Essential Functionality**
  - Focus on functionality unique to your ServiceNow instance
  - Prioritize areas with higher risk exposure
  - Balance validation depth with long-term maintenance effort
- **2. Create Tests to Validate Essential Functions**
  - Begin creating tests after functionality stabilizes to avoid rework
  - Iterative development may require frequent updates to ATF tests
- **3. Package Tests into Suites**
  - Group related tests into suites for organized execution
  - Tests can belong to multiple suites; suites can be newly created or reused
- **4. Run or Schedule Test Execution**
  - Suites can be executed on-demand or scheduled
  - Individual tests must be run manually
  - Test steps run either:
    - **Client-side** via test runner in a new browser window
    - **Server-side** directly against the instance backend
- **5. Monitor and Fix Issues**
  - Review detailed results at suite, test, and step level
  - Leverage runtime screenshots and logs for efficient debugging

#### Running Tests Overview

- more details in [Run Tests](#run-tests)
- **Execution Behavior**
  - Tests can run concurrently unless grouped within a suite
  - Tests in a suite run sequentially; suite can abort on failure if configured
- **Test Data & Isolation**
  - Each test is isolated from others; no cross-test data sharing
  - Output values from one test step can only be used by other steps within the same test
  - Impersonated users are automatically unimpersonated at test end or on next impersonation
  - All instance data changes are rolled back after test completion (create/delete/update)
- **Environment Control**
  - ATF must not be run in production environments
  - Common risks of running in production:
    - Temporary data becomes visible to users before rollback
    - Performance degradation
    - Triggering unintended actions (emails, approvals, etc.)
    - Exposure of sensitive data during impersonation
    - Persistent audit history despite rollback
  - ATF is disabled by default on all instances via system property
  - ATF objects should still be promoted to production for cloning consistency across environments

#### ATF Cost Factors

- **Significant Factors**
  - **Level of Test Detail**
    - More detailed tests increase complexity and maintenance
    - Consider test frequency and who maintains them
  - **Quality of Existing Development**
    - Poor design may require refactoring before tests can be created
  - **Number of Client-side Tests**
    - Slower to execute and unit test compared to server-side steps
    - Evaluate if UI coverage can be minimized in favor of server-side validation
  - **Uniqueness of Each Test**
    - Most impactful factor; unique tests require custom logic and effort
    - Reusable patterns reduce time if test steps, forms, or logic overlap
- **Not Significant Factors**
  - **Number of Test Steps**
    - Does not directly affect development effort; tests can be cloned and adjusted
  - **Number of Test Cases**
    - Less relevant if cases are similar; reuse and modification streamline development

#### Quick Start Tests

- Quick start tests are baseline ATF test templates delivered by ServiceNow
- Designed for frequently required and critical use cases
- Benefits:
  - Reduce development time by providing ready-made test examples
  - Install with demo data from corresponding ServiceNow plugins
  - Can be copied, customized, and run against your instance-specific data
  - Serve as learning tools for ATF best practices
  - Allow annotation to track customizations if the original test changes
- Usage Notes:
  - Quick start tests are inactive and read-only by default
  - Must be copied and configured before running on real data
  - Always check for existing quick start tests before building new ones
- [docs: Available quick start tests by application or feature](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/reference/available-quick-start-tests.html?state=seamless)

### Run Tests

- [**Roles**](#atf-roles): Test Designer, Test Administrator, Web Service Tester

- **Test Execution Basics**

  - Enable ATF via system property (disabled by default to protect production)
  - Tests run a sequence of test steps
  - Test stops at first failing step; subsequent steps are skipped
  - Test results include detailed logs and screenshots
  - Output values from one test step can only be used by other steps within the same test
  - Each test is isolated from others; no cross-test data sharing
  - Impersonated users are automatically unimpersonated at test end or on next impersonation

- **Parallel vs Sequential Execution**

  - Manually run individual tests can execute in parallel (after initial run to track modified records)
  - Tests in a test suite run sequentially; suites can abort on failure if configured
  - Developer Portal instances do not support parallel test execution

- **Rollback Behavior**

  - All changes made during a test are rolled back (create/update/delete)
  - Rollback is based on the impersonated user's activity
  - Rollback excludes:
    - specific tables and their extensions:
      - History [sys_history_line]
      - ECC Queue [ecc_queue]
      - Email [sys_email]
      - Email Log [sys_email_log]
      - Report Execution [report_executions]
      - Report Stats [report_stats]
    - Custom exclusions: add `excludedFromRollback=true` to the Collection record in _System Definition > Dictionary_ after the first test run
    - Asynchronous changes: (e.g., events, email notifications, workflows) may be missed if not completed before rollback

- **Client vs Server Test Steps**

  - Client steps simulate UI actions (run in separate browser window)
  - Server steps interact directly with the instance backend
  - Browser performance can affect UI test execution speed – [see browser recommendations](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/concept/browser-recommendations-atf.html)

- **Monitoring and Debugging**

  - Track running/waiting tests under: _Automated Test Framework > Run > Waiting/Running Test Runs_
  - Cancel pending tests from the waiting list
  - Only test results persist — step data/variables are not retained
  - Use Run Test progress window to view execution in real-time
  - If closed, reopen via [Run Test progress view](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-view-progress.html)

- **Environment Control**

  - ATF must not be run in production environments
  - Risks of running ATF in production:
    - Temporary data visible before rollback
    - Performance degradation
    - Triggering emails, approvals, or other business actions
    - Exposing sensitive data during impersonation
    - Audit history is persisted even after rollback
  - ATF objects should still be promoted to production for clone consistency across environments

- **Tips**
  - UI test steps include intelligent waits (e.g., "Waiting for the form to be calm")
  - To avoid conflicts while making instance updates during test runs: Use a different browser or open an Incognito window

#### Run Test Suites

- **Purpose**

  - Efficiently run groups of related tests (e.g., regression tests) with a single action
  - Ensure tests work both individually and within the context of a suite

- **Requirements**

  - User must have one of the [ATF Roles](#atf-roles)
  - ATF must be enabled on the instance

- **Execution Behavior**

  - Test suites run tests sequentially, one at a time
  - Child test suites run automatically; their order cannot be defined
  - If a test fails, suite behavior (abort or continue) is configurable
  - A test only runs once per suite execution, even if included multiple times
  - Each test is isolated — no shared state between them

- **Result Rollup**

  - Failed test step → test fails → test suite fails → parent suite (if any) fails
  - Test suite results include:
    - Individual test results
    - Results of any child test suites

- **Monitoring Suite Runs**

  - Navigate to: _Automated Test Framework > Run > Waiting/Running Suite Runs_
  - Multiple suites can run at the same time, but their included tests still run one at a time

- **Troubleshooting**

  - If the **Run Test Suite** button is missing:
    - Ensure you’re not impersonating another user
    - Confirm ATF is enabled in system properties

- Tips
  - Test suites can be scheduled for automated execution
  - After a failed run, use **Re-run Failed Tests** to avoid rerunning successful tests
  - Use [comparison tools](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-compare-runs.html) to analyze:
    - Execution times per test/test step
    - Pass/fail trends across test suite runs

#### Troubleshoot a Failing Test

- **Goal**: Use built-in ATF debugging tools — **breakpoints** and **pause before rollback** — to troubleshoot and resolve failing tests effectively.

- **Run vs Debug Test**

  - **Run Test**: Executes the test normally; ignores breakpoints
  - **Debug Test**: Pauses test execution at specified breakpoints to inspect behavior step-by-step

- **Using Breakpoints**

  - Add breakpoints to any test step via right-click > **Add/Remove Breakpoint**
  - While debugging, the test pauses at each breakpoint for analysis
  - Use the **step over** feature to proceed through each test step
    - client runner shows live forms -> manual intervention and testing is possible
  - Breakpoints are user-specific and not shared between users
  - Run Test ignores all breakpoints, so removal is optional after debugging

- **Pause Before Rollback**

  - Option to pause a test **after all steps pass but before rollback**
  - Allows inspection of instance data (inserted/updated records) in a live environment
  - To use:
    - Open test from **Automated Test Framework > Tests**
    - Click **Debug Test**
    - Enable **Pause Before Rollback** checkbox
    - Run the test and inspect data before selecting **Continue** to trigger rollback
  - Default pause duration is 10 minutes; override with system property: `sn_atf.breakpoint.timeout`

- **Supported Use Cases**
  - Works with all test types: individual, suite, parameterized
  - Supports all step types: client and server-side
  - Scheduled tests always run in standard **Run Test** mode (not Debug)

#### Test Runner vs. Cloud Runner

- **Test Runner (Local)**
  - Runs tests in your local browser window
  - Browser must remain open and active throughout execution
  - Requires user presence to monitor and prevent system sleep
  - Best for **debugging and troubleshooting**, where step-by-step visibility is needed
- **Cloud Runner (ServiceNow Cloud)**
  - Introduced in the **Tokyo release** via the _ATF Test Generator and Cloud Runner_ app from the [ServiceNow Store](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)
  - Runs tests on ServiceNow’s cloud infrastructure — no local browser required
  - Frees the user to work on other tasks while tests run in the background
  - Not suitable for troubleshooting — execution is not visible during the run
  - Comes with **2 free concurrent tests**; up to **7 parallel tests** available as a paid upgrade
- **Considerations**
  - Not ideal for organizations with strict data control policies (e.g., government agencies)
  - Check with your System Administrator to determine if this app is appropriate for your environment
  - If installed, **Cloud Runner** will appear as a test execution option
- **Resources**
  - [ServiceNow Store – ATF Test Generator and Cloud Runner](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)
  - [docs: Exploring ATF Test Generator and Cloud Runner](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/administer/atf-test-generator-cloud-runner/concept/atf-tg-cr-landing.html)

### Create Tests

#### Options for Test Creation

- **Prioritize test creation approaches:**
  - Copy a [**Quick Start Test**](#copy-and-configure-quick-start-tests) (provided by ServiceNow)
  - Copy an existing test from your organization
  - Create a new [test from scratch](#create-tests-from-scratch) (most effort required)

#### Automatically Generate Tests

- The **ATF Test Generator and Cloud Runner** (introduced in Tokyo) automatically creates ATF tests by analyzing instance behaviors and workflows.
  - Ideal for regression testing and instance validation after changes or upgrades.
  - Available via the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/application/db1676d7421441106f046193880e0b37)

#### Copy and Configure Quick Start Tests

- **Quick start tests** accelerate test development by providing reusable baseline tests

  - Focused on common and critical use cases
  - Installed with demo data from ServiceNow plugins
  - Can be copied and customized for instance-specific data
  - Annotate custom tests to note changes from original

- **How to copy and configure a quick start test:**

  1. Navigate to **Automated Test Framework > Tests** and open desired quick start test (inactive/read-only).
  2. Set the correct **application scope** matching your target test.
  3. Click **Copy Test**
  4. Update **test step input variables** to reflect instance-specific data.
  5. Add or modify test steps for custom requirements.
  6. Save and include the test in your test suites.

- **Alternative:** Copy existing custom tests within your organization, following the same process.

- [Available quick start tests by application or feature](https://docs.servicenow.com/csh?topicname=available-quick-start-tests.html&version=latest)

#### Create Tests from Scratch

- **Create tests from scratch** when no suitable existing tests are available.
- Before creating:

  - Walk through steps manually in ServiceNow and document actions precisely.

- **How to create a test from scratch:**
  1. Navigate to **Automated Test Framework > Tests**, click **New**.
  2. Fill in initial details:
     - **Name:** Clear and descriptive.
     - **Application Scope:** Matches functionality tested.
     - **Parameterized Testing:** Enables multiple runs with different inputs ([Learn more](https://docs.servicenow.com/csh?topicname=parameterized-tests.html&version=latest)).
     - **Description:** Clearly define expected outcomes.
  3. Save to display **Test Steps** and **Test Results** related lists.
  4. Use **Add Test Step** to define each action or assertion step.
  5. Optional features include:
     - **Run Test** to debug immediately.
     - **Debug Test** to pause at breakpoints or before rollback.
     - **Mutually Exclusive Tests** to prevent concurrent execution conflicts.
     - **Add Test Template** to reuse grouped test steps (created by ATF Admin).
     - **Copy Test** for quick creation of similar tests.

#### Test Step Configurations

- **Test steps** use predefined **test step configurations**:

  - Define step behavior, input variables, and output variables
  - Require no coding; easily configurable through provided settings

- **User Impersonation Steps**:

  - Commonly used as the first step to validate role-based authorizations
  - Two methods available:
    - **Create a User** (recommended from New York onwards): dynamically creates and impersonates a temporary user, automatically removed after test completion
    - **Impersonate**: uses a pre-existing user for the duration of the test only

- **Available ServiceNow Test Step Categories**:

  - **Application Navigator** (UI): Verify menu/module access ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-app-navigator-category.html&version=latest))
  - **Custom UI** (UI): Validate custom UI elements ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-custom-ui-category.html&version=latest))
  - **Email** (Server): Test email notifications ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-email-category&version=latest))
  - **Form** (UI): Check fields and UI actions ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-form-category.html&version=latest))
  - **Forms in Service Portal** (UI): Validate Service Portal forms ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-forms-portal-category.html&version=latest))
  - **List and Related List** (UI): Test list views/actions ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-list-related-list&version=latest))
  - **Reporting** (Server): Confirm report accessibility
  - **Responsive Dashboards** (Server): Confirm dashboard visibility
  - **REST** (Server): Validate REST web services ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-rest-category.html&version=latest))
  - **Server** (Server): Perform server-side actions (query/update/script) ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-server-category.html&version=latest))
  - **Service Catalog** (UI): Test catalog item transactions ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-service-catalog-category.html&version=latest))
  - **Service Catalog in Service Portal** (UI): Test catalog items via Service Portal ([Docs](https://docs.servicenow.com/csh?topicname=test-steps-catalog-portal-category.html&version=latest))

- **Passing Variables Between Test Steps**:
  - Output variables from a step can feed input variables of subsequent steps within the same test (e.g., User IDs, Record IDs)
  - Tests remain isolated; output variables cannot pass between separate tests

#### Configure Test Steps

- After selecting a **test step configuration**, configure the test step by specifying the required **input variables**.

  - Example (**Impersonate** step):
    - **Execution Order**: Defines run sequence; auto-adjusts when changed.
    - **Step Config**: Identifies the chosen configuration; cannot change afterward.
    - **Input Variables**: Configuration-specific fields (e.g., User ID).
    - **Output Variables Picker**: Allows passing values from previous test steps.

- After configuring inputs, submit the step to add it to the test.

- **Identify Output Variables**:

  - Output variables aren't displayed directly in the test step creation window.
  - Locate them under **Automated Test Framework > Administration > Step Configurations**, selecting the relevant configuration.

- **Step Configurations**:
  - **Step Environment**: Indicates execution location (server or user interface).
  - **Class Type**: Specifies implementation (Java class or script-based).
  - **Template Reminder**: Instructions shown when using test templates.
  - **HTML Description**: Overview of behavior, inputs, and outputs (seen during step selection).
  - Review the **Output Variables** related list for available outputs.
