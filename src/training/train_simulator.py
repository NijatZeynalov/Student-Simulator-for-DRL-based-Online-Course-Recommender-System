import pandas as pd
from simulator import StudentSimulator

if __name__ == "__main__":
    student_data = pd.read_csv('path/to/processed_student_data.csv').to_dict('records')
    course_data = pd.read_csv('path/to/processed_course_data.csv').to_dict('records')
    simulator = StudentSimulator(student_data, course_data)
    simulated_behavior = simulator.simulate_behavior()
    simulated_df = pd.DataFrame(simulated_behavior)
    simulated_df.to_csv('path/to/simulated_student_data.csv', index=False)
    print("Student simulation complete and data saved.")
