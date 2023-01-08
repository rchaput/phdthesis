"""
This file is used as a helper to load the data profiles for the Smart Grid
use case.

Data profiles are stored as NumPy binary files, in the `data/` folder, e.g.,
`data/profile_office_annually.npz`.

This file contains a function that loads and parses such files to return a
profile:
- Array of need per hour
- Personal storage's capacity
- Maximum action range
"""

from collections import namedtuple
from pathlib import Path
import numpy as np
import pandas as pd


data_folder = Path(__file__).parent / '..' / 'data'

AgentProfile = namedtuple('AgentProfile', ['needs', 'action_limit', 'max_storage'])


def load_agent_profile(filename: str):
    profile_path = data_folder / f'{filename}.npz'
    profile = np.load(str(profile_path))
    needs = profile['needs']
    action_limit = profile['action_limit'][0]
    max_storage = profile['max_storage'][0]
    return AgentProfile(needs, action_limit, max_storage)
