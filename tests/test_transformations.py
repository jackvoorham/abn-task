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
