import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-carra-model-levels',
    {
        'format': 'netcdf',
        'variable': [
            'cloud_cover', 'graupel', 'specific_cloud_ice_water_content',
            'specific_cloud_liquid_water_content', 'specific_cloud_rain_water_content', 'specific_cloud_snow_water_content',
        ],
        'model_level': [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31', '32', '33',
            '34', '35', '36',
            '37', '38', '39',
            '40', '41', '42',
            '43', '44', '45',
            '46', '47', '48',
            '49', '50', '51',
            '52', '53', '54',
            '55', '56', '57',
            '58', '59', '60',
            '61', '62', '63',
            '64', '65',
        ],
        'product_type': 'analysis',
        'time': [
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
        ],
        'year': '2018',
        'month': '09',
        'day': [
            '27', '28',
        ],
        'domain': 'west_domain',
    },
    'download.nc')
