#!/usr/bin/env python
#
#
import yaml
import json

my_list = range(8)
my_list.append('hello')
my_list.append('test')
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.123'
my_list[-1]['device'] = 'router'
my_list[-1]['IOS'] = '15.1(5)'

with open("list_to_yaml_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("list_to_jason_file.json", "w") as f:
    json.dump(my_list, f)


