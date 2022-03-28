from game.SpaceInvaders import SpaceInvaders
from controller.KeyboardController import KeyboardController

def main():
    controller = KeyboardController()
    game = SpaceInvaders(display=True, state_type="tabular")
    state = game.reset()
    while True:
        action = controller.select_action(state)
        state, reward, is_done, infos = game.step(action)
        print(state)
        print(reward)


if __name__ == '__main__' :
    main()