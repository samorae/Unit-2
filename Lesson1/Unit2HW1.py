
"""
Name: Eli Samora
Date: 3/6/2025
Description: Unit 2 HW 1
"""
class Restaurant:
    """A simple attempt to model a dog."""

    def __init__(self, name: str, cuisine: str) -> None:
        """Creates a new dog object

        Args:
            name (str): Name of dog
            age (int): Age of dog
        """
        self.name = name
        self.cuisine = cuisine

    def restaurant_description(self) -> None:
        """Describes the restuarant"""
        print(f"Restaurant name: {self.name}\nRestaurant Cuisine: {self.cuisine}")

    def res_open(self) -> None:
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now Open!")

def main():
    res_one = Restaurant("Panda Express", "Chinese")
    res_two = Restaurant("Burger Kings","American")
    res_three = Restaurant("Taco Bell","Mexican")
    print(f"The first restuarants name {res_one.name}")
    print(f"The first restaurants food is {res_one.cuisine}")
    print(f"The second restaurants name is {res_two.name}")
    print(f"The second restaurants food is {res_two.cuisine}")
    print(f"The second restaurants name is {res_three.name}")
    print(f"The second restaurants food is {res_three.cuisine}")
    
    res_one.res_open()
    res_one.restaurant_description()
    
    res_two.res_open()
    res_two.restaurant_description()
    
    res_three.res_open()
    res_three.restaurant_description()
    
if __name__ == "__main__":
    main()