#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate DPI | ----\n", fg("red")))

# class
class DPI:
    def __init__(self, dots, inches):
        self.dots = dots
        self.inches = inches

    # output magic method
    def __repr__(self):
        output = stylize(self.get_dpi(self.dots, self.inches), fg("red"))
        return f"\nAn image with the width of {self.dots} px ({self.inches} inches)\nhas a DPI of {output}.\n"

    # methods
    def get_dpi(self, d, i):
        dpi = round(d / i)
        return dpi

# main execution
if __name__ == "__main__":
    # user interaction
    dots_wide = float(input("Width of image in pixels (dots): "))
    inches_wide = float(input("Width of image in inches: "))

    print(DPI(dots_wide, inches_wide))
