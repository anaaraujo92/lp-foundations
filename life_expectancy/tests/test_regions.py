"""Tests the Region Enum Module"""

from typing import List
from life_expectancy.regions import Region

def test_valid_regions():
    """
    Test the 'get_countries' class method of the Region enum module.
    
    It verifies that the list of regions returned by the function is equal in size
    and content to the list of expected regions provided as an argument.
    """
    expected_regions = ['AT','FI','FT','ES','EL','EE','DK','DE','CZ','CY','CH','BG','BE','FX','SK','SI',\
    'SE','RO','PT','PL','NO','NL','LU','LT','IT','UK','IS','HU','IE','MT','MK','LI',\
    'FR','RS','HR','LV','UA','TR','ME','AL','AZ','GE','BY','AM','MD','SM','RU','XK'
    ]
    actual_regions: List[str] = Region.get_countries()
    
    assert len(actual_regions) == len(expected_regions)
    assert set(actual_regions) == set(expected_regions)

