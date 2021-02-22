import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-carra-single-levels',
    {
        'format': 'grib',
        'domain': 'west_domain',
        'level_type': 'surface_or_atmosphere',
        'variable': 'total_precipitation',
        'product_type': 'forecast',
        'time': [
            '00:00', '12:00',
        ],
        'leadtime_hour': [
            '6', '9', '12',
            '15', '18',
        ],
        'year': '2017',
        'month': '09',
        'day': [
            '14', '15',
        ],
    },
    'download.grib')
