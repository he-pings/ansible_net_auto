Video9 - Demo of Ansible Handlers 

This video describesa the use of Ansible Handlers. In this demo we modify the BGP policy which requires a reset of the
BGP neighbor. As Ansible is idempotent the BGP policy change will only applied if it doesnt already appear in the config.
Therefore we onbly want to clear the BGP neighbors if the config was changed. This is the function of ansible handlers. 
Handlers are just tasks that only run when Ansible makes a change, monitoring the Ansible "changed" variable. 


The config sections calls 3 tasks, to configure an ACL, a router-map and modify redistirubte OSPF on the BGP process. Each
tasks calls the handlers to 1) clear the bgp peers and 2) copy run start. These handler tasks are only run if any of the
main tasks results in a config change.

The ios_bgp module is used for the BGP config and imperative vs declarative (intent based) methodlogy is briefly discussed.
