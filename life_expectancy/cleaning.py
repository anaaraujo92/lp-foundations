""" Function for clean data """
import argparse
import pandas as pd

def clean_data(country):
    """Function to load and clean the tsv file for a specific country.

    Returns dataframe cleaned and saved as csv
    """
    raw_data = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t")

    df_data = raw_data.melt(id_vars=["unit,sex,age,geo\\time"],
                                   var_name="year", value_name="value")

    df_data[['unit', 'sex','age', 'region'
             ]] = df_data['unit,sex,age,geo\\time'].str.split(",", expand=True)

    df_data.drop(columns=['unit,sex,age,geo\\time'], inplace=True)
    df_data['year'] = pd.to_numeric(df_data['year'], errors='coerce')
    df_data['value'] = pd.to_numeric(df_data['value'], errors='coerce')
    df_data = df_data.dropna(subset=['value'])
    c_life_expec = df_data[df_data['region'] == country]
    c_life_expec.to_csv(f"life_expectancy/data/{country.lower()}_life_expectancy.csv", index=False)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description=
                                     'Clean life expectancy data for a specific country.')
    parser.add_argument('--country', default='PT',
                        help='Country code for which data should be cleaned (default: PT)')
    args = parser.parse_args()

    clean_data(args.country)
