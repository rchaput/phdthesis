"""
Some common definitions that help us parse and analyse the experiments' results.
"""


import re

# Regex to get the run ID from its path
run_id_pattern = re.compile(r'.*/run_(\d+)/?')


def get_run_id(run_path):
    return int(run_id_pattern.match(run_path).group(1))
