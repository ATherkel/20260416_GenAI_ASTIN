import pandas as pd
import openpyxl # noqa: F401


def load_claims(path, **kwargs):
    return pd.read_excel(path, **kwargs,)


def compute_loss_ratio(df):
    return df["incurred"].sum() / df["premium"].sum()


def show_table(df):
    print(df)

def save_report(result, path):
    return_string = f"Loss ratio: {result:.2%}\n"

    print(return_string)
    with open(path, "w") as f:
        f.write(return_string)


if __name__ == "__main__":
    df = load_claims("data/sample.xlsx", sheet_name = "results")
    show_table(df)
    ratio = compute_loss_ratio(df)
    save_report(ratio, "report.txt")
