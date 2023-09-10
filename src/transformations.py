import pandas as pd


def filter_by_countries(df, countries=None):
    if countries is None:
        countries = ["United Kingdom", "Netherlands"]

    return df[df["country"].isin(countries)]


def sanitize_client_data(df, columns_to_drop=["first_name", "last_name"]):
    return df.drop(columns=columns_to_drop)
