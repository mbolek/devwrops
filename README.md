# devwrops - DevOps Wroclaw Meetup #7 28.02.2017
**Prometheus 101**

This is the code used/created for the Meetup. It contains all the necessary details to run a basic, but full, prometheus stack:
- prometheus server
- alertmanager
- node_exporter (for system metrics)
- blackbox exporter (to test external system)
- redis + redis_exporter
- haproxy + haproxy_exporter
- cadvisor

To run you jest need to clone the repo and issue:
`vagrant up`

Then proceed to http://localhost:9090 for the prometheus interface or http://localhost:9093 for the alertmanager interface.
Grafana http://localhost:3000 with admin/admin

Tested with Ansible 2.1.1.0 and VirtualBox 5.1-5.1.14
