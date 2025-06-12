#!/usr/bin/python3
"""Adds arguments to a Python list and saves them to a file."""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if file exists, otherwise start fresh
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Append command-line args (excluding script name)
items.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(items, filename)
