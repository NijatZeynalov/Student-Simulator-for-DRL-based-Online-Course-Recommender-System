import pandas as pd

def load_data(student_data_path, course_data_path):
    student_data = pd.read_csv(student_data_path)
    course_data = pd.read_csv(course_data_path)
    return student_data, course_data

def preprocess_data(student_data, course_data):
    # Add any preprocessing steps here
    student_data['enrollment_date'] = pd.to_datetime(student_data['enrollment_date'])
    course_data['n_enrolled'] = course_data['n_enrolled'].str.replace(',', '').astype(int)
    return student_data, course_data
