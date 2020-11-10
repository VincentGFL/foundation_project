from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import Stocks, Orders, Sales

class StockCheck:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        all_stocks = Stocks.query.all()
        for stocks in all_stocks:
            if stocks.name == field.data:
                raise ValidationError(self.message)


