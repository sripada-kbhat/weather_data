from weather_api_service import db
from weather_api_service.models.ForecastAudit import ForecastAudit
import sqlalchemy 

def get_top_n_users(n: int) -> (int, str, dict, int):
    try:
        #query ForecastAudit table to get the top n users
        rows = db.session.execute(db.select([
            ForecastAudit.username,
            sqlalchemy.func.count(ForecastAudit.username).label("request_count")
        ]).order_by(sqlalchemy.desc("request_count")).group_by(ForecastAudit.username)).fetchmany(n)
        #iterate over each output row to form the response json 
        top_n_users = []
        for row in rows:
            top_n_users.append({
                'username': row[0],
                'usage_count': row[1]
            })
        message = 'List of Top N Users requesting for forecast'
        status = 200
        totalCount = len(top_n_users)

    except Exception as e:
        top_n_users = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, top_n_users, totalCount

def get_top_n_countries(n: int, country_data: list[dict]) -> (int, str, dict, int):
    try:
        #query ForecastAudit table to get the top n cities
        rows = db.session.execute(db.select([
            ForecastAudit.city,
            sqlalchemy.func.count(ForecastAudit.city).label("request_count")
        ]).order_by(sqlalchemy.desc("request_count")).group_by(ForecastAudit.city)).fetchall()
        #iterate over each row and lookup into country data to get the country from city name. maintain request count for country in a dictonary
        countries_dict = {}
        for row in rows:
            country_row = filter(lambda x: x['name'] == row[0], country_data)
            country = list(country_row)[0]['country']
            if country in countries_dict:
                countries_dict[country] += row[1]
            else:
                countries_dict[country] = row[1]
        #iterate over the country dict to form the response jsonm
        top_n_countries = []
        for key,value in countries_dict.items():
            top_n_countries.append({
                'country': key,
                'usage_count': value
            })
        top_n_countries = sorted(top_n_countries, key=lambda x: x['usage_count'], reverse=True)[:n]
        message = 'List of Top N Countries being requested for forecast'
        status = 200
        totalCount = len(top_n_countries)

    except Exception as e:
        top_n_countries = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, top_n_countries, totalCount

def get_top_n_cities(n: int) -> (int, str, dict, int):
    try:
        #query ForecastAudit table to get the top n cities
        rows = db.session.execute(db.select([
            ForecastAudit.city,
            sqlalchemy.func.count(ForecastAudit.city).label("request_count")
        ]).order_by(sqlalchemy.desc("request_count")).group_by(ForecastAudit.city)).fetchmany(n)
        #iterate over each output row to form the response json 
        top_n_cities = []
        for row in rows:
            top_n_cities.append({
                'city': row[0],
                'usage_count': row[1]
            })
        message = 'List of Top N Cities being requested for forecast'
        status = 200
        totalCount = len(top_n_cities)

    except Exception as e:
        top_n_cities = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, top_n_cities, totalCount
