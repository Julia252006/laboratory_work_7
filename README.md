Brain Academy. Python Course. Laboratory Work #7.1.1

Write an object oriented program that show building material property
and storage quantity:
 
 1. Define the class "Building"
 2. Create class constructor with arguments - material, 
 color, number (with default value - 0) and store place
 3. Material that will accept name for building material
 4. Color that will accept color for building material
 5. Number is a variable value for material quantity
 6. Place will show place where this material can be placed:
  6.1. number < 0 = "out of stock"
  6.2. 0 < number < 100 = "warehouse"
  6.3 else - "Remote warehouse"

```python 
class Building:

    def __init__(self, material, color, number=0):
        self.__material = material
        self.__color = color
        self.__number = number

    def place(self):
        if self.__number < 0:
            print('Out of stock')
        elif 0 < self.__number < 100:
            print('Warehouse')
        else:
            print('Remote warehouse')

obj1 = Building('wood', 'brown', -20) 
obj2 = Building('stone', 'grey', 10)
obj3 = Building('stone', 'grey', 110)
obj1.place()
obj2.place()
obj3.place()
```

Brain Academy. Python Course. Laboratory Work #7.1.2 

Write an object oriented program that show building material property
and storage quantity: 
 1. Recreate the Lab 1 Code and methods and calls of class object
 2. Create method "plus" for adding material quantity by some count with
 corresponding changing to number and place
 3. Create method "minus" for decreasing material quantity by some count with
 corresponding changing to number and place
 4. Create object for white brick with 300 as initial quantity
 5. Create object for brown plank with 20 as initial quantity
 6. Print objects variables
 7. Add 50 bricks to first object
 8. Remove 3 planks from second object


```python 
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

    def place(self):
        if self.__number < 0:
            print('Out of stock')
        elif 0 < self.__number < 100:
            print('Warehouse')
        else:
            print('Remote warehouse')

    # Create method "plus" for adding material quantity by some
    # count with corresponding changing to number and place
    def plus(self, number_to_add):
        self.__number += number_to_add

    # Create method minus" for decreasing material quantity by some
    # count with corresponding changing to number and place
    def minus(self, number_to_add):
        self.__number -= number_to_add

    def __str__(self):
        return 'Building:\n\tmaterial: {}\n\tcolor: {}\n\tnumber: {}\n'\
               .format(self.__material, self.__color, self.__number)

brick = Building('brick', 'white', 300)
plank = Building('plank', 'brown', 20)

print(brick)
print(plank)

brick.plus(50)
plank.minus(30)

print('number of bricks:', brick.number)
print('number of planks:', plank.number)
```

Brain Academy. Python Course. Laboratory Work #7.1.3 

Write an object oriented program that
show building material property and storage quantity:

 1. Import all data from Lab 2
 2. Create object for yellow brick with 200 as initial quantity
 3. Create object for red plank with 10 as initial quantity
 4. Print objects variables
 5. Add 1 bricks to first object
 6. Remove 2 planks from second object


```python 
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
```
Brain Academy. Python Course. Laboratory Work #7.2.1
 
Write an object oriented program 
that show building material property and storage quantity:
 1. Define the class "Building"
 2. Create class constructor with arguments - material, color, number
    (with default value - 0) and store place
 3. Material that will accept name for building material
 4. Color that will accept color for building material
 5. Number is a variable value for material quantity should be protected
 6. Place will show place where this material can be placed:
  6.1 number < 0 = "out of stock"
  6.2 0 < number < 100 = "warehouse"
  6.3 else - "Remote warehouse"
 7. Create method "plus" for adding material quantity by some count with
    corresponding changing to protected number and place
 8. Create method "minus" for decreasing material quantity by some count with
    corresponding changing to number and place
 9. Create object for white brick with 300 as initial quantity
 10. Create object for brown plank with 20 as initial quantity
 11. Print objects variables
 12. Add 50 bricks to first object
 13. Remove 3 planks from second object
 

```python 

```