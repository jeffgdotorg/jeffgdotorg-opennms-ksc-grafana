#!/usr/bin/env python3

import snmp_graph
import ksc_report
import grafana_dashboard
import file_output
#import grafana_api

g_url_base = "http://localhost:3000"
g_api_key = "eyJrIjoiRURGa25RSkpwTTlQYXQ2WVY2emZXMjFRb2VjQkFLcksiLCJuIjoicHl0aG9uLXB1c2hlciIsImlkIjoxfQ=="
output_dir = "./dashboards/"

sg = snmp_graph.load_graphs("/Users/jeffg/Documents/clients/USPTO/2020/20201222_ksc_report_to_grafana/snmp-graph.properties.d")
ksc = ksc_report.load_reports("/Users/jeffg/Documents/clients/USPTO/2020/20201222_ksc_report_to_grafana/ksc-performance-reports.xml")

for report in ksc:
  dash_dict = grafana_dashboard.empty_dashboard()
  grafana_dashboard.set_dashboard_title(dash_dict, 'SKELETON ' + report.get('title'))
  graphs_per_line = int(report.get('graphs_per_line')) if int(report.get('graphs_per_line')) > 0 else 1
  panel_width = 24 // graphs_per_line
  panel_height = 9
  panel_id = 1
  panel_x = 0
  panel_y = 0
  for graph in report:
    title = graph.get('title') + ' – ' + snmp_graph.get_title(sg, graph.get("graphtype"))
    description = snmp_graph.get_name(sg, graph.get("graphtype"))
    left_y_label = snmp_graph.get_vertical_label(sg, graph.get("graphtype"))
    resource = graph.get("resourceId")
    attributes = snmp_graph.get_attributes(sg, graph.get("graphtype"))
    expressions = snmp_graph.get_expressions(sg, graph.get("graphtype"))
    visible_vars = snmp_graph.get_visible_vars(sg, graph.get("graphtype"))
    new_panel = grafana_dashboard.graph_panel(panel_id, title, description, left_y_label, resource, attributes, expressions, visible_vars, panel_height, panel_width, panel_x, panel_y)
    panel_id += 1
    grafana_dashboard.append_panel(dash_dict, new_panel)
    if (panel_x + panel_width >= 24):
      panel_y += panel_height
      panel_x = 0
    else:
      panel_x += panel_width
  file_output.write_to_file(output_dir, dash_dict)
