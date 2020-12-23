#!/usr/bin/env python3

import re
from pathlib import Path
from jproperties import Properties

def load_graphs(props_dir):
  pd = Path(props_dir)
  props = Properties()
  for this_file in pd.iterdir():
    if (this_file.is_file()):
      with open(this_file, "rb") as f:
        props.load(f, "utf-8")
        props.reset()
  return props

def get_name(props, graph_name):
  return _get_graph_prop(props, graph_name, 'name')

def get_attributes(props, graph_name):
  pat = re.compile('\s*,\s*')
  vals = _get_graph_prop(props, graph_name, 'columns')
  if (vals is None):
    return []
  return pat.split(vals)

def get_resource_type(props, graph_name):
  return _get_graph_prop(props, graph_name, 'type')

def get_vertical_label(props, graph_name):
  pat = re.compile('\s+--vertical-label="(.*?)"\s+')
  graph_cmd = _get_command(props, graph_name)
  if (graph_cmd is None):
    return None
  mat = pat.search(graph_cmd)
  if mat:
    return mat.group(1)

def _get_command(props, graph_name):
  return _get_graph_prop(props, graph_name, 'command')

def _get_graph_prop(props, graph_name, sub_prop):
  key = str('report.' + graph_name + '.' + sub_prop)
  if (key in props):
    return props[key].data
  else:
    return None
