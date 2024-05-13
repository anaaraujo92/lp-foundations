from unittest.mock import patch
import pandas as pd
import pytest
from life_expectancy.loadings_savings import load_data

def test_load_data(eu_life_expectancy_raw_sample):
    """Unit test for load_data function"""

    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw_sample):
        data = load_data("fake_path.csv")
        pd.testing.assert_frame_equal(data, eu_life_expectancy_raw_sample)
