def calculate_metrics(simulated_data):
    completion_rate = simulated_data['completion_status'].value_counts(normalize=True).get('Completed', 0)
    avg_time_spent = simulated_data['time_spent'].mean()
    avg_satisfaction_rating = simulated_data['satisfaction_rating'].mean()

    metrics = {
        'completion_rate': completion_rate,
        'avg_time_spent': avg_time_spent,
        'avg_satisfaction_rating': avg_satisfaction_rating
    }

    return metrics


def print_metrics(metrics):
    print(f"Completion Rate: {metrics['completion_rate']:.2f}")
    print(f"Average Time Spent: {metrics['avg_time_spent']:.2f} hours")
    print(f"Average Satisfaction Rating: {metrics['avg_satisfaction_rating']:.2f}")


if __name__ == "__main__":
    import pandas as pd

    simulated_data = pd.read_csv('path/to/simulated_student_data.csv')
    metrics = calculate_metrics(simulated_data)
    print_metrics(metrics)
