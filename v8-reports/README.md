Video8 - Simple Report Generation using Ansible with set_fact & textfsm library

This video describes troubleshooting a BGP MTU issue, where a BGP peer cannot determine the correct MTU due to a 
carrier Layer 2 dot1tunnel network being in the path. This cause the BGP peering to reset every holdtime interval.

The objective of the video is to run a report to determine the state of all BGP peerings to undertsanding the following:

	1. BGP State - Established , IDLE 
        2. BGP negotiated Maximum Segment Size
        3. BGP uptime - checking if any neighbors have an uptime of less than 5 minutes.


The following playbooks are discussed:

1-bgp-MSS.yml - shows how to determine BGP MSS using show ip bhp nei and storing the byte value as a custom fact, using 
                set_fact. This new custom fact then can be used in reports. Also shows why not all show commands are easy
                to parse. Python split is used to pinpoint the MSS byte size from the show command output.

2-check_bgp   - Introduces the textfsm library with Network-to-Codes templates, allowing us to simply parse ios commands
                without having to use comoplex regex statements. Uses jinja2 to generate a per device csv file and the
                ansible assemble module to collate all device csv files into one report. As a csv file the report can then
                be opened in excel. 
