from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Stocks, Orders, Sales
from application.form import StockForm

#Home screen
@app.route('/', methods=['POST', 'GET'])
def index():
    stocks = Stocks.query.all()

    return render_template('index.html', title='Stock Checking', stocks=stocks)
#Add records for stocks
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

#Update existing records
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    form = StockForm()
    stock = Stocks.query.get(id)
    if form.validate_on_submit():
        stock.stockname = form.stockname.data
        stock.stockprice = form.stockprice.data
        stock.stockinstore = form.stockinstore.data
        stock.stocktype = form.stocktype.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.stockname.data = stock.stockname
        form.stockprice.data = stock.stockprice
        form.stockinstore.data = stock.stockinstore
        form.stocktype.data = stock.stocktype
    return render_template('update.html', title='Update stock information', form=form)



