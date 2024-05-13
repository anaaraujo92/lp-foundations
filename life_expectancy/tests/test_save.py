from unittest.mock import patch
import pandas as pd
import pytest
from life_expectancy.loadings_savings import save_data

def test_save_data():
    """Unit test for save_data method"""

    with patch('pandas.DataFrame.to_csv') as mock_to_csv:

        df = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['A', 'B', 'C']
        })

        save_data(df, "fake_data.csv")

        mock_to_csv.assert_called_once_with("fake_data.csv", index=False)

if __name__ == "__main__":
    pytest.main([__file__])
