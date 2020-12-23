import xml.etree.ElementTree as ET

def load_reports(file_path):
  tree = ET.parse(file_path)
  root = tree.getroot()
  return root
