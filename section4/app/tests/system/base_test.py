from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        app.testing = True #tells flask that we are in testing mode (Error/Exceptions will be displayed differently)
        self.app = app.test_client