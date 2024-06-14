"""Context Interface and Strategies"""

# Import libraries
from enum import Enum
from abc import ABC, abstractmethod
from pandas import DataFrame
import pandas as pd
from life_expectancy.regions import Region
from life_expectancy.loadings_savings import load_data_json, save_data
from life_expectancy.cleaning import clean_data, clean_data_json

class Strategy(ABC):
    """
    Strategy interface which declares the common operations.
    """
    @abstractmethod
    def load(self, path: str) -> DataFrame:
        pass
    @abstractmethod
    def clean(self, df: DataFrame, region_filter: Enum) -> DataFrame:
        pass
    @abstractmethod
    def save(self, df: DataFrame, path: str) -> None:
        pass

class ConcreteTsvStrategy(Strategy):
    def load(self, path):
        df = pd.read_csv(path, sep='\t', engine='python', index_col=False)
        return df
    def clean(self, df: DataFrame, region_filter: Enum) -> DataFrame:
        region = Region(region_filter)  
        return clean_data(df, region)
    def save(self, df: DataFrame, path: str) -> None:
        save_data(df, path)

class ConcreteJsonStrategy(Strategy):
    def load(self, path: str) -> DataFrame:
        return load_data_json(path)
    def clean(self, df: DataFrame, region_filter: Enum) -> DataFrame:
        return clean_data_json(df, region_filter)
    def save(self, df: DataFrame, path: str) -> None:
        save_data(df, path)

class Context:
    """
    Class which implements the Context object.
    It defines the interface for the defined strategies.
    """

    def __init__(self, strategy=None) -> None:
        """Initialize Context object."""
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """Allowing the Context to define the strategy object."""
        self._strategy = strategy

    def get_strategy(self) -> Strategy:
        """Allowing the Context to get the strategy object."""
        return self._strategy

    def data_workflow(self, input_path: str, region: Enum, output_path: str) -> None:
        """Steps to load, clean, and save the data."""
        if self._strategy is None:
            raise ValueError("Strategy is not set.")
        df = self._strategy.load(input_path)
        clean_df = self._strategy.clean(df, region)
        self._strategy.save(clean_df, output_path)
