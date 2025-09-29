# src/data_processing.py
import pandas as pd

DEFAULT_COLUMNS = [
    "cord_uid", "title", "abstract", "publish_time",
    "authors", "journal", "source_x", "doi"
]

def load_metadata(path="data/metadata.csv", nrows=None, usecols=None):
    """
    Load metadata.csv safely. Use nrows for quick sampling during development.
    """
    usecols = usecols or DEFAULT_COLUMNS
    df = pd.read_csv(path, usecols=[c for c in usecols if c in pd.read_csv(path, nrows=0).columns],
                     parse_dates=["publish_time"] if "publish_time" in usecols else None,
                     infer_datetime_format=True,
                     nrows=nrows,
                     low_memory=False)
    # normalize column names
    if "source_x" in df.columns:
        df = df.rename(columns={"source_x": "source"})
    return df

def clean_metadata(df):
    """
    Basic cleaning:
      - dedupe
      - fill text NA with empty strings
      - parse dates
      - extract year/month
      - add simple word counts
    """
    # dedupe if cord_uid exists
    if "cord_uid" in df.columns:
        df = df.drop_duplicates(subset=["cord_uid"])
    else:
        df = df.drop_duplicates()

    # text fields
    for col in ["title", "abstract", "journal", "authors", "source"]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()

    # publish_time -> datetime
    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["year"] = df["publish_time"].dt.year
        df["month"] = df["publish_time"].dt.month
    else:
        df["year"] = pd.NA
        df["month"] = pd.NA

    # word counts
    df["abstract_word_count"] = df.get("abstract", "").apply(lambda x: len(str(x).split()))
    df["title_word_count"] = df.get("title", "").apply(lambda x: len(str(x).split()))

    return df
