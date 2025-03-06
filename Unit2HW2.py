class Restaurant:
    """Creates a restaurant scenario"""

    def __init__(self, restaurant_name: str, num_customers: int, open_time: int)->None:
        
        self.restaurant_name = restaurant_name
        self.num_customers = num_customers 
        self.open_time = open_time

    def set_number_served(self):
        print(f'{self.restaurant_name} has served {self.num_customers} customers')

    def increment_number_served(self,served):
        self.num_customers = served
    def restaurant_open(self):
        print(f'It is almost {self.open_time}, time to open up')
        print(f'{self.restaurant_name} is now open!')
    def increment_time(self):
        print("hello")

def main():
    res = Restaurant("Burgerville", 0, 8)
    print(f'This is {res.restaurant_name}')
    
    res.restaurant_open()
    res.set_number_served()
    res.increment_number_served(64)
    res.set_number_served()  




if __name__ == "__main__":
    main()