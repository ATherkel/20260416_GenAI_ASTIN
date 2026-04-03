import pandas as pd
import openpyxl # noqa: F401


def load_claims(path, **kwargs):
    return pd.read_excel(path, **kwargs,)


def compute_loss_ratio(df):
    return df["incurred"].sum() / df["premium"].sum()


def show_table(df):
    print(df)

def save_report(result, path):
    with open(path, "w") as f:
        f.write(f"Loss ratio: {result:.2%}\n")


if __name__ == "__main__":
    df = load_claims("data/sample.xlsx", sheet_name = "mixed_dtype")
    show_table(df)
    # ratio = compute_loss_ratio(df)
    # save_report(ratio, "report.txt")
