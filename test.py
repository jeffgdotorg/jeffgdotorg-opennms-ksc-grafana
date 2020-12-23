#!/usr/bin/env python3

import json
import snmp_graph
import ksc_report
import grafana_dashboard

sg = snmp_graph.load_graphs("/Users/jeffg/git/horizon-work/opennms-base-assembly/src/main/filtered/etc/snmp-graph.properties.d/")
ksc = ksc_report.load_reports("/Users/jeffg/Documents/clients/USPTO/2020/20201222_ksc_report_to_grafana/ksc-performance-reports.xml")

for report in ksc:
  dash_dict = grafana_dashboard.empty_dashboard
  #grafana_dashboard.set_dashboard_title(dash_dict, report.get('title'))
  for graph in report:
    title = snmp_graph.get_name(sg, graph.get("graphtype"))
    description = snmp_graph.get_command(sg, graph.get("graphtype"))
    left_y_label = snmp_graph.get_vertical_label(sg, graph.get("graphtype"))
    resource = graph.get("resource")
    attributes = snmp_graph.get_attributes(sg, graph.get("graphtype"))
    new_panel = grafana_dashboard.graph_panel(title, description, left_y_label, resource, attributes)
    grafana_dashboard.append_panel(dash_dict, new_panel)
    print(json.dumps(dash_dict))
