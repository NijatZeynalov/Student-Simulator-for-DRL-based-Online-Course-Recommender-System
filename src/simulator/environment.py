class Environment:
    def __init__(self, course_data, student_data):
        self.course_data = course_data
        self.student_data = student_data
        self.current_state = None

    def reset(self):
        self.current_state = self._get_initial_state()
        return self.current_state

    def step(self, action):
        # Execute the action and return the new state, reward, and whether the episode is done
        new_state = self._take_action(action)
        reward = self._calculate_reward(new_state)
        done = self._check_done(new_state)
        self.current_state = new_state
        return new_state, reward, done

    def _get_initial_state(self):
        # Return the initial state
        initial_state = {
            'student_profile': random.choice(self.student_data),
            'available_courses': random.sample(self.course_data, 10)
        }
        return initial_state

    def _take_action(self, action):
        # Update the state based on the action
        # For simplicity, assume action is an index of the course in available_courses
        new_course = self.current_state['available_courses'][action]
        new_state = {
            'student_profile': self.current_state['student_profile'],
            'selected_course': new_course
        }
        return new_state

    def _calculate_reward(self, state):
        # Calculate and return the reward for the given state
        if state['selected_course']['difficulty'] <= state['student_profile']['level']:
            return 1
        return -1

    def _check_done(self, state):
        # Check if the episode is done
        # For simplicity, assume the episode ends after one step
        return True