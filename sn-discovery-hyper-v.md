# Hyper-V Discovery

## TODO

- [ ]

## Resources

### Courses

- [ ]

### Links

- [docs: Hyper-V discovery](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/discovery/reference/r_DiscoveryForHyperV.html)
- [KB0687582 How Discovery captures Model ID and Manufacturer for servers and devices](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687582)
-

### Labs

- []

## Doc Summary

Microsoft Hyper-V is a virtualization application included with Windows Server 2008. It divides a physical machine into multiple partitions (virtual machines), managed by the Hyper-V Manager application. This functionality extends across multiple versions of Hyper-V Server (2008, 2012, 2012 R2, 2016, 2019), with specific support for discovery using patterns in the latest versions.

## Key Features

- **Failover Clustering:** Managed with Failover Cluster Manager.
- **Live Migration:** Allows moving VMs between cluster nodes without downtime.
- **Discovery Support:** Available for Hyper-V Server versions from 2008 to 2019, with pattern-based discovery recommended for newer installations on Windows 2016.

## Configuration Requirements

- **Credentials:** Windows credentials with Domain administrator rights are necessary.
- **PowerShell:** Must be enabled on the MID Server used for discovering Hyper-V servers and instances.

## Discovery Tools

- **Classifiers, Probes, and Patterns:** Specific probes and patterns are designated for Hyper-V Servers, focusing on standalone servers not running on Windows 2008.
- Probes include:
  - Windows - ADM
  - Windows - Installed Software
  - Hyper-V specific probes for clusters, resource pools, virtual machines, and virtual networks.
    - Hyper-V - Cluster\*
    - Hyper-V - Resource Pools\*
    - Hyper-V - Virtual Machines\*
    - Hyper-V - Virtual Networks
- pattern: Hyper-V Server

## Data Collection

### Virtual Instances

Collected data includes Object ID, Name, State, CPUs, Memory, Network Adapters, Disks, and Virtual Serial Numbers, all stored in the `cmdb_ci_hyper_v_instance` table.

### Virtual Servers and Networks

Includes details like Name, Chassis Type, OS, Host Name, IP Address, and Virtual Status, stored in respective `cmdb_ci_hyper_v_server` and `cmdb_ci_hyper_v_network` tables.

### Resource Pools and Clusters

Data on resource pools includes Name, ID, Capacity, Allocation Units, and Resource Type, while clusters relate to the Windows Clusters they reside on.

## Relationships and Table Modifications

Discovery maps relationships between the host machine, virtual machines, networks, and other resources. It adjusts database tables to accommodate data from multiple virtualization products.

## Cloning Virtual Machines

Instructions are provided for cloning Hyper-V VMs, ensuring unique IDs for imported machines to avoid duplicates in Discovery.
