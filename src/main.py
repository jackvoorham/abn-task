import logging
import argparse

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
