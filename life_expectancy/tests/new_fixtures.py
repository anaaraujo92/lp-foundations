from pathlib import Path
import pandas as pd
from life_expectancy.cleaning import clean_data

DATA_DIR = Path("C:/Users/afaraujo/OneDrive - Hovione/Documents/DareData/Foundations-LP/assignments/life_expectancy/data")
FIXTURES_DIR = Path("C:/Users/afaraujo/OneDrive - Hovione/Documents/DareData/Foundations-LP/assignments/life_expectancy/tests/fixtures")

if __name__ == "__main__":
    original_data = pd.read_csv(DATA_DIR /
                                "eu_life_expectancy_raw.tsv", sep="\t")
    sample_input = original_data.sample(n=100, random_state=0)
    sample_input.to_csv(FIXTURES_DIR /
                           "eu_life_expectancy_raw_sample.tsv",
                            index=False, sep="\t")

    sample_output = clean_data(sample_input)
    sample_output.to_csv(FIXTURES_DIR /
                            "eu_life_expectancy_raw_sample_expected.csv",
                            index=False)
