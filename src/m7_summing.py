"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Tim Wilson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import rosegraphics as rg
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    #Test 1
    expected=.13416
    answer=sum_cosines(3)
    print('Sum Cosines Test 1 expected', expected)
    print('         actual:', answer)
    #Test 2
    answer = sum_cosines(5)
    expected=-.2358184620
    print('Sum Cosines Test 2 expected', expected)
    print('         actual:', answer)
    #Test 3
    answer = sum_cosines(10)
    expected=-.4174477460
    print('Sum Cosines Test 3 expected', expected)
    print('         actual:', answer)
    print('--------------------------------------------------')


def sum_cosines(n):
    total=0
    if n>=0:
        for k in range(n+1):
            total=total+math.cos(k)
        return(total)

    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    expected=11.8544
    answer=sum_square_roots(5)
    print('Sum of Square Roots Test 1 Expected', expected)
    print(          'actual:',answer)
    expected = 36.4653
    answer = sum_square_roots(11)
    print('Sum of Square Roots Test 2 Expected', expected)
    print('          actual:', answer)
    expected =5.8637
    answer = sum_square_roots(3)
    print('Sum of Square Roots Test 1 Expected', expected)
    print('actual:', answer)
    print('--------------------------------------------------')


def sum_square_roots(n):
    total=0
    for k in range(n+1):
        total=total+math.sqrt(2*k)
    return(total)

    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
