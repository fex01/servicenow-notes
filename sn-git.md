# Git: Source Control & Collaborative Development

## Resources

### 📘 Courses

- [x] [Source Control Fundamentals](https://learning.servicenow.com/lxp/en/now-platform/source-control-fundamentals?id=learning_course_prev&course_id=e55406cc47fa7954db63fb25126d43dc)

## Content

### Source Control Basics

- **Definition**: Source control tracks and manages application changes over time.
- **Scope in ServiceNow**:
  - Application files include database tables, scripts, flows, ACLs, and more.
  - Managed via **Studio**, ServiceNow's IDE.
- **Benefits**:
  - 🗄️ **Backup**: Code is stored outside the platform
  - 📜 **Change Tracking**: View and compare historical changes
  - 📦 **Version Control**: Revert to previous versions
  - 🤝 **Parallel Development**: Multiple devs can work on the same app
  - 🧹 **Code Organization**: Separate in-progress and release-ready code
- **Key Git Terminology**:
  - **Repository**: Where source files live
  - **Remote repository**: Hosted Git (e.g., GitHub)
  - **Local repository**: Developer's Studio project
  - **Branch**: Parallel line of development
  - **Main**: Default or primary branch
- **Source Control vs Update Sets**:
  - Update Sets = traditional method (XML-based transport)
  - Source Control = modern method with:
    - Remote storage
    - Branching support
    - Conflict resolution tools
    - No need for XML files

### Initial Setup & Linking

- hands on: [Labs > Activity 1: Create the wish list application and link it to source control](#activity-1-create-the-wish-list-application-and-link-it-to-source-control)

1. **Generate an SSH public/private key pair**

   - Use an online tool or terminal to generate the key pair
   - Enables authentication between ServiceNow and GitHub
   - Keep the private key secure for later use in Studio

2. **Create a GitHub repository**

   - Create an empty repository on GitHub (no README or license)
   - Add the **SSH public key** to GitHub under _Settings > SSH and GPG Keys_
   - ✅ _Developer Tip: Name the GitHub repo the same as the application for easy identification_

3. **Create a new application in Studio**

   - In **ServiceNow Studio**, select **Create Application**
   - Provide a name and description, then open the app

   - Create credentials:
     - Navigate to **Connection & Credential Aliases**
     - Add a new record
     - **Name the credential record**
     - Create a **new credential** under the _Connections_ tab
     - Paste the **SSH private key** into the credential
     - Save and confirm the credential appears under _Connections_

4. **Link the application to source control**

   - Copy the **SSH URL** from the GitHub repository (under the _SSH_ tab)
   - In Studio:

     - Go to `Source Control > Link to Source Control`
     - Paste the URL and select **SSH** as the protocol
     - Submit to link the application to the repository

   - Confirmation:
     - A success message confirms linking
     - Source control **status icons** will appear:
       - In the _Select Application_ dialog (for all apps)
       - In the Studio footer (for the current application)

### Importing an Application from Source Control

Admins can import existing applications into a non-production instance using Studio.

- **Use case**: Continue development or testing of an application stored in a GitHub repository
- **How to import**:

  1. Copy the **SSH URL** from the GitHub repository
  2. Open **Studio**: `System Applications > Studio`
  3. In the **Select Application** dialog, choose **Import From Source Control**
  4. Complete the **Import Application** dialog:
     - **Network protocol**: Select `SSH`
     - **URL**: Paste the SSH repo link from GitHub
     - **Credential**: Choose the credential record with the SSH private key
     - **Branch**: Use `main` or any existing branch in the repo
     - **MID Server Name** _(optional)_: Use only if needed for connectivity
     - **Default Email** _(optional)_:
       - Pulls from `sys_user` email
       - Can manually define and apply to all committers

- Select **Import** to load the application into the current instance

### Committing Changes

- hands on: [Labs > Activity 2: Commit changes](#activity-2-commit-changes)
- Use `Source Control > Commit Changes` in Studio to save local changes to the remote GitHub repository
- If the **Commit Changes** option is disabled but changes exist, reload the Studio browser window
- Opens a **Select files to commit** dialog:
  - Lists changes by user (Update Sets)
  - Option to view all changes via **All Update Sets**
  - Displays selection ratio (e.g., `8 of 12` changes selected)
- After selecting files, click **Continue**
- In the **Confirm files to commit** dialog:
  - Review the selected application files
  - Enter a **Commit comment**
    - 💡 _Tip_: Use a standardized format (e.g., developer initials + summary)
- Click **Commit Files** to finalize the commit
- On successful commit, click **Close**
- Under the hood, this process performs multiple Git operations:
  - **Stages** the selected files
  - **Commits** them to the local repository
  - **Pushes** them to the remote repository

### Comparing Versions

- Developers can compare application file versions **before committing** changes to source control
- In the **Select files to commit to source control** dialog:

  - Select the **Compare** icon next to a file to open a comparison view

- The **Compare to Commit** window opens in a new tab or window:

  - **Commit Version**: Last version committed to the repository
  - **Current Version**: Modified version pending commit
  - Differences between the two are highlighted

- For Script and HTML fields:

  - The full content may not display inline
  - Select the **More details** icon for a **line-by-line comparison** dialog

- **Line-by-line comparison features**:

  - **Red dotted underline**: Text removed in the Current Version
  - **Green dotted underline**: Text added in the Current Version
  - **Blue highlights**: Lines modified or moved
  - **Left gutter**: Line numbers in the Commit Version
  - **Right gutter**: Line numbers in the Current Version
  - **Center gutter**: Visual diff of line alignment and change tracking

- Use the **Toggle Locked Scrolling** icon to enable/disable synchronized scrolling between the two versions

### Branch Management

- A **branch** is a set of code changes in a repository with a unique name
- Used to develop new features, create fixes, or experiment without impacting the main app
- Only one branch can be active per application in a ServiceNow instance

- **Branch lifecycle stages**:
  - **Commit**: Save work to the branch (multiple commits allowed)
  - **Pull**: Create a pull request in GitHub to request a review of branch changes
  - **Merge**: Integrate completed branch into the upstream (source) branch via GitHub
  - **Delete**: Remove the branch post-merge or to abandon work

#### Creating a Branch in Studio

- hands on: [Labs > Activity 3: Create a branch](#activity-3-create-a-branch)
- Open `Source Control > Create Branch`
- Enter a **Branch Name** (no spaces allowed)
- Select **Create Branch**
- On success, select **Close**
- ⚠️ If branch creation fails:
  - Check error message (e.g., invalid branch name with spaces)
  - Use **Back** to fix and retry

#### Viewing Branches in GitHub

- GitHub defaults to showing the **main** branch
- Use the **branch dropdown** to switch views
- When viewing a different branch:
  - GitHub compares it to `main`
  - Shows unique commits and files in that branch

#### Switching Branches in Studio

- Commit or stash all changes before switching
- Go to `Source Control > Switch Branch`
- Select the target branch > Click **Switch Branch**
- If uncommitted changes exist:
  - Choose to **Stash** or **Discard** before switching

#### Merging Changes

- hands on: [Labs > Activity 4: Merge changes](#activity-4-merge-changes)

- Merging moves changes from a development branch into another branch (typically `main`)
- The merge process begins with a **pull request** created in GitHub
- A pull request signals that work is ready for review and merge
- In GitHub:
  - Select the development branch
  - Click the **Contribute** link
  - Click **Open pull request**
  - On the pull request page, review the list of changed files
  - Update the pull request title (default is the most recent commit message)
  - Click **Create pull request**
- Developers can discuss the pull request in the **Conversation** tab
- Additional commits can be pushed to the branch while the pull request is open
- Once the pull request is ready and conflicts are resolved:
  - Click **Merge pull request**
  - Click **Confirm merge**
- GitHub will block the merge if there are unresolved conflicts
- After a successful merge, click **Delete branch** to clean up the feature branch
- To delete an **unmerged** or abandoned branch:
  - Go to the **Branches** tab in GitHub
  - Click the **Delete this branch** icon next to the target branch
- Deleting merged or unused branches helps keep the repository organized

### Applying Remote & Stashed Changes

- hands on: [Labs > Activity 5: Use stashed changes](#activity-5-use-stashed-changes)

- Use **Apply Remote Changes** in Studio to pull updates from the remote repository into the current (active) branch
- Changes apply only to the **active branch**
- Commit or stash any uncommitted changes before applying remote changes
- To apply:

  - Go to `Source Control > Apply Remote Changes`
  - In the dialog, click **Apply Remote Changes**
  - If uncommitted changes exist, Studio prompts to **stash** or **discard** them

- **Stashing** allows developers to temporarily save local changes without committing
- Stashing removes changes from the working branch but retains them locally for later reuse
- Stashes are not saved to the remote repository
- If the application is deleted or the instance wiped, **stashed changes are lost**
- Only users with `admin` or `source_control` roles can use stashing features
- To stash:

  - Go to `Source Control > Stash Local Changes`
  - Review the list of application files (stash includes all uncommitted changes)
  - Enter a **Stash Description**
  - Click **Stash Local Changes**, then click **Close**
  - ⚠️ Files cannot be stashed selectively — either all or none
  - 💡 _Tip_: Add detailed descriptions to help identify stashes later

- To **apply** a stash:

  - Go to `Source Control > Manage Stashes`
  - If the menu item is disabled, there are no stashes
  - In the **Manage Stashes** dialog, click **Apply** next to the target stash
  - On success, click **Close**

- After applying a stash:

  - Changes are locked to a stash-specific Update Set
  - To modify them, either:
    - Commit the changes
    - Or click the user link in the message to move them to your own Update Set

- Once stashed changes are committed, the stash can be safely deleted
- Applying a stash **does not** automatically delete it
- To delete a stash:
  - Go to `Source Control > Manage Stashes`
  - Click **Delete** next to the stash
  - Click **Delete Stash**
  - The dialog does not show stash contents — use date/time and descriptions to identify them
- Keeping the stash list clean improves usability and prevents confusion

### Working with Tags

- hands on: [Labs > Activity 6: Create a tag](#activity-6-create-a-tag)
- A tag is a fixed reference to a specific commit in an application's source control history
- Tags are typically used to mark release versions (e.g., `v1.0`) but can represent any known development point
- Developers can use tags to:
  - Return to a stable state
  - Create branches from specific versions (e.g., to fix a defect in `v1.0`)
- Only users with the `admin` or `source_control` role can create tags in Studio
- All desired changes must be committed before creating a tag
- To create a tag in Studio:
  - Open `Source Control > Create Tag`
  - Enter a **Tag Name** (no spaces allowed)
  - Click **Create Tag**, then **Close**
  - Tag is pushed to the remote repository automatically
- If tag creation fails (e.g., due to invalid name), an error message appears
  - Use **Back** to revise and retry with a valid tag name
- Tags are viewable in GitHub under the **Tags** tab on the **Code** page
- To use a tag as a starting point for new development:
  - Open `Source Control > Create Branch`
  - Use the **Create from Tag** field to base the new branch on a selected tag

### Collaborative Development

- Source control supports collaborative development in scoped applications by enabling:

  - Independent work through branches
  - Isolated fixes/enhancements via tags
  - Pre-merge collaboration using pull requests
  - Remote source availability for distributed teams
  - App movement across non-prod instances without Update Sets

- 🔀 Common development scenarios:

  - **Single instance, single developer**
    - Solo work; branches used for testing without impacting stable code
  - **Single instance, multiple developers**
    - One branch active at a time
    - Devs use personal Update Sets
    - One shared sign-in connects Studio to source control
    - Studio commits show ServiceNow user (not necessarily author)
    - Remote repo commits use source control user's identity
  - **Multiple instances, multiple developers**
    - Each instance can work on its own branch
    - Use `<instance_name>/branch-name` for clarity
    - Follow same commit behavior as single instance/multi-dev

- ⚠️ Conflicts occur when:

  - A remote change overlaps with a local one during Apply Remote Changes
  - A stashed change overlaps with current local edits

- 🛡️ Avoiding conflicts:

  - Files are locked when edited, shown as read-only to others
  - Warning displays the first editor's name
  - Options:
    - **View differences** between versions
    - **Edit in first updater's Update Set**
    - **Edit in current user's Update Set**
    - **Commit changes** before others modify
  - ➡️ Hands on: [### Activity 7: Avoid conflicts](#activity-7-avoid-conflicts)

- 🛠️ Resolving conflicts (Stash conflicts):
  - Listed in **Apply Stashed Changes** dialog
  - For each file, select an action:
    - **Take Stashed**: Use stash version, ignore current
    - **Discard Stashed**: Use current, ignore stash
    - **Save Merge**: Manually merge using Move Right, then save
  - Use **Manually Apply** link to compare and choose
  - Conflict must be marked as "Conflict Resolved" to proceed
  - All conflicts must be resolved before stash can be applied
  - ➡️ Hands on: [### Activity 8: Resolve conflicts](#activity-8-resolve-conflicts)

## Labs

### Activity 1: Create the Wish List application and link it to source control

**🎯 Goal:**  
Create a basic ServiceNow application (Wish List), configure source control authentication, and link the application to a GitHub repository using SSH.

---

1. **Generate SSH Key Pair**

   - Use an online tool or terminal
     - Algorithm: `ECDSA`
     - Key Size: `256`
     - Passphrase: `wishlist`
     - command: `ssh-keygen -t ecdsa -b 256 -f ~/tmp -N "wishlist"`
   - Copy the **public key** for GitHub and **private key** for Studio

2. **Add SSH Key to GitHub**

   - Log in to GitHub > Profile > **Settings**
   - Go to **SSH and GPG Keys** > click **New SSH key**
   - Title: `wishlist`  
     Key: _(Paste the public key)_
   - Click **Add SSH key**

3. **Create GitHub Repository**

   - Profile > Your Repositories > **New**
   - Repository name: `wishlist`
   - Description: `Wish List Now Platform Application`
   - select _Public_
   - Select **Add a README file**
   - Click **Create repository**

4. **Create Application in Studio**

   - Go to **System Applications > Studio**
   - Click **Create Application**
     - Name: `WishList`
     - Description: `Create personal wish lists`
   - Create a new role:
     - Name: `user`
   - Format: Select `Classic`
   - Create new table:
     - _Create table from scratch_
     - Fields:
       - **Item** (String, 125 chars, Mandatory)
       - **Requester** (Reference to `sys_user`, Mandatory)
     - Table Label: `Wish Item`
   - Complete Guided App Creator and go to **Studio**

5. **Create Credential Record**

   - In Studio: `Create Application File > Connection & Credential Aliases`
   - Name: `WishList`  
     Save (don’t submit)
   - Under _Connections_ tab > click **New**
     - Name: `WishList`
     - Credential: Create new > **SSH Private Key Credentials**
       - Name: `WishList`
       - Username: _(GitHub username)_
       - Password: _(GitHub password)_
       - SSH Passphrase: `wishlist`
       - SSH Private Key: _(Paste from step 1)_
     - Click **Submit**
   - In GitHub: Copy the **HTTPS URL** of the repo
   - Back in Studio: Paste into `Connection URL` field > Click **Submit**

6. **Link Application to Source Control**

   - In Studio > Open `WishList` app
   - Source Control > **Link to Source Control**
     - Network Protocol: `SSH`
     - URL: _(SSH URL from GitHub repo)_
     - Credential: `WishList`
     - Branch: `main`
     - Commit Comment: `Initial Wish List application commit`
   - Click **Link to Source Control**
   - Confirm success message > Click **Close**

7. **Verify in GitHub**
   - Go to the `wishlist` repo on GitHub
   - Refresh page to confirm app files are visible

---

### Activity 2: Commit Changes

**🎯 Goal:**  
Update the Wish List application's data model, compare file versions, and commit the changes to the connected GitHub repository.

---

1. **Update the Wish Item Table**

   - Open the `WishList` application in Studio
   - Navigate to `Data Model > Tables > Wish Item`
   - Add new fields:
     - **Quantity** — Type: `Integer`
     - **URL** — Type: `URL`
   - Set the **Item** field as the Display value
     - Double-click `Display` column for Item > Set to `true`
   - Click **Update** to save table changes

2. **Commit Changes to Source Control**

   - Go to `Source Control > Commit Changes`
   - Review the files listed in the **Select files to commit** dialog

3. **Compare Version Differences**

   - Click the **Compare** icon for:
     - `Wish Item.Item` Dictionary Entry (updated field)
     - `Wish Item.Quantity` Dictionary Entry (new field)
   - Close each comparison window after review

4. **Finalize the Commit**

   - Ensure all files are selected
   - Click **Continue**
   - Enter a Commit comment (e.g., `AB: Added Quantity and URL fields and made Item field the display value on Wish Item table`)
   - Click **Commit Files**
   - Click **Close** when the commit completes

5. **Verify in GitHub**
   - Open the `wishlist` repository on GitHub
   - Refresh the page if needed
   - Confirm that the latest commit message matches the one you entered

### Activity 3: Create a Branch

**🎯 Goal:**  
Create a development branch for the Wish List application, add a new field (Display name), commit the changes, and verify branch isolation between main and feature branches.

---

1. **Review the Application**

   - In the **main ServiceNow browser window** (not Studio), **reload the page** to ensure the newly created application is visible
   - Go to `Wish List > Wish Item > Create New`
     - Create two records with different Requester/Quantity values
     - Confirm records display in list view

2. **Create a Branch in Studio**

   - Open the `WishList` application in Studio
   - Go to `Source Control > Create Branch`
   - Enter **Branch Name**: `Add Display Name`
     - ⚠️ If rejected (due to spaces), use `AddDisplayName`
   - Click **Create Branch**
   - Click **Close**

3. **Add Display Name Field**

   - In Application Explorer, go to `Forms & UI > Forms > Wish Item [Default view]`
   - Drag a **String** field onto the form
   - Arrange the form layout as needed
   - Configure field:
     - Label: `Display name`
     - Name: `display_name`
     - Max length: `300`
     - Read Only: ☑️
   - Save the form
   - In the main ServiceNow window, verify the field appears on the form via `Wish List > Wish Item > All`

4. **Commit the Changes**

   - In Studio: `Source Control > Commit Changes`
   - Select all files > Click **Continue**
   - Commit comment: `<your initials>: Added Display name field`
   - Click **Commit Files**
   - Click **Close** after confirmation

5. **Verify the Commit in GitHub**

   - Open the `wishlist` repository in GitHub
   - Refresh the browser
   - Use the branch selector to switch to `AddDisplayName`
   - Confirm your latest commit appears in this branch

6. **Switch to Main Branch and Verify Isolation**
   - In Studio: `Source Control > Switch Branch`
   - Select `main` and click **Switch Branch**
   - Verify branch switch via the Studio footer
   - In `Data Model > Tables > Wish Item`, confirm **Display name** field does not exist
   - In the main ServiceNow window, open any record and confirm the **Display name** field is not present

---

### Activity 4: Merge Changes

**🎯 Goal:**  
Merge the `AddDisplayName` branch of the Wish List application into the `main` branch using GitHub, then apply the updated changes to the local ServiceNow Studio repository.

---

1. **Merge the Branch in GitHub**

   - In GitHub, click **Compare & pull request** for the `AddDisplayName` branch
   - On the **Open a pull request** page:
     - Review the list of changed files
     - Set pull request title: `Display name field added`
     - Click **Create pull request**
   - After GitHub confirms no conflicts:
     - Click **Merge pull request**
     - Click **Confirm merge**
   - Click **Delete branch** to remove `AddDisplayName`

2. **Apply Remote Changes in Studio**

   - In Studio: `Source Control > Apply Remote Changes`
   - In the dialog, click **Apply Remote Changes**
   - When successful, click **Close**

3. **Verify the Changes in Studio**
   - In Application Explorer: `Data Model > Tables > Wish Item`
   - Confirm the **Display name** field appears in the **Table Columns** list

### Activity 5: Use Stashed Changes

**🎯 Goal:**  
Create and stash local application changes, apply the stash to a different branch, and delete the stash after use.

---

1. **Create the Target Branch (UserExperience)**

   - Open the `WishList` application in Studio
   - Go to `Source Control > Create Branch`
   - Branch Name: `UserExperience`
   - Click **Create Branch**, then **Close**

2. **Create Another Branch for Incorrect Work (AddPurchaseDetails)**

   - Create a new branch: `AddPurchaseDetails`
   - In Studio: `Create Application File > Client Script`
   - Configure:
     - Name: `Wish Item Set Requester`
     - Table: `Wish Item`
     - UI Type: `All`
     - Type: `onLoad`
     - Description: `Set the Requester to the currently logged in user for new Wish Item records`
   - Replace script content with:

   ```js
   function onLoad() {
     if (g_form.isNewRecord()) {
       g_form.setValue("requester", g_user.userID);
     }
   }
   ```

   - Click **Submit**
   - Close the Client Script tab

3. **Stash the Change**

   - Go to `Source Control > Stash Local Changes`
   - Stash Description: `Wish Item Set Requester Client Script`
   - Click **Stash Local Changes**
   - Click **Close** on success

4. **Switch to Correct Branch and Apply the Stash**

   - Switch to `UserExperience` branch via `Source Control > Switch Branch`
   - Go to `Source Control > Manage Stashes`
   - Click **Apply** for the `Wish Item Set Requester Client Script` stash
   - Click **Close**
   - Verify the Client Script is available under `Client Development > Client Scripts`

5. **Commit the Change**

   - Go to `Source Control > Commit Changes`
   - Select all files > Click **Continue**
   - Commit Comment: `<your initials>: Added Wish Item Set Requester Client Script`
   - Click **Commit Files**, then **Close**

6. **Delete the Stash**
   - Go to `Source Control > Manage Stashes`
   - Click **Delete** for the `Wish Item Set Requester Client Script` stash
   - In the dialog, click **Delete Stash**
   - Click **Close Dialog**

### Activity 6: Create a Tag

**🎯 Goal:**  
Create a `v0.1` tag as a development checkpoint for the Wish List application and verify it in GitHub.

---

1. **Merge the UserExperience Branch**

   - In GitHub, switch to the `UserExperience` branch
   - Click the **Contribute** link > Select **Open pull request**
   - Name the pull request (e.g., `Merge UX for 0.1 release`)
   - Click **Create pull request**
   - Click **Merge pull request**, then **Confirm merge** and **Delete branch**

2. **Switch to the Main Branch in Studio**

   - Open the `WishList` application in Studio
   - Go to `Source Control > Switch Branch`
   - Select the `main` branch > Click **Switch Branch**
   - On success, click **Close**

3. **Create a Tag**

   - Go to `Source Control > Create Tag`
   - Tag Name: `v0.1` (no spaces allowed)
   - Click **Create Tag**
   - On success, click **Close**

4. **Verify the Tag in GitHub**
   - Open the `wishlist` repository on GitHub
   - On the **Code** tab, click the **Tags** link
   - Confirm that `v0.1` appears in the list of tags

### Activity 7: Avoid Conflicts

**🎯 Goal:**  
Demonstrate how Studio handles concurrent development and avoids conflicts through Update Set ownership.

---

1. **Impersonate Fred Luddy and Create a Branch**

   - In the main ServiceNow window, impersonate **Fred Luddy**  
     (`User menu > Impersonate user > Fred Luddy`)
   - Open the `WishList` application in Studio  
     (`All > System Applications > Studio`)
   - Go to `Source Control > Create Branch`
   - Configure the branch:
     - **Branch Name:** `ConflictTesting`
     - **Create from Tag:** `v0.1`
   - Click **Create Branch** > **Close**

2. **Create Two Business Rules as Fred**

   - **Validate Quantity**
     - Table: `Wish Item`
     - _Advanced_
     - When:
       - `before`
       - `insert`
       - `update`
     - Condition: `Quantity less than or is 0`
     - Action: `Abort action`
   - **Populate Display name**

     - Table: `Wish Item`
     - _Advanced_
     - When:
       - `before`
       - `insert`
       - `update`
     - Condition (Advanced):
       `current.item.changes() || current.requester.changes() || current.operation() == 'insert'`
     - Script:

       ```js
       (function executeRule(current, previous /*null when async*/) {
         // Calculate Display name value by listing the item followed by the
         // User in parentheses. For example, Pencils (Fred Luddy)

         current.display_name =
           current.item + " (" + current.requester.name + ")";
       })(current, previous);
       ```

3. **Impersonate Carol Coughlin and Update Validate Quantity**

   - Impersonate **Carol Coughlin**  
     (`User menu > Impersonate user > Carol Coughlin`)
   - Open `All > Update Sets > Local Update Sets`
   - Create a new Update Set:
     - **Name:** `Carol Coughlin`
     - **Application:** `WishList`
     - **State:** `In Progress`
     - **Submit and Make Current**
   - Open the `WishList` app in Studio
   - Open **Validate Quantity**
   - In warning message, click **Carol Coughlin** link
   - Actions:
     - _Add message_ `Please add a quantity greater than zero`
   - Click **Update**

4. **Update Populate Display name in Fred’s Update Set**

   - Open **Populate Display name**
   - In warning, click **Fred Luddy** link
   - Update condition:  
     `... || current.quantity.changes()`
   - Replace script with:

     ```js
     (function executeRule(current, previous /*null when async*/) {
       // Calculate Display name value by listing the item followed by the
       // Quantity in parentheses, a dash, and then the Requester
       // For example, Comic Boxes (10) - Fred Luddy

       current.display_name =
         current.item +
         " (" +
         current.quantity +
         ") - " +
         current.requester.name;
     })(current, previous);
     ```

   - Click **Update**

5. **Review Commit Changes and Cancel**

   - Open `Source Control > Commit Changes`
   - Review Update Set assignments
   - Click **Cancel**

### Activity 8: Resolve Conflicts

**🎯 Goal:**  
Intentionally create conflicts between stashed and modified Business Rules and resolve them using Studio's conflict resolution tools.

---

1. **Stash and Apply Original Business Rules**

   - Reload the ServiceNow window
   - If not already impersonating, impersonate **Carol Coughlin**
   - Open the `Wish List` application in **Studio**
   - Go to `Source Control > Stash Local Changes`
     - **Stash Description:** `Original Populate and Validate Business Rules`
   - Click **Stash Local Changes**, then **Apply Stashed Changes**, then **Close**

2. **Modify Business Rules**

   - **Validate Quantity**

     - Open `Server Development > Business Rules > Validate Quantity`
     - Set:
       - **Order:** `50`
       - **Condition:** `Quantity less than 1`
     - Click **Update**

   - **Populate Display name**

     - Open `Server Development > Business Rules > Populate Display name`
     - If prompted, click **Carol Coughlin** to edit
     - In the Script field, add a comment with any text
     - Click **Update**

   - Close both Business Rule tabs

3. **Apply Stashed Changes and Resolve Conflicts**

   - Go to `Source Control > Manage Stashes`
   - Click **Apply** for the stash: `Original Populate and Validate Business Rules`
   - In the **Apply Stashed Changes** dialog:
     - For `Validate Quantity`, click **Manually Apply**
     - Review the differences and click **Discard Stashed**
     - For `Populate Display name`, set Action to **Take Stashed Changes**
   - Click **Apply Stashed Changes**, then **Close**

4. **Verify Conflict Resolution**

   - Open `Validate Quantity` in Application Explorer
     - Confirm the **Order** and **Condition** match the modified version
   - Open `Populate Display name`
     - Confirm the added comment is no longer present in the Script
