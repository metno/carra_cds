import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-carra-single-levels',
    {
        'format': 'grib',
        'variable': '2m_temperature',
        'level_type': 'surface_or_atmosphere',
        'domain': 'west_domain',
        'product_type': 'analysis',
        'time': [
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
        ],
        'year': '2012',
        'month': '07',
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
    },
    'download.grib')
