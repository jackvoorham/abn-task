from transformations import (
    filter_by_countries,
    sanitize_client_data,
    sanitize_financial_data,
    merge_data,
    rename_columns,
)


def transform_data(client_df, financial_df, countries):
    """
    Transform the client and financial data into the final data set

    Parameters:
    client_df (pandas.DataFrame): The client data DataFrame
    financial_df (pandas.DataFrame): The financial data DataFrame

    Returns:
    pandas.DataFrame: The final data set
    """

    client_df_transformed = client_df.pipe(filter_by_countries, countries).pipe(
        sanitize_client_data
    )

    financial_df_transformed = sanitize_financial_data(financial_df)

    return rename_columns(merge_data(client_df_transformed, financial_df_transformed))
