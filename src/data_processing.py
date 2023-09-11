from transformations import (
    filter_by_countries,
    sanitize_client_data,
    sanitize_financial_data,
    merge_data,
    rename_columns,
)


def transform_data(client_df, financial_df, countries):
    client_df_transformed = client_df.pipe(filter_by_countries, countries).pipe(
        sanitize_client_data
    )

    financial_df_transformed = sanitize_financial_data(financial_df)

    return rename_columns(merge_data(client_df_transformed, financial_df_transformed))
