import pandas as pd
from life_expectancy.cleaning import load_data, clean_data

def create_input_fixture():
    """Create input fixture by sampling data."""
    data = load_data('life_expectancy/data/eu_life_expectancy_raw.tsv')
    sample_data = data.sample(n=300)
    sample_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_raw.tsv',
                        sep='\t', index=False)

def create_expected_fixture(input_fixture, country="PT"):
    """Create expected fixture by cleaning input data."""
    input_data = pd.read_csv(input_fixture, sep='\t')
    cleaned_data = clean_data(input_data, country)
    cleaned_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_expected.csv',
                        index=False)

def main():
    """for main function"""
    create_input_fixture()
    create_expected_fixture('life_expectancy/tests/fixtures/eu_life_expectancy_raw.tsv')

if __name__ == '__main__':
    main()
