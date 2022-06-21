# Calculate the Volume of a Cylinder

Here are the requirements from the original challenge:

## Requirements

Write a Python 3 program called **cylindervolumecalc.py** that accepts user input from the keyboard for radius and height of a cylinder and outputs the volume based on the following equation.

V = πr2h

The volume of a cylinder is π (3.14159) times the radius squared times the height of the cylinder.

The following are additional requirements for this challenge:

- User input may not cause the program to crash. Exceptions from invalid user input must be handled gracefully. The user is to be given feedback about invalid input and given the opportunity to supply the input without needing to run the program again.
- Negative values for radius and height are not to be accepted from the user. If a negative value is provided the user is to be given feedback and asked again for the value.
- After each calculation the user is to be prompted if they want to perform another calculation. If they answer with a “y” then they are to be prompted for new input and another calculation is to be performed. If they provide any other response the program is to exit.

Use previously written code and the web as a reference for [Interactive Input and Exception Handling](https://www.w3schools.com/python/python_try_except.asp)

## Support

The equation for calculating the volume of a cylinder, V=πr2h, contains π. You could just use 3.14159 in place of π, but Python has the value for π defined and you can use it in your program.

See: [Math.Pi in Python](https://www.w3schools.com/python/ref_math_pi.asp)

If you import the python math library, in it is the definition for π.  To use it, place import math at the top of the program, then use math.pi where the value of π is required.

Check out the following code:

```python
import math
print(math.pi)
```

When it is run, it displays:

```python
3.141592653589793
```

