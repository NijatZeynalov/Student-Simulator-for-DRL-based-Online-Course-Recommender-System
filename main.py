import os
import pandas as pd

from src.data_preprocessing import preprocess_student_data, preprocess_course_data
from src.simulator.student_simulator import StudentSimulator
from src.training import train_recommender
from src.evaluation import evaluate_simulator, evaluate_recommender

if __name__ == "__main__":
    # Define file paths
    raw_student_data_path = 'data/raw/historical_student_data_10000.csv'
    raw_course_data_path = 'data/raw/edx_courses.csv'
    processed_student_data_path = 'data/processed/processed_student_data.csv'
    processed_course_data_path = 'data/processed/processed_course_data.csv'
    simulated_data_path = 'data/simulation_results/simulated_student_data.csv'

    # Step 1: Preprocess the data
    preprocess_student_data.preprocess_student_data(raw_student_data_path, processed_student_data_path)
    preprocess_course_data.preprocess_course_data(raw_course_data_path, processed_course_data_path)

    # Step 2: Simulate student behavior
    student_data = pd.read_csv(processed_student_data_path).to_dict('records')
    course_data = pd.read_csv(processed_course_data_path).to_dict('records')
    simulator = StudentSimulator(student_data, course_data)
    simulated_behavior = simulator.simulate_behavior()
    simulated_df = pd.DataFrame(simulated_behavior)
    simulated_df.to_csv(simulated_data_path, index=False)

    # Step 3: Train the recommender system
    train_recommender.train_recommender(processed_course_data_path, simulated_data_path)

    # Step 4: Evaluate the simulator
    evaluate_simulator.evaluate_simulator(simulated_data_path)

    # Step 5: Evaluate the recommender system
    evaluate_recommender.evaluate_recommender()

