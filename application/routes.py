from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Stocks, Orders, Sales
from application.form import StockForm

@app.route('/', methods=['POST', 'GET'])
def index():
    stocks = Stocks.query.all()

    return render_template('index.html', title='Stock Checking')

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = StockForm()
    if form.validate_on_submit():
        stock = Stocks(
                stockname = form.stockname.data,
                stockprice = form.stockprice.data,
                stockinstore = form.stockinstore.data,
                stocktype = form.stocktype.data)
        db.session.add(stock)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new stock", form=form)

