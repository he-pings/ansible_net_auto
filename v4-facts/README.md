Video4 - Ansible Facts and Fact Caching


The playbooks in this repo are part of my youtube network automation series. Video4 describes the gathering of facts and the benefits of fact caching. 

Playbooks:

1. ios_facts.yml - Gather facts using the ios_facts network module
2. fact_cache.yml - Gather facts and cache all facts into the fact_cache directory
3. verify_nei.yml - Display BGP Neighbor IP Address using the fact Cache
4. verify_nei_nocache.yml - Gather Facts before diplaying BGP Neighbor IP, demonstarting how the fact gatherings slows the playbook run.

Playbook 3 & 4 and run using the time command to demonstrate the speed difference for example:


time ansible-playbook -i hosts verify_nei.yml 
