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
