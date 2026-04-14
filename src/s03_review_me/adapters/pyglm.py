import importlib

from .base import ModelAdapter


class PyglmAdapter(ModelAdapter):
    def __init__(self, family="normal"):
        self.family = family
        self.model = None

    def train(self, X, y):
        pyglm = importlib.import_module("pyglm")
        family_obj = getattr(pyglm.families, self.family.capitalize())()
        self.model = pyglm.GLM(family=family_obj)
        self.model.fit(X.values, y.values)

    def predict(self, X):
        if self.model is None:
            raise RuntimeError("Call train before predict")
        return self.model.predict(X.values)
