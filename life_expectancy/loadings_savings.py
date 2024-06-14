"""
Script for loading and saving the data

This script loads life expectancy data from a TSV file, cleans it, and then saves it to a CSV file.
"""

import argparse
import json
import pandas as pd
from life_expectancy.cleaning import clean_data

def load_data(path) -> pd.DataFrame:
    """Load data from a TSV file.
    Args:
        path (str): The path to the TSV file.
    Returns:
        pd.DataFrame: The loaded data as a DataFrame."""
    df = pd.read_csv(path, sep="\t")
    df.columns = [col.replace("\\", "") for col in df.columns]
    return df

def load_data_json(path) -> pd.DataFrame:
    """Load data from a JSON file.
    Args:
        path (str): The path to the JSON file.
    Returns:
        pd.DataFrame: The loaded data as a DataFrame."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            # Optionally reorder columns if needed
            return df
    except FileNotFoundError as e:
        print(f"File '{path}' not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{path}': {e}")
        return None

def save_data(df, path) -> None:
    """Save the data to a CSV file.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        path (str): The path to the output CSV file."""
    df.to_csv(path, index=False)

def main(path="life_expectancy/data/eu_life_expectancy_raw.tsv", country="PT"):
    """Main function to load, clean, and save data.
    Args:
        path (str): The path to the input TSV file.
        country (str): The country code to filter the data."""
    df = load_data(path)
    cleaned_data = clean_data(df, country)
    save_data(cleaned_data, "life_expectancy/data/pt_life_expectancy.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='life_expectancy/data/eu_life_expectancy_raw.tsv')
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()
    main(args.path, args.country)
