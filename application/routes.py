from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Stocks, Orders, Sales
from application.form import StockForm, OrderForm, SaleForm

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

#Delete records
@app.route('/delete/<int:id>')
def delete(id):
    stock = Stocks.query.get(id)
    db.session.delete(stock)
    db.session.commit()
    return redirect(url_for('index'))

#Order Form
@app.route('/order', methods=['POST', 'GET'])
def order():
    order = Orders.query.all()
        
    return render_template('order.html', title='Order', order=order)

#Add Order Form
@app.route('/addorder', methods=['POST', 'GET'])
def addorder():
    form = OrderForm()
    if form.validate_on_submit():
        order = Orders(date = form.date.data)     
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('order'))
    return render_template('addorder.html', title='Add an Order', form=form)

#Delete records for order
@app.route('/deleteorder/<int:id>')
def deleteorder(id):
    order = Orders.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('order'))

#Update records for order
@app.route('/updateorder/<int:id>', methods=['POST', 'GET'])
def updateorder(id):
    form = OrderForm()
    formsale = SaleForm()
    formstock = StockForm()
    order = Orders.query.get(id)
    sale = Sales.query.all()
    stock = Stocks.query.all()
    orderlist = []
    for order in Orders.query.all():
        choices = [(stock.id, stock.stockname) for stock in Stocks.query.all()]
        formsale.stocklist.choices = choices
        if formsale.validate_on_submit():
            orderlist.append(formsale.stocklist.data)
    if form.validate_on_submit():
        order.date = form.date.data
        db.session.commit()
        return redirect(url_for('order'))
    elif request.method == 'GET':
        form.date.data = order.date

    return render_template('updateorder.html', title='Update order information', form=form, formsale=formsale, formstock=formstock)
