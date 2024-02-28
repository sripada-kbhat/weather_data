from flask import request, make_response
from weather_api_service import app, db, secret_key, getResponseHeaders
from weather_api_service.models.HttpResponse import HttpResponse
from weather_api_service.services import Analytics as analytics_service
import json


@app.route('/analytics/top_n_users', methods=['GET'])
def top_n_users():
    try:
        n: int = int(request.args.get('n'))  if request.args.get('n') else 10
        status, message, data, totalCount = analytics_service.get_top_n_users(n)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

@app.route('/analytics/top_n_countries', methods=['GET'])
def top_n_countries():
    try:
        n: int = int(request.args.get('n'))  if request.args.get('n') else 10
        country_file = './weather_api_service/data/country_data.json'
        infile = open(country_file , encoding='UTF-8')
        country_data = json.load(infile)
        status, message, data, totalCount = analytics_service.get_top_n_countries(n, country_data)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

@app.route('/analytics/top_n_cities', methods=['GET'])
def top_n_cities():
    try:
        n: int = int(request.args.get('n'))  if request.args.get('n') else 10
        status, message, data, totalCount = analytics_service.get_top_n_cities(n)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())
