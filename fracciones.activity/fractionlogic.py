# -*- coding: utf-8 -*-
"""
Contain the logic of fractions and comparations of fractions.

"""
import random
DENOMINATOR_MIN = 4
DENOMINATOR_MAX = 10


class Fraction(object):

    def __init__(self):
        self.numerator = None
        self.denominator = None
        
    def __eq__(self,other_fraction):
        if (self.numerator * other_fraction.denominator == self.denominator * other_fraction.numerator) and type(other_fraction) is Fraction:
            return True 
        else:
            return False
            

class FractionLogic(object):

    def __init__(self):
        self.fraction = Fraction()
        

    def generate(self):
        """Generate new fraction"""
        if DENOMINATOR_MIN < 1:
            raise Exception("DENOMINATOR_MIN need be greather than 0")
        self.fraction.denominator = random.randrange(DENOMINATOR_MIN, DENOMINATOR_MAX)
        self.fraction.numerator = random.randrange(0, self.fraction.denominator+1)


    def get_current(self):
        """Return the current fraction, raise an exception if generate_fraction
        hasn't called before"""
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before get_current_fraction")
        return (self.fraction.numerator, self.fraction.denominator)
        
        
    def get_current_cake(self):
        """Return the current fraction, raise an exception if generate_fraction
        hasn't called before"""
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before get_current_fraction")
        return (self.fraction)


    def is_equal(self, fraction):
        """DEPRECATED: Check if fraction is equal that the internal"""
        if not(type(fraction) is Fraction and self.fraction.denominator is not None):
            raise Exception("fraction must be a tuple of length 2")
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before is_equal")
        return fraction.numerator * self.fraction.denominator == fraction.denominator * self.fraction.numerator


    def __repr__(self):
        if self.fraction.denominator is None:
            return "<FractionLogic(Undefined)>"
        return "<FractionLogic(%i,%i)>"%(self.fraction.numerator,self.fraction.denominator)
