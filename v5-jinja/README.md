Video5 - Ansible Router&Switch Config Deployment using Jinja2 Templates


The playbooks in this repo are part of my youtube network automation series. Video5 describes using Jinga2 templates to deploy BGP, OSPF Routing as well as VLAN config to Switches.

Playbooks:

1. fact_cache.yml - Gather facts and cache all facts into the fact_cache directory
2. gen_config.yml - Generate BGP, OSPF & VLAN Config using the template module and deploy using ios_config

