import argparse
import pandas as pd
from life_expectancy.cleaning import clean_data

def load_data(path) -> pd.DataFrame:
    """Load data from a TSV file."""
    df = pd.read_csv(path, sep="\t")
    df.columns = [col.replace("\\", "") for col in df.columns]
    return df

def save_data(df, path) -> None:
    """Save the data to a CSV file."""
    df.to_csv(path, index=False)

def main(path="life_expectancy/data/eu_life_expectancy_raw.tsv", country="PT"):
    """Main function to load, clean, and save data."""
    df = load_data(path)
    cleaned_data = clean_data(df, country)
    save_data(cleaned_data, "life_expectancy/data/pt_life_expectancy.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='life_expectancy/data/eu_life_expectancy_raw.tsv')
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()
    main(args.path, args.country)
