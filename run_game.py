import os
from sys import argv
from time import time

from controller import AgentInterface
from controller.qagent import QAgent
from controller.random_agent import RandomAgent
from epsilon_profile import EpsilonProfile
from game.SpaceInvaders import SpaceInvaders


def test(game: SpaceInvaders, agent: AgentInterface, nepisodes: int, same=True, display=False):
    sum_rewards = 0.
    for _ in range(nepisodes):
        state = game.reset() if same else game.reset()
        terminal = False
        state = game.reset()

        while not terminal:
            action = agent.select_greedy_action(state)
            next_state, reward, terminal = game.step(action)
            sum_rewards += reward
            state = next_state
    return sum_rewards



if __name__ == '__main__':
    if len(argv) < 11:
        n_episodes = int(argv[1])
        max_steps = int(argv[2])
        final_episode = int(argv[3])
        gamma = float(argv[4])
        alpha = float(argv[5])
        eps_profile = EpsilonProfile(float(argv[6]), float(argv[7]))
        sampling = int(argv[8])
        fileName = str(argv[9])
    else:
        print('\n\nUsage: python3 run_game.py <n_episodes> <max_steps> <final_episode> <gamma> <alpha> <eps_begin> <eps_end> <sampling> <fileName>\n')
        exit(1)



    game = SpaceInvaders(sampling, display=False)
    controller = RandomAgent(game.na)
    state = game.reset()
    random_score = 0
    is_done = False
    
    for _ in range(final_episode):
        while not is_done:
            action = controller.select_action(state)
            state, reward, is_done = game.step(action)
            random_score += reward

    print('Joueur random avant apprentissage - score moyen : {}'.format(random_score / final_episode))

    
    agent = QAgent(game, eps_profile, gamma, alpha, sampling, fileName)


    startTime = time()
    agent.learn(game, n_episodes, max_steps)
    endTime = time()
    agent.saveQToFile(os.path.join(fileName))
    

    print(
        "############################################################################"
    )
    print("    sampling: ", sampling)
    print("    n_episodes: ", n_episodes)
    print("    max_steps: ", max_steps)
    print("    gamma: ", gamma)
    print("    alpha: ", alpha)
    print("    eps_profile (initial, final, dec_episode, dec_step): ",
          eps_profile.initial, eps_profile.final, eps_profile.dec_episode,
          eps_profile.dec_step)
    print ("Durée de l'apprentissage : " + str(endTime - startTime))
    print(
        "############################################################################"
    )

    rewards = test(game, agent, final_episode, display=False)
    print("Score moyen après entrainement : {}".format(rewards/final_episode))


