from flask import request, make_response
from weather_api_service import app, db, secret_key, getResponseHeaders
from weather_api_service.models.HttpResponse import HttpResponse
from weather_api_service.services import Geo as geo_service
import json


@app.route('/countries', methods=['GET'])
def countries():
    try:
        country_file = './weather_api_service/data/country_data.json'
        infile = open(country_file , encoding='UTF-8')
        country_data = json.load(infile)
        status, message, data, totalCount = geo_service.get_countries_list(country_data)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

@app.route('/cities', methods=['POST'])
def cities():
    try:
        payload: dict = request.json
        country: str = payload.get('country', None)
        country_file = './weather_api_service/data/country_data.json'
        infile = open(country_file , encoding='UTF-8')
        country_data = json.load(infile)
        status, message, data, totalCount = geo_service.get_cities_list(country_data, country)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())
