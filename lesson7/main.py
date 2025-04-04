from Car import Car
from ElectricCar import ElectricCar as EC
import random 
def main():
    my_leaf = EC("Nissan","Leaf",2024,60)
    print(my_leaf.battery_level)
    print(my_leaf.make)

if __name__ == '__main__':
    main()