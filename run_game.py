from controller import AgentInterface
from controller.qagent import QAgent
from epsilon_profile import EpsilonProfile
from game.SpaceInvaders import SpaceInvaders


def test(game: SpaceInvaders, agent: AgentInterface, max_steps: int, nepisodes: int = 10, same=True, display=False):
    n_steps = max_steps
    sum_rewards = 0.
    for _ in range(nepisodes):
        state = game.reset() if same else game.reset()
        for step in range(10000):
            action = agent.select_greedy_action(state)
            next_state, reward, terminal = game.step(action)

            sum_rewards += reward
            if terminal:
                n_steps = step + 1  # number of steps taken
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
    # controller = RandomAgent(game.na)
    # controller = KeyboardController()
    agent = QAgent(game, eps_profile, gamma, alpha)
    agent.learn(game, n_episodes, max_steps)

    print()
    print(
        "############################################################################"
    )
    print("FINISHED LEARNING")
    print("    n_episodes: ", n_episodes)
    print("    max_steps: ", max_steps)
    print("    gamma: ", gamma)
    print("    eps_profile (initial, final, dec_episode, dec_step): ",
          eps_profile.initial, eps_profile.final, eps_profile.dec_episode,
          eps_profile.dec_step)
    print(
        "############################################################################"
    )

    rewards = test(game, agent, max_steps, display=True)
    print('rewards: {}'.format(rewards))


if __name__ == '__main__':
    main()
