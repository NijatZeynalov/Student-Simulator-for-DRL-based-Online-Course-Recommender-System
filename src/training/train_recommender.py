from ..recommender.drl_recommender import DRLRecommender
from ..recommender.policy_network import PolicyNetwork
from ..simulator.environment import Environment
import pandas as pd

if __name__ == "__main__":
    course_data = pd.read_csv('path/to/processed_course_data.csv').to_dict('records')
    student_data = pd.read_csv('path/to/processed_student_data.csv').to_dict('records')
    env = Environment(course_data, student_data)
    policy_net = PolicyNetwork(state_size=10, action_size=10)
    recommender = DRLRecommender(policy_net, env)
    recommender.train(episodes=1000)
    print("Recommender system training complete.")
