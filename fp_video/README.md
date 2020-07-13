The plays in this branch refer to 2 of my youtube video's:

1. "Jinja filer plugins incld ttp"
2. "Jinja Macro - QOS report using TTP template"


Video 1 above describes creating custom filter_plugins. The first example simply passes the output of "show version"
into the filter_plugin python class and returns an interface number depending to router model type. Thje returned value
is saved to a custom fact called wan_interface. This fact can be called in any task or template for the current host.

The second example in video 1 describes integrating the TTP module into a custom filter_plugin. TTP can be used to create
structured data from unstructured show commands. In this example I create a TTP template to generate structured QoS data
from "show run | section policy-map" commands, using TTP templates.

Video2 continues from video2 by interrogating the generated QoS structured data to generate a QoS report. As QoS bandwidth
values can be in percentage, kbps or bps form we need to re-calculate the values to 1 common form. A jinja macro is used
for this purpose, it takes as input either a percentage or kbps value and returns a bps value. The generated report is in
csv format that allows opening in excel.
