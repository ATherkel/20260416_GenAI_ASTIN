from pathlib import Path

import pandas as pd
import openpyxl  # noqa: F401

REQUIRED_COLUMNS = {"incurred", "premium"}


def load_claims(path, **kwargs):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_excel(path, **kwargs)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df


def compute_loss_ratio(df, by=None):
    if by is not None:
        cols = [by] if isinstance(by, str) else list(by)
        missing = set(cols) - set(df.columns)
        if missing:
            raise ValueError(f"Columns not found in DataFrame: {missing}")
        grouped = df.groupby(by)
        premium = grouped["premium"].sum()
        incurred = grouped["incurred"].sum()
        result = incurred / premium
        result.name = "loss_ratio"
        return result.replace([float("inf"), float("-inf")], float("nan"))
    total_premium = df["premium"].sum()
    if total_premium == 0:
        raise ZeroDivisionError("Total premium is zero; cannot compute loss ratio.")
    return df["incurred"].sum() / total_premium


def show_table(df):
    print(df)


def save_report(result, path):
    return_string = f"Loss ratio: {result:.2%}\n"

    print(return_string)
    with open(path, "w") as f:
        f.write(return_string)


if __name__ == "__main__":
    df = load_claims("data/sample.xlsx", sheet_name="results")
    show_table(df)
    ratio = compute_loss_ratio(df)
    save_report(ratio, "report.txt")
