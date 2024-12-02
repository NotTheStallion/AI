import numpy as np
from envs import Env1, Env2, Env3

class MonteCarloAgent():
    def __init__(self, env, gamma=0.9, epsilon=0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        
        self.policy = np.random.randint(env.num_states, size=env.num_actions)
        
        self.V = np.zeros(env.num_states)
        self.N = np.zeros(env.num_states)
        
        self.returns = {(s, a): [] for s in range(env.num_states) for a in range(env.num_actions)}
        self.state = 0
        self.action = 0
        self.trajectory = []
    
    def generate_trajectory(self):
        self.trajectory = []
        state = self.env.reset()
        while state != self.env.terminate_state:
            # action = self.policy(state)
            action = np.random.choice(self.env.num_actions) if np.random.rand() < self.epsilon else self.policy[int(state)] # epsilon-greedy
            next_state, reward = self.env.play(int(state), int(action))
            self.trajectory.append((int(state), int(action), int(reward)))
            state = next_state
        self.trajectory.append((self.env.terminate_state, -1, -1))
            
    def update(self, trajectory):
        G = 0
        for state, action, reward in reversed(self.trajectory):
            G = self.gamma * G + reward
            self.N[state] += 1
            self.V[state] += (G - self.V[state]) / self.N[state]
    
    def train(self, n_episodes):
        for _ in range(n_episodes):
            self.generate_trajectory()
            self.update(self.trajectory)
            print(self.V)
            print(self.N)
            print()


class SAESAAgent():
    def __init__(self, env, gamma=0.9, epsilon=0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        
        self.policy = np.random.randint(env.num_states, size=env.num_actions)
        
        self.Q = np.zeros((env.num_states, env.num_actions))
        self.N = np.zeros((env.num_states, env.num_actions))
        
        self.state = 0
        self.action = 0
        self.trajectory = []
    
    def generate_trajectory(self):
        self.trajectory = []
        state = self.env.reset()
        while state != self.env.terminate_state:
            # action = self.policy(state)
            action = np.random.choice(self.env.num_actions) if np.random.rand() < self.epsilon else self.policy[int(state)] # epsilon-greedy
            next_state, reward = self.env.play(int(state), int(action))
            self.trajectory.append((int(state), int(action), int(reward)))
            state = next_state
        self.trajectory.append((self.env.terminate_state, -1, -1))
    
    def update(self, trajectory):
        for state, action, reward in trajectory:
            self.N[state, action] += 1
            self.Q[state, action] += self.alpha * (reward + self.gamma * self.Q[state, action] - self.Q[state, action])

if __name__ == "__main__":
    env = Env2()
    agent = MonteCarloAgent(env)
    agent.generate_trajectory()
    print(agent.trajectory)
    agent.update(agent.trajectory)
    agent.train(1000)
    print(agent.policy)