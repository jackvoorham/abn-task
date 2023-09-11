import argparse
import pandas as pd
import os


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dp1", help="Path to client dataset", type=str, required=True)
    parser.add_argument(
        "-dp2", help="Path to financial dataset", type=str, required=True
    )
    parser.add_argument(
        "-c", help="List of countries to filter on", type=str, nargs="+"
    )
    return parser.parse_args()


def load_data(client_data_path, financial_data_path):
    client_df = pd.read_csv(client_data_path)
    financial_df = pd.read_csv(financial_data_path)
    return client_df, financial_df


def save_data(data, output_directory=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if output_directory is None:
        output_directory = os.path.join(script_dir, "..", "client_data")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, "data.csv")
    data.to_csv(output_file_path, index=False)
