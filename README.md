# ABN Interview Task

This repository contains the code for the ABN assignemnt. It offers a way to process the two datasets. We have implemented a command line app and a Flask Rest API.

## Folder Structure

- **README.md** - This file
- **.gitignore**
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
