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
  attrs = []
  pat = re.compile('DEF:(\S+)={rrd\d+}:(\S+):')
  graph_cmd = get_command(props, graph_name)
  if (graph_cmd is None):
    return []
  return re.findall(pat, graph_cmd)

def get_resource_type(props, graph_name):
  return _get_graph_prop(props, graph_name, 'type')

def get_vertical_label(props, graph_name):
  pat = re.compile('--vertical-label="(.*?)"')
  graph_cmd = get_command(props, graph_name)
  if (graph_cmd is None):
    return None
  mat = pat.search(graph_cmd)
  if mat:
    return mat.group(1)

def get_title(props, graph_name):
  pat = re.compile('--title="(.*?)"')
  graph_cmd = get_command(props, graph_name)
  if (graph_cmd is None):
    return None
  mat = pat.search(graph_cmd)
  if mat:
    return mat.group(1)

def get_expressions(props, graph_name):
  exprs = []
  pat = re.compile('CDEF:(\S+)=(\S+)\s+')
  graph_cmd = get_command(props, graph_name)
  if (graph_cmd is None):
    return []
  return re.findall(pat, graph_cmd)

def get_visible_vars(props, graph_name):
  vars = {}
  pat = re.compile("""(AREA|LINE.?|STACK):(\w+)#([0-9A-Fa-f]+):["'](.*?)["']""")
  graph_cmd = get_command(props, graph_name)
  if (graph_cmd is None):
    return {}
  for vv_mat in pat.finditer(graph_cmd):
    vars[ vv_mat.group(2) ] = { 'type': vv_mat.group(1), 'var': vv_mat.group(2), 'color': vv_mat.group(3), 'label': str(vv_mat.group(4)).strip() }
  return vars

def get_command(props, graph_name):
  return _get_graph_prop(props, graph_name, 'command')

def _get_graph_prop(props, graph_name, sub_prop):
  key = str('report.' + graph_name + '.' + sub_prop)
  if (key in props):
    return props[key].data
  else:
    return None
