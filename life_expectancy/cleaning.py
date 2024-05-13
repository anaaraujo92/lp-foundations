import pandas as pd


def clean_data(df, country="PT") -> pd.DataFrame:
    """Clean the data for a specific country (default country: 'PT')."""
    df_copy = df.copy()
    df_copy.rename(columns={df_copy.columns[0]: 'unit,sex,age,geo_time'}, inplace=True)
    df_copy[['unit', 'sex', 'age', 'geo_time']] = (
        df_copy['unit,sex,age,geo_time'].str.split(',', expand=True)
    )
    df_copy.drop('unit,sex,age,geo_time', axis=1, inplace=True)
    df_melted = df_copy.melt(id_vars=['unit', 'sex', 'age', 'geo_time'],
                             var_name='year', value_name='value')
    df_melted['region'] = df_melted['geo_time'].str[-2:]
    df_melted['year'] = df_melted['year'].str.extract(r'(\d+)').astype('int64')
    df_melted['value'] = pd.to_numeric(df_melted['value'], errors='coerce')
    df_cleaned = df_melted.dropna(subset=['value'])
    c_life_expec = df_cleaned[df_cleaned['region'] == country]
    return c_life_expec
