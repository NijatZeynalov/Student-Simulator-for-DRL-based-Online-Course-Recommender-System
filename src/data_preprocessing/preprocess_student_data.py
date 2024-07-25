import pandas as pd

def preprocess_student_data(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)

    # Perform necessary preprocessing steps
    # Convert enrollment_date to datetime
    df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])

    # Example: Filter out entries with missing satisfaction ratings
    df = df.dropna(subset=['satisfaction_rating'])

    # Save the preprocessed data
    df.to_csv(output_file, index=False)