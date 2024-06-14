import pandas as pd
from .regions import Region

def clean_data(df: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Clean the data for a specific country."""
    df_copy = df.copy()
    df_copy.rename(columns={df_copy.columns[0]: 'unit,sex,age,geo_time'}, inplace=True)
    df_copy[['unit', 'sex', 'age', 'geo_time']] = df_copy['unit,sex,age,geo_time'
                                                          ].str.split(','
    , expand=True)
    df_copy.drop('unit,sex,age,geo_time', axis=1, inplace=True)
    df_melted = df_copy.melt(id_vars=['unit', 'sex', 'age',
                                      'geo_time'], var_name='year', value_name='value')
    df_melted['region'] = df_melted['geo_time'].str[-2:]
    df_melted['year'] = df_melted['year'].str.extract(r'(\d+)').astype('int64')
    df_melted['value'] = pd.to_numeric(df_melted['value'], errors='coerce')
    df_cleaned = df_melted.dropna(subset=['value'])
    c_life_expec = df_cleaned[df_cleaned['region'] == country.name]
    return c_life_expec

def clean_data_json(df: pd.DataFrame, region: Region) -> pd.DataFrame:
    """
    Function which cleans a DataFrame created from life expectancy json file by:
        - Renaming 'country' to 'region' and 'life_expectancy' to 'value' columns.
        - Dropping 'flag' and 'flag_detail' columns.
        - Filtering the DataFrame by region.
    Args:
        - df: DataFrame: Loaded json file as Pandas DataFrame.
        - region: Enum which will filter the DataFrame by region.
    Returns:
        - df_filt: DataFrame: Cleaned Pandas DataFrame.
    """
    df_updated = df.rename(columns={"country": "region", "life_expectancy": "value"})
    df_cleaned = df_updated.drop(columns=["flag", "flag_detail"])
    df_filtered = df_cleaned[df_cleaned['region'] == region.name]
    return df_filtered
