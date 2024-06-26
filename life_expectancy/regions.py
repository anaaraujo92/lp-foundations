from enum import Enum, auto

class Region(Enum):
    """Class to handle the different regions"""
    AL = auto()
    AM = auto()
    AT = auto()
    AZ = auto()
    BE = auto()
    BG = auto()
    BY = auto()
    CH = auto()
    CY = auto()
    CZ = auto()
    DE = auto()
    DE_TOT = auto()
    DK = auto()
    EA18 = auto()
    EA19 = auto()
    EE = auto()
    EEA30_2007 = auto()
    EEA31 = auto()
    EFTA = auto()
    EL = auto()
    ES = auto()
    EU27_2007 = auto()
    EU27_2020 = auto()
    EU28 = auto()
    FI = auto()
    FT = auto()
    FR = auto()
    FX = auto()
    GE = auto()
    HR = auto()
    HU = auto()
    IE = auto()
    IS = auto()
    IT = auto()
    LI = auto()
    LT = auto()
    LU = auto()
    LV = auto()
    MD = auto()
    ME = auto()
    MK = auto()
    MT = auto()
    NL = auto()
    NO = auto()
    PL = auto()
    PT = auto()
    RO = auto()
    RS = auto()
    RU = auto()
    SE = auto()
    SI = auto()
    SK = auto()
    SM = auto()
    TR = auto()
    UA = auto()
    UK = auto()
    XK = auto()

    @classmethod
    def get_countries(cls):
        """Function to filter non-countries"""
        non_countries = {"DE_TOT", "EA18", "EA19", "EEA30_2007", "EEA31", "EFTA",
                          "EU27_2007", "EU27_2020", "EU28"}
        return [reg.name for reg in cls if reg.name not in non_countries]
