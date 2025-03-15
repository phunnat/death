# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:57:46 2025

@author: natha
"""



import yaml
f = open(r"C:\Users\natha\Documents\GitHub\death\detections\rule_573.yml", "r")
f2 = open(r"C:\Users\natha\Documents\GitHub\death\detections\rule_574.yaml", "r")

content=f.read()

content2=f2.read()

# Convert to dictionary
parsed_dict = yaml.safe_load(content)
parsed_dict2 = yaml.safe_load(content2)

for key, value in parsed_dict.items():
    if key == "actions":
        if value == 'email':
            print("action is email")
    elif key == "qualifiedSearch":
        if value.contains("index"):
            print("index is specified")
        else:
            print("index is not specified")
    
    
parsed_dict['actions']
