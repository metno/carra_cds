import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-carra-height-levels',
    {
        'format': 'netcdf',
        'domain': 'east_domain',
        'variable': [
            'wind_direction', 'wind_speed',
        ],
        'height_level': [
            '100_m', '150_m', '15_m',
            '200_m', '250_m', '300_m',
            '30_m', '400_m', '500_m',
            '50_m', '75_m',
        ],
        'product_type': 'forecast',
        'time': [
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
        ],
        'leadtime_hour': [
            '1', '2', '3',
        ],
        'year': '2008',
        'month': '03',
        'day': [
            '03', '04',
        ],
    },
    'download.nc')
