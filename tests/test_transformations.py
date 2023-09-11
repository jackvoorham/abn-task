import pandas as pd
from src.transformations import (
    filter_by_countries,
    sanitize_client_data,
    sanitize_financial_data,
    merge_data,
    rename_columns,
)


def test_filter_by_countries():
    test_data = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "country": ["United Kingdom", "Netherlands", "France", "Spain"],
        }
    )

    result = filter_by_countries(test_data, ["United Kingdom", "Netherlands"])

    # Assert properties
    assert result.shape == (2, 2)
    assert "France" not in result["country"].values
    assert "Spain" not in result["country"].values


def test_sanitize_client_data():
    test_data = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "first_name": ["John", "Jane", "Mary"],
            "last_name": ["Doe", "Doe", "Smith"],
        }
    )

    result = sanitize_client_data(test_data)

    # Assert properties
    assert result.shape == (3, 1)
    assert "first_name" not in result.columns
    assert "last_name" not in result.columns


def test_sanitize_financial_data():
    test_data = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "cc_n": ["1234", "5678", "9012", "3456"],
        }
    )

    result = sanitize_financial_data(test_data)

    # Assert properties
    assert result.shape == (4, 1)
    assert "cc_n" not in result.columns