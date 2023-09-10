import logging
import argparse
import pandas as pd
from transformations import (
    filter_by_countries,
    sanitize_client_data,
    sanitize_financial_data,
    merge_data,
    rename_columns,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("Starting the application")

    logging.info("Parsing the arguments")
    parser = argparse.ArgumentParser()

    parser.add_argument("-dp1", help="Path to client dataset", type=str, required=True)
    parser.add_argument(
        "-dp2", help="Path to financial dataset", type=str, required=True
    )
    parser.add_argument(
        "-c", help="List of countries to filter on", type=str, nargs="+", required=True
    )

    args = parser.parse_args()

    logging.info("Client data path: %s", args.dp1)
    logging.info("Financial data path: %s", args.dp2)
    logging.info("Countries: %s", args.c)

    client_df = pd.read_csv(args.dp1)
    financial_df = pd.read_csv(args.dp2)

    client_df_transformed = client_df.pipe(filter_by_countries, args.c).pipe(
        sanitize_client_data
    )

    financial_df_transformed = sanitize_financial_data(financial_df)

    final_data = rename_columns(
        merge_data(client_df_transformed, financial_df_transformed)
    )

    print(final_data.head())
