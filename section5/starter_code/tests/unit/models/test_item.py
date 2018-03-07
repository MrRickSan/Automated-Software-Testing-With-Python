from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):

     def test_create_item(self):
         item = ItemModel("Test", 19.99)

         self.assertEqual(item.name, 'Test',
                          "The name of the item after creation does not equal the contructor argument.")
         self.assertEqual(item.price, 19.99,
                          "The price of the item after creation does not equal the contructor argument.")

     def test_item_json(self):
         item = ItemModel('Test', 19.99)
         expected = {
             'name': 'Test',
             'price': 19.99 }

         self.assertDictEqual(item.json(), expected,
                              "The json export of the item is incorrect. Received {}, expected {}.".format(item.json(),
                                                                                                           expected))