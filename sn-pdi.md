# PDI Configuration

## TODO

- [ ]

## Resources

### Courses

- [ ]

### Links

- community: Provision your PDI or company/customer instances quicker, smarter:
  - [01 Setting-up your personal user account](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2288041)
  - [02 Recommended System Properties and User Preferences](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2288015)
  - [03 Favorite Favorites](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2287999)
  - [04 Applying Plugins](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2268118#:~:text=There%27s%20are%20always%20some%20plugins,plugin%20takes%20hours)
    - [second post: Activate plugin via script / automatically](https://www.servicenow.com/community/servicenow-ai-platform-forum/activate-plugin-via-script-automatically/m-p/1107124)
  - [05 Applying Utilities](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2287979)

### Labs

- []

## Scripting the PDI

### User Record Setup

- [01 Setting-up your personal user account](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2288041)

```js
var grUser = new GlideRecord("sys_user");
grUser.initialize();
grUser.setValue("user_name", "felix.miske");
grUser.setValue("first_name", "Felix");
grUser.setValue("last_name", "Miske");
grUser.setValue("preferred_language", "en");
grUser.setValue("time_zone", "Europe/Berlin");
grUser.setValue("date_format", "dd-MM-yyyy");
grUser.setNewGuidValue("felix.miske");
grUser.autoSysFields();
grUser.insert();
```

### System Properties and Preferences

- [02 Recommended System Properties and User Preferences](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2288015)

```js
(function () {
  var userSysId = gs.getUserID();
})();

var grUser = new GlideRecord("sys_user");
grUser.get(userSysId);

grUser.setValue("preferred_language", "en");
grUser.setValue("time_zone", "Europe/Amsterdam");
grUser.setValue("date_format", "dd-MM-yyyy");
grUser.update();

var grUserPreference = new GlideRecord("sys_user_preference");
grUserPreference.addQuery("user", userSysId);
grUserPreference.deleteMultiple();

var userpreferenceObj = [
  {
    name: "glide.ui.application_picker.in_header",
    value: "true",
  },
  {
    name: "glide.ui.update_set_picker.in_header",
    value: "true",
  },
  {
    name: "glide.ui.related_list_timing",
    value: "deferred",
  },
  {
    name: "rowcount",
    value: "100",
  },
  {
    name: "syslog.db.order.direction",
    value: "DESC",
  },
  {
    name: "syslog.db.order",
    value: "sys_created_on",
  },
  {
    name: "sys_update_xml.db.order.direction",
    value: "DESC",
  },
  {
    name: "sys_update_xml.db.order",
    value: "sys_updated_on",
  },
  {
    name: "com.glideapp.dashboards.homepage_notification.dont_ask_me_again",
    value: "true",
  },
  {
    name: "home_refresh",
    value: "off",
  },
  {
    name: "table.highlighting",
    value: "false",
  },
];

for (var i = 0; i < userpreferenceObj.length; i++) {
  var grUserPreference = new GlideRecord("sys_user_preference");
  grUserPreference.initialize();
  grUserPreference.setValue("user", userSysId);
  grUserPreference.setValue("name", userpreferenceObj[i].name);
  grUserPreference.setValue("value", userpreferenceObj[i].value);
  grUserPreference.insert();
}
```

### Favorites

- [03 Favorite Favorites](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2287999)

```js
var grBookmark = new GlideRecord("sys_ui_bookmark");
grBookmark.addQuery("user", userSysId);
grBookmark.deleteMultiple();

var grBookmarkGroup = new GlideRecord("sys_ui_bookmark_group");
grBookmarkGroup.addQuery("user", userSysId);
grBookmarkGroup.deleteMultiple();

var grBookmarkGroup = new GlideRecord("sys_ui_bookmark_group");
grBookmarkGroup.initialize();
grBookmarkGroup.setValue("title", "Development");
grBookmarkGroup.setValue("user", userSysId);
grBookmarkGroup.setValue("color", "normal");
grBookmarkGroup.insert();

var bookmarkObj = [
  {
    icon: "list",
    color: "green",
    title: "Customer Updates > Me, Last 7 days",
    url: "sys_update_xml_list.do?sysparm_query=sys_updated_by%3Djavascript&colon;gs.getUserName()%5Esys_updated_onONLast%207%20days%40javascript&colon;gs.beginningOfLast7Days()%40javascript&colon;gs.endOfLast7Days()",
  },
  {
    icon: "list",
    color: "green",
    title: "System Log > Today",
    url: "syslog_list.do?sysparm_query=sys_created_onONToday%40javascript&colon;gs.daysAgoStart(0)%40javascript&colon;gs.daysAgoEnd(0)",
  },
  {
    icon: "console",
    color: "red",
    title: "Background Script",
    url: "/sys.scripts.do",
  },
  {
    icon: "console",
    color: "red",
    title: "Fix Script",
    url: "/sys_script_fix.do?sys_id=-1",
  },
];

for (var i = 0; i < bookmarkObj.length; i++) {
  var grBookmark = new GlideRecord("sys_ui_bookmark");
  grBookmark.initialize();
  grBookmark.setValue("group", grBookmarkGroup.getUniqueValue());
  grBookmark.setValue("user", userSysId);
  grBookmark.setValue("icon", bookmarkObj[i].icon);
  grBookmark.setValue("color", bookmarkObj[i].color);
  grBookmark.setValue("order", i + 1);
  grBookmark.setValue("title", bookmarkObj[i].title);
  grBookmark.setValue("url", bookmarkObj[i].url);
  grBookmark.insert();
}
```

### Plugins

- sources:
  - [Applying Plugins](https://www.servicenow.com/community/developer-blog/provision-your-pdi-or-company-customer-instances-quicker-smarter/ba-p/2268118#:~:text=There%27s%20are%20always%20some%20plugins,plugin%20takes%20hours)
  - [Activate plugin via script / automatically](https://www.servicenow.com/community/servicenow-ai-platform-forum/activate-plugin-via-script-automatically/m-p/1107124)
  - [github](https://github.com/ServiceNowDevProgram/code-snippets/blob/main/Fix%20scripts/Install%20Base%20PDI%20Plugins/install_plugins.js)
- background script to enable plugins in PDI
  - potential plugins to enable:
    - `com.snc.i18n.german`

```js
// Change to "false" to avoid demo data with the plugins
var include_demo_data = true;

var plugins = [];

// Add or remove plugins by adding or removing plugins.push lines to the code below:

plugins.push("sn_store_agile_mob");
plugins.push("com.snc.i18n.german");

var main = new GlideMultiPluginManagerWorker();
main.setPluginIds(plugins);
main.setIncludeDemoData(include_demo_data);
//main.setLoadDemoDataOnly(true); // Can be used to install demo data after installation of plugins.
main.setProgressName("Plugin Installer");
main.setBackground(true);
main.start();

gs.info(
  "Plugin installation has been initiated, please note that installation runs in the background and can take some time."
);
gs.info(
  "Please visit the following URLs to monitor the state of the installed plugins."
);
gs.info(
  "The installation has finished when all the following plugins have reached State=Active."
);
gs.info(
  "https://" +
    gs.getProperty("instance_name") +
    ".service-now.com/nav_to.do?uri=%2Fv_plugin_list.do%3Fsysparm_query%3DidIN" +
    plugins.join(",")
);
gs.info(
  "A more detailed installation progress can also be seen in the Upgrade History log:"
);
gs.info(
  "https://" +
    gs.getProperty("instance_name") +
    ".service-now.com/nav_to.do?uri=sys_upgrade_history_list.do"
);
```
