import pandas as pd

from .adapters import PygamAdapter, PyglmAdapter
from .data import prepare_features


def build_model(kind="pygam", **kwargs):
    if kind == "pygam":
        return PygamAdapter(**kwargs)
    if kind == "pyglm":
        return PyglmAdapter(**kwargs)
    raise ValueError("Unknown kind")


def train(model, df, target, features):
    X, y = prepare_features(df, target, features)
    model.train(X, y)
    return model


def predict(model, df, features):
    X = pd.get_dummies(df[features], drop_first=False)
    return model.predict(X)
