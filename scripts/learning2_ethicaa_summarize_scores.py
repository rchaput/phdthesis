
"""
This script is used to summarize the scores from the 'learning2'
(Ethicaa / Lajima) experiments.

It cannot be used without the original experiments data (located in
`../data/contribution2/remote/ethicaa`), but provided just in case to show
how data were processed to produce `ethicaa_scores.csv`.
"""

import os
from pathlib import Path
from glob import glob
import traceback

import pandas as pd

from scripts.common import get_run_id

# Paths to the different folders
data_dir = Path(__file__).parent.parent / "data" / "contribution2"
experiments_dir = data_dir / "remote" / "ethicaa"

# Variables that describe both our experiments and the file hierarchy
all_models = ['Q-DSOM-1', 'Q-SOM-1']
all_profiles = ['daily', 'annually']
all_sizes = ['small', 'medium']
all_rewards = ['affordability',
               'decremental',
               'default',
               'env_sustain',
               'inclusiveness',
               'supply_security']


def get_run_score(run_path):
    score_path = os.path.join(run_path, 'score.txt')
    with open(score_path, 'r') as f:
        return float(f.readline().strip())


def summarize_data():
    data = []
    for model in all_models:
        for profile in all_profiles:
            for size in all_sizes:
                for reward in all_rewards:
                    path = os.path.join(experiments_dir, model, profile, size, reward)
                    runs = glob(f'{path}/job_*/run_*/')
                    for run in runs:
                        try:
                            run_id = get_run_id(run)
                            run_score = get_run_score(run)
                            data.append({
                                'Model': model,
                                'ConsumptionProfile': profile,
                                'EnvironmentSize': size,
                                'JudgesConfiguration': reward,
                                'Run': run_id,
                                'Score': run_score,
                            })
                        except:
                            print(f'Error in path {run}')
                            traceback.print_exc()
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    df = summarize_data()
    result_file = data_dir / 'ethicaa_scores.csv'
    df.to_csv(result_file, index=False)
