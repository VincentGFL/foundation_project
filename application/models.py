from application import db

class Stocks(db.Model):
    id = db.Cloumn(db.Integer, primary_key=True)
    name = db.Cloumn(db.String(30), nullable=False, unique=True)
    price = db.Cloumn(db.Float(6,2), nullable=False)
    instore = db.Column(db.Integer, default=0)
    stype = db.Column(db.String(30), nullable=False)

class Orders(db.Model):
    id = db.Cloumn(db.Integer, primary_key=True)
    date = db.Cloumn(db.DateTime)

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stocks_id = db.Column('stocks_id', db.Integer, db.ForeignKey('stocks.id'))
    orders_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))
