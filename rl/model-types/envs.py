import numpy as np

class Env:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def play(self, state, action):
        raise NotImplementedError("This method should be overridden by subclasses")

class Env1(Env):
    def __init__(self):
        super().__init__(2, 2)
        # transitions[state][action] = [probability, next_state]
        self.transitions = np.array([
            [[1/2, 1], [2/3, 0]],
            [[0, 1], [1, 1]]
        ])

        # rewards[state][action] = reward
        self.rewards = np.array([
            [2, 4],
            [10, 10]
        ])
        
        self.terminate_state = 1

    def play(self, state, action):
        next_state = self.transitions[state, action, 1]
        reward = self.rewards[state, action]
        return next_state, reward

class Env2(Env):
    def __init__(self):
        super().__init__(4, 4)
        self.num_actions = 4
        self.num_states = 4
        self.transitions = np.array([
            [[0.5, 1], [0.5, 2], [0.1, 3], [0.7, 0]],
            [[0.3, 2], [0.7, 3], [0.2, 0], [0.8, 1]],
            [[0.6, 3], [0.4, 0], [0.9, 1], [0.1, 2]],
            [[0.8, 0], [0.2, 1], [0.3, 2], [0.7, 3]]
        ])
        self.rewards = np.array([
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7]
        ])
        self.terminate_state = 3

    def play(self, state, action):
        next_state = self.transitions[state, action, 1]
        print(f"s: {state}, a: {action}, s': {next_state}")
        reward = self.rewards[state, action]
        return next_state, reward

class Env3(Env):
    def __init__(self):
        super().__init__(2, 2)
        self.transitions = np.array([
            [[0, 1], [1, 0]],
            [[0, 1], [1, 0]]
        ])
        self.rewards = np.array([
            [1, 0],
            [2, 1]
        ])

    def play(self, state, action):
        next_state = self.transitions[state, action, 1]
        reward = self.rewards[state, action]
        return next_state, reward