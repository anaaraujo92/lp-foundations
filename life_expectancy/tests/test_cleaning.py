"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import load_data, clean_data, save_data, main
from . import OUTPUT_DIR

TEST_INPUT_PATH = "life_expectancy/data/eu_life_expectancy_raw.tsv"

def test_clean_data():
    """Run the `clean_data` function and compare the output to the expected output"""
    raw_data = load_data(TEST_INPUT_PATH)
    cleaned_data = clean_data(raw_data, country="PT")
    TEMP_OUTPUT_PATH = "life_expectancy/data/pt_life_expectancy.csv"
    save_data(cleaned_data, TEMP_OUTPUT_PATH)
    pt_life_expectancy_expected = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")
    pt_life_expectancy_actual = pd.read_csv(TEMP_OUTPUT_PATH)
    pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)

def test_main_functionality():
    input_path = "life_expectancy/data/eu_life_expectancy_raw.tsv"
    temp_output_path = "life_expectancy/data/pt_life_expectancy.csv"
    main(input_path, country="PT")
    expected_data = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")
    actual_data = pd.read_csv(temp_output_path)
    pd.testing.assert_frame_equal(actual_data, expected_data)