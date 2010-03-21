# -*- coding: utf-8 -*-
"""
Contain the logic of fractions and comparations of fractions.

"""
import random
DENOMINATOR_MIN = 4
DENOMINATOR_MAX = 10


class FractionLogic(object):
    
    def __init__(self):
        self.numerator = None
        self.denominator = None


    def generate(self):
        """Generate new fraction"""
        if DENOMINATOR_MIN < 1:
            raise Exception("DENOMINATOR_MIN need be greather than 0")
        self.denominator = random.randrange(DENOMINATOR_MIN, DENOMINATOR_MAX)
        self.numerator = random.randrange(0, self.denominator+1)


    def get_current(self):
        """Return the current fraction, raise an exception if generate_fraction
        hasn't called before"""
        if self.denominator is None:
            raise Exception("generate_fraction must be called before get_current_fraction")
        return (self.numerator, self.denominator)


    def is_equal(self, fraction):
        """Check if fraction is equal that the internal"""
        if not(type(fraction) is tuple and len(fraction) == 2):
            raise Exception("fraction must be a tuple of length 2")
        if self.denominator is None:
            raise Exception("generate_fraction must be called before is_equal")
        return fraction[0] * self.denominator == fraction[1] * self.numerator


    def __repr__(self):
        if self.denominator is None:
            return "<FractionLogic(Undefined)>"
        return "<FractionLogic(%i,%i)>"%(self.numerator,self.denominator)
