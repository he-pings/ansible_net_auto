Video6 - Automated Testing with Ansible Assert


The playbooks in this repo are part of my youtube network automation series. Video6 describes using ansible to implement automated testing using the Ansible Assert module.

Playbooks:

branch_ping.yml
-rw-rw-r--. 1 daveyn daveyn  138 Apr 27 23:09 branch_vlans.yml
-rw-rw-r--. 1 daveyn daveyn  127 Apr 27 22:20 fact_cache.yml
-rw-rw-r--. 1 daveyn daveyn 1373 Apr 28 07:32 verify_bgp.yml
-rw-rw-r--. 1 daveyn daveyn  377 Apr 28 03:16 verify_br_ping.yml
-rw-rw-r--. 1 daveyn daveyn  669 Apr 28 03:18 verify_ospf.yml
-rw-rw-r--. 1 daveyn daveyn  729 Apr 28 03:02 verify_ping.yml

1. fact_cache.yml - Gather facts and cache all facts into the fact_cache directory
2. verify_bgp.yml - Assert that each BGP session is in an "Established" state
3. verify_ospf.yml - Run on Routers, assert that Site Switch IP appears in OSPF Neighbor Table
4. verify_ping.yml - Verify each Switch SVI via pinging -  
5. verify_br_ping.yml - Verifies Pings with an include_task module as you can only have 1 task in a loop
