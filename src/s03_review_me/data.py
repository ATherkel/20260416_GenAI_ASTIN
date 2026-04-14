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
