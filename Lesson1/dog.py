class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name: str, age: int) -> None:
        """Creates a new dog object

        Args:
            name (str): Name of dog
            age (int): Age of dog
        """
        self.name = name
        self.age = age

    def sit(self) -> None:
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

def main():
    dog_one = Dog("Pierre",2)
    dog_two = Dog("Bentley",8)
    print(f"The first dog's name is {dog_one.name}")
    print(f"The first dog's age is {dog_one.age}")
    
    print(f"The second dog's name is {dog_two.name}")
    print(f"The second dog's age is {dog_two.age}")
    
    dog_one.sit()
    dog_one.roll_over()
    
    dog_two.sit()
    dog_two.roll_over()
    
if __name__ == "__main__":
    main()