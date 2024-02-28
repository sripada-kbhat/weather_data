
def get_countries_list(country_data: list[dict]) -> (int, str, dict, int):
    try:
        #get unique countries from country data
        unique_countries = list(set(dic['country'] for dic in country_data))
        message = 'List of Countries'
        status = 200
        totalCount = len(unique_countries)

    except Exception as e:
        unique_countries = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, unique_countries, totalCount

def get_cities_list(country_data: list[dict], country: str) -> (int, str, dict, int):
    try:
        #filter country data with the given input country name
        filtered_country_data = filter(lambda x: x['country'] == country, country_data)
        #get unique cities from the filtered country list
        unique_cities = list(set(dic['name'] for dic in filtered_country_data))
        message = 'List of Cities of {country}'.format(country = country)
        status = 200
        totalCount = len(unique_cities)

    except Exception as e:
        unique_cities = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, unique_cities, totalCount
