from weather_api_service import db
from datetime import datetime

class ForecastAudit(db.Model):
    __tablename__ = 'forecast_audit'
    audit_id = db.Column(db.String(255), primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    days = db.Column(db.String(255), nullable=False)

    def __init__(self, username, city, days):
        self.audit_id = datetime.now()
        self.username = username
        self.city = city
        self.days = days

    def to_json(self):
        return dict(
            username=self.username,
            city=self.city,
            days=self.days
        )
