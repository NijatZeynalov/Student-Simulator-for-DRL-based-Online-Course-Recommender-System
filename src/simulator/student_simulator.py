import random, datetime

class StudentSimulator:
    def __init__(self, student_data, course_data):
        self.student_data = student_data
        self.course_data = course_data

    def simulate_behavior(self):
        simulated_data = []
        for student in self.student_data:
            for course in random.sample(self.course_data, random.randint(1, len(self.course_data)//2)):
                enrollment_date = self.random_date()
                completion_status = random.choice(['Completed', 'Not Completed'])
                time_spent = random.randint(5, 100) if completion_status == 'Completed' else random.randint(1, 20)
                satisfaction_rating = random.randint(3, 5) if completion_status == 'Completed' else random.randint(1, 3)
                simulated_data.append({
                    'student_id': student['student_id'],
                    'course_id': course['course_id'],
                    'enrollment_date': enrollment_date,
                    'completion_status': completion_status,
                    'time_spent': time_spent,
                    'satisfaction_rating': satisfaction_rating
                })
        return simulated_data

    @staticmethod
    def random_date(start=datetime.date(2022, 1, 1), end=datetime.date(2023, 1, 1)):
        return start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))
