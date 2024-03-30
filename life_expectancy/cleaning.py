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
    
    # Salvar o número total de linhas do DataFrame original
    total_rows_original = df_melt.shape[0]
    
    df_melt = df_melt.dropna(subset=['value'])
    
    # Verificar se o número de linhas do DataFrame limpo corresponde ao número total de linhas do DataFrame original
    if df_melt.shape[0] != total_rows_original:
        print(f"WARNING: Number of rows after cleaning ({df_melt.shape[0]}) is different from total number of rows in the original DataFrame ({total_rows_original})")
    
    c_life_expec = df_melt[df_melt['region'] == country]
    
    # Ajustar índice e colunas para corresponder ao dataframe esperado
    c_life_expec.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']  # Renomear colunas
    c_life_expec = c_life_expec[['unit', 'sex', 'age', 'region', 'year','value']]  # Reordenar colunas

    c_life_expec.to_csv("life_expectancy/data/pt_life_expectancy.csv", index=False)  # Salvar sem índice
    return c_life_expec