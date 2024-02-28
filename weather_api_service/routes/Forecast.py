from flask import request, make_response
from weather_api_service import app, db, secret_key, getResponseHeaders, token_required
from weather_api_service.models.HttpResponse import HttpResponse
from weather_api_service.services import Forecast as forecast_service
import json

@app.route('/forecast', methods=['POST'])
@token_required
def forecast(current_user):
    try:
        payload: dict = request.json
        city: str = payload.get('city', None)
        days: int = payload.get('days', None)
        if days > 14 or days < 0:
            status, message, data, totalCount = (400, 'Invalid values for days in payload. days should be between 0 and 14', None, None)
        else:
            status, message, data, totalCount = forecast_service.get_forecast(city, days, current_user)
        response = HttpResponse(message=message, status=status, data=data, totalCount=totalCount)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())
