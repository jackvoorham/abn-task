import pandas as pd

DEFAULT_RENAME_MAPPINGS = {
    "id": "client_identifier",
    "btc_a": "bitcoin_address",
    "cc_t": "credit_card_type",
}


def filter_by_countries(df, countries=None):
    if countries is None:
        countries = ["United Kingdom", "Netherlands"]

    return df[df["country"].isin(countries)]


def sanitize_client_data(df, columns_to_drop=["first_name", "last_name"]):
    return df.drop(columns=columns_to_drop)


def sanitize_financial_data(df, columns_to_drop=["cc_n"]):
    return df.drop(columns=columns_to_drop)


def merge_data(df1, df2, merge_column="id"):
    return pd.merge(df1, df2, on=merge_column)


def rename_columns(
    df,
    column_names_mapping=DEFAULT_RENAME_MAPPINGS,
):
    return df.rename(columns=column_names_mapping)
