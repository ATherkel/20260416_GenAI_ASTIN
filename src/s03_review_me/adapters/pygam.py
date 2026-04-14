import importlib

from .base import ModelAdapter


class PygamAdapter(ModelAdapter):
    def __init__(self, family="linear"):
        self.family = family
        self.model = None

    def train(self, X, y):
        pygam = importlib.import_module("pygam")
        if self.family == "linear":
            self.model = pygam.LinearGAM()
        elif self.family == "logistic":
            self.model = pygam.LogisticGAM()
        else:
            raise ValueError("family must be linear or logistic")
        self.model.fit(X.values, y.values)

    def predict(self, X):
        if self.model is None:
            raise RuntimeError("Call train before predict")
        return self.model.predict(X.values)
