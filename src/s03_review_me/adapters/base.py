class ModelAdapter:
    def train(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError
