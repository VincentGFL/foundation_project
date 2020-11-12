from application import db

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stockname = db.Column(db.String(30), nullable=False, unique=True)
    stockprice = db.Column(db.Float(6,2), nullable=False)
    stockinstore = db.Column(db.Integer, default=0)
    stocktype = db.Column(db.String(30), nullable=False)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stocks_id = db.Column('stocks_id', db.Integer, db.ForeignKey('stocks.id'))
    orders_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))
