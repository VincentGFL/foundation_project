import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Stocks, Orders, Sales

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True)
        return app

    def setUp(self):
        db.create_all()
       # testdata1 = Stocks(stockname="BlackWidow", stockprice=150, stockinstore=100, stocktype="Keyboard")
       # testdata2 = Orders(date="30-05-2010")
       # db.session.add(testdata1)
       # db.session.add(testdata2)
       # db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all

class TestViews(TestBase):
    def test_index_get(self):
       # testdata1 = Stocks(stockname="BlackWidow", stockprice=150, stockinstore=100, stocktype="Keyboard")
       #testdata2 = Orders(date="30-05-2010")
       # db.session.add(testdata1)
       #db.session.add(testdata2)
       # db.session.commit()
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)

#    def test_update_get(self):
#        response = self.client.get(url_for('update', follow_redurects=True))
#        assert request.path == url_for('update/1')
#        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 302)

    def test_order_get(self):
        response = self.client.get(url_for('order'))
        self.assertEqual(response.status_code, 200)

    def test_addorder_get(self):
        response = self.client.get(url_for('addorder'))
        self.assertEqual(response.status_code, 200)

#    def test_order_get(self):
#        response = self.client.get(url_for('updateorder'))
#        self.assertEqual(response.status_code, 200)
#
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add'),
            data =dict(stockname="BlackWidow", stockprice=150, stockinstore=100, stocktype="Keyboard")
        )
        self.assertIn(b'BlackWidow', response.data)

class TestAddOrder(TestBase):
    def test_addorder_post(self):
        response = self.client.post(
            url_for('addorder'),
            data = dict(date="30-05-2010")
        )
        self.assertIn(b'30-05-2010',response.data)
#
#class TestDelete(TestBase):
#    def test_delete_stock(self):
#        uid="/1"
#        response = self.client.post(url_for('delete'),
#                data = dict(stockname="BlackWidow"),
#                follow_redirects=True
#                )
#        self.assertEqual(response.status_code,200)
#
