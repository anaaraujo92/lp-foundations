"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data, clean_data_json
from life_expectancy.regions import Region

def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    input_data = eu_life_expectancy_raw_sample
    eu_life_expectancy_expected = eu_life_expectancy_raw_sample_expected
    cleaned_data = clean_data(input_data, Region.PT)
    cleaned_data.reset_index(drop=True, inplace=True)
    eu_life_expectancy_expected.reset_index(drop=True, inplace=True)
    assert cleaned_data['year'].dtype == 'int64', "Year column type mismatch"
    assert eu_life_expectancy_expected['year'].dtype == 'int64', "Expected year column mismatch"
    pd.testing.assert_frame_equal(cleaned_data, eu_life_expectancy_expected)

def test_clean_data_json(eu_life_expectancy_json_sample, eu_life_expectancy_json_sample_expected):
    """Run the `clean_data_json` function and compare the output to the expected output"""
    input_data = eu_life_expectancy_json_sample
    expected_output = eu_life_expectancy_json_sample_expected
    df_updated = input_data.rename(columns={"country": "region", "life_expectancy": "value"})
    assert "region" in df_updated.columns and "value" in df_updated.columns, "Rename Failed."
    df_cleaned = df_updated.drop(columns=["flag", "flag_detail"])
    assert ("flag" not in df_cleaned.columns and
            "flag_detail" not in df_cleaned.columns), "Exclusion Failed."
    c_life_expec_json = df_cleaned[df_cleaned['region'] == Region.PT.name]
    assert not c_life_expec_json.empty, "Filter by region Failed."
    cleaned_data = clean_data_json(input_data, Region.PT)
    cleaned_data.reset_index(drop=True, inplace=True)
    expected_output.reset_index(drop=True, inplace=True)
    cleaned_data['year'] = cleaned_data['year'].astype('int64')
    expected_output['year'] = expected_output['year'].astype('int64')
    pd.testing.assert_frame_equal(cleaned_data, expected_output)
