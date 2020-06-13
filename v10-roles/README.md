Video10 - Demo on Ansible Roles - A simple role to deploy vlans


The playbooks in this repo are part of my youtube network automation series. This video describes use of Ansible Roles.

What are Roles? A way to package a group of variables, tasks, j2 templates, automated testing etc. which can then be re-used or shared.

Creating Roles: Using the ansible-galaxy init <role-name> to create necessary role directory strcuture.

Playbooks:

1. switch-conf.yml - Main playbook used to call the deploy_vlans role

   Playbook includes a simple ios_command module to demonstrate that when using the "roles" module, roles will always run before tasks.

   First example simply calls the role using variaables stored in group_vars (vlans) and roles defaults (ospf vars).
   Second example demo's how to pass variable values when calling the role.
   Third example demonstrates use of the "include_role" module which allows looping through role with necessary variables. In this example vlans 50, 60 and 70 are all passed into the role.

Roles:

deploy_vlans role is stored in the playbook "roles" sub-directory.
