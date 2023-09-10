import pandas as pd

DEFAULT_RENAME_MAPPINGS = {
    "id": "client_identifier",
    "btc_a": "bitcoin_address",
    "cc_t": "credit_card_type",
}


def filter_by_countries(df, countries=["United Kingdom", "Netherlands"]):
    """
    Filter client data by countries

    Parameters:
    client_data_df (pandas.DataFrame): The client data DataFrame
    countries (list): A list of countries to filter by
                      Default is ['United Kingdom', 'Netherlands'].

    Returns:
    pandas.DataFrame: The filtered client data DataFrame
    """
    return df[df["country"].isin(countries)]


def sanitize_client_data(df, columns_to_drop=["first_name", "last_name"]):
    """
    Sanitize client data by dropping specified columns.
    Default columns to drop are first name and last name.

    Parameters:
    df (pandas.DataFrame): The client data DataFrame
    columns_to_drop (list): List of column names to drop from the DataFrame
                            Default is ["first_name", "last_name"].

    Returns:
    pandas.DataFrame: The sanitized client data DataFrame
    """
    return df.drop(columns=columns_to_drop)


def sanitize_financial_data(df, columns_to_drop=["cc_n"]):
    """
    Sanitize financial data by dropping specified columns
    Default column to drop is the credit card number column.

    Parameters:
    df (pandas.DataFrame): The financial data DataFrame
    columns_to_drop (list): List of column names to drop from the DataFrame.
                            Default is ["cc_n"].

    Returns:
    pandas.DataFrame: The sanitized financial data DataFrame
    """
    return df.drop(columns=columns_to_drop)


def merge_data(df1, df2, merge_column="id"):
    """
    Merge two DataFrames on the specified column

    Parameters:
    df1 (pandas.DataFrame): The first DataFrame
    df2 (pandas.DataFrame): The second DataFrame
    merge_column (str): The column to merge on. Default is "id"

    Returns:
    pandas.DataFrame: The merged DataFrame
    """
    return pd.merge(df1, df2, on=merge_column)


def rename_columns(
    df,
    column_names_mapping=DEFAULT_RENAME_MAPPINGS,
):
    """
    Rename columns of the dataframe as per the mapping provided.

    Parameters:
    df (pandas.DataFrame): The DataFrame with columns to be renamed
    column_names_mapping (dict): A dictionary containing column renaming mappings,
                                where keys are original column names and values are new column names.
                                    The default mapping is:
                                id -> client_identifier
                                btc_a -> bitcoin_address
                                cc_t -> credit_card_type


    Returns:
    pandas.DataFrame: The DataFrame with renamed columns
    """
    return df.rename(columns=column_names_mapping)
