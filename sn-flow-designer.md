# Flow Designer

## Resources

- **Webapp**: [Flow Chart Creator](https://app.diagrams.net/)
- **Docs**:
  - [Flow Error Handler](https://docs.servicenow.com/csh?topicname=flow-error-handler.html&version=latest)
  - Flow Designer trigger types
  - Flow Designer actions
  - Inline scripts
  - Transform functions
  - Flow execution details
  - Activate flow reporting
  - Flow diagramming view
  - Flow Template Builder
  - Building subflows
  - User access to Flow Designer
  - Application scope
  - Publish an application to the application repository
  - Publish an application to the ServiceNow Store
- **YouTube**: [Academy Session #10: Getting Started with Decision Builder](https://www.youtube.com/watch?v=0edK6z6yFAs)
- **Courses**:
  - [x] [Flow Designer: Introduction - Washington](https://nowlearning.servicenow.com/lxp/en/pages/lxp-search?id=search&q=Flow%20Designer:%20Introduction%20-%20Washington&spa=1)
  - [x] [Configure Orchestration, Flow Designer, and Integration Hub](https://nowlearning.servicenow.com/lxp/en/it-operations-management/configure-orchestration-flow-designer-and?id=learning_course_prev&course_id=4f63e5f7db3f4010785e2a59139619a7)
  - [ ] [Flow Designer: Error Handling](https://nowlearning.servicenow.com/lxp/en/pages/lxp-search?id=search&q=Flow%20Designer:%20Error%20Handling&spa=1)

---

## Flow Designer: Introduction - Washington

### Benefits of Flow Designer

- Combines multiple platform automation capabilities, configurations, and runtime information for creating, operating, and troubleshooting flows from a single interface.
- No-code approach with natural language for triggers, actions, inputs, and outputs.
- Library of reusable flow components.
- Upgrade-safe platform logic replaces complex custom scripts.
- Develop, share, and reuse custom flow components.
- Display flows as diagrams.

### Main Components of Flow Designer

- **Flow**: Automated process consisting of a trigger and a sequence of actions.
  - Automates business logic for applications or processes (e.g., updating records, approvals, tasks, notifications).
- **Subflow**: Reusable sequence of actions, inputs, and outputs (no trigger).
  - Runs within a flow, subflow, or script.
- **Action**: Reusable no-code operation.
- **Spoke**: Scoped application containing actions and subflows for managing specific tables (e.g., ITSM spokes, Field Service spoke).

### Navigation in Flow Designer

- **Workflow Studio**:
  - Path: `All > Process Automation > Workflow Studio`
  - Workflow types: Playbooks, flows, subflows, actions, data stream actions, decision tables.
  - Features: Resume where you left off, latest updates, resources (docs, videos, community site, etc.).
- **Flow Page**:
  - Elements: Data pills, actions, triggers, flow name, state.
  - Views: Standard, Diagram.
  - Buttons: Test, Edit, (De-)Activate, More Actions, Help.

## Create a Flow

### What is a Flow?

- Automates business logic for an application/process.
- Runs automatically when trigger conditions are met.
- Composed of:
  - **Flow Properties**
  - **Trigger**
  - **Sequence of Actions**
  - **Flow Logic** (optional)
  - **Flow Data**: Created, collected, and used during execution.

### Flow Properties

- **Flow Name**: Descriptive name of the flow.
- **Description**: Explanation of the flow's purpose.
- **Application**: Scope of the flow (cannot be changed after saving).
- **Protection**: Read-only setting.
- **Run As**: System/user who triggers the flow.
- **Run with Role(s)**: Permissions for execution.

### Flow Processing

1. **Trigger**: Scheduler creates an event in the queue when conditions are met.
2. **System Processing**:
   - Processes the event to start the flow.
   - Builds a process plan containing actions, inputs, and steps.
   - Runs the process plan within the application scope.
   - Stores execution details in a **context record**.
3. **Execution Details**:
   - Outcome state, runtime duration, log messages, configuration, and runtime values.
   - Possible outcomes: Complete, In Progress, Waiting, Canceled, Error.

### Trigger Types

- **Record-Based**
- **Schedule-Based**
- **Application-Based**

### Input Types

- Common types include:
  - Boolean, Date/Time, Integer, String, Email, File Attachment.
  - Reference, List, HTML, Password, URL, Workflow, XML, and more.

### Troubleshooting and Logs

- Use Flow Designer > Active Flows to confirm whether a flow was triggered.
- View logs to inspect:
  - Inputs and outputs for each step.
  - Action execution results (e.g., command outputs).
- Ensure the flow is activated for production scenarios.

---

## Flow Designer Actions

Flow Designer, with IntegrationHub, enables the creation of reusable actions for executing commands or processes against targets. Actions can include inputs, outputs, and dynamic configurations, enhancing flexibility and reusability.

### Steps to Configure and Execute an Action

1. **Access Flow Designer**:
   - Navigate to **Flow Designer > Designers** to create **Actions**, **Flows**, or **Subflows**.
   - Actions are specific tasks; here, an action is created to execute a command against a target.
2. **Create an Action**: New > Action
   - Define the action name (e.g., "Get Network Adapter Example").
   - Set the scope and defaults.
   - Add steps for execution (e.g., using SSH functionality from IntegrationHub).
3. **Set Up SSH Step**:
   - Define:
     - **Connection**: Use pre-configured credentials.
     - **Host**: Specify a target (e.g., a Linux machine via a mid-server).
     - **Command**: Hardcode a command (e.g., `ifconfig`) initially.
4. **Test the Action**:
   - Run the action within Flow Designer.
   - Review logs directly within the interface, including runtime and configuration details for target and command.

### Enhancing the Action with Inputs

1. **Add Inputs**:
   - Define input variables (e.g., `hostname` and `command`).
   - Replace hardcoded values in the SSH step with data pills linked to inputs.
2. **Test with Dynamic Inputs**:
   - Provide values for the inputs during testing (e.g., target hostname and command).
   - View runtime values in logs to verify correct execution.
3. **Add Output**:
   - Define an output variable (e.g., `SSH Output`) to capture results from the SSH step.
   - Use this output in other flows or subflows.

### Reusability of Flow Designer Actions

- **Dynamic Inputs**: Actions can dynamically receive hostnames, commands, and other parameters.
- **Outputs**: Results from actions can be leveraged in broader flows or subflows.
- **Integration**: Actions defined in Flow Designer can be embedded into larger workflows for enhanced process automation.

### Best Practices for Flow Designer Actions

- Start with hardcoded values to confirm functionality.
- Gradually introduce inputs and outputs for scalability and flexibility.
- Use Flow Designer's built-in logs and data panel to verify and debug configurations dynamically.

---

## Subflows

A Subflow is a reusable workflow element that can call actions, other subflows, or include flow logic. This example demonstrates creating a subflow that passes inputs to an action and executes it.

### Configuring a Subflow to Call an Action

#### Steps to Configure a Subflow with an Action

1. **Create the Subflow**:
   - Navigate to Flow Designer and click **+** to create a subflow.
   - Name the subflow (e.g., "Example Two Subflow") and click **Submit**.
2. **Define Subflow Inputs**:
   - Create input variables (e.g., `subflow_hostname` and `subflow_command`) for values to be passed into the subflow.
   - Save the inputs.
3. **Add the Action**:
   - Under the **Actions** section, select the previously created action (e.g., "Get Network Adapter Example One").
   - Assign the action's parameters:
     - Initially, hardcode values (e.g., IP address or command) to test functionality.
   - Save the subflow.
4. **Test the Subflow**:
   - Run the subflow and check the logs for results.
   - Review the output (e.g., `ifconfig` results) and confirm successful execution.

#### Enhancing the Subflow with Dynamic Inputs

1. **Link Subflow Inputs to the Action**:
   - Modify the action step to use subflow inputs (e.g., `subflow_hostname` and `subflow_command`) instead of hardcoded values.
   - Drag input data pills into the action's parameter fields.
2. **Test Dynamic Input Execution**:
   - Provide runtime values for the inputs during the test (e.g., an IP address and a command like `ls`).
   - Confirm:
     - Runtime values are passed to the action.
     - Output matches the expected result (e.g., `ls` results or `ifconfig`).

#### Logging and Debugging Subflows with Actions

- **Logging Features**:
  - Subflow logs display input, output, and runtime values.
  - Logs also detail execution specifics, such as:
    - MID server used.
    - Credentials leveraged.
    - Target host.
- **Troubleshooting**:
  - Errors occur if required inputs are not provided during execution.
  - Logs make it easier to identify missing or incorrect configurations.

#### Best Practices for Subflows with Actions

- Start with hardcoded values to verify functionality before introducing dynamic inputs.
- Use subflow inputs to make actions and subflows reusable and flexible.
- Utilize the built-in logging to debug and optimize workflows effectively.

### Configuring a Subflow to Call an Orchestration Workflow

Subflows in Flow Designer can call orchestration workflows, passing dynamic inputs and handling outputs. This process enables seamless integration between subflows and traditional workflows for targeted automation.

#### Steps to Configure the Subflow with an Orchestration Workflow

1. **Create or Copy a Subflow**:
   - Copy an existing subflow or create a new one to reuse inputs (e.g., `hostname` and `command`).
   - Save and ensure the subflow is properly configured.
2. **Add the Workflow to the Subflow**:
   - Under **Flow Logic**, choose **Call a Workflow**.
   - Ensure the target workflow is **published** and **contextual** in its properties.
   - Select the workflow and confirm it accepts the necessary parameters (e.g., `hostname`, `command`).
3. **Test with Hardcoded Values**:
   - Initially, pass hardcoded values to the workflow parameters (e.g., IP address, specific commands).
   - Execute the subflow and verify results:
     - View execution context and workflow activity history.
     - Check outputs, such as network adapter information or command results.
4. **Enhance with Subflow Inputs**:
   - Replace hardcoded values with input variables (e.g., `subflow_hostname` and `subflow_command`).
   - Map the inputs dynamically into the workflow parameters.
   - Test by providing runtime values for the inputs to confirm correct execution.

#### Capturing and Logging Results

1. **Log Workflow Outputs**:
   - Add a logging step to capture workflow outputs.
   - Access outputs (e.g., ScratchPad variables) returned by the workflow.
   - View results in logs to verify the success of the workflow and examine outputs like command results or error information.
2. **Access Execution Details**:
   - View execution state, credentials, and MID server details.
   - Examine inputs and outputs for runtime and configuration values.

#### Key Concepts

- **Workflow Context**: Provides a detailed record of the workflow execution, including activity history and execution details.
- **ScratchPad Variables**:
  - Used to store outputs like command results or error messages.
  - Available in JSON format for logging or further processing.

### Creating a UI Action to Call a Subflow

UI Actions provide the ability to trigger subflows directly from record forms, enabling users to execute commands or processes based on context-specific inputs.

#### Steps to Create a UI Action for a Subflow

1. **Build the Subflow**:
   - **Define Inputs**: Include a `sys_id` input to identify the record calling the subflow.
   - **Lookup Record**:
     - Use the `Lookup Record` action to find the record matching the `sys_id` provided.
   - **Call an Action**:
     - Use an action (e.g., SSH action) to execute commands.
     - Pass dynamic inputs (e.g., IP address and command) from the record fields.
   - **Update Record**:
     - Use an `Update Record` action to write results (e.g., action output) back to a specific field (e.g., comments or work notes).
   - **Test**:
     - Test the subflow by providing a `sys_id` and verifying the results.
2. **Publish the Subflow**:
   - Publish the subflow to generate a **code snippet** for triggering it:
     - Click **More Actions menu** (three vertical dots) > **Copy snippet**.
3. **Create the UI Action**: System Definitions > UI Actions > New
   - **Define Properties**:
     - **Name**: Assign a meaningful name (e.g., "Execute Subflow").
     - **Table**: Specify the target table (e.g., Linux Server or Incident).
     - **Type**: Choose button or form link as the UI action type.
   - **Insert Script**:
     - Paste the copied code snippet from the subflow.
     - Modify the script to dynamically pass the `sys_id` of the current record to the subflow input:
       - Replace the hardcoded `sys_id` with `current.getValue('sys_id');`.
4. **Test the UI Action**:
   - Access a record on the target table.
   - Trigger the UI action.
   - Verify that:
     - The subflow executes correctly using the record’s data.
     - Results are updated in the specified field (e.g., comments or work notes).

#### Use Cases Examples for UI Actions

1. **CI Record**:
   - **Scenario**: Execute commands like `ifconfig` against a Linux server.
   - **Steps**:
     - Use `sys_id` to find the server record.
     - Pass the server's IP address and a command (e.g., from a description field) to the action.
     - Write action output to the **comments** field.
2. **Incident Record**:
   - **Scenario**: ITIL users execute commands against devices linked to an incident’s configuration item (CI).
   - **Steps**:
     - Add a **command** field to the incident form for user input.
     - Use the incident’s CI to retrieve the target IP address.
     - Execute the command via the subflow.
     - Write results to the **work notes** field.

#### Best Practices for UI Actions with Subflows

- **Dynamic Inputs**: Ensure subflows dynamically use record-specific data to avoid hardcoding values.
- **Test Thoroughly**: Verify the subflow works with various record configurations and inputs.
- **Field Selection**:
  - Use meaningful fields for user inputs (e.g., `description` or custom fields like `command`).
  - Update relevant fields (e.g., `comments` or `work notes`) to reflect results.
- **Activate Subflows and UI Actions**: Ensure both are published and active in the system.

#### Summary for UI Actions with Subflows

- **Subflow Creation**:
  - Input: `sys_id`.
  - Actions: Lookup, execution (via action), and update.
- **UI Action**:
  - Links subflow to the record form.
  - Executes the subflow dynamically based on the record's `sys_id`.
- **Results**:
  - Automates command execution and writes results back to records, enhancing operational efficiency.
