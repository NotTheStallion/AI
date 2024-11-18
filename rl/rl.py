import numpy as np


class MDP():
    def __init__(self, n_states, n_actions,  gamma):
        self.n_states = n_states
        self.n_actions = n_actions
        self.gamma = gamma
        self.current_state = 0
        self.init_state = 0
        
        self.transitions = np.zeros((n_states, n_actions, n_states)) # P(s'|s, a) : S x A x S ---> [0, 1]
        self.rewards = np.zeros((n_states, n_actions)) # R(s, a) : S x A ---> R
    
    def _set_transitions(self, transitions):
        self.transitions = transitions
    
    def _set_rewards(self, rewards):
        self.rewards = rewards
    
    def play(self, action) -> [int, float]:
        print(f"Playing action {action}")
        self.current_state = np.random.choice(self.n_states, p=self.transitions[self.current_state, action]) # s' ~ P(s'|s, a)
        return self.current_state, self.rewards[self.current_state, action]

    def reset(self):
        self.current_state = self.init_state
        return self.current_state

    def simulate(self, agent, n_steps) -> list:
        print("# Simulation")
        states = []
        rewards = []
        print(f"Initial state {self.current_state}")
        for i in range(n_steps):
            print(f"# Step {i}")
            action = agent.choose_action(self.current_state)
            new_state, reward = self.play(action)
            print(f"New state {new_state}")
            states.append(new_state)
            rewards.append(reward)
        return states, rewards

class Agent():
    def __init__(self, mdp : MDP, policy):
        self.mdp = mdp
        self.n_states = mdp.n_states
        self.n_actions = mdp.n_actions
        self.policy = policy
        
    def choose_action(self, state) -> int:
        return self.policy[state]



if __name__ == "__main__":
    n_states = 2
    n_actions = 2
    gamma = 0.9
    transitions = np.array([
        [[0, 1],   # s1 -> a1 -> s2
         [1, 0]],  # s1 -> a2 -> s1
        [[0, 1], # s2 -> a1 -> s2
         [1, 0]] # s2 -> a2 -> s1
        ]) # s x a x s = 2x2x2
    rewards = np.array([
        [1, 0], # s1 -> a1 -> r = 1, s1 -> a2 -> r = 0
        [2, 1]  # s2 -> a1 -> r = 2, s2 -> a2 -> r = 1
        ]) # s x a = 2x2
    
    policy = [[0, 1], # s1 -> a1 with prob 1, s1 -> a2 with prob 0
              [1, 0]  # s2 -> a1 with prob 1, s2 -> a2 with prob 0
              ] # s x a = 2x2
    
    mdp = MDP(n_states, n_actions, gamma)
    mdp._set_transitions(transitions)
    mdp._set_rewards(rewards)
    
    agent = Agent(mdp, policy)
    
    mdp.simulate(agent, 10)