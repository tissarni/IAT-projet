from time import sleep
from game.SpaceInvaders import SpaceInvaders
from controller.keyboard import KeyboardController
from controller.random_agent import RandomAgent
from epsilon_profile import EpsilonProfile
from controller.qagent import QAgent
from controller import AgentInterface


def test(game: SpaceInvaders, agent: AgentInterface, max_steps: int, nepisodes : int = 10, speed: float = 0., same = True, display: bool = False):
    n_steps = max_steps
    sum_rewards = 0.
    for _ in range(nepisodes):
        state = game.reset() if (same) else game.reset()

        for step in range(max_steps):
            action = agent.select_greedy_action(state)
            next_state, reward, terminal = game.step(action)

            sum_rewards += reward
            if terminal:
                n_steps = step+1  # number of steps taken
                break
            state = next_state
    return n_steps, sum_rewards


def main():

    n_episodes = 1000
    max_steps = 100
    gamma = 1.
    alpha = 0.2
    eps_profile = EpsilonProfile(1.0, 0)


    game = SpaceInvaders(display=True)
    #controller = RandomAgent(game.na)
    #controller = KeyboardController()
    agent = QAgent(game, eps_profile, gamma, alpha)
    agent.learn(game, n_episodes, max_steps)

    test(game, agent, max_steps, speed=0.1, display=True)


if __name__ == '__main__' :
    main()
