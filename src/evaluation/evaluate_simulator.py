import pandas as pd


def evaluate_simulator(simulated_data_path):
    simulated_data = pd.read_csv(simulated_data_path)
    completion_rate = simulated_data['completion_status'].value_counts(normalize=True)['Completed']
    avg_time_spent = simulated_data['time_spent'].mean()
    avg_satisfaction_rating = simulated_data['satisfaction_rating'].mean()

    print(f"Completion Rate: {completion_rate:.2f}")
    print(f"Average Time Spent: {avg_time_spent:.2f} hours")
    print(f"Average Satisfaction Rating: {avg_satisfaction_rating:.2f}")


if __name__ == "__main__":
    evaluate_simulator('path/to/simulated_student_data.csv')
