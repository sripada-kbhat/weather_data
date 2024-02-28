import requests
from weather_api_service.config import *
from weather_api_service.models.ForecastAudit import ForecastAudit as ForecastAudit
from weather_api_service import db

def get_forecast(city: str, days: str, current_user: str)-> (int, str, dict, int):
    try:
        #audit the request from user 
        audit_request(city, days, current_user)
        #form the GET url params for weather API forecast endpoint
        forecast_params = '?q={city}&days={days}&alerts=no&aqi=no&key={key}'.format(city=city, days=str(days), key= weather_api_key)
        weather_api_forecast_url = weather_api_base_url + '/forecast.json' + forecast_params
        #call weather API forecast endpoint
        forecast_response = requests.get(weather_api_forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            message = 'Forecast for {city} for {days} days'.format(city=city, days=days)
            status = 200
            totalCount = len(forecast_data['forecast']['forecastday'])
            return status, message, forecast_data, totalCount
        else:
            forecast_data = None
            message = forecast_response.reason
            status = forecast_response.status_code
            totalCount = None
            return status, message, forecast_data, totalCount

    except Exception as e:
        forecast_data = None
        message = str(e)
        status = 500
        totalCount = None

    return status, message, forecast_data, totalCount

def audit_request(city: str, days: str, current_user: str) -> None:
    try:
        audit_row = ForecastAudit(current_user, city, days)
        db.session.add(audit_row)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
