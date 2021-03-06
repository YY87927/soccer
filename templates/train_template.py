from env import SoccerEnv
from agents.common.training_opponent import StationaryOpponent, RandomSwitchOpponent, RLBasedOpponent

# set environment
env = SoccerEnv(width=5, height=5, goal_size=3)

# set agents
agentME = "add your agent here"
agentOP = StationaryOpponent(env_width=env.width, env_height=env.height, env_goal_size=env.goal_size)

# parameters
EPISODES = 5000

for i in range(EPISODES):
    state = env.reset()

    done = False
    while not done:
        env.show()
        print()

        # agent 1 decides its action
        actionME = "choose your action here"

        # agent 2 decides its action
        actionOP = agentOP.get_action(state)

        # perform actions on the environment
        done, reward_l, reward_r, state_, actions = env.step(actionME, actionOP)

        # training process of agent 1
        """ do some training here """

        # training process of agent 2
        agentOP.adjust(done, reward_r, i)

        state = state_
