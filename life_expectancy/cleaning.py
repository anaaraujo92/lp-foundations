""" Function for clean data """
import argparse
import pandas as pd

def clean_data(country="PT"):
    """Function to load and clean the tsv file for a specific country.

    Returns dataframe cleaned and saved as csv
    """
    df = pd.read_csv("life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t")
    df.columns =  [col.replace("\\","") for col in df.columns]

    df_melt = df.melt(id_vars=["unit,sex,age,geotime"],
                                   var_name="year", value_name="value")

    df_melt[['unit', 'sex','age', 'region'
             ]] = df_melt['unit,sex,age,geotime'].str.split(",", expand=True)

    df_melt.drop(columns=['unit,sex,age,geotime'], inplace=True)
    df_melt['year'] = df_melt['year'].str.extract(r'(\d+)').astype(int)
    df_melt['value'] = pd.to_numeric(df_melt['value'], errors='coerce')
    df_melt = df_melt.dropna(subset=['value'])
    c_life_expec = df_melt[df_melt['region'] == country]
    # adjust index and columns
    c_life_expec.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']
    c_life_expec = c_life_expec[['unit', 'sex', 'age', 'region', 'year','value']]
    c_life_expec.to_csv("life_expectancy/data/pt_life_expectancy.csv", index=False)
    return c_life_expec
if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()
    clean_data(args.country)
