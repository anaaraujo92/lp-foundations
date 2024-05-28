"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.regions import Region

def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    input_data = eu_life_expectancy_raw_sample

    eu_life_expectancy_expected = eu_life_expectancy_raw_sample_expected

    cleaned_data = clean_data(input_data, Region.PT)
    cleaned_data.reset_index(drop=True, inplace=True)
    eu_life_expectancy_expected.reset_index(drop=True, inplace=True)
    cleaned_data['year'] = cleaned_data['year'].astype('int64')
    eu_life_expectancy_expected['year'] = eu_life_expectancy_expected['year'].astype('int64')
    pd.testing.assert_frame_equal(
        cleaned_data, eu_life_expectancy_expected
    )
