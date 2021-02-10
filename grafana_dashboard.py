#!/usr/bin/env python3

import re
from rpn_dict import jexl_for_rpn

def empty_dashboard():
  dash_dict = {}
  dash_dict['__inputs'] = [ { 'name': 'DS_OPENNMS-PM', 'label': 'opennms-pm', 'description': '', 'type': 'datasource', 'pluginId': 'opennms-helm-performance-datasource', 'pluginName': 'OpenNMS Performance' } ]
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

def graph_panel(panel_id, title, description, left_y_label, resource, attributes, expressions, visible_vars, height = 9, width = 12, x_loc = 0, y_loc = 0):
  ref_idx = 0
  resource_pat = re.compile('^node.*?\[(.*?)\]\.(\w+\[.*?\])$')
  node_id = None
  resource_id = None
  resource_mat = resource_pat.search(str(resource))
  if (resource_mat):
    node_id = resource_mat.group(1)
    resource_id = resource_mat.group(2)

  panel_dict = { 'aliasColors': {}, 'bars': False, 'dashLength': 10, 'dashes': False, 'datasource': '${DS_OPENNMS-PM}', 'description': description, 'fill': 1, 'fillGradient': 0, 'gridPos': { 'h': height, 'w': width, 'x': x_loc, 'y': y_loc }, 'hiddenSeries': False, 'id': panel_id, 'legend': { 'show': True, 'alignAsTable': True }, 'lines': True, 'lineWidth': 1, 'nullPointMode': 'null', 'options': { 'dataLinks': [] }, 'percentage': False, 'pointradius': 2, 'renderer': 'flot', 'seriesOverrides': [], 'spaceLength': 10, 'stack': False, 'steppedLine': False, 'targets': [], 'thresholds': [], 'timeFrom': None, 'timeRegions': [], 'timeShift': None, 'title': title, 'tooltip': { 'shared': True, 'sort': 0, 'value_type': 'individual' }, 'type': 'graph', 'xaxis': { 'buckets': None, 'mode': 'time', 'name': None, 'show': True, 'values': [] }, 'yaxes': [], 'yaxis': { 'align': False, 'alignLevel': None } }

  for bute in attributes:
    ref_id = 'A' + str(ref_idx)
    attr_label = get_label_for_var(bute[0], visible_vars, node_id, resource_id)
    do_hide = bute[0] not in visible_vars
    panel_dict['targets'].append( { 'type': 'attribute', 'attribute': bute[1], 'label': attr_label, 'nodeId': node_id, 'refId': ref_id, 'resourceId': resource_id, 'hide': do_hide } )
    panel_dict['yaxes'].append( { 'format': 'short', 'label': left_y_label if ref_id == 0 else '', 'logBase': 1, 'max': None, 'min': None, 'show': True } )
    ref_idx += 1

  ref_idx = 0
  for expr in expressions:
    ref_id = 'E' + str(ref_idx)
    expr_label = get_label_for_var(expr[0], visible_vars, node_id, resource_id)
    do_hide = expr[0] not in visible_vars
    panel_dict['targets'].append( { 'type': 'expression', 'label': expr_label, 'expression': jexl_for_rpn(expr[1]), 'refId': ref_id, 'hide': do_hide } )
    panel_dict['yaxes'].append( { 'format': 'short', 'label': left_y_label if ref_id == 0 else '', 'logBase': 1, 'max': None, 'min': None, 'show': True } )
    ref_idx += 1

  return panel_dict

def append_panel(dash_dict, panel_dict):
  dash_dict['panels'].append( panel_dict )
  return dash_dict

def get_label_for_var(var_name, visible_vars, node_id, resource_id):
  label_base = var_name
  if var_name in visible_vars:
    if 'label' in visible_vars[var_name]:
      label_base = visible_vars[var_name]['label']
      label_suffix = 'nodeToLabel(' + node_id + ')'
      if resource_id != 'nodeSnmp[]':
        label_suffix += ' :: resourceToLabel(' + node_id + ', ' + resource_id + ')'
      return label_base + ': ' + label_suffix
  else:
    return var_name
