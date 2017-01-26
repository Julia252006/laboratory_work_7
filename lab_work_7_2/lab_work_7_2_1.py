# 1. Define the class "Building"
# 2. Create class constructor with arguments - material, color, number
#   (with default value - 0) and store place
# 3. Material that will accept name for building material
# 4. Color that will accept color for building material
# 5. Number is a variable value for material quantity should be protected
# 6. Place will show place where this material can be placed:
#   6.1 number < 0 = "out of stock"
#   6.2 0 < number < 100 = "warehouse"
#   6.3 else - "Remote warehouse"
# 7. Create method "plus" for adding material quantity by some count with
#    corresponding changing to protected number and place
# 8. Create method "minus" for decreasing material quantity by some count with
#    corresponding changing to number and place
# 9. Create object for white brick with 300 as initial quantity
# 10. Create object for brown plank with 20 as initial quantity
# 11. Print objects variables
# 12. Add 50 bricks to first object
# 13. Remove 3 planks from second object

class Building:

    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        self._number = number

    def place(self):
        if self._number < 0:
            print('Out of stock')
        elif 0 < self._number < 100:
            print('Warehouse')
        else:
            print('Remote warehouse')

    def plus(self, number_to_add):
        self._number += number_to_add

    def minus(self, number_to_add):
        self._number -= number_to_add

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    material = property(get_material, set_material)
    color = property(get_color, set_color)
    number = property(get_number, set_number)

brick = Building('brick', 'white', 300)
plank = Building('plank', 'brown', 20)

print(brick)
print(plank)

brick.plus(50)
plank.minus(3)

print('50 brick added to brick-building. Left: {}'.format(brick.get_number()))
print('3 planks removed from plank-building. Left: {}'.format(plank.get_number()))