import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-carra-single-levels',
    {
        'format': 'netcdf',
        'domain': 'west_domain',
        'level_type': 'surface_or_atmosphere',
        'variable': [
            'albedo', 'surface_latent_heat_flux', 'surface_net_solar_radiation',
            'surface_net_thermal_radiation', 'surface_sensible_heat_flux', 'surface_solar_radiation_downwards',
            'surface_thermal_radiation_downwards',
        ],
        'product_type': 'forecast',
        'time': [
            '00:00', '12:00',
        ],
        'leadtime_hour': [
            '6', '9', '12',
            '15', '18',
        ],
        'year': '2012',
        'month': '07',
        'day': '12',
    },
    'download.nc')
