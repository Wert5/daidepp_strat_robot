from typing_extensions import Literal

POWER = Literal["AUS", "ENG", "FRA", "GER", "ITA", "RUS", "TUR"]
UNIT_TYPE = Literal["AMY", "FLT"]

PROVINCE_LAND_SEA = Literal[
    "ALB",
    "ANK",
    "APU",
    "ARM",
    "BEL",
    "BER",
    "BRE",
    "BUL",
    "CLY",
    "CON",
    "DEN",
    "EDI",
    "FIN",
    "GAS",
    "GRE",
    "HOL",
    "KIE",
    "LON",
    "LVN",
    "LVP",
    "MAR",
    "NAF",
    "NAP",
    "NWY",
    "PIC",
    "PIE",
    "POR",
    "PRU",
    "ROM",
    "RUM",
    "SEV",
    "SMY",
    "SPA",
    "STP",
    "SWE",
    "SYR",
    "TRI",
    "TUN",
    "TUS",
    "VEN",
    "YOR",
    "WAL",
]
PROVINCE_LANDLOCK = Literal[
    "BOH",
    "BUD",
    "BUR",
    "MOS",
    "MUN",
    "GAL",
    "PAR",
    "RUH",
    "SER",
    "SIL",
    "TYR",
    "UKR",
    "VIE",
    "WAR",
]
PROVINCE_SEA = Literal[
    "ADR",
    "AEG",
    "BAL",
    "BAR",
    "BLA",
    "BOT",
    "EAS",
    "ENG",
    "HEL",
    "ION",
    "IRI",
    "LYO",
    "MAO",
    "NAO",
    "NTH",
    "NWG",
    "SKA",
    "TYS",
    "WES",
]
PROVINCE_COAST = Literal[
    "STP NCS", "STP SCS", "SPA NCS", "SPA SCS", "BUL ECS", "BUL SCS"
]
PROVINCE = Literal[PROVINCE_LAND_SEA, PROVINCE_LANDLOCK, PROVINCE_SEA, PROVINCE_COAST]
PROVINCE_NO_COAST = Literal[PROVINCE_LAND_SEA, PROVINCE_LANDLOCK, PROVINCE_SEA]

SEASON = Literal["SPR", "SUM", "FAL", "AUT", "WIN"]

TRY_TOKENS = Literal[
    "PRP",
    "PCE",
    "ALY",
    "VSS",
    "DRW",
    "SLO",
    "NOT",
    "NAR",
    "YES",
    "REJ",
    "BWX",
    "FCT",
    "XDO",
    "DMZ",
    "AND",
    "ORR",
    "SCD",
    "OCC",
    "CHO",
    "INS",
    "QRY",
    "THK",
    "IDK",
    "SUG",
    "HOW",
    "WHT",
    "EXP",
    "SRY",
    "FOR",
    "IFF",
    "XOY",
    "YDO",
    "SND",
    "FWD",
    "BCC",
    "WHY",
    "POB",
]

SUPPLY_CENTER = Literal[
    "ANK",
    "BEL",
    "BER",
    "BRE",
    "BUD",
    "BUL",
    "CON",
    "DEN",
    "EDI",
    "GRE",
    "HOL",
    "KIE",
    "LON",
    "LVP",
    "MAR",
    "MOS",
    "MUN",
    "NAP",
    "NWY",
    "PAR",
    "POR",
    "ROM",
    "RUM",
    "SER",
    "SEV",
    "SMY",
    "SPA",
    "STP",
    "SWE",
    "TRI",
    "TUN",
    "VEN",
    "VIE",
    "WAR",
]
