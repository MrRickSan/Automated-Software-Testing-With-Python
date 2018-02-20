# This coding exercise requires you to complete two method implementations.

# The franchise  method, which takes in a store as argument. It should return
#  a new Store  object, with a name equal to the argument + " - franchise" .
# The store_details  method, which also takes in a store as argument. It should
#  return a string representing the argument.

# A few examples:
# store = Store("Test")
# store2 = Store("Amazon")
# store2.add_item("Keyboard", 160)
 
# Store.franchise(store)  # returns a Store with name "Test - franchise"
# Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
 
# Store.store_details(store)  # returns "Test, total stock price: 0"
# Store.store_details(store2)  # returns "Amazon, total stock price: 160"

# When completing the store_details  method, you may need to convert the output
#  of store.stock_price  to an integer. You can do this like so: int(store.stock_price) .

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")
        
    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return("{}, total stock price: {}".format(store.name, int(store.stock_price())))

store = Store("Wallmart")
store.add_item("Mouse", 80)
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)
Store.store_details(store)