"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Tim Wilson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window=rg.RoseWindow()
    circle1=rg.Circle(rg.Point(150,50),30)
    circle2=rg.Circle(rg.Point(90,90),40)
    circle2.fill_color='blue'
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()


    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window=rg.RoseWindow()
    circle=rg.Circle(rg.Point(200,100),90)
    circle.fill_color='blue'
    circle.outline_thickness=4
    p1=rg.Point(100,50)
    p2=rg.Point(150,70)
    rect=rg.Rectangle(p1,p2)
    rect.outline_thickness=3
    circle.attach_to(window)
    rect.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(circle.center.x)
    print(circle.center.y)

    print(rect.outline_thickness)
    print(rect.fill_color)
    print('Point(',((rect.corner_2.x)+(rect.corner_1.x))/2,((((rect.corner_2.y)+(rect.corner_1.y))/2)),')')
    print((((rect.corner_2.x)+(rect.corner_1.x))/2))
    print((((rect.corner_2.y)+(rect.corner_1.y))/2))

    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window=rg.RoseWindow()
    line1=rg.Line(rg.Point(20,100),rg.Point(300,200))
    line1.get_midpoint()
    line2 = rg.Line(rg.Point(200, 150), rg.Point(100, 70))
    line2.thickness=5
    line2.get_midpoint()
    print(line1.get_midpoint())
    print(line1.get_midpoint(rg.Line((line1.start.x),(line1.end.x))))
    print(line1.get_midpoint(rg.Line((line1.start.y),(line1.end.y))))
    print(line2.get_midpoint())
    print(line2.get_midpoint(rg.Line(rg.Point(200,0),rg.Point(100,0))))
    print(line2.get_midpoint(rg.Line(rg.Point(0,150),rg.Point(0,70))))
    # TODO: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
