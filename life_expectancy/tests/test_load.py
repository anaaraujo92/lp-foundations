from unittest.mock import patch
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from life_expectancy.loadings_savings import load_data_json
from life_expectancy.context import Context, ConcreteTsvStrategy

def test_load_data(eu_life_expectancy_raw_sample):
    """Verify the function can load the tsv data from the fixture."""
    # Patch the `read_csv()` function with the mocked one
    with patch("life_expectancy.loadings_savings.pd.read_csv") as mock_read_csv:
        # Define what read_csv should return
        mock_read_csv.return_value = pd.DataFrame()
        # Call the loader method and assert the mocked function was called
        context = Context()
        context.set_strategy(ConcreteTsvStrategy())
        context._strategy.load(eu_life_expectancy_raw_sample)
        mock_read_csv.assert_called_once_with(eu_life_expectancy_raw_sample, sep='\t',
                                              engine='python', index_col=False)
@pytest.fixture
def eu_life_expect_json():
    data = {
        'unit': ['YR', 'YR'],
        'sex': ['F', 'T'],
        'age': ['Y65', 'Y_LT1'],
        'country': ['AT', 'SK'],
        'year': [2021, 1960],
        'life_expectancy': [64.0, 70.3],
        'flag': [None, None],
        'flag_detail': [None, None]
    }
    return pd.DataFrame(data)

def test_load_json(eu_life_expect_json):
    """Verify the function can load the json data from the fixture."""
    # Patch the `read_json()` function with the mocked one
    with patch("life_expectancy.loadings_savings.pd.read_json") as mock_read_json:
        mock_read_json.return_value = eu_life_expect_json
        temp_json_file = "test_data.json"
        eu_life_expect_json.to_json(temp_json_file)
        loaded_df = load_data_json(temp_json_file)
        loaded_df.reset_index(drop=True, inplace=True)
        eu_life_expect_json.reset_index(drop=True, inplace=True)
        assert loaded_df is not None, "Loaded DataFrame is None"
        assert_frame_equal(loaded_df, eu_life_expect_json, check_dtype=False)
