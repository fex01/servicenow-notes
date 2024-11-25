# Flows

## TODO

- [ ]

## Resources

### Expanded Notes

- [Flow Designer](./sn-flow-designer.md)

### Courses

- [x] [Configure Orchestration, Flow Designer, and Integration Hub](https://nowlearning.servicenow.com/lxp/en/it-operations-management/configure-orchestration-flow-designer-and?id=learning_course_prev&course_id=4f63e5f7db3f4010785e2a59139619a7)
  - [Orchestration Workflow](#orchestration-workflow)
  - [Flow Designer](./sn-flow-designer.md)

### Links

- [Docs](https://docs.servicenow.com/)
- [Developer](http://developer.servicenow.com/)
- [CSC (Customer Success Center)](https://www.servicenow.com/success.html)
- [Community](https://www.servicenow.com/community/)
- [YouTube](https://www.youtube.com/user/servicenowinc)
- [Center of Excellence and Innovation (CoEI)](https://www.servicenow.com/success/playbook/center-excellence-innovation-coei.html)

### Labs

- []

## Topics

### Orchestration Workflow

Orchestration workflows execute tasks (e.g., commands) against specific targets, leveraging inputs and variables for dynamic execution.

#### Workflow Steps

1. **Run Command Activity**:
   - **Hardcoded Example**:
     - Target hostname and command are predefined.
     - Results are stored in a variable (e.g., `output`) and passed to `ScratchPad`.
   - **Execution**:
     - Click **Start** to execute the workflow.
     - Results can be verified in the ECC Queue (e.g., command output like `ifconfig`).
2. **Using Input Variables**:
   - Define variables to make the workflow dynamic.
   - Example: Replace hardcoded hostname with a hostname input variable.
   - Steps:
     1. Define an input under **Edit Inputs** (e.g., hostname, command).
     2. Use inputs during execution by providing values dynamically (e.g., IP address or command).
3. **Modifying Workflows**:
   - Add new inputs (e.g., `command` variable) to make workflows flexible.
   - Inputs can be used to:
     - Change target IP addresses.
     - Modify commands dynamically.
   - Verify execution results in the ECC Queue.

#### Best Practices for Orchestration Workflows

- Start with hardcoded values to ensure target reachability and expected results.
- Gradually introduce input variables to scale and make workflows more dynamic.
- Test workflows thoroughly to confirm successful execution and accurate results.

#### Key Concepts for Orchestration Workflows

- **Inputs and Variables**: Allow dynamic customization of workflows.
- **ECC Queue**: Central location for verifying input records and execution results.
- **Scaling**: Use inputs to adapt workflows for various targets and commands.

---
