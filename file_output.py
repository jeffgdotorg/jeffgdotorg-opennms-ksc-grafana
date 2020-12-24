#!/usr/bin/env python3

import re
import json

def write_to_file(output_dir, dash_dict):
  title = dash_dict['title']
  filename_pat = re.compile('( /:)')
  filename = filename_pat.sub('_', title) + '.json'
  with open(output_dir + '/' + filename, 'w') as file:
    file.write(json.dumps(dash_dict))
