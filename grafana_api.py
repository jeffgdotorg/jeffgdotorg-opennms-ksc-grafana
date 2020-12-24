#!/usr/bin/env python3

import json
import requests

def post_dashboard(g_url_base, g_api_key, dash_dict):
  post_url = g_url_base + "/api/dashboards/db"
  post_headers = { 'Authorization': 'Bearer ' + g_api_key, 'Content-type': 'application/json', 'Accept': 'application/json' }
  post_data = { 'dashboard': dash_dict, 'overwrite': True }
  resp = requests.post(post_url, headers=post_headers, data=json.dumps(post_data))
  return resp
