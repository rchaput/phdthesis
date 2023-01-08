"""
This script is used to get detailed data about experiments from the 'learning1'.

Unfortunately, it cannot be used as-is because it relies on the Smart Grid
simulator (located in `/Users/rchaput/PhD/Code`) and experiments data
(located in `../data/contribution1/remote/`).
It is provided just in case, to show how the experiments data were processed
to produce `agents_details.pkl.xz`.

Detailed data include:
- rewards per agent at each time step
- properties (comfort, equity, ...) about agents at each time step
- etc.
"""

import os
from pathlib import Path
from glob import glob
import sys
import traceback

import pandas as pd
from tqdm import tqdm

from scripts.common import get_run_id

sys.path.insert(0, '/Users/rchaput/PhD/Code')
from src.simulator import Simulator

# Paths to the different folders
data_dir = (Path(__file__).parent / '..' / 'data/contribution1').resolve()
print(f'Data dir = {data_dir}')
experiments_dir = data_dir / 'remote'
print(f'Experiments dir = {experiments_dir}')

# Variables that describe both our experiments and the file hierarchy
all_models = ['DDPG', 'MADDPG', 'Q-DSOM-1', 'Q-SOM-1']
all_profiles = ['annually']
all_sizes = ['small']
all_rewards = ['equity', 'overconsumption', 'multiobj-prod', 'multiobj-sum',
               'adaptability1', 'adaptability2']


def get_details():
    data = []
    for model in tqdm(all_models, position=0):
        for profile in tqdm(all_profiles, position=1):
            for size in tqdm(all_sizes, position=2):
                for reward in tqdm(all_rewards, position=3):
                    path = os.path.join(experiments_dir, model, profile, size, reward)
                    runs = glob(f'{path}/job_*/run_*/')
                    for run in tqdm(runs, position=4):
                        try:
                            run_id = get_run_id(run)
                            sim = Simulator.load(os.path.join(run, 'data.pkl.bz'))
                            for num_step, step in tqdm(enumerate(sim.env.history), position=5):
                                for agent in tqdm(sim.env.agents, position=6):
                                    agent_reward = step.rewards[agent]
                                    agent_comfort = step.agent_comfort[agent]
                                    data.append({
                                        'Model': model,
                                        'ConsumptionProfile': profile,
                                        'EnvironmentSize': size,
                                        'RewardFunction': reward,
                                        'Run': run_id,
                                        'Step': num_step,
                                        'Agent': agent.name,
                                        'Reward': agent_reward,
                                        'Comfort': agent_comfort,
                                    })
                            del sim
                        except:
                            traceback.print_exc()
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    df = get_details()
    result_file = data_dir / 'agents_details.pkl.xz'
    df.to_pickle(result_file, compression='xz')
