
# tests/test_routes.py

import unittest
from game import app,db
from game.forms import User

class TestRoutes(unittest.TestCase):

    """
    each test must begin with the 'test' name
    They use assertions to verify expected behavior or outcomes.
    self.app.get('/login'): Sends a GET request to the specified route.
    response.status_code, response.data: Accesses the response status code and data.
    self.assertEqual(), self.assertIn(): Asserts that the actual value matches the expected value. 
    """

    # Define a setUp method to be executed before each test method
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        
        # Set up the Flask application context and create a test database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/gamer'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.create_all()
        self.app_context = app.app_context()
        self.app_context.push()

    # Define a test method for testing the login page
    def test_login_page(self):
        # Send a GET request to the login page
        response = self.app.get('/login')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data contains the word "Login"
        self.assertIn(b'Login', response.data)

    # follows from the above code
    def test_sign_up(self):
        response = self.app.get('/Register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    # Define a test method for testing the booking page without authentication
    def booking_page_test(self):
        response = self.app.get('/Bookings')
        # Assert that the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)  # 302 is for redirection
        # Assert that the response data contains a redirection to the login page
        self.assertIn(b'Location: http://127.0.0.1/login', response.data)

    def test_database_connection(self):
        # Test database connection by querying a simple record
        """ user = User(username='duke', email_address='duke@hotmail.com', phone_no='0912345678', password_hash='12345')
        db.session.add()
        db.session.commit() """

        queried_user = User.query.filter_by(username='duke').first()

        # adding, updating, Deleting items, query
        if not  queried_user:
            queried_user = User(username='duke', email_address='duke@hotmail.com', phone_no='0912345678', password_hash='12345')
            db.session.add(queried_user)
            db.session.commit()
        
        else:
            queried_user.email_addres = 'duke@gmail.com'

            db.session.delete(queried_user)
            db.session.commit()
       
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email_address, 'duke@hotmail.com')

    

if __name__ == '__main__':
    unittest.main()
