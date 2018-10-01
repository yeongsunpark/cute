#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re
import json

sys.path.insert(0,'..')

# input_dir = "/home/msl/ys/cute/law/data4"
# output_dir = "/home/msl/ys/cute/law/data4_out"

json_data = open("/home/msl/ys/cute/law/doc2text_2.json", "r")
d = json_data.read()
d = json.loads(d)
print (d['input_dir'])
json_data.close()
