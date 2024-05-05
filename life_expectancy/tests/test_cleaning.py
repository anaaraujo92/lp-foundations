import pandas as pd
import pytest
from unittest.mock import patch
from life_expectancy.cleaning import clean_data, save_data, main
from life_expectancy.tests.new_fixtures import create_input_fixture, create_expected_fixture
from . import OUTPUT_DIR

TEST_INPUT_PATH = "life_expectancy/data/eu_life_expectancy_raw.tsv"

# Fixture for input data
@pytest.fixture
def input_fixture(country="PT"):
    return create_input_fixture()

# Fixture for expected output
@pytest.fixture
def expected_fixture(input_fixture: None):
    return create_expected_fixture(input_fixture)

def test_clean_data(input_fixture: None):
    """Test the clean_data function, mocking pd.DataFrame.to_csv and assert it with the correct arguments."""
    with patch('pd.DataFrame.to_csv') as mock_to_csv:
        clean_data(input_fixture, country="PT")
        mock_to_csv.assert_called_once_with(index=False)

def test_main_functionality(input_fixture: None):
    """Test the main function, mocking pd.DataFrame.to_csv and assert it with the correct arguments."""
    with patch('pd.DataFrame.to_csv') as mock_to_csv:
        main(TEST_INPUT_PATH, country="PT")
        mock_to_csv.assert_called_once_with("life_expectancy/data/pt_life_expectancy.csv", index=False)

def test_save_data(input_fixture: None):
    """Test save_data function, mocking pd.DataFrame.to_csv and assert it with the correct arguments."""
    with patch('pd.DataFrame.to_csv') as mock_to_csv:
        save_data(input_fixture, "test_output.csv")
        mock_to_csv.assert_called_once_with(input_fixture, "test_output.csv", index=False)