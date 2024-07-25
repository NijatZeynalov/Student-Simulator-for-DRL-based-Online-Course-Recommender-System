from ..recommender.drl_recommender import DRLRecommender
from ..recommender.policy_network import PolicyNetwork
from ..simulator.environment import Environment
import pandas as pd


def evaluate_recommender(episodes=100):
    course_data = pd.read_csv('path/to/processed_course_data.csv').to_dict('records')
    student_data = pd.read_csv('path/to/processed_student_data.csv').to_dict('records')
    env = Environment(course_data, student_data)
    policy_net = PolicyNetwork(state_size=10, action_size=10)
    recommender = DRLRecommender(policy_net, env)

    total_rewards = 0
    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_rewards = 0

        while not done:
            action = recommender.recommend(state)
            new_state, reward, done = env.step(action)
            episode_rewards += reward
            state = new_state

        total_rewards += episode_rewards
        print(f"Episode {episode + 1}: Reward: {episode_rewards}")

    average_reward = total_rewards / episodes
    print(f"Average Reward over {episodes} episodes: {average_reward:.2f}")


if __name__ == "__main__":
    evaluate_recommender()
