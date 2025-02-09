# SNow Tricks

## To Sort

- [Pricing](https://partnerportal.service-now.com/kb?id=kb_article_view&sysparm_article=KB0011614&campid=146442&cid=e:eDM-PTR-Vancouver.email09%2F20-20SEP23-Global.Email1&utm_source=marketo&utm_medium=email&utm_campaign=eDM-PTR-Vancouver.email09%2F20-20SEP23-Global.Email1&mkt_tok=MDg5LUFOUy02NzMAAAGOUkyKeFE825UAMvR_MneTnj2Dk6GBSFzu2c0v_qgvsd_4UuP4FO3IkQxYGIRSFH6RgeVLpDO2QGqVsPyNMm4PRrlp64a74AlJADleRYujDiRlgkB4&sys_kb_id=6dbeca678795bd50de17ea473cbb3510&spa=1)
  - overview decks
  - gezielte decks pro module
  - capability übersicht

## Resources

- [Data Models](https://www.snow-mirror.com/wp-content/uploads/2016/07/ServiceNow-Data-Model-v3.4.pdf)

## Filter Navigator

- `sys_user.list` - open table
- `sys_user.form` - form view for new record
- `sys_user.config` - configuration view
- `sys_user.filter` - does not load records before filter criteria are defined (use for large tables)
- `LIST` / `FORM` / `CONFIG` - open in new tab

## Search

- `*` + search-term - contains
- `%`+ search-term - ends with
- search-term + `%` - starts with
- `=` + search-term - equals
- `!*` + search-term - does not contain
- `!=` + search-term - does not equal

## Utility URLs

- more at [docs](https://docs.servicenow.com/csh?topicname=navigate-using-url.html&version=latest)
- `side_door.do` - to circumvent external login provider (SSO) for troubleshooting
- `/stats.do` - Stats and Info for the current node
  - Instance Version
- `/xmlstats.do` - Same as `stats.do` but formatted as XML
- `/thread_pool_stats.do` - Thread queue depth and AMB queue
- `/sn_agent_workspace_stats.do` - Agent workspace build and component versions
- `/cancel_my_transaction.do` - Name says it all
- `/side_door.do` - Bypass SSO redirect and go to `login.do`
- `/logout.do` - Immediately log out
- `/cache.do` - Flush all the caches (Do not do on customer instance without approval!)
  - `sys_db_cache` - Database-backed cache records are stored here.
  - `sys_cache_flush` - Cache flushes are written here to sync cache flushing across nodes.

## Keyboard Shortcuts

### Default

| Shortcut         | Action        |
| ---------------- | ------------- |
| `CTRL + ALT + G` | Global Search |
| `CTRL + ALT + C` | All >         |
| `CTRL + ALT + F` | All > Filter  |
| `CTRL + ALT + I` | Impersonate   |

### SNow Studio

| Shortcut          | Action         |
| ----------------- | -------------- |
| `CMD + SHIFT + O` | Go To `<file>` |
| `CMD + SHIFT + C` | Create New     |
| `CMD + SHIFT + F` | Code Search    |
| `/u` + name       | User           |

### Syntax Editor Shortcuts

| Action                           | Shortcut                                |
| -------------------------------- | --------------------------------------- |
| Display a list of valid elements | `Ctrl + Spacebar`                       |
| List methods for a class         | Enter a period after a valid class name |
| Help                             | `Ctrl` (`Cmd`) + `H`                    |
| Format selected code             | `ALT` (`Cmd`) + `Shift` + `F`           |
| Toggle comment                   | `Ctrl` (`Cmd`) + `/`                    |
| Insert macro text                | Type a macro keyword and press `Tab`    |
| Start search                     | `Ctrl` (`Cmd`) + `F`                    |
| Find next                        | `Enter`                                 |
| Find previous                    | `Shift` + `Enter`                       |
| Replace                          | `Ctrl` (`Cmd`) + `F`                    |
| Replace all                      | `Ctrl` (`Cmd`) + `F`                    |
| Display Syntax Editor Macros     | Type `help` and press `Tab`             |

### Client Script Tester Shortcut

| Shortcut           | Action                        |
| ------------------ | ----------------------------- |
| `Ctrl + Shift + J` | Client Script Tester Shortcut |

## Dictionary Info

Form > right-click Label > Show ‘Field Name’

## What is licensed?

Subscription Management

## Roles

- Which roles contain a specific subrole?
  - `sys_user_role_contains.list`
    - Search for subrole in column `Contains`
- Which user has a specific role?
  - `sys_user_role.list` > open _role_ record > Related List Users

## Manually Set a Password

[Password Policy Properties](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/integrate/authentication/reference/password-policy-properties.html)

## Check Customizations

- [community: How to trace customizations in ServiceNow?](https://www.servicenow.com/community/now-platform-forum/how-to-trace-customizations-in-servicenow/m-p/3008258)
  - check `sys_metadata_customization`
  - check `sys_update_xml`
