import numpy as np
import pandas as pd

from controller import AgentInterface
from epsilon_profile import EpsilonProfile
from game.SpaceInvaders import SpaceInvaders


class QAgent(AgentInterface):

    def __init__(self, game: SpaceInvaders, eps_profile: EpsilonProfile, gamma: float, alpha: float, sampling: int,
                 fileLog: str):

        # Initialise la fonction de valeur Q
        self.Q = np.zeros([int(800 / sampling), int(600 / sampling), 2, game.na])

        self.game = game
        self.na = game.na

        # Paramètres de l'algorithme
        self.gamma = gamma
        self.alpha = alpha

        self.eps_profile = eps_profile
        self.epsilon = self.eps_profile.initial

        self.qvalues = pd.DataFrame(data={'episode': [], 'score': []})
        self.fileLog = fileLog

    def learn(self, game, n_episodes, max_steps):

        n_steps = np.zeros(n_episodes) + max_steps

        # Execute N episodes 
        for episode in range(n_episodes):
            # Reinitialise l'environnement
            state = game.reset()

            # Execute K steps 
            for step in range(max_steps):
                # Selectionne une action 
                action = self.select_action(state)
                # Echantillonne l'état suivant et la récompense
                next_state, reward, terminal = game.step(action)
                # Mets à jour la fonction de valeur Q
                self.updateQ(state, action, reward, next_state)
                print("\r#> Episode {}/{} Step {}/{} Q sum {}".format(episode, n_episodes, step, max_steps,
                                                                      np.sum(self.Q)), end=" ")

                if terminal:
                    n_steps[episode] = step + 1
                    break

                state = next_state
            # Mets à jour la valeur du epsilon
            self.epsilon = max(self.epsilon - self.eps_profile.dec_episode / (n_episodes - 1.), self.eps_profile.final)

            # Sauvegarde et affiche les données d'apprentissage
            if n_episodes >= 0:
                state = game.reset()
                self.save_log(episode)
                state = game.reset()

        self.qvalues.to_csv('visualisation/' + self.fileLog + '.csv')

    def updateQ(self, state: 'Tuple[int, int, int]', action: int, reward: float, next_state: 'Tuple[int, int, int]'):
        self.Q[state][action] = (1 - self.alpha) * self.Q[state][action] + self.alpha * (
                reward + self.gamma * np.max(self.Q[next_state]))

    def select_action(self, state: 'Tuple[int, int, int]'):
        if np.random.rand() < self.epsilon:
            a = np.random.randint(self.na)
            return a
        else:
            a = self.select_greedy_action(state)
            return a

    def select_greedy_action(self, state: 'Tuple[int, int, int]'):
        mx = np.max(self.Q[state])
        # greedy action with random tie break
        return np.random.choice(np.where(self.Q[state] == mx)[0])

    def save_log(self, episode):
        self.qvalues = pd.concat([self.qvalues, pd.DataFrame.from_records([{
            'episode': episode,
            'sumQ': np.sum(self.Q)
        }])])

    def saveQToFile(self, file):
        np.save(file, self.Q)
