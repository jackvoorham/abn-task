# ABN Interview Task

This repository contains the code for the ABN assignment. It offers a way to process the two datasets. We have implemented a command line app and a Flask Rest API.

## High Level Overview

As for a high level overview of the core logic of the app the following steps are done. First, we load the datasets. Then, the datasets are sanizitzed, removing Personal Identifiable Information. We remove the first and second name from the first dataset and credit card number from the second dataset. Subsequently, the first dataset undergoes a filtering process to only retain the data of clients in specified countries. In our case, the default is the UK and The Netherlands. Then the sanitized datasets are merged together on the **id** field. After this, we rename the columns to improve readability of the dataset for users.

## Folder Structure

- **README.md** - This file
- **requirements.txt** - Requirements to run scripts
- **.gitignore**
- **logs/** - Folder to store log files
- **client_data/**
  - **data.csv** - The final, processed dataset
- **raw_data/**
  - **dataset_one.csv** - The first dataset
  - **dataset_two.csv** - The second dataset
- **src/**
  - **data_processing.py** - Script containing functions for the full processing pipeline
  - **logging_config.py** - Script containing the logging configuration
  - **main.py** - Main script for the command line application
  - **transformations.py** - Script containing the necessary transformation functions
  - **utils.py** - Script containing the utility functions
  - **flask/**
    - **app.py** - Script containing the Flask endpoint
- **tests/**
  - **test_transformations.py** - Script containing tests for transformation functions

## Running The Application

To clone and install the requirements:

```sh
git clone <repository_url>
cd abn-task
pip install -r requirements.txt
```

### Running The Command Line App

To run the command line app, we can run from root:

```sh
python src/main.py -dp1 ./raw_data/dataset_one.csv -dp2 ./raw_data/dataset_two.csv -c "United Kingdom,Netherlands"
```

Where

**-dp1** specifies the path to the first dataset,
**-dp2** specifies the path to the second dataset, and
**-c** specifies the countries to filter, separated by commas. This can also be skipped, whereas the default of United Kingdom and Netherlands is used.

This command will process the data in the specified datasets filtering for the United Kingdom and Netherlands. The processed data will be stored in the **client_data/data.csv** file.

### Runing The Flask App

To run the Flask app from the root directory, use the following command:

```sh
python src/flask/app.py
```

This will initiate the Flask application on your local machine. By default, the application will start on port 5000. You can access it by visiting http://127.0.0.1:5000 in your web browser.

The endpoints are as following:

- **POST /process_data**  
  To process data using tis endpoint, you can use a curl command like below:

  ```sh
  curl -X POST \
  -F "dp1=./raw_data/dataset_one.csv" \
  -F "dp2=./raw_data/dataset_two.csv" \
  -F "countries=United Kingdom,Netherlands" \
  http://127.0.0.1:5000/process_data
  ```

Here,

- **dp1**: Specifies the path to the first dataset (relative to the root directory).
- **dp2**: Specifies the path to the second dataset (relative to the root directory).
- **countries**: Specifies the countries to filter, separated by commas. This parameter can be omitted to use the default countries (United Kingdom and Netherlands).

Calling this endpoint will result in the processed data.

- **GET /download_data**  
  You can download the processed data file by visiting this URL in your browser:
  [http://127.0.0.1:5000/download_data](http://127.0.0.1:5000/download_data)

## Running The Tests

Tests are available for the transformation functions. To run the tests run in the command line:

```sh
pytest tests/test_transformations.py
```

Which will output a report of all test functions.
