from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from application.models import Stocks, Orders, Sales

#Check for Stock name, return error if same name in stock name
class StockCheck:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        all_stocks = Stocks.query.all()
        for stocks in all_stocks:
            if stocks.stockname == field.data:
                raise ValidationError(self.message)

#Form for adding new stock
class StockForm(FlaskForm):
    stockname = StringField('Name', validators=[DataRequired(),
                StockCheck(message='Stock name already exist')])
    stockprice = DecimalField('Price', places=2)
    stockinstore = IntegerField('Stock in store')
    stocktype = SelectField('Stock Type', choices=[("keyboard", "Keyboard"),
                                                    ("mouse", "Mouse"),
                                                    ("headset", "Headset"),
                                                    ("game", "Game"),
                                                    ("others", "Other")])
    submit = SubmitField('Submit')
    

