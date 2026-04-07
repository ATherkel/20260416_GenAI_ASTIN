import importlib
import pandas as pd


def pre_analyze(df, target):
	return {
		"rows": int(len(df)),
		"columns": int(df.shape[1]),
		"missing": int(df.isna().sum().sum()),
		"target_mean": float(df[target].mean()) if target in df.columns else None,
	}


def prepare_features(df, target, features):
	if target not in df.columns:
		raise ValueError(f"Missing target: {target}")
	missing = [f for f in features if f not in df.columns]
	if missing:
		raise ValueError(f"Missing features: {missing}")
	X = pd.get_dummies(df[features], drop_first=False)
	y = df[target]
	return X, y


class ModelAdapter:
	def train(self, X, y):
		raise NotImplementedError

	def predict(self, X):
		raise NotImplementedError


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
