from epsilon_profile import EpsilonProfile
from game.SpaceInvaders import SpaceInvaders
from controller.KeyboardController import KeyboardController
from controller.qagent import QAgent

def main():

    n_episodes = 2000
    max_steps = 1000
    eps = EpsilonProfile(1., 0.1)
    controller = KeyboardController()
    game = SpaceInvaders(display=True, state_type="tabular")
    # controller = QAgent(game, eps, 0.99, 0.2)
    # controller.learn(game, n_episodes, max_steps)
    state = game.reset()
    while True:
        action = controller.select_action(state)
        state, reward, is_done = game.step(action)
        # print(state)
        # print(reward)


if __name__ == '__main__' :
    main()