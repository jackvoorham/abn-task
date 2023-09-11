from flask import Flask, request, send_from_directory
import os
import sys
import logging

sys.path.append("src")
from data_processing import transform_data
from utils import load_data, save_data

app = Flask(__name__)


@app.route("/process_data", methods=["POST"])
def process_data():
    """
    Process the uploaded client and financial data
    """
    client_data_path = request.form["dp1"]
    financial_data_path = request.form["dp2"]
    countries = request.form["countries"].split(",")

    if not countries:
        countries = ["United Kingdom", "Netherlands"]

    client_data, financial_data = load_data(client_data_path, financial_data_path)

    transformed_data = transform_data(client_data, financial_data, countries)
    save_data(transformed_data)

    return "Data process complete", 200


@app.route("/download_data", methods=["GET"])
def download_data():
    """
    Download the processed data from the client_data directory
    """
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    client_data_dir = os.path.join(base_dir, "client_data")

    return send_from_directory(client_data_dir, "data.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
