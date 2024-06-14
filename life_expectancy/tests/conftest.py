"""Pytest configuration file"""
from pathlib import Path
import pandas
import pytest

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pandas.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pandas.read_csv(Path(__file__).parent / "fixtures" / "pt_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample() -> pandas.DataFrame:
    """Fixture to load a sample of the eu_life_expectancy.tsv file to serve as 
    input of the cleaning script"""
    return pandas.read_csv(Path(__file__).parent / "fixtures" /
                           "eu_life_expectancy_raw_sample.tsv", sep="\t")


@pytest.fixture(scope="session")
def eu_life_expectancy_raw_sample_expected() -> pandas.DataFrame:
    """Fixture to load the expected output of cleaning 
    the eu_life_expectancy_raw_sample.tsv file"""
    return pandas.read_csv(Path(__file__).parent / "fixtures" /
                           "eu_life_expectancy_raw_sample_expected.csv")

@pytest.fixture(scope="session")
def expected_regions():
    """Fixture to get the list of the expected countries"""
    return [
        'AL', 'AM', 'AT', 'AZ', 'BE', 'BG', 'BY', 'CH', 'CY', 'CZ',  'DE', 'DK', 'EE', 'EL',
        'ES', 'FI', 'FT', 'FR', 'FX', 'GE', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU',
        'LV', 'MD', 'ME', 'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'RU', 'SE','SI',
        'SK', 'SM', 'TR', 'UA', 'UK', 'XK'
    ]
