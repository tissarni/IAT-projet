from game.SpaceInvaders import SpaceInvaders

def main():
    game = SpaceInvaders(display=True)
    running = True
    while running:
        action = 0
        state, reward, is_done, infos = game.step(action)
        # print(state)
        # print(reward)
        # print(is_done)

if __name__ == '__main__' :
    main()