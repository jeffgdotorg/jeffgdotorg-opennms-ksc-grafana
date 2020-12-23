#!/usr/bin/env python3

import re

def empty_dashboard():
  dash_dict = {}
  dash_dict['__inputs'] = [ { 'name': 'DS_OPENNMS-PM', 'label': 'opennms-pm', 'description': '', 'type': 'datasource', pluginId: 'opennms-helm-performance-datasource', pluginName: 'OpenNMS Performance' } ]
  dash_dict['__requires'] = [ { 'type': 'grafana', 'id': 'grafana', 'name': 'Grafana', 'version': '6.7.5' }, { 'type': 'panel', 'id': 'graph', 'name': 'Graph', 'version': '' }, { 'type': 'datasource', 'id': 'opennms-helm-performance-datasource', 'name': 'OpenNMS Performance', 'version': '1.0.0' } ]
  dash_dict['editable'] = True
  dash_dict['gnetId'] = None
  dash_dict['graphTooltip'] = 0
  dash_dict['id'] = None
  dash_dict['links'] = []
  dash_dict['panels'] = []
  dash_dict['schemaVersion'] = 22
  dash_dict['style'] = 'dark'
  dash_dict['tags'] = []
  dash_dict['templating'] = { 'list': [] }
  dash_dict['time'] = { 'from': 'now-7d', 'to': 'now' }
  dash_dict['timepicker'] = { 'refresh_intervals': [ '5s', '10s', '30s', '1m', '5m', '15m', '30m', '1h', '2h', '1d' ] }
  dash_dict['timezone'] = ''
  dash_dict['title'] = 'SKELETON New dashboard'
  dash_dict['uid'] = None
  dash_dict['variables'] = { 'list': [] }
  return dash_dict

def set_dashboard_title(dash_dict, title):
  dash_dict['title'] = title

def graph_panel(title, description, left_y_label, resource, attributes):
  ref_idx = 0
  resource_pat = re.compile('^(node.*?\[.*?\])\.(\w+\[.*?\])$')
  node_id = None
  resource_id = None
  resource_mat = resource_pat.search(str(resource))
  if (resource_mat):
    node_id = resource_mat.group(1)
    resource_id = resource_mat.group(2)

  panel_dict = { 'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_OPENNMS-PM}', 'description': description, 'fill': 1, 'fillGradient': 0, 'gridPos': { 'h': 9, 'w': 12, 'x': 0, 'y': 0 }, 'hiddenSeries': False, 'id': None, 'legend': {}, 'lines': True, 'lineWidth': 1, 'nullPointMode': 'null', 'options': { 'dataLinks': [] }, 'percentage': False, 'pointradius': 2, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': title, 'tooltip': { 'shared': True, 'sort': 0, 'value_type': 'individual' }, 'type': 'graph', 'xaxis': { 'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': [] }, 'yaxes': [], 'yaxis': { 'align': False, 'alignLevel': None } }

  for bute in attributes:
    ref_id = 'A' + str(ref_idx)
    ref_idx += 1
    panel_dict['targets'].append( [ { 'attribute': bute, 'label': '', 'nodeId': node_id, 'refId': ref_id, 'resourceId': resource_id, 'type': 'attribute' } ] )
    panel_dict['yaxes'].append( [ { 'format': 'short', 'label': left_y_label if ref_id == 0 else '', 'logBase': 1, 'max': None, 'min': None, 'show': True } ] )

  return panel_dict

def append_panel(dash_dict, panel_dict):
  dash_dict['panels'].append( panel_dict )
  return dash_dict
