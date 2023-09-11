import argparse
import pandas as pd
import os


def parse_arguments():
    """
    Parse the command line arguments and return them

    Returns:
    argparse.Namespace: The parsed arguments
    """

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
    """
    Load the client and financial data from the specified paths

    Parameters:
    client_data_path (str): The path to the client data
    financial_data_path (str): The path to the financial data

    Returns:
    tuple: A tuple containing the client and financial data DataFrames
    """

    client_df = pd.read_csv(client_data_path)
    financial_df = pd.read_csv(financial_data_path)
    return client_df, financial_df


def save_data(data, output_directory=None):
    """
    Save the data to the specified output directory

    Parameters:
    data (pandas.DataFrame): The data to save
    output_directory (str): The output directory to save the data to, default is None which saves to the client_data directory
    """

    script_dir = os.path.dirname(os.path.abspath(__file__))
    if output_directory is None:
        output_directory = os.path.join(script_dir, "..", "client_data")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file_path = os.path.join(output_directory, "data.csv")
    data.to_csv(output_file_path, index=False)
