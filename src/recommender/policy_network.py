import numpy as np

class PolicyNetwork:
    def __init__(self, state_size, action_size, learning_rate=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.weights = np.random.rand(state_size, action_size)

    def predict(self, state):
        probabilities = np.dot(state, self.weights)
        action = np.argmax(probabilities)
        return action

    def update(self, state, action, reward, new_state, done, gamma):
        target = reward + gamma * np.max(np.dot(new_state, self.weights)) * (1 - done)
        prediction = np.dot(state, self.weights)[action]
        error = target - prediction

        # Update weights
        self.weights[:, action] += self.learning_rate * error * state
