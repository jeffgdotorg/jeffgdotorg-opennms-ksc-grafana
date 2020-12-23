#!/usr/bin/env python3

import snmp_graph
import ksc_report

sg = snmp_graph.load_graphs("/Users/jeffg/git/horizon-work/opennms-base-assembly/src/main/filtered/etc/snmp-graph.properties.d/")
#print(snmp_graph.get_attributes(sg, 'mib2.HCbits'))
#print(snmp_graph.get_vertical_label(sg, 'mib2.HCbits'))

ksc = ksc_report.load_reports("/Users/jeffg/Documents/clients/USPTO/2020/20201222_ksc_report_to_grafana/ksc-performance-reports.xml")
for report in ksc:
  print("Report: " + report.get("title"))
  for graph in report:
    print("\tGraph: " + graph.get("title"))
    print("\t\tAttributes: " + str(snmp_graph.get_attributes(sg, graph.get("graphtype"))))
