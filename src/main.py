import os
import logging
from logging_config import setup_logging
from data_processing import transform_data
from utils import parse_arguments, load_data, save_data


def main():
    setup_logging()

    logging.info("Starting the application")

    args = parse_arguments()

    logging.info("Client data path: %s", args.dp1)
    logging.info("Financial data path: %s", args.dp2)
    logging.info("Countries: %s", args.c)

    client_data, financial_data = load_data(args.dp1, args.dp2)

    final_data = transform_data(client_data, financial_data, args.c)

    save_data(final_data)


if __name__ == "__main__":
    main()
