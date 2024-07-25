import pandas as pd

def preprocess_course_data(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)

    # Perform necessary preprocessing steps

    df = df.dropna(subset=['course_description'])

    # Save the preprocessed data
    df.to_csv(output_file, index=False)