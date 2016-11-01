#!/usr/bin/env python
#
# class 1 exe 7
#
import yaml
import json
from pprint import pprint as pp

with open("list_to_yaml_file.yml") as f:
    list_from_yaml = yaml.load(f)

for i in list_from_yaml:
    pp(i)

with open("list_to_jason_file.json") as f:
    list_from_json = json.load(f)

for i in list_from_json:
    pp(i)

