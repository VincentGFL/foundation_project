import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Stocks, Orders, Sales

# Set test variables for test admin user
test_name = "BlackWidow"
test_price = 120
test_instore = 130
test_type = "Keyboard"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
        app.config['SECRET_KEY'] = "Hererer"
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/linguofu303/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAddStock(TestBase):

    def test_addstock(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be 
        redirected to the login page
        """

        # Click add a stock link
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)

        # Fill in add a stock form
        self.driver.find_element_by_xpath('//*[@id="stockname"]').send_keys(test_name)
        self.driver.find_element_by_xpath('//*[@id="stockprice"]').send_keys(
            test_price)
        self.driver.find_element_by_xpath('//*[@id="stockinstore"]').send_keys(
            test_instore)
        self.driver.find_element_by_xpath('//*[@id="stocktype"]').send_keys(
            test_type)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to index page
        assert url_for('index') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
