# 1. Import all data from Lab 2
# 2. Create object for yellow brick with 200 as initial quantity
# 3. Create object for red plank with 10 as initial quantity
# 4. Print objects variables
# 5. Add 1 bricks to first object
# 6. Remove 2 planks from second object

class Building:

    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        self.__number = number

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    material = property(get_material, set_material)
    color = property(get_color, set_color)
    number = property(get_number, set_number)

    def plus(self, number_to_add):
        self.__number += number_to_add

    def minus(self, number_to_add):
        self.__number -= number_to_add

# Create object for yellow brick with 200 as initial quantity
brick = Building('brick', 'yellow', 200)
# Create object for red plank with 10 as initial quantity
plank = Building('plank', 'red', 10)

print(brick)
print(plank)

brick.plus(1)
plank.minus(2)

print('One brick added to brick-building. Left: {}'.format(brick.get_number()))
print('Two planks removed from plank-building. Left: {}'.format(plank.get_number()))
