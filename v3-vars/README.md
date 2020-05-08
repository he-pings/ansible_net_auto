Video3 - Ansible - Using Variables, Lists and Dictionaries


The playbooks in this repo are part of my youtube network automation series. Video3 describes the use of variables,
lists and dictionaries. A simple NTP configuration playbook is used to demonstarte the use of each data construct. The video also discusses Ansible variable precedence inclduing use of host_vars versus group_vars.

Playbooks:

1. ntp_var.yml - deploy ntp config using simple scalr variables
2. ntp_list.yml - deploy ntp config using lists 
3. ntp_dict.yml - deploy ntp config using dictionaries
4. ntp_dict_hvgv.yml - deploy ntp config using dictionaries while demonstarting the host_vars and group_vars usage
