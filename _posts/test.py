DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    ]

>>> country_code = {country: code for code, country in DIAL_CODES}
>>> country_code
{'Brazil': 55, 'Indonesia': 62, 'Pakistan': 92, 'Russia': 7, 'China': 86, 'United States': 1, 'Japan': 81, 'India': 91, 'Nigeria': 234, 'Bangladesh': 880}
>>> {code: country.upper() for country, code in country_code.items() if code < 66}
{1: 'UNITED STATES', 7: 'RUSSIA', 62: 'INDONESIA', 55: 'BRAZIL'}