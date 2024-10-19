Positive learning == no penality

https://www.labri.fr/perso/zemmari/rl/

A stochastic env == things happen in a random manner.
The policy maps states to actions to maximize a reward.


Course plan :
- multi-armed bandits
- exploration and exploitation
- MDPs
- dynamic programming
- Monte carlo, temporal difference learning, sarsa, q learning
- function approx, gradient methods, monte carlo tree search (mcts)
- deel reinforcement learning (DQN)
- multi-agent reinforcement learning


all the models are MDPs but some are model based and the rest are model free
model based means we know the transition rules
model free means the models find the actions it can do (monte carlo)

In both model types, the states and actions have to be defined (mandatory)

$\gamma=0$ myopic agent (agent only cares about imidiate reward)
$\gamma=1$ agent is far sighted (cares about fututre rewards)

the episode terminates when the number of max steps is reached. (you have to have an idea of the number of actions)

Exploit what you already know or explore other solutions.

The new type of action choosing is a probabilistic choice : $a_i$ is chosen from a distribution of probabilites. Its reward follows the same distribution.

UCB reaches log(T) complexity of optimization.

