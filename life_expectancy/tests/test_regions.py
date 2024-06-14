"""Tests the Region Enum Module"""

from life_expectancy.regions import Region

def test_valid_regions(expected_regions):
    """Function to verify if the actual list corresponds is equal to the list of countries"""
    assert expected_regions == Region.get_countries()
