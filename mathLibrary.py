from math import floor, pow, sqrt, sin, cos, tan, radians, isclose
# return the integer number (trunk or floor):
real_number = float(input('Enter the real number: '))
print(f"Let me show you the integer part: {floor(real_number)}")

# return the hypotenuse:
adjacent_side = float(input('Enter the adjacent side: '))
opposite_side = float(input('Enter the opposite side: '))
hypotenuse_side = round(sqrt(pow(adjacent_side, 2) + pow(opposite_side, 2)), 2)
print('The hypotenuse is: {}'. format(hypotenuse_side))

# return the sine, cosine and tangent of the given angle


angle = float(input('Enter the angle in degrees: '))
angleInRadians = radians(angle)
print(
    f"sin{angle:.0f}°={sin(angleInRadians):.1f}\n"
    f"cos{angle:.0f}°={cos(angleInRadians):.1f}"
)
if isclose(cos(angleInRadians), 0, abs_tol=1e-9):
    print(f"tan{angle:.0f}°=undefined")
else:
    print(f"tan{angle:.0f}°={tan(angleInRadians)}")

