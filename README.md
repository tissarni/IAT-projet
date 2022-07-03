# IAT-projet
Welcome in the github designed for the IAT-project 2022.

## Setup

1. Get the source code by cloning this github locally
```bash
git clone https://github.com/aurelienDelageInsaLyon/IAT-projet
cd IAT-projet
```

2. Install the dependancies
```bash
pip3 install -r requirements.txt
```

## Run the application in our best environment

```bash
python3 run_game.py 500 1500 10 0.95 0.1 1.0 0 1 [output_file]
```
### Visualize the evolution of sumQ according to the number of episodes
```bash
python3 logAnalyser.py visualisation/[output_file]
```
### Script parameters
```
python3 run_game.py <n_episodes> <max_steps> <final_episode> <gamma> <alpha> <eps_begin> <eps_end> <sampling> <fileName>

- n_episodes : Number of episodes during the learn phase
- max_steps : Number of steps maximum during an episode
- final_episode : Number of episodes during the test phase
- gamma : Gamma hyperparameter for the Q-learning algorithm
- alpha : Gamma hyperparameter for the Q-learning algorithm
- eps_begin : Initial epsilon hyperparameter for the epsilon-greedy algorithm
- eps_end :  Final epsilon hyperparameter for the epsilon-greedy algorithm
- sampling : Sampling factor for the get_state function (defines the grid size for the learning phase)
- fileName : Name of the file where the logs will be saved
```