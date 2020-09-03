import gym
import gym_minecraft

env = gym.make('MinecraftBasic-v0')
env.init(start_minecraft=True)
env.reset()

done = False
while not done:
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

env.close()