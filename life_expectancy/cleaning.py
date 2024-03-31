import argparse
import pandas as pd

def load_data(path):
    """Load data from a TSV file."""
    df = pd.read_csv(path, sep="\t")
    df.columns = [col.replace("\\", "") for col in df.columns]
    return df

def clean_data(df, country="PT"):
    """Clean the data to a specific country."""
    df_melt = df.melt(id_vars=["unit,sex,age,geotime"],
                      var_name="year", value_name="value")
    df_melt[['unit', 'sex', 'age', 'region'
             ]] = df_melt['unit,sex,age,geotime'].str.split(",", expand=True)
    df_melt.drop(columns=['unit,sex,age,geotime'], inplace=True)
    df_melt['year'] = df_melt['year'].str.extract(r'(\d+)').astype(int)
    df_melt['value'] = pd.to_numeric(df_melt['value'], errors='coerce')
    df_melt = df_melt.dropna(subset=['value'])
    c_life_expec = df_melt[df_melt['region'] == country]
    return c_life_expec

def save_data(df, path):
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
