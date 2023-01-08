"""
This script is used to summarize the scores from the 'learning1' experiments.

It cannot be used without the original experiments' data, but is provided
to show how data were processed to produce the `scores.csv` file.
"""

import os
from pathlib import Path
from glob import glob
import traceback

import pandas as pd

from scripts.common import get_run_id

# Paths to the different folders
data_dir = Path(__file__).parent / '..' / 'data/contribution1'
experiments_dir = data_dir / 'remote'

# Variables that describe both our experiments and the file hierarchy
all_models = ['DDPG', 'MADDPG', 'Q-DSOM-1', 'Q-SOM-1']
all_profiles = ['daily', 'annually']
all_sizes = ['small', 'medium']
all_rewards = ['equity', 'overconsumption', 'multiobj-prod', 'multiobj-sum',
               'adaptability1', 'adaptability2']


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
                                'RewardFunction': reward,
                                'Run': run_id,
                                'Score': run_score,
                            })
                        except:
                            traceback.print_exc()
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    df = summarize_data()
    result_file = data_dir / 'scores.csv'
    df.to_csv(result_file, index=False)
