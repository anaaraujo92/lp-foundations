from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.regions import Region
import argparse


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "life_expectancy/data"
FIXTURES_DIR = BASE_DIR / "life_expectancy/tests/fixtures"

def create_fixtures(country: Region) -> None:
    """Create fixtures for testing.
    Args: country (Region): The country code to filter the data."""
    original_data = pd.read_csv(DATA_DIR / "eu_life_expectancy_raw.tsv", sep="\t")
    sample_input = original_data.sample(n=100, random_state=0)
    sample_input.to_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample.tsv", index=False, sep="\t")

    sample_output = clean_data(sample_input, country)
    sample_output.to_csv(FIXTURES_DIR / "eu_life_expectancy_raw_sample_expected.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create fixtures for life expectancy data.")
    parser.add_argument('--country', type=str, required=True, help='Country code to filter the data.')
    args = parser.parse_args()
    
    country = Region[args.country]
    