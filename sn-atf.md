# Automated Test Framework (ATF)

## TODO

- [ ]

## Resources

### Courses

- [x][ATF Learning Path](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-essentials?id=learning_path_prev&path_id=e7c6e2e2876b19946a0bedbd0ebb3592)
  - [x][ATF Introduction](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-introduction?id=learning_course_prev&course_id=2eebce6687a319946a0bedbd0ebb35db)
  - [x][ATF Run Tests and Test Suites](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-run-tests-and-test-suites?id=learning_course_prev&course_id=0ff09ea2872719946a0bedbd0ebb35d9)
  - [x][ATF Create and Schedule Tests and Test Suites](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-create-and-schedule-tests-and?id=learning_course_prev&course_id=ff945eae872719946a0bedbd0ebb3584)
  - [x][ATF Additional Tips, Techniques, and Resources](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-additional-tips-techniques-and?id=learning_course_prev&course_id=5cf816ae876719946a0bedbd0ebb3539)
  - [x][ATF Administration](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-administration?id=learning_course_prev&course_id=0f5e1a6687e719946a0bedbd0ebb351a)
- [ATF Micro Certificate Assessment](https://learning.servicenow.com/lxp/en/now-platform/automated-test-framework-atf-micro-certification-assessment?id=learning_path_prev&path_id=e22631dddbdef300760a71043996191f)

### Links

#### 🛠️ Core Documentation

- [ATF Documentation Overview](https://docs.servicenow.com/csh?topicname=automated-test-framework.html&version=latest)  
  Comprehensive guide to ATF concepts, features, and usage.

- [ATF Release Notes](https://docs.servicenow.com/csh?topicname=automated-test-framework-rn.html&version=latest)  
  Stay up to date with changes and enhancements.

- [Known Error Portal (Now Support login required)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597477)  
  Identify known issues for your specific release.

#### ⚙️ ATF Plugins & Tools

- [**ATF Test Generator and Cloud Runner** – ServiceNow Store](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)  
  Auto-generates ATF tests by analyzing workflows and behaviors. Includes Cloud Runner for client-side test execution on ServiceNow infrastructure.

- [Exploring ATF Test Generator and Cloud Runner – Product Docs](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/administer/atf-test-generator-cloud-runner/concept/atf-tg-cr-landing.html)

#### 🧪 Test Components & Execution

- [Available Quick Start Tests](https://docs.servicenow.com/csh?topicname=available-quick-start-tests.html&version=latest)  
  List of baseline ATF tests by app/feature.

- [Test Step Categories and Configurations](https://docs.servicenow.com/csh?topicname=test-step-categories.html&version=latest)

- [View the Progress of Automated Tests](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-view-progress.html)

- [Compare Results and Execution Times](https://www.servicenow.com/docs/bundle/yokohama-application-development/page/administer/auto-test-framework/task/atf-compare-runs.html)

- [ATF System Properties](https://docs.servicenow.com/csh?topicname=atf-admin-properties.html&version=latest)

- [ATF Headless Browser](https://docs.servicenow.com/csh?topicname=atf-headless-browser.html&version=latest)

#### 🚫 Error Handling & Debugging

- [Allowed Client Errors](https://docs.servicenow.com/csh?topicname=whitelisted-client-errors.html&version=latest)  
  Let tests continue despite known client-side JS errors.

- [Identify and Resolve Client Errors](https://docs.servicenow.com/csh?topicname=identify-and-resolve-client-errors.html&version=latest)

#### 🧩 Related Applications

- [Test Management 2 – Strategic Portfolio Management](https://www.servicenow.com/docs/bundle/yokohama-it-business-management/page/product/test-management2/concept/test-management-overview.html)  
  Manage manual and automated test plans together.

- [Locale settings](https://docs.servicenow.com/csh?topicname=locales.html&version=latest)

#### ✅ Best Practices & Use Cases

- [When and How to Use ATF (PDF)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/automated-test-framework-use.pdf)

- [ATF Best Practices (PDF)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/automated-test-framework-best-practices.pdf)

#### 📺 ServiceNow Video Channels

- [NOW Support YouTube Channel](https://www.youtube.com/c/NOWsupport/videos)

- [Developer Program YouTube Channel](https://www.youtube.com/c/ServiceNowDevProgram/videos)

- [Community YouTube Channel](https://www.youtube.com/c/ServiceNowCommunity/videos)

#### 📝 Developer Blog Highlights

- [ATF Debugging in San Diego](https://developer.servicenow.com/blog.do?p=/post/san-diego-atf-debugging/)

- [Building Testable Components for ATF](https://developer.servicenow.com/blog.do?p=/post/atf-testable-components/)

#### 🌐 ServiceNow Community Articles

- [How to Avoid ATF Testing Failures](https://community.servicenow.com/community?id=community_blog&sys_id=84dc2665dbd0dbc01dcaf3231f96190f)

- [Now Community: Reduce ATF maintenance with custom steps](https://community.servicenow.com/community?id=community_blog&sys_id=ec74896fdb3d9010d5c4d9d9689619ff)

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

#### Activity 2 - Create a test from scratch (ATF Create Tests)

- **Goal**: Create and run a test to verify correct pricing for an Apple iPhone 13 Pro catalog order (500MB data, Silver, 512GB storage).

- **Steps**:

  - **A. Manual Verification**

    - Navigate: **Self-Service > Service Catalog > Mobiles > Apple iPhone 13 Pro**
    - Set variables:
      - **Replacement?**: No
      - **Monthly Data**: 500MB
      - **Color**: Silver
      - **Storage**: 512GB
    - Add to cart; confirm pricing:
      - **Price**: $1,299.99
      - **Recurring Price**: $41.00 (Monthly)

  - **B. Set Locale**

    - Navigate: **System Properties > System Localization**
    - Set **Locale code**: `en.US`, save changes.
    - [docs: Locale settings](https://docs.servicenow.com/csh?topicname=locales.html&version=latest)

  - **C. Create the Test**

    - Navigate: **Automated Test Framework > Tests**, set scope to **Global**
    - Create new test:
      - **Name**: Apple iPhone 13 Pro: 500MB/ Silver/ 512GB
      - **Description**: Expected Result: when a silver Apple iPhone 13 Pro with 500MB and 512GB is ordered, the Price is $1,299.99, the Recurring Price is $41.00, and the Recurring Price Frequency is Monthly
    - Save

  - **D. Add Test Steps**

    1. **Create a User**

       - Category: **Server**, Configuration: **Create a User**

    2. **Open Catalog Item**

       - Category: **Service Catalog**, Configuration: **Open a Catalog Item**
       - Item: **Apple iPhone 13 Pro**

    3. **Set Variable Values**

       - Category: **Service Catalog**, Configuration: **Set Variable Values**
       - Replacement: **No**
       - Monthly Data Allowance (data_plan): **500MB**
       - Color: **Silver**
       - Storage: **512GB**

    4. **Set Catalog Item Quantity**

       - Category: **Service Catalog**, Configuration: **Set Catalog Item Quantity**
       - Quantity: **1**

    5. **Add Item to Shopping Cart**

       - Category: **Service Catalog**, Configuration: **Add Item to Shopping Cart**
       - Assert type: **Successfully added item to Shopping Cart**

    6. **Validate Price and Recurring Price**
       - Category: **Service Catalog**, Configuration: **Validate Price and Recurring Price**
       - Price: **$1,299.99**
       - Recurring Price: **$41.00**
       - Frequency: **Monthly**

  - **E. Run and Validate**
    - Select **Run Test** and launch client runner
    - Verify test results:
      - Initially may fail if incorrect variable values (e.g., Storage set to 256GB instead of 512GB)
      - Correct any errors (e.g., update storage variable) and re-run test
      - Ensure successful execution and correct price validation

#### Activity 3 - Create parent and child test suites (ATF Create Tests)

- **Goal**: Create a parent test suite (**My New Test Suite A**) and a child test suite (**My New Test Suite B**) to organize tests for efficient execution.

- **Steps**:

  - **A. Create Parent Test Suite**

    - Navigate to **Automated Test Framework > Suites**, set application scope to **Global**.
    - Create new suite:
      - **Name**: `My New Test Suite A`
      - **Filter**: `Name | starts with | Open`
      - Click **Update count** (should find 2 matching tests).
      - **Description**: `Parent Test Suite containing "Open" Tests and a child Test Suite`
    - Save suite; verify two tests are dynamically added.

  - **B. Create Child Test Suite**

    - Create another new suite:
      - **Name**: `My New Test Suite B`
      - **Description**: `Child Test Suite containing 3 Tests`
    - Manually add these tests:
      1. **Failing Jasmine Test**
         - Set **Abort on failure**: `true`
         - **Execution order**: `1`
      2. **Simple UI Test**
         - **Execution order**: `2`
      3. **Open an Existing Record**
         - **Execution order**: `3`
    - Set **Parent suite**: `My New Test Suite A`
    - Save and confirm the parent-child relationship.

  - **C. Run Parent Test Suite**

    - Open `My New Test Suite A` and select **Run Test Suite**.
    - Choose a client runner browser; run the test suite.
    - Observe execution of parent and child suites.

  - **D. Review Results**

    - Check results:
      - Parent tests should pass; child suite (`My New Test Suite B`) expected to fail.
      - Confirm `Failing Jasmine Test` failed as expected, causing subsequent tests to skip due to abort on failure.
      - Note: "Open an Existing Record" runs only once (from parent suite) even if included in both suites.

  - **E. Update Test Suite to Continue After Failure**

    - Open `My New Test Suite B`, update `Failing Jasmine Test`:
      - Set **Abort on failure**: `false`.
      - Save changes.

  - **F. Re-run Failed Tests**
    - Navigate to previous test suite results (**Automated Test Framework > Suite Results**).
    - Select **Re-run Failed Tests**.
    - Verify:
      - Only previously failed tests run (`Failing Jasmine Test` and `Simple UI Test`).
      - Test suite continues despite failure, executing remaining tests.

#### Activity 4 – Schedule a test suite (ATF Create Tests)

- **Goal**: Create a daily schedule to run two existing test suites and ensure a scheduled client test runner is available for UI steps.

- Steps:

  - **A. Launch Scheduled Client Test Runner**

    - Hold **Shift** and click: **Automated Test Framework > Run > Scheduled Client Test Runner**
    - Keep the new browser window open (this runner supports UI test execution)

  - **B. Create the Schedule**

    - Navigate to **ATF > Schedules**
    - Set scope to **Global**
    - Click **New**, name it **Daily Schedule**
    - Keep **Run frequency = Daily**
    - Set **Time** to ~15 minutes from now (24-hour format)
    - Click **Save**

  - **C. Add Test Suites**

    - In **Scheduled Suites** related list, click **New**
    - Add **Simple Parent Test Suite** with **Execution order = 100**, keep Browser/OS = Any
    - Click **Submit**
    - Add **Test Suite with Several Successful Members** with **Execution order = 200**
    - Click **Submit**

  - **D. Run the Schedule**
    - Confirm the scheduled test runner is still active via **ATF > Run > Active Scheduled Test Runners**
    - Reopen the schedule via **ATF > Schedules**
    - Wait for automatic execution or click **Execute Now**
    - Keep the test runner window visible for performance
    - Review results via **ATF > Suite Results**

- Notes:
  - Only **test suites** can be scheduled (not individual tests)
  - Scheduled test runners are required for UI steps in scheduled runs

#### Activity 1 - Enable ATF to run on instances (ATF Administration)

- **Goal**: Enable the ATF system properties that allow running tests and test suites, including scheduled execution, on a non-production instance.

- **Steps**:

  - Navigate to **Automated Test Framework > Tests** and open _Basic UI Test_.
  - Confirm **Run Test** is not available and the message indicates test execution is disabled.
  - Click the blue banner link or go to **Automated Test Framework > Administration > Properties**.
  - Set the following properties:
    - **Enable test/test suite execution**: Yes
    - **Enable schedule test suite execution**: Yes
  - Select **Save** to apply changes.
  - Reopen _Basic UI Test_ and verify the **Run Test** button is now visible.

- **Result**: Instance is now configured to support both manual and scheduled ATF test execution.

#### Activity 2 - Create a test template (ATF Administration)

- **A. Create the "Reject a Request" Test Template**

  - Set application scope to **Global**
  - Navigate to: `Automated Test Framework > Administration > Test Templates`
  - Select **New**
  - Set **Name**: `Reject a Request`
  - Open the test template list (unlock the list)
  - Add the following test step configurations in order:
    - Impersonate
    - Record Query
    - Open an Existing Record
    - Set Field Values
    - Click a UI Action
  - Set **Description**: `Open an existing request and reject it`
  - Select **Submit**

- **B. Create the Test**

  - Ensure application scope is **Global**
  - Go to: `Automated Test Framework > Tests`
  - Select **New**
  - Set **Name**: `Reject Change Request by Approver`
  - Set **Description**: `Reject a Change Request assigned to the Help Desk by an Approver`
  - Select **Save**

  Add the following test steps manually:

  - **Impersonate**
    - User: `Fred Luddy`
  - **Record Insert**
    - Table: `Change Request [change_request]`
    - Fields:
      - Assignment group: Help Desk
      - Type: Normal
      - Short Description: Rejected
  - **Open an Existing Record**
    - Table: `Change Request`
    - Record: Reference `Step 2: Record Insert > Record`
  - **Record Update**
    - Table: `Change Request`
    - Record: Reference `Step 2: Record Insert > Record`
    - Field:
      - State: Assess

- **C. Add the Test Template**

  - Select **Add Test Template**
  - Template: `Reject a Request`
  - Table: `Approval [sysapproval_approver]`
  - Select **Add**

  Configure the test steps added from the template:

  - **Impersonate**
    - User: `User 1` (approver)
  - **Record Query**
    - Timeout: `5`
    - Conditions:
      - Approver is `Step 5: Impersonate > User`
      - Approving is `Step 2: Record Insert > Record`
  - **Open an Existing Record**
    - Record: `Step 6: Record Query > First record`
  - **Set Field Values**
    - State: Rejected
    - Comments: `Need more documentation`
  - **Click a UI Action**
    - UI Action: `Reject`

- **D. Run the Test**
  - Select **Run Test** on the test form
  - Choose a **client test runner** for UI steps
  - Verify the test passes or debug and re-run as needed

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

#### Test Creation Best Practices

- **Create and impersonate a user**

  - Always start tests by creating and impersonating a user.
  - Prefer the **Create a User** method to dynamically add and impersonate a temporary user.
    - Avoids dependency on existing user records.
    - Automatically rolled back after test completion.
  - Limit use of **Impersonate existing user** to specific scenarios:
    - Risk of test failure if user details or IDs differ between instances.
    - May cause test inconsistency across development, test, and production environments.

- **Keep tests short**

  - Short tests isolate failures, making debugging quicker.
  - A test stops executing on the first failure; shorter tests help identify multiple errors faster.

- **Consider ACL security**

  - By default, ACL security (**Enforce security**) is applied to Record Insert, Update, Query, and Delete steps.
  - Disable security checks for setup actions; keep enabled for verification steps.

- **Test outcomes, not every step**

  - Focus tests on final outcomes (e.g., verifying Flow Designer outcomes), not each intermediate step.
  - Build test conditions to trigger flows or rules, then confirm the expected result.

- **Consistent date/time formatting**

  - When tests set client-side date/time fields, ensure impersonated users use the system date/time settings.
  - ServiceNow’s default user (**ATF.User**) provides consistent Date format and Time zone.

- **Prepare for parallel testing**

  - Design tests to run independently without relying on existing data.
  - Create all necessary data within the test setup to ensure test isolation and compatibility with parallel execution.

- **Know limitations**
  - Client test runners cannot access ServiceNow navigation bar or banner elements.

#### Test Suites

- **Test suites** group related tests and child test suites for easier execution.

  - Tests can belong to multiple suites, but a suite can only have one parent.
  - Tests within suites run sequentially and independently.
  - If a test is included multiple times within the suite hierarchy, it only executes once per suite run.
  - Test suites can:
    - Run concurrently with other suites
    - Re-run only previously failed tests
    - Be scheduled to run automatically
  - **Unit testing best practice:** Always verify new tests within a suite to ensure reliable execution under realistic workload conditions.

- **Adding tests to suites:**

  - **Manual approach:**  
    Use **Test Suite Tests** related list; select **New**, then add individual tests.
  - **Dynamic approach (via filter):**
    - Efficient for adding multiple tests based on criteria (e.g., test naming patterns).
    - Define filter conditions on the test suite form; matching tests are added automatically.
    - Dynamic filter updates suite membership automatically when new matching tests are created.
    - Caution: Applying a dynamic filter removes previously manually added tests unless re-added individually afterward.

- **Test execution order & failure handling:**

  - **Execution order:** Defines test sequence; editable directly from the suite’s test list.
  - **Abort on failure:** Configured per test; defaults to **false**, meaning other tests continue executing after a failure.

- **Managing child test suites:**

  - **Adding a new child suite:** On the parent suite’s **Child Test Suites** related list, select **New** to create a new suite as a child.
  - **Assigning existing suite as child:**
    - Open the existing child suite (**Automated Test Framework > Suites**).
    - Set the **Parent suite** field to the desired parent suite.
    - Save (**Update**) to create the relationship.
    - Confirm by viewing the parent suite’s **Child Test Suites** related list.

- **Create Schedules**
  - Only **test suites** can be scheduled (not individual tests).
  - **Scheduling must be enabled** via system property: `sn_atf.suite.scheduled_tests.enabled` (disabled by default).
  - Should remain **disabled on production**; valid and commonly used in **DEV/TEST** environments.
  - Navigate to **Automated Test Framework > Schedules**, click **New** to define:
    - **When** the test suite(s) should run (e.g., daily, weekly).
    - Save the schedule to enable the **Scheduled Suites** related list.
  - Add one or more test suites to the schedule:
    - Define **run requirements** for each (e.g., execution order, run condition scripts).
    - Note: **Conditional scripts** only execute as part of the **scheduled run**; **on-demand frequency** will skip them.
  - Test suites within the same schedule run **sequentially** (one after another).
  - Multiple different schedules can execute **concurrently**.

#### Scheduled Client Test Runners

- Required for executing **scheduled test suites** that include **UI test steps**.
- **Starting with Rome**: ServiceNow automatically spins up scheduled client test runners when needed — no manual setup required.
- These are **not the same** as manual/on-demand client test runners.
- Test Designers can view availability via **Automated Test Framework > Run > Active Scheduled Test Runners**.
- For scheduling across specific browser/OS environments (e.g., Chrome on Windows), ensure the required config is supported.
- ATF Test Administrators can launch additional runners if necessary.
- View current queue: **Automated Test Framework > Run > Waiting/Running Suite Runs**

### Tips and Tricks

#### Allowed Client Errors

- Client-side JavaScript errors are a common cause of test failures in ATF; these occur in the browser (vs. server-side errors on the instance).
- Even if the client error is unrelated to the test logic, it can still cause test step or suite failures.
- **Allowed Client Errors** lets test designers whitelist known or acceptable client-side errors so tests can continue running.
- Recommended use cases:
  - Temporarily allow errors while building or awaiting fixes.
  - Allow known, unimportant, or unresolvable errors (e.g., in legacy scripts).
- Test Designers (e.g., Doug and Alicia) can allow client errors directly from test results or logs.

- **How ATF handles allowed client errors**:
  - Allowed errors use a `contains` match on the error message (not exact).
  - Can be configured to log as:
    - **Warning**: test step succeeds with warning, message appears in output/log.
    - **Ignored**: test step succeeds silently, message logged with Ignored status.
- Manage entries via: **ATF > Run > Allowed Client Errors**

  - Fields:
    - **Report level** (Warning / Ignored)
    - **Error location** (Client / Server)
    - **Error message**
    - **Created from test**
    - **Delete** once resolved

- Review historical client-side error messages via: **ATF > Run > Reported Client Errors**

  - Filter for `Type is Server Error` to include server-side messages as well.

- Server-side error detection is enabled by default (from Tokyo); can be disabled per test.
- Helpful links:
  - [Allowed client errors](https://docs.servicenow.com/csh?topicname=whitelisted-client-errors.html&version=latest)
  - [Resolve client errors](https://docs.servicenow.com/csh?topicname=identify-and-resolve-client-errors.html&version=latest)

#### Custom User Interface Testing

- ATF supports testing **custom user interfaces** like UI Pages and UI Macros using specific tools and test step configurations.
- Two key features to explore further:

  - **Custom UI test step configurations**
  - **Page Inspector**

- **Custom UI test step configurations**:

  - Designed to interact with and validate HTML/JavaScript components on custom pages.
  - Help test the behavior and visibility of elements in non-standard UI.
  - Ideal area for deeper self-study and advanced use cases.
  - More info: [Custom UI testing](https://docs.servicenow.com/csh?topicname=custom-ui-test-steps.html&version=latest)

- **Page Inspector**:

  - Analyzes which HTML and JavaScript elements on a page are testable by ATF.
  - Saves time by confirming testability before building a test.
  - How to enable:
    - Go to **User Menu > Preferences > Debugging > Automated Test Framework Page Inspector**
  - Key components:
    - **Frame highlight**: indicates the current page under inspection
    - **Inspector pane**: lists the testable components
    - **Target selector**: drag to highlight and inspect specific elements

- More info: [Page Inspector](https://docs.servicenow.com/csh?topicname=atf-page-inspector.html&version=latest)

#### Additional ATF Best Practices

- **Avoid repeating UI steps**

  - Don’t duplicate testing the same UI functionality in multiple tests.
  - Reuse server test steps for speed and efficiency.

- **Always validate updates**

  - Follow every **Record Update** step with a **Record Validation** step.
  - Prevent silent failures caused by things like Data Policies.

- **Focus on functionality, not data permutations**

  - Test that changes occur as intended, not every possible input combination.

- **Use Timeout on server steps**

  - Wait for asynchronous actions (e.g., workflows, emails) to complete.
  - Set intelligent `Timeout` values (15–60 seconds) to allow for server-side processing.
  - Helpful during debugging for record inspection before rollback.

- **Avoid conditional logic**

  - Instead of branching logic, create separate tests for different conditions.
  - Simpler, clearer test maintenance.

- **Use random selection**

  - Select input records dynamically using server script to avoid brittle hard-coded values.
  - Prevents issues during migration and enhances test robustness.

- **Keep tests short**

  - Easier to isolate failures and rerun quicker.
  - More efficient for identifying issues.

- **Use Cloud Runner**
  - Run ATF tests on ServiceNow’s infrastructure via the ATF Test Generator and Cloud Runner app.
  - Frees up your local machine.
  - Store link: [ATF Test Generator and Cloud Runner](https://store.servicenow.com/sn_appstore_store.do#!/store/application/db1676d7421441106f046193880e0b37/1.0.17?referer=%2Fstore%2Fsearch%3Flistingtype%3Dallintegrations%25253Bancillary_app%25253Bcertified_apps%25253Bcontent%25253Bindustry_solution%25253Boem%25253Butility%25253Btemplate%26q%3DATF%2520Test%2520Generator%2520and%2520Cloud%2520Runner&sl=sh)

### ATF Administration

#### ATF Roles

- **Test Designer** (`atf_test_designer`)

  - Most common role; suitable for app developers and QA testers
  - Can:
    - Create, edit, and delete tests and test suites
    - Add test steps using predefined configurations
    - Run tests and view results
    - View system properties (read-only)
  - Cannot:
    - Create or edit test step configurations
  - Skills: Low-code/no-code experience; debugging familiarity helpful

- **Test Administrator** (`atf_test_admin`)

  - Manages system-level ATF configuration and client test runners
  - Can:
    - Do everything a Test Designer can
    - Configure ATF system properties
    - Create and manage test step configurations using scripts
    - Maintain test result retention and client test runners
    - Support complex test failures and environment management
  - Skills: Advanced scripting/programming

- **Web Service Tester** (`atf_ws_designer`)
  - Specializes in web service test development (REST/SOAP)
  - Can:
    - Do everything a Test Designer can
    - Create tests for APIs and integrations
    - Support advanced debugging involving integration logic
  - Skills: Advanced scripting and API knowledge

#### ATF Properties

- **ATF System Properties Overview**

  - Configured by ATF Test Administrators to control test execution, scheduling, screenshots, runner behavior, and more.
  - Navigate to: **Automated Test Framework > Administration > Properties**

- **Test Execution Controls**

  - `Enable test/test suite execution`: Allows tests/suites to run on the instance (disabled by default).
  - `Enable scheduled test suite execution`: Enables scheduling (should remain disabled on PROD).

- **Debugging**

  - `sn_atf.debug`: Enables enhanced logs and a Debug Info tab in the client test runner.

- **Screenshot Settings**

  - `sn_atf.screenshots.capture`: Capture options (all, failures only, or none).
  - `sn_atf.screenshots.use_glide_screenshot`: High-fidelity screenshots (default: true for new instances).
  - `sn_atf.screenshots.capture_full_page`: Full-page capture (performance impact).
  - `sn_atf.screenshots.timeout`, `height`, `width`: Control screenshot performance and dimensions.

- **Custom UI Testing**

  - `sn_atf.custom_ui.capture_all_page_data`: Ensures up-to-date data during custom UI test steps by refreshing the page.

- **Client Test Runner Settings**

  - `sn_atf.runner.heartbeat_interval`: Time between client runner check-ins.
  - `sn_atf.runner.timeout`: Time before a runner is marked offline.
  - `sn_atf.runner.retention_interval`: Time before offline runners are deleted.

- **Reporting**

  - `sn_atf.max_suite_results`: Sets max results in the test suite aging report.
  - Email formatting options for result summaries: text content and color coding for pass/fail statuses.

- **Headless Client Test Runners (Docker)**

  - Properties prefixed with `sn_atf.headless.*` configure test runner containers for UI testing without a visible browser.
  - Includes username/password credentials, Docker image, browser/OS settings, and login UI field IDs.

- **Admin Tips**

  - Property changes apply only to new test runners.
  - Always select **Save** to apply changes in the Properties form.

- **Reference**
  - [ATF System Properties – ServiceNow Docs](https://docs.servicenow.com/csh?topicname=atf-admin-properties.html&version=latest)

#### Test Runner Options

- **Overview**

  - There are three types of ATF test runners:
    - **Cloud Runner** – runs tests on ServiceNow-hosted infrastructure
    - **Client Test Runner** – runs tests in a browser window on the local machine
    - **Headless Browser** – runs UI tests without a visible browser; used behind firewalls

- **Cloud Runner**

  - Introduced in the Tokyo release
  - Enables background execution of UI tests using ServiceNow’s cloud resources
  - Best for freeing up local machines during test execution
  - **Not recommended** for sensitive or confidential environments
  - Requires installation from the [ServiceNow Store](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)

- **Client Test Runner**

  - Original test runner method
  - Recommended for:
    - On-prem data privacy requirements
    - Step-by-step test observation
    - Specific browser testing scenarios
  - Types:
    - **Manual Client Test Runner**: launched via _Run > Client Test Runner_ (hold `Shift`)
    - **Scheduled Client Test Runner**: launched via _Run > Scheduled Client Test Runner_ (hold `Shift`)
  - Environment is based on the browser/OS where it is launched
  - Tips for running scheduled client test runners:
    - Launch in a separate window
    - Disable sleep mode and screen saver
    - Ensure system remains awake and powered on
    - Maintain 100% browser zoom for best screenshots
    - Prefer virtual machines for security and availability

- **Headless Browser**

  - Runs UI tests without an open browser window
  - Ideal for automated, behind-the-firewall execution
  - Requires configuration via `sn_atf.headless.*` system properties
  - Uses Docker containers and login credentials to execute UI tests securely

- **Test Queue Monitoring**

  - Use these modules to monitor test and suite execution:
    - _Run > Active Manual Test Runners_
    - _Run > Active Scheduled Test Runners_
    - _Run > Waiting/Running Test Runs_
    - _Run > Waiting/Running Suite Runs_

- **Reference Links**
  - [Cloud Runner App – ServiceNow Store](https://store.servicenow.com/store/app/e4292f6e1be06a50a85b16db234bcbc3)
  - [Client and Scheduled Test Runners](https://docs.servicenow.com/csh?topicname=atf-test-runners.html&version=latest)
  - [ATF Headless Browser](https://docs.servicenow.com/csh?topicname=atf-headless-browser.html&version=latest)

#### Test Result Retention Policies

- **Retention Strategy Options**

  - Accumulated ATF results can be managed through:
    - Importing results into production via Import Sets
    - Using Data Preservers in sub-production to protect during cloning
    - Allowing automatic deletion after 30 days unless flagged for retention

- **Importing Results into Production**

  - Use [Import Sets](https://docs.servicenow.com/csh?topicname=import-sets-landing-page.html&version=latest) to move test data into production
  - Requires mapping external data into ATF result tables

- **Preserving Results in Sub-Prod**

  - Define [Data Preservers](https://docs.servicenow.com/csh?topicname=data-preservation.html&version=latest) to prevent overwriting during instance clones
  - Helps keep test history intact for UAT or development tracking

- **Automatic Deletion**
  - Default retention: 30 days for test and test suite result records
  - To keep specific results:
    - Open result record and check `Retain indefinitely`
  - Retention window can be modified through table cleanup policies
    - [Modify cleanup configuration](https://docs.servicenow.com/csh?topicname=atf-edit-table-cleanup.html&version=latest)
    - Recommended only for experienced system administrators

#### Migrate ATF Development

- **Migration Workflow**

  - Develop ATF objects in DEV
  - Migrate to TEST
  - Run tests in TEST
  - Migrate to PROD
  - Clone PROD back to TEST and DEV
  - Re-run ATF after upgrade in DEV
  - Use update sets (name them clearly with "ATF" included)

- **User and Group Sys_ID Consistency**

  - Tests often rely on users/groups (e.g., Impersonate, Assignment Group)
  - Sys_IDs must match across instances to prevent test failures
  - ServiceNow does not migrate users/groups automatically

- **Checklist for Consistent User References**

  - Create reference users/groups in PROD
  - Match test user group assignments to real user roles
  - Create an "ATF Test Users" group and include all test users/groups
  - Clone PROD to sub-prod to maintain sys_id consistency

- **Options to Avoid Sys_ID Dependencies**

  - Use **Create a User** test step configuration (preferred)
  - Build a custom test step to create temporary users
  - Dynamically query a user at test runtime

- **Post-Clone Setup**

  - Clone-inherited test users will be inactive
  - Use post-clone scripts to automatically activate test users/groups

- **Data Preservation**
  - Avoid overwriting ATF development objects during clones
  - Use data preservers to protect critical ATF test data

#### Create Test Templates

- **Purpose**

  - Test templates group common test step configurations for reuse.
  - Only **ATF Test Administrators** can create templates.
  - Test Designers can add templates to tests and configure steps as needed.

- **Use Cases**

  - Common sequences (e.g., approval simulation, form entry, field validation).
  - Steps are unconfigured—input values must be added after insertion.
  - For pre-configured steps, use a sample test instead.

- **How to Create a Test Template**

  - Set application scope (using picker or system settings).
  - Go to: `Automated Test Framework > Administration > Test Templates`
  - Select **New**.
  - Enter a **Name** and (optional) **Description**.
  - Add **Test Step Configurations** in desired order using the lookup icon.
  - Submit the form to save the template.

- **How to Use a Test Template**

  - Test Designers select **Add Test Template** from a test.
  - Select a template and click **Add**.
  - Test step configurations are copied into the test as editable test steps.
  - Instructions for configuring the steps are auto-appended to the test description.

- **Additional Guidance**
  - Templates are not pre-filled with values—use test samples if needed.
  - more about [creating tests](#create-tests)
  - [lab Create a test template](#activity-2---create-a-test-template-atf-administration)

#### Custom Test Step Configurations

- Custom test step configurations allow Test Administrators to define reusable server-side logic for ATF.
- Only available for **server-side** actions — not UI interactions.
- Created via: **Automated Test Framework > Administration > Step Configurations**

**Configuration involves:**

- Completing the initial form (Name, Category, Class type, Description).
- Writing two scripts:
  - **Description generation script**: dynamically defines the step description visible in the test.
    - [Learn more](https://docs.servicenow.com/csh?topicname=atf-config-desc-script.html&version=latest)
  - **Step execution script**: performs the actual server-side logic during the test run.
    - [Learn more](https://docs.servicenow.com/csh?topicname=atf-config-script.html&version=latest)
- Adding input and output variables that pass data into and out of the test step.

**Best Practices:**

- Use descriptive names and clear instructions for reuse by Test Designers.
- Consider skipping script writing initially and defining input/output variables first.
- Modify the layout via **Edit Variables Layout** for better test step configuration UI.
- Good use cases include:
  - Generating dynamic data
  - Setting time/date formats
  - Getting a random user or approver
  - Verifying emails or approvals
  - Creating workflows like "Approve all Approvals"

**Run Server Side Script vs Custom Step Config:**

- _Run Server Side Script_: ad-hoc, one-off use; not reusable across tests.
- _Custom Step Configuration_: reusable, scripted by Test Admins, visible to all designers.

**Example to review in PDI:**

- `Custom Scripted StepConfig` (available in the instance)

**More inspiration:**

- [Now Community: Reduce ATF maintenance with custom steps](https://community.servicenow.com/community?id=community_blog&sys_id=ec74896fdb3d9010d5c4d9d9689619ff)
